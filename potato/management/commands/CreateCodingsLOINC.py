from django.core.management.base import BaseCommand
from potato.models import *

class Command(BaseCommand):

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        # Create LOINC codings for vital signs
        vital_signs_codings = [
            {
                'system': 'http://loinc.org',
                'code': '85353-1',
                'display': 'Vital signs, weight, height, head circumference, oxygen saturation and BMI panel'
            },
            {
                'system': 'http://loinc.org',
                'code': '9279-1',
                'display': 'Respiratory Rate'
            },
            {
                'system': 'http://loinc.org',
                'code': '8867-4',
                'display': 'Heart rate'
            },
            {
                'system': 'http://loinc.org',
                'code': '2708-6',
                'display': 'Oxygen saturation in Arterial blood'
            },
            {
                'system': 'http://loinc.org',
                'code': '8310-5',
                'display': 'Body temperature'
            },
            {
                'system': 'http://loinc.org',
                'code': '8302-2',
                'display': 'Body height'
            },
            {
                'system': 'http://loinc.org',
                'code': '9843-4',
                'display': 'Head Occipital-frontal circumference'
            },
            {
                'system': 'http://loinc.org',
                'code': '29463-7',
                'display': 'Body weight'
            },
            {
                'system': 'http://loinc.org',
                'code': '39156-5',
                'display': 'Body mass index (BMI) [Ratio]'
            },
            {
                'system': 'http://loinc.org',
                'code': '85354-9',
                'display': 'Blood pressure panel with all children optional'
            },
            {
                'system': 'http://loinc.org',
                'code': '8480-6',
                'display': 'Systolic blood pressure'
            },
            {
                'system': 'http://loinc.org',
                'code': '8462-4',
                'display': 'Diastolic blood pressure'
            },
            {
                'system': 'http://loinc.org',
                'code': '3137-7',
                'display': 'Body height Measured'
            },
            {
                'system': 'http://loinc.org',
                'code': '3138-5',
                'display': 'Body height Stated'
            },
            {
                'system': 'http://loinc.org',
                'code': '8301-4',
                'display': 'Body height Estimated'
            },
            {
                'system': 'http://loinc.org',
                'code': '8305-5',
                'display': 'Body height --post partum'
            },
            {
                'system': 'http://loinc.org',
                'code': '8306-3',
                'display': 'Body height --lying'
            },
            {
                'system': 'http://loinc.org',
                'code': '8307-1',
                'display': 'Body height --preoperative'
            },
            {
                'system': 'http://loinc.org',
                'code': '8308-9',
                'display': 'Body height --standing'
            },
            {
                'system': 'http://loinc.org',
                'code': '92999-2',
                'display': 'Body height --sitting'
            }
        ]

        # Create a binding for LOINC vital signs
        binding, created = FHIR_GP_Binding.objects.get_or_create(
            binding_rule="http://loinc.org"
        )

        # Create codings and associate with binding
        for coding_data in vital_signs_codings:
            coding, created = FHIR_GP_Coding.objects.get_or_create(
                system=coding_data['system'],
                code=coding_data['code'],
                defaults={'display': coding_data['display']}
            )
            binding.binding_codings.add(coding)

        self.stdout.write(self.style.SUCCESS('Successfully created LOINC vital signs codings'))
        