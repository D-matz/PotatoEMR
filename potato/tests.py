from django.test import TestCase
from potato.models import *

class FHIRPatientNameTest(TestCase):
    def test_patient_name_value(self):
        p = FHIR_Patient()
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
