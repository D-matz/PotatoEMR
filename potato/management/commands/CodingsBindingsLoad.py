import os
import json
from django.core.management.base import BaseCommand
from django.core import serializers
from potato.models import FHIR_GP_Coding, FHIR_GP_Binding

class Command(BaseCommand):
    help = 'Loads FHIR_GP_Coding and FHIR_GP_Binding data from CodingsAndBindings.json'

    #hard question is what to do if models are using codings/bindings not in this json
    #if we delete those codings/bindings, those codeableconcept fields in model will go blank
    def handle(self, *args, **options):
        file_path = os.path.join(os.getcwd(), 'potato', 'management', 'commands', 'CodingsAndBindings.json')
        try:
            with open(file_path, 'r') as f:
                combined_data = json.load(f)

            # Create a mapping of existing records by their natural key
            existing_codings = {
                (c.system, c.code) 
                for c in FHIR_GP_Coding.objects.all()
            }
            
            for obj in serializers.deserialize('json', json.dumps(combined_data)):
                if isinstance(obj.object, FHIR_GP_Coding):
                    key = (obj.object.system, obj.object.code)
                    if key not in existing_codings:
                        obj.save()
                else:
                    obj.save()

            print(f'Successfully loaded data from {file_path}')
        except FileNotFoundError:
            print(f'File not found: {file_path}')
        except json.JSONDecodeError:
            print(f'Invalid JSON in file: {file_path}')
