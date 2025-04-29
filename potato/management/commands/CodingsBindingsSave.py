import os
import json
from django.core.management.base import BaseCommand
from django.core import serializers
from potato.models import FHIR_GP_Coding, FHIR_GP_Binding

class Command(BaseCommand):
    help = 'Dumps all FHIR_GP_Coding and FHIR_GP_Binding data to CodingsAndBindings.json'

    def handle(self, *args, **options):
        # Serialize both model querysets
        codings_json = serializers.serialize('json', FHIR_GP_Coding.objects.all())
        bindings_json = serializers.serialize('json', FHIR_GP_Binding.objects.all())

        # Merge and dump
        combined_data = json.loads(codings_json) + json.loads(bindings_json)

        # Write to file
        file_path = os.path.join(os.getcwd(), 'CodingsAndBindings.json')
        with open(file_path, 'w') as f:
            json.dump(combined_data, f, indent=2)

        print(f'Successfully dumped to {file_path}')
