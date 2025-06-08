from django.core.management.base import BaseCommand
from potato.models import *
import random
import string
import os
from datetime import datetime, timedelta, timezone, date

# Patient names that should have photos (defined in mock_pics.py)
photo_patient_names = [
    'Elijah Wood', 'Ian McKellen', 'Christopher Lee', 'Liv Tyler', 'Orlando Bloom',
    'Sean Astin', 'Viggo Mortensen', 'John Rhys-Davies', 'Billy Boyd', 'Dominic Monaghan',
    'Sean Bean', 'Andy Serkis', 'Miranda Otto', 'John Noble', 'Ian Holm',
    'Hugo Weaving', 'Karl Urban', 'David Wenham', 'Cate Blanchett', 'Brad Dourif',
    'Bernard Hill', 'Howard Shore'
]

class Command(BaseCommand):
    def handle(self, *args, **options):  
        # Use existing patients with photos (they should be created by mock_pics.py first)
        patient_model_list = []
        
        # Collect existing patients only
        for patient_name in photo_patient_names:
            for pt in FHIR_Patient.objects.all():
                if pt.get_one_name() == patient_name:
                    patient_model_list.append(pt)
                    break
        
        if len(patient_model_list) == 0:
            print("No patients with photos found. Please run mock_pics.py first to create the patients.")
            return

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
            if(len(practitioner_model_list) != 0):
                #can't create any appointmnts for this location if we didn't give it any practitioners
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

        # Create observations for all patients
        FHIR_Observation.objects.all().delete()
        
        # Get all observation codes
        height_codes = FHIR_GP_Coding.objects.filter(
            system="http://loinc.org", 
            code__in=["8302-2", "8306-3"]  # Body height and Body height --lying
        )
        weight_code = FHIR_GP_Coding.objects.get(system="http://loinc.org", code="29463-7")
        circumference_code = FHIR_GP_Coding.objects.get(system="http://loinc.org", code="9843-4")
        bmi_code = FHIR_GP_Coding.objects.get(system="http://loinc.org", code="39156-5")
        respiratory_rate_code = FHIR_GP_Coding.objects.get(system="http://loinc.org", code="9279-1")
        heart_rate_code = FHIR_GP_Coding.objects.get(system="http://loinc.org", code="8867-4")
        oxygen_saturation_code = FHIR_GP_Coding.objects.get(system="http://loinc.org", code="2708-6")
        temperature_code = FHIR_GP_Coding.objects.get(system="http://loinc.org", code="8310-5")
        systolic_bp_code = FHIR_GP_Coding.objects.get(system="http://loinc.org", code="8480-6")
        diastolic_bp_code = FHIR_GP_Coding.objects.get(system="http://loinc.org", code="8462-4")
        bp_code = FHIR_GP_Coding.objects.get(system="http://loinc.org", code="85354-9")

        for patient_model in patient_model_list:
            # Create random observation dates (0-210 days after birth)
            birth_date = datetime.combine(patient_model.birthDate, datetime.min.time()).replace(tzinfo=timezone.utc)
            observation_dates = []
            for i in range(15):
                random_days = random.randint(0, 210)
                observation_date = birth_date + timedelta(days=random_days)
                observation_dates.append((random_days, observation_date))
            
            observation_dates.sort(key=lambda x: x[0])

            # Height observations
            current_height = random.uniform(45, 55)  # Starting height in cm
            for days, observation_date in observation_dates:
                observation = FHIR_Observation.objects.create(
                    value_Quantity=FHIR_GP_Quantity.objects.create(value=current_height, unit="cm", system="http://unitsofmeasure.org", code="cm"),
                    subject_Patient=patient_model,
                    status='final',
                    effective_dateTime=observation_date
                )
                height_code = random.choice(height_codes)
                observation.code_cc.add(height_code)
                growth = random.uniform(6, 10) * (210 - days) / 210
                current_height += growth

            # Weight observations
            current_weight = random.uniform(2.5, 3.5)  # Starting weight in kg
            for days, observation_date in observation_dates:
                observation = FHIR_Observation.objects.create(
                    value_Quantity=FHIR_GP_Quantity.objects.create(value=current_weight, unit="kg", system="http://unitsofmeasure.org", code="kg"),
                    subject_Patient=patient_model,
                    status='final',
                    effective_dateTime=observation_date
                )
                observation.code_cc.add(weight_code)
                growth = random.uniform(1.5, 2.5) * (210 - days) / 210
                current_weight += growth

            # Head circumference observations
            current_circumference = random.uniform(32, 35)  # Starting head circumference in cm
            for days, observation_date in observation_dates:
                circumference_quantity = FHIR_GP_Quantity.objects.create(value=current_circumference, unit="cm", system="http://unitsofmeasure.org", code="cm")
                observation = FHIR_Observation.objects.create(value_Quantity=circumference_quantity, subject_Patient=patient_model, status='final', effective_dateTime=observation_date)
                observation.code_cc.add(circumference_code)
                growth = random.uniform(2, 3) * (210 - days) / 210
                current_circumference += growth

            # BMI observations
            height_observations_models = FHIR_Observation.objects.filter(subject_Patient=patient_model, code_cc__system="http://loinc.org", code_cc__code="8302-2")
            weight_observations_models = FHIR_Observation.objects.filter(subject_Patient=patient_model, code_cc__system="http://loinc.org", code_cc__code="29463-7")
            for height_observation_model in height_observations_models:
                weight_observation_model = weight_observations_models.filter(effective_dateTime=height_observation_model.effective_dateTime).first()
                if weight_observation_model:
                    height_in_meters = height_observation_model.value_Quantity.value / 100
                    bmi_value = weight_observation_model.value_Quantity.value / (height_in_meters * height_in_meters)
                    bmi_time = weight_observation_model.effective_dateTime
                    
                    bmi_quantity = FHIR_GP_Quantity.objects.create(value=bmi_value, unit="kg/m2", system="http://unitsofmeasure.org", code="kg/m2")
                    observation = FHIR_Observation.objects.create(value_Quantity=bmi_quantity, subject_Patient=patient_model, status='final', effective_dateTime=bmi_time)
                    observation.code_cc.add(bmi_code)

            # Respiratory rate observations
            for days, observation_date in observation_dates:
                respiratory_rate_value = random.uniform(30, 60)
                respiratory_quantity = FHIR_GP_Quantity.objects.create(
                    value=respiratory_rate_value, 
                    unit="/min", 
                    system="http://unitsofmeasure.org", 
                    code="/min"
                )
                observation = FHIR_Observation.objects.create(
                    value_Quantity=respiratory_quantity, 
                    subject_Patient=patient_model, 
                    status='final', 
                    effective_dateTime=observation_date
                )
                observation.code_cc.add(respiratory_rate_code)

            # Heart rate observations
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
                    subject_Patient=patient_model, 
                    status='final', 
                    effective_dateTime=observation_date
                )
                observation.code_cc.add(heart_rate_code)

            # Oxygen saturation observations
            for days, observation_date in observation_dates:
                oxygen_saturation_value = random.uniform(95, 100)
                oxygen_saturation_quantity = FHIR_GP_Quantity.objects.create(
                    value=oxygen_saturation_value, 
                    unit="%", 
                    system="http://unitsofmeasure.org", 
                    code="%"
                )
                observation = FHIR_Observation.objects.create(
                    value_Quantity=oxygen_saturation_quantity, 
                    subject_Patient=patient_model, 
                    status='final', 
                    effective_dateTime=observation_date
                )
                observation.code_cc.add(oxygen_saturation_code)

            # Temperature observations
            for days, observation_date in observation_dates:
                temperature_value = random.uniform(36.5, 37.5)
                temperature_quantity = FHIR_GP_Quantity.objects.create(
                    value=temperature_value, 
                    unit="Cel", 
                    system="http://unitsofmeasure.org", 
                    code="Cel"
                )
                observation = FHIR_Observation.objects.create(
                    value_Quantity=temperature_quantity, 
                    subject_Patient=patient_model, 
                    status='final', 
                    effective_dateTime=observation_date
                )
                observation.code_cc.add(temperature_code)

            # Blood pressure observations
            for days, observation_date in observation_dates:
                systolic_value = random.uniform(70, 100)
                diastolic_value = random.uniform(40, 70)
                
                bp_observation = FHIR_Observation.objects.create(
                    subject_Patient=patient_model,
                    status='final',
                    effective_dateTime=observation_date
                )
                bp_observation.code_cc.add(bp_code)
                
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

            print(f"Created observations for {patient_model.get_one_name()}")

        print(f"Created observations for {len(patient_model_list)} patients")

        # Create AllergyIntolerance records
        FHIR_AllergyIntolerance.objects.all().delete()
        choices_clinicalStatus_allergy = FHIR_GP_Coding.objects.filter(codings__binding_rule=FHIR_AllergyIntolerance.BINDING_clinicalStatus)
        choices_verificationStatus_allergy = FHIR_GP_Coding.objects.filter(codings__binding_rule=FHIR_AllergyIntolerance.BINDING_verificationStatus)
        choices_type_allergy = FHIR_GP_Coding.objects.filter(codings__binding_rule=FHIR_AllergyIntolerance.BINDING_type)
        choices_code_allergy = FHIR_GP_Coding.objects.filter(codings__binding_rule=FHIR_AllergyIntolerance.BINDING_code)
        
        for patient_model in patient_model_list:
            # Create 1-4 allergies per patient  
            for i in range(0, random.randint(1, 4)):
                allergy_model = FHIR_AllergyIntolerance.objects.create(
                    patient=patient_model,
                    onset_dateTime=datetime.now(timezone.utc) - timedelta(days=random.randint(0, 365 * 5)),
                    criticality=random.choice(FHIR_AllergyIntolerance.CriticalityChoices.values) if hasattr(FHIR_AllergyIntolerance, 'CriticalityChoices') else None
                )
                if choices_clinicalStatus_allergy:
                    allergy_model.clinicalStatus_cc.set([random.choice(choices_clinicalStatus_allergy)])
                if choices_verificationStatus_allergy:
                    allergy_model.verificationStatus_cc.set([random.choice(choices_verificationStatus_allergy)])
                if choices_type_allergy:
                    allergy_model.type_cc.set([random.choice(choices_type_allergy)])
                if choices_code_allergy:
                    allergy_model.code_cc.set([random.choice(choices_code_allergy)])
        print(f"Created {FHIR_AllergyIntolerance.objects.count()} allergies")

        # Create Encounter records
        FHIR_Encounter.objects.all().delete()
        
        for patient_model in patient_model_list:
            # Create 2-6 encounters per patient
            for i in range(0, random.randint(2, 6)):
                # Planned dates (usually a few days before actual)
                planned_start = datetime.now(timezone.utc) - timedelta(days=random.randint(0, 365 * 2))
                planned_end = planned_start + timedelta(hours=random.randint(1, 8))
                
                # Actual dates (might be slightly different from planned)
                actual_start = planned_start + timedelta(minutes=random.randint(-30, 30))  # ±30 min variance
                actual_end = planned_end + timedelta(minutes=random.randint(-30, 30))    # ±30 min variance
                
                # Create a period object for the actual encounter period
                period_model = FHIR_GP_Period.objects.create(
                    start_datetime=actual_start,
                    end_datetime=actual_end
                )
                
                encounter_model = FHIR_Encounter.objects.create(
                    subject_Patient=patient_model,
                    actualPeriod=period_model,
                    plannedStartDate=planned_start,
                    plannedEndDate=planned_end,
                    status=random.choice(FHIR_Encounter.StatusChoices.values) if hasattr(FHIR_Encounter, 'StatusChoices') else None
                )
        print(f"Created {FHIR_Encounter.objects.count()} encounters")

        # Create DocumentReference records (notes)
        FHIR_DocumentReference.objects.all().delete()
        
        note_templates = [
            "Patient presents with routine checkup. Vital signs stable. No acute concerns noted.",
            "Follow-up visit for ongoing condition management. Patient reports improvement in symptoms.",
            "Vaccination visit completed without complications. Patient tolerated well.",
            "Developmental assessment performed. Patient meeting age-appropriate milestones.",
            "Acute care visit for minor illness. Treatment plan discussed with parents."
        ]
        
        # Get all encounters to link notes to
        all_encounters = list(FHIR_Encounter.objects.all())
        
        for patient_model in patient_model_list:
            # Get encounters for this patient
            patient_encounters = [enc for enc in all_encounters if enc.subject_Patient == patient_model]
            
            # Create 3-8 notes per patient
            for i in range(0, random.randint(3, 8)):
                doc_model = FHIR_DocumentReference.objects.create(
                    date=datetime.now(timezone.utc) - timedelta(days=random.randint(0, 365 * 2)),
                    description=random.choice(note_templates),
                    status=random.choice(FHIR_DocumentReference.StatusChoices.values) if hasattr(FHIR_DocumentReference, 'StatusChoices') else None
                )
                
                # Link to a random encounter for this patient (if any exist)
                if patient_encounters:
                    selected_encounter = random.choice(patient_encounters)
                    doc_model.context_Encounter.add(selected_encounter)
                    
        print(f"Created {FHIR_DocumentReference.objects.count()} document references (notes)")

        # Create Immunization records
        FHIR_Immunization.objects.all().delete()
        # Note: vaccineCode binding is "TODO" so we'll skip it for now
        
        for patient_model in patient_model_list:
            # Create 5-12 immunizations per patient (typical pediatric schedule)
            birth_date = datetime.combine(patient_model.birthDate, datetime.min.time()).replace(tzinfo=timezone.utc)
            
            # Standard immunization schedule (approximate ages in days)
            immunization_ages = [2, 30, 60, 120, 180, 365, 450, 540, 730, 1095, 1460]
            
            for age_days in immunization_ages[:random.randint(5, len(immunization_ages))]:
                immunization_date = birth_date + timedelta(days=age_days + random.randint(-7, 7))  # Add some variance
                
                immunization_model = FHIR_Immunization.objects.create(
                    patient=patient_model,
                    occurrence_dateTime=immunization_date,
                    primarySource=True,
                    status=random.choice(FHIR_Immunization.StatusChoices.values) if hasattr(FHIR_Immunization, 'StatusChoices') else None
                )
        print(f"Created {FHIR_Immunization.objects.count()} immunizations")

        # Create MedicationRequest records
        FHIR_MedicationRequest.objects.all().delete()
        choices_medication_code = FHIR_GP_Coding.objects.filter(codings__binding_rule=FHIR_MedicationRequest.BINDING_medication)
        
        for patient_model in patient_model_list:
            # Create 1-5 medication requests per patient
            for i in range(0, random.randint(1, 5)):
                med_request_model = FHIR_MedicationRequest.objects.create(
                    subject_Patient=patient_model,
                    authoredOn=datetime.now(timezone.utc) - timedelta(days=random.randint(0, 365 * 2)),
                    status=random.choice(FHIR_MedicationRequest.StatusChoices.values) if hasattr(FHIR_MedicationRequest, 'StatusChoices') else None,
                    intent=random.choice(FHIR_MedicationRequest.IntentChoices.values) if hasattr(FHIR_MedicationRequest, 'IntentChoices') else None
                )
                if choices_medication_code:
                    med_request_model.medication_cc.set([random.choice(choices_medication_code)])
        print(f"Created {FHIR_MedicationRequest.objects.count()} medication requests")

        # Create MedicationDispense records
        FHIR_MedicationDispense.objects.all().delete()
        
        # Create dispenses for some of the medication requests
        medication_requests = list(FHIR_MedicationRequest.objects.all())
        for med_request in random.sample(medication_requests, min(len(medication_requests), random.randint(len(medication_requests)//2, len(medication_requests)))):
            med_dispense_model = FHIR_MedicationDispense.objects.create(
                subject_Patient=med_request.subject_Patient,
                whenHandedOver=med_request.authoredOn + timedelta(days=random.randint(0, 7)),
                status=random.choice(FHIR_MedicationDispense.StatusChoices.values) if hasattr(FHIR_MedicationDispense, 'StatusChoices') else None
            )
            med_dispense_model.authorizingPrescription.add(med_request)
            if choices_medication_code:
                med_dispense_model.medication_cc.set(med_request.medication_cc.all())
        print(f"Created {FHIR_MedicationDispense.objects.count()} medication dispenses")

        # Create MedicationAdministration records
        FHIR_MedicationAdministration.objects.all().delete()
        
        # Create administrations for some of the medication requests
        for med_request in random.sample(medication_requests, min(len(medication_requests), random.randint(len(medication_requests)//3, len(medication_requests)//2))):
            # Create multiple administrations for each request (daily doses, etc.)
            for day in range(0, random.randint(1, 14)):
                admin_date = med_request.authoredOn + timedelta(days=day)
                med_admin_model = FHIR_MedicationAdministration.objects.create(
                    subject_Patient=med_request.subject_Patient,
                    occurrence_dateTime=admin_date,
                    request=med_request,
                    status=random.choice(FHIR_MedicationAdministration.StatusChoices.values) if hasattr(FHIR_MedicationAdministration, 'StatusChoices') else None
                )
                if choices_medication_code:
                    med_admin_model.medication_cc.set(med_request.medication_cc.all())
        print(f"Created {FHIR_MedicationAdministration.objects.count()} medication administrations")

        print("All mock data creation completed successfully!")