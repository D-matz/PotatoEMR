from django.test import TestCase
from potato.models import *
from datetime import date, datetime

class FHIRPatientTest(TestCase):
    def test_patient_name_value(self):
        birth_date_instance = FHIR_primitive_DateField.objects.create(date=date(1990, 5, 15))
        p = FHIR_Patient.objects.create(birth_date=birth_date_instance)
        p.save()
        self.assertEqual(str(p), "Unnamed Patient")

        name1 = FHIR_Patient_Name.objects.create(
            patient=p,
            text="bob moses"
        )
        name1.save()
        self.assertEqual(str(p), "bob moses")


        name2 = FHIR_Patient_Name.objects.create(
            patient=p,
            text="mr power broker"
        )
        name2.save()
        self.assertEqual(str(p), "bob moses, mr power broker")
