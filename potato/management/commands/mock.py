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

        FHIR_Condition.objects.all().delete()
        choices_clinicalStatus = FHIR_GP_Coding.objects.filter(codings__binding_rule=FHIR_Condition.BINDING_clinicalStatus)
        choices_verificationStatus = FHIR_GP_Coding.objects.filter(codings__binding_rule=FHIR_Condition.BINDING_verificationStatus)
        choices_severity = FHIR_GP_Coding.objects.filter(codings__binding_rule=FHIR_Condition.BINDING_severity)
        choices_code = FHIR_GP_Coding.objects.filter(codings__binding_rule=FHIR_Condition.BINDING_code)
        print("choices_clinicalStatus", FHIR_Condition.BINDING_clinicalStatus, choices_clinicalStatus)
        for patient_model in patient_model_list:
            for i in range(0, random.randint(3, 7)):
                condition_model = FHIR_Condition.objects.create(subject_Patient=patient_model,
                                                                onset_dateTime=datetime.now(timezone.utc) - timedelta(days=random.randint(0, 365 * 10)))
                condition_model.clinicalStatus_cc.set([random.choice(choices_clinicalStatus)])
                condition_model.verificationStatus_cc.set([random.choice(choices_verificationStatus)])
                condition_model.severity_cc.set([random.choice(choices_severity)])
                condition_model.code_cc.set([random.choice(choices_code)])
        print(FHIR_Condition.objects.count(), "conditions created")

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

        pedro_patient_model = FHIR_Patient.objects.create(
            gender=FHIR_Patient.GenderChoices.MALE,
            birthDate=datetime(2024, 3, 14, tzinfo=timezone.utc)
        )
        pedro_patient_name_model = FHIR_Patient_name.objects.create(text="Pedro",  Patient=pedro_patient_model)
        FHIR_Observation.objects.all().delete()
        
        height_codes = FHIR_GP_Coding.objects.filter(
            system="http://loinc.org", 
            code__in=["8302-2", "8306-3"]  # Body height and Body height --lying
        )
        # Create random observation dates (0-210 days after birth)
        birth_date = pedro_patient_model.birthDate
        observation_dates = []
        for i in range(15):
            random_days = random.randint(0, 210)
            observation_date = birth_date + timedelta(days=random_days)
            observation_dates.append((random_days, observation_date))
        
        observation_dates.sort(key=lambda x: x[0])


        
        current_height = random.uniform(45, 55)  # Starting height in cm
        for days, observation_date in observation_dates:
            print("observation_date", observation_date, "days", days, "current_height", current_height)
            observation = FHIR_Observation.objects.create(
                value_Quantity=FHIR_GP_Quantity.objects.create(value=current_height, unit="cm", system="http://unitsofmeasure.org", code="cm"),
                subject_Patient=pedro_patient_model,
                status='final',
                effective_dateTime=observation_date
            )
            height_code = random.choice(height_codes)
            observation.code_cc.add(height_code)
            growth = random.uniform(6, 10) * (210 - days) / 210
            current_height += growth
        print(f"Created 15 height observations for Pedro")

        # Add weight observations for Pedro
        weight_code = FHIR_GP_Coding.objects.get(system="http://loinc.org", code="29463-7")
        current_weight = random.uniform(2.5, 3)  # Starting weight in kg
        current_weight = 2.34
        for days, observation_date in observation_dates:
            observation = FHIR_Observation.objects.create(
                value_Quantity=FHIR_GP_Quantity.objects.create(value=current_weight, unit="kg", system="http://unitsofmeasure.org", code="kg"),
                subject_Patient=pedro_patient_model,
                status='final',
                effective_dateTime=observation_date
            )
            observation.code_cc.add(weight_code)
            growth = random.uniform(1.5, 2.5) * (210 - days) / 210
            current_weight += growth
        print(f"Created 15 weight observations for Pedro")

        # Add head circumference observations for Pedro
        circumference_code = FHIR_GP_Coding.objects.get(system="http://loinc.org", code="9843-4")
        current_circumference = random.uniform(32, 35)  # Starting head circumference in cm
        for days, observation_date in observation_dates:
            circumference_quantity = FHIR_GP_Quantity.objects.create(value=current_circumference, unit="cm", system="http://unitsofmeasure.org", code="cm")
            observation = FHIR_Observation.objects.create(value_Quantity=circumference_quantity, subject_Patient=pedro_patient_model, status='final', effective_dateTime=observation_date)
            observation.code_cc.add(circumference_code)
            # Head circumference grows more in early months
            growth = random.uniform(2, 3) * (210 - days) / 210
            current_circumference += growth
        print(f"Created 15 head circumference observations for Pedro")

        # Add BMI observations for Pedro
        bmi_code = FHIR_GP_Coding.objects.get(system="http://loinc.org", code="39156-5")
        height_observations_models = FHIR_Observation.objects.filter(subject_Patient=pedro_patient_model, code_cc__system="http://loinc.org", code_cc__code="8302-2")
        weight_observations_models = FHIR_Observation.objects.filter(subject_Patient=pedro_patient_model, code_cc__system="http://loinc.org", code_cc__code="29463-7")
        for height_observation_model in height_observations_models:
            # adding BMI observations for days we have both height and weight
            weight_observation_model = weight_observations_models.filter(effective_dateTime=height_observation_model.effective_dateTime).first()
            # Using the formula: BMI = weight(kg) / (height(m))²
            height_in_meters = height_observation_model.value_Quantity.value / 100
            bmi_value = weight_observation_model.value_Quantity.value / (height_in_meters * height_in_meters)
            bmi_time = weight_observation_model.effective_dateTime
            
            bmi_quantity = FHIR_GP_Quantity.objects.create(value=bmi_value, unit="kg/m2", system="http://unitsofmeasure.org", code="kg/m2")
            observation = FHIR_Observation.objects.create(value_Quantity=bmi_quantity, subject_Patient=pedro_patient_model, status='final', effective_dateTime=bmi_time)
            observation.code_cc.add(bmi_code)
            print("add BMI observation", observation)
        print(f"Created {FHIR_Observation.objects.filter(subject_Patient=pedro_patient_model, code_cc__system='http://loinc.org', code_cc__code='39156-5').count()} BMI observations for Pedro")

        # Add respiratory rate observations for Pedro
        respiratory_rate_code = FHIR_GP_Coding.objects.get(system="http://loinc.org", code="9279-1")
        for days, observation_date in observation_dates:
            # Normal respiratory rate for infants: 30-60 breaths per minute
            respiratory_rate_value = random.uniform(30, 60)
            respiratory_quantity = FHIR_GP_Quantity.objects.create(
                value=respiratory_rate_value, 
                unit="/min", 
                system="http://unitsofmeasure.org", 
                code="/min"
            )
            observation = FHIR_Observation.objects.create(
                value_Quantity=respiratory_quantity, 
                subject_Patient=pedro_patient_model, 
                status='final', 
                effective_dateTime=observation_date
            )
            observation.code_cc.add(respiratory_rate_code)
        print(f"Created 15 respiratory rate observations for Pedro")

        # Add heart rate observations for Pedro
        heart_rate_code = FHIR_GP_Coding.objects.get(system="http://loinc.org", code="8867-4")
        for days, observation_date in observation_dates:
            heart_rate_value = random.uniform(80, 160)
            heart_rate_quantity = FHIR_GP_Quantity.objects.create(
                value=heart_rate_value, 
                unit="/min", 
                system="http://unitsofmeasure.org", 
                code="/min"
            )
            observation = FHIR_Observation.objects.create(
                value_Quantity=heart_rate_quantity, 
                subject_Patient=pedro_patient_model, 
                status='final', 
                effective_dateTime=observation_date
            )
            observation.code_cc.add(heart_rate_code)
        print(f"Created 15 heart rate observations for Pedro")

        # Add oxygen saturation observations for Pedro
        oxygen_saturation_code = FHIR_GP_Coding.objects.get(system="http://loinc.org", code="2708-6")
        for days, observation_date in observation_dates:
            # Normal oxygen saturation: 95-100%
            oxygen_saturation_value = random.uniform(95, 100)
            oxygen_saturation_quantity = FHIR_GP_Quantity.objects.create(
                value=oxygen_saturation_value, 
                unit="%", 
                system="http://unitsofmeasure.org", 
                code="%"
            )
            observation = FHIR_Observation.objects.create(
                value_Quantity=oxygen_saturation_quantity, 
                subject_Patient=pedro_patient_model, 
                status='final', 
                effective_dateTime=observation_date
            )
            observation.code_cc.add(oxygen_saturation_code)
        print(f"Created 15 oxygen saturation observations for Pedro")

        # Add temperature observations for Pedro
        temperature_code = FHIR_GP_Coding.objects.get(system="http://loinc.org", code="8310-5")
        for days, observation_date in observation_dates:
            # Normal temperature for infants: 36.5-37.5°C
            temperature_value = random.uniform(36.5, 37.5)
            temperature_quantity = FHIR_GP_Quantity.objects.create(
                value=temperature_value, 
                unit="Cel", 
                system="http://unitsofmeasure.org", 
                code="Cel"
            )
            observation = FHIR_Observation.objects.create(
                value_Quantity=temperature_quantity, 
                subject_Patient=pedro_patient_model, 
                status='final', 
                effective_dateTime=observation_date
            )
            observation.code_cc.add(temperature_code)
        print(f"Created 15 temperature observations for Pedro")

        # Add blood pressure observations for Pedro
        systolic_bp_code = FHIR_GP_Coding.objects.get(system="http://loinc.org", code="8480-6")
        diastolic_bp_code = FHIR_GP_Coding.objects.get(system="http://loinc.org", code="8462-4")
        for days, observation_date in observation_dates:
            # Normal blood pressure for infants: systolic 70-100, diastolic 40-70
            systolic_value = random.uniform(70, 100)
            diastolic_value = random.uniform(40, 70)
            
            # Create the main blood pressure observation first
            bp_code = FHIR_GP_Coding.objects.get(system="http://loinc.org", code="85354-9")
            bp_observation = FHIR_Observation.objects.create(
                subject_Patient=pedro_patient_model,
                status='final',
                effective_dateTime=observation_date
            )
            bp_observation.code_cc.add(bp_code)
            
            # Now create component observations with the parent observation already set
            systolic_component = FHIR_Observation_component.objects.create(
                Observation=bp_observation,
                value_Quantity=FHIR_GP_Quantity.objects.create(
                    value=systolic_value, 
                    unit="mm[Hg]", 
                    system="http://unitsofmeasure.org", 
                    code="mm[Hg]"
                )
            )
            systolic_component.code_cc.add(systolic_bp_code)
            
            diastolic_component = FHIR_Observation_component.objects.create(
                Observation=bp_observation,
                value_Quantity=FHIR_GP_Quantity.objects.create(
                    value=diastolic_value, 
                    unit="mm[Hg]", 
                    system="http://unitsofmeasure.org", 
                    code="mm[Hg]"
                )
            )
            diastolic_component.code_cc.add(diastolic_bp_code)
        print(f"Created 15 blood pressure observations for Pedro")