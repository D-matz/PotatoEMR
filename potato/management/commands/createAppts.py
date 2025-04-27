from django.core.management.base import BaseCommand
from potato.models import *
import random
import string
from datetime import datetime, timedelta, timezone

class Command(BaseCommand):
    def handle(self, *args, **options):
        FHIR_Patient.objects.all().delete()
        patientNames = ["Peter", "Paul", "Patricia", "Paula", "Philip", "Phoebe", "Penelope", "Preston", "Piper", "Patrick", "Priscilla", "Paxton", "Palmer", "Poppy", "Pierce", "Peyton", "Pearl", "Pilar", "Phoenix", "Prudence"]
        for pname in patientNames:
            patient_model = FHIR_Patient.objects.create()
            patient_name_model = FHIR_Patient_name.objects.create(text=pname, Patient=patient_model)
        patient_model_list = FHIR_Patient.objects.all()
        print("patients", patient_model_list)

        FHIR_Appointment.objects.all().delete()
        FHIR_Practitioner.objects.all().delete()
        FHIR_Location.objects.all().delete()
        FHIR_PractitionerRole.objects.all().delete()
        locations = ["Alaska clinic", "Arizona clinic", "Alabama clinic", "Arkansas clinic", "California clinic"]
        for loc in locations:
            FHIR_Location.objects.create(name=loc)
        location_model_list = FHIR_Location.objects.all()
        names = ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah", "Ian", "Julia"]
        for name in names:
            practitioner_model = FHIR_Practitioner.objects.create()
            practitioner_humanName_model = FHIR_Practitioner_name.objects.create(text=name, Practitioner=practitioner_model)
            practitionerRole_model = FHIR_PractitionerRole.objects.create(practitioner=practitioner_model)
            locNums = random.sample(range(len(location_model_list)), 2)
            for locNum in locNums:
                practitionerRole_model.location.add(location_model_list[locNum])
        for i in range(0, 300):
            appt_model = FHIR_Appointment.objects.create()
            loc_model = random.choice(location_model_list)
            practitioner_model_list = FHIR_Practitioner.objects.filter(PractitionerRole_practitioner__location=loc_model).distinct()
            pract_model = random.choice(practitioner_model_list)

            FHIR_Appointment_participant.objects.create(
                Appointment=appt_model,
                actor_Location=loc_model
            )
            FHIR_Appointment_participant.objects.create(
                Appointment=appt_model,
                actor_Practitioner=pract_model
            )
            FHIR_Appointment_note.objects.create(
                Appointment=appt_model,
                text=''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(13))
            )
            appt_model.subject_Patient = random.choice(patient_model_list)
            appt_model.status = random.choice(FHIR_Appointment.StatusChoices.values)
            random_seconds = random.randint(0, 3 * 24 * 60 * 60)
            random_seconds_duration = (15 * 60) + random.randint(0, 30 * 60)
            future_time_start = datetime.now(timezone.utc) + timedelta(seconds=random_seconds)
            future_time_end = datetime.now(timezone.utc) + timedelta(seconds=random_seconds + random_seconds_duration)
            start_isoformat = future_time_start.isoformat(timespec='milliseconds')
            end_isoformat = future_time_end.isoformat(timespec='milliseconds')
            appt_model.start = start_isoformat
            appt_model.end = end_isoformat
            appt_model.save()
        print("locations:", FHIR_Location.objects.all())
        print("practitioners:", FHIR_Practitioner.objects.all())
        print("practitionerRoles", FHIR_PractitionerRole.objects.all())
        print("appointments", FHIR_Appointment.objects.all())
