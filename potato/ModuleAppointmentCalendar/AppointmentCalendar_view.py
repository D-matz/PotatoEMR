from django.shortcuts import render, redirect
from datetime import date, datetime, timedelta
from .AppointmentCalendar_form import ApptClndrForm
from potato.models import FHIR_Appointment, FHIR_Location, FHIR_Practitioner, FHIR_Encounter, FHIR_Encounter_Participant, FHIR_Appointment_Participant
from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.db import transaction

def getOrCreateApptEncounter(appt_model):
    # get or create first encounter for appointment
    encounter_models = FHIR_Encounter.objects.filter(appointment=appt_model)
    if encounter_models.count() == 0:
        with transaction.atomic():
            appt_part_location_model = FHIR_Appointment_Participant.objects.filter(appointment=appt_model, actor_location__isnull=False).first()
            if appt_part_location_model is None:
                print("no location found for appointment, not going to create encounter")
                return None
            appt_part_practitioner_model = FHIR_Appointment_Participant.objects.filter(appointment=appt_model, actor_practitioner__isnull=False).first()
            if appt_part_practitioner_model is None:
                print("no practitioner found for appointment, could technically create an encounter without a practionier but deciding not to")
                return None
            new_encounter_model = FHIR_Encounter.objects.create(
                status=FHIR_Encounter.StatusChoices.PLANNED,
                location_ref=appt_part_location_model.actor_location,
                subject_patient=appt_model.subject_patient,
                subject_group=appt_model.subject_group,
            )
            FHIR_Encounter_Participant.objects.create(
                encounter=new_encounter_model,
                actor_practitioner=appt_part_practitioner_model.actor_practitioner,
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
        .filter(appointment_participant__actor_practitioner=apptInfo['Practitioner'])
        .filter(appointment_participant__actor_location=apptInfo['Location'])
        .filter(
            Q(start__gte=chosenDate_iso, start__lt=next_day.isoformat()) |
            Q(end__gte=chosenDateTmrw_iso, end__lt=next_day.isoformat()))
        .distinct())
    print("num apts:", len(appointment_model_list))

    sorted_appts = sorted(appointment_model_list, key=lambda appt: datetime.fromisoformat(appt.start))

    appt_list = []
    for appt_model in sorted_appts:
        encounter_model = getOrCreateApptEncounter(appt_model)
        calendar_entry = {
            'id': appt_model.id,
            'patient': str(appt_model.subject_patient),
            'patient_id': appt_model.subject_patient.id,
            'status': str(appt_model.status),
            'notes': str(appt_model.notes.first()),
            'start': datetime.fromisoformat(appt_model.start).strftime("%H:%M"),
            'end': datetime.fromisoformat(appt_model.end).strftime("%H:%M"),
            'encounter_id': encounter_model.id
        }
        for participant in appt_model.appointment_participant.all():
            practitioner = participant.actor_practitioner
            if practitioner: calendar_entry['provider'] = str(practitioner)
        appt_list.append(calendar_entry)

    #print(appt_list)
    return render(request, template, {'ApptClndrForm': ApptClndrForm(apptInfo), 'appt_list': appt_list})

def calendar_whole(request):
    if not FHIR_Location.objects.exists(): return HttpResponse("error no locations saved")
    default_location = FHIR_Location.objects.first()
    if default_location is None: practitioner_id = None
    else:
        practitioner_models =  FHIR_Practitioner.objects.filter(practitioner_roles__location=default_location.id)
        if not practitioner_models.exists(): practitioner_id = None
        else: practitioner_id = FHIR_Practitioner.objects.filter(practitioner_roles__location=default_location.id).first().id
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
    chosen_location_practitioners = FHIR_Practitioner.objects.filter(practitioner_roles__location=chosen_location_id).distinct()
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
