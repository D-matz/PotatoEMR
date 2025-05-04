from django.shortcuts import render, redirect
from datetime import date, datetime, timedelta
from .AppointmentCalendar_form import ApptClndrForm
from potato.models import FHIR_Appointment, FHIR_Location, FHIR_Practitioner, FHIR_Encounter, FHIR_Encounter_participant, FHIR_Appointment_participant, FHIR_Encounter_location
from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.db import transaction

def getOrCreateApptEncounter(appt_model):
    # get or create first encounter for appointment
    encounter_models = FHIR_Encounter.objects.filter(appointment=appt_model)
    if encounter_models.count() == 0:
        with transaction.atomic():
            appt_part_location_model = FHIR_Appointment_participant.objects.filter(Appointment=appt_model, actor_Location__isnull=False).first()
            if appt_part_location_model is None:
                print("no location found for appointment, not going to create encounter")
                return None
            appt_part_practitioner_model = FHIR_Appointment_participant.objects.filter(Appointment=appt_model, actor_Practitioner__isnull=False).first()
            if appt_part_practitioner_model is None:
                print("no practitioner found for appointment, could technically create an encounter without a practionier but deciding not to")
                return None
            new_encounter_model = FHIR_Encounter.objects.create(
                status=FHIR_Encounter.StatusChoices.PLANNED,
                subject_Patient=appt_model.subject_Patient,
                subject_Group=appt_model.subject_Group,
            )
            FHIR_Encounter_location.objects.create(
                Encounter=new_encounter_model,
                location=appt_part_location_model.actor_Location,
                status=FHIR_Encounter_location.StatusChoices.PLANNED
            )
            FHIR_Encounter_participant.objects.create(
                Encounter=new_encounter_model,
                actor_Practitioner=appt_part_practitioner_model.actor_Practitioner,
            )
            new_encounter_model.appointment.set([appt_model])
        if new_encounter_model is None:
            return HttpResponse("error failed to create encounter for appointment")
        return new_encounter_model
    else:
        return encounter_models.first()

def calendar(request, template, apptInfo):
    print(apptInfo['Location'], apptInfo['Practitioner'], apptInfo['Date'])
    if isinstance(apptInfo['Date'], str):
        chosenDate = datetime.strptime(apptInfo['Date'], "%Y-%m-%d").date()
    else:
        chosenDate = apptInfo['Date']
    next_day = chosenDate + timedelta(days=1)
    chosenDate_iso = chosenDate.isoformat()
    chosenDateTmrw_iso = next_day.isoformat()

    appointment_model_list = (FHIR_Appointment.objects
        .filter(Appointment_participant__actor_Practitioner=apptInfo['Practitioner'])
        .filter(Appointment_participant__actor_Location=apptInfo['Location'])
        .filter(
            Q(start__gte=chosenDate_iso, start__lt=next_day.isoformat()) |
            Q(end__gte=chosenDateTmrw_iso, end__lt=next_day.isoformat()))
        .distinct())
    print("num apts:", len(appointment_model_list))

    sorted_appts = sorted(appointment_model_list, key=lambda appt: datetime.fromisoformat(appt.start))

    appt_list = []
    for appt_model in sorted_appts:
        encounter_model = getOrCreateApptEncounter(appt_model)
        print("encounter", encounter_model, encounter_model.id)
        appt_list_item = {
            'id': appt_model.id,
            'patient': str(appt_model.subject_Patient),
            'patient_id': appt_model.subject_Patient.id,
            'status': str(appt_model.status),
            'notes': str(appt_model.Appointment_note.first()),
            'start': datetime.fromisoformat(appt_model.start).strftime("%H:%M"),
            'end': datetime.fromisoformat(appt_model.end).strftime("%H:%M"),
            'encounter_id': encounter_model.id
        }
        for participant in appt_model.Appointment_participant.all():
            practitioner = participant.actor_Practitioner
            if practitioner: appt_list_item['provider'] = str(practitioner)
        appt_list.append(appt_list_item)

    #print(appt_list)
    return render(request, template, {'ApptClndrForm': ApptClndrForm(apptInfo), 'appt_list': appt_list})

def calendar_whole(request):
    if not FHIR_Location.objects.exists(): return HttpResponse("error no locations saved")
    default_location = FHIR_Location.objects.first()
    if default_location is None: practitioner_id = None
    else:
        practitioner_models =  FHIR_Practitioner.objects.filter(PractitionerRole_practitioner__location=default_location.id)
        if not practitioner_models.exists(): practitioner_id = None
        else: practitioner_id = FHIR_Practitioner.objects.filter(PractitionerRole_practitioner__location=default_location.id).first().id
    apptInfo = {
        'Date': date.today(),
        'Location': default_location.id,
        'Practitioner': practitioner_id
    }
    return calendar(request, "AppointmentCalendar_home.html", apptInfo)


def calendar_partial(request):
    #receive form, they may change to new location or new practitioner
    #should only show practitioners from the chosen location
    #so if they changed location, set practitioner field to first practitioner for that location
    chosen_location_id = request.GET['Location']
    chosen_practitioner_id = request.GET['Practitioner']
    chosen_location_practitioners = FHIR_Practitioner.objects.filter(PractitionerRole_practitioner__location=chosen_location_id).distinct()
    if FHIR_Practitioner.objects.get(id=chosen_practitioner_id) not in chosen_location_practitioners:
        chosen_practitioner_id = chosen_location_practitioners.first().id
    apptInfo = {
        'Date': request.GET['Date'],
        'Location': chosen_location_id,
        'Practitioner': chosen_practitioner_id
    } #apptInfo is copy of request but we might change their practitioner
    return calendar(request, "AppointmentCalendar_partial.html", apptInfo)

def calendar_peek(request, appt_id):
    appt_model = get_object_or_404(FHIR_Appointment, id=appt_id)
    encounter_model = getOrCreateApptEncounter(appt_model)
    return render(request, "AppointmentCalendar_peek.html", {"appt": appt_model, "encounter_id": encounter_model.id})
