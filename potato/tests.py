from django.test import TestCase
from potato.models import *
from datetime import date, datetime

class FHIRPatientFieldsTest(TestCase):
    def test_patient_name_value(self):
        p = FHIR_Patient()
        bday = FHIR_primitive_DateField()
        bday.date = date(1990, 1, 1)
        bday.save()
        p.birth_date = bday
        p.save()
        self.assertEqual(str(p), "Unnamed Patient")

        n = FHIR_GP_HumanName()
        n.text = "bob moses"
        n.save()
        fpn = FHIR_Patient_Name()
        fpn.patient = p
        fpn.name = n
        fpn.save()
        self.assertEqual(str(p), "bob moses")

        n1 = FHIR_GP_HumanName()
        n1.text = "mr power broker"
        n1.save()
        fpn1 = FHIR_Patient_Name()
        fpn1.patient = p
        fpn1.name = n1
        fpn1.save()
        self.assertEqual(str(p), "bob moses, mr power broker")

        telecom_instance = FHIR_GP_ContactPoint()
        telecom_instance.save()
        patient_telecom = FHIR_Patient_Telecom.objects.create(
            telecom=telecom_instance,
            patient=p
        )
        deathTime = FHIR_primitive_DateTimeField()
        deathTime.datetime = datetime(1999, 1, 1)
        deathTime.save()

        practitioner_instance = FHIR_Practitioner()
        practitioner_instance.save()

        p.active = True
        p.gender = FHIR_Patient.GenderChoices.MALE
        p.deceased_date_time = deathTime
        p.marital_status=FHIR_Patient.MaritalStatus.MARRIED
        p.multiple_birth_boolean = False
        p.generalPractitioners_practitioner.add(practitioner_instance)

        
