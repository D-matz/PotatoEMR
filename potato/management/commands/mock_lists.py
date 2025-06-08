from django.core.management.base import BaseCommand
from potato.models import *
import random

class Command(BaseCommand):
    def handle(self, *args, **options):

        #if no list with name "middle earth" exists, create one with all luthien patients as items
        middle_earth_list = FHIR_List.objects.filter(title="Middle Earth").first()
        if not middle_earth_list:
            middle_earth_list = FHIR_List.objects.create(
                title="Middle Earth"
            )
            luthien_practitioner = FHIR_Practitioner.objects.filter(Practitioner_name__text__contains='Lúthien Tinúviel').first()
            if luthien_practitioner:
                for patient in FHIR_Patient.objects.filter(generalPractitioner_Practitioner=luthien_practitioner):
                    FHIR_List_entry.objects.create(
                        List=middle_earth_list,
                        item_Patient=patient
                    )

        condition_list = FHIR_List.objects.filter(title="Conditions").first()
        if not condition_list:
            condition_list = FHIR_List.objects.create(
                title="Example list 2"
            )
            for patient in FHIR_Patient.objects.filter(Condition_subject__isnull=False).distinct():
                if random.random() < 0.5:
                    FHIR_List_entry.objects.create(
                        List=condition_list,
                        item_Patient=patient
                    )