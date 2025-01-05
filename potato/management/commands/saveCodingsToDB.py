from django.core.management.base import BaseCommand
from ...FHIR_DataTypes.FHIR_generalpurpose import FHIR_GP_Coding
import os, importlib


class Command(BaseCommand):
    help = 'Save FHIR codings from potato/FHIR_Codings'

    def handle(self, *args, **options):
        codings_dir = 'potato/FHIR_Codings'
        for filename in os.listdir(codings_dir):
            if filename.endswith('.py') and not filename.startswith('__'):
                module_name = filename[:-3]
                codingfile = importlib.import_module(f"potato.FHIR_Codings.{module_name}")
                
                numCreated = 0
                print(codingfile.system, len(codingfile.coding))
                for coding_data in codingfile.coding:
                    coding, created = FHIR_GP_Coding.objects.get_or_create(
                        system=codingfile.system,
                        code=coding_data['code'],
                        defaults={
                            'version': codingfile.version,
                            'display': coding_data['display'],
                            'userSelected': False
                        }
                    )
                    if created:
                        numCreated = numCreated + 1
                self.stdout.write(f"Created {numCreated} codings for {module_name}")
