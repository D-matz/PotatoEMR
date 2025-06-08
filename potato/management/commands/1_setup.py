from django.core.management.base import BaseCommand
from django.core.management import call_command
from potato.models import *

class Command(BaseCommand):
    help = 'Runs CodingsBindingsLoad followed by mock to set up initial data'

    def handle(self, *args, **options):
        GREEN = '\033[92m'
        RESET = '\033[0m'

        print(f"{GREEN}Deleting existing patients, practitioners, and lists...{RESET}")
        FHIR_Patient.objects.all().delete()
        FHIR_Practitioner.objects.all().delete()
        FHIR_List.objects.all().delete()

        print(f"{GREEN}Loading codings and bindings...{RESET}")
        call_command('CodingsBindingsLoad')

        print(f"{GREEN}Creating LOTR patients with photos...{RESET}")
        call_command('mock_pics')

        print(f"{GREEN}Creating patients with conditions, appointments, practitioners, locations...{RESET}")
        call_command('mock_data')

        print(f"{GREEN}Creating lists...{RESET}")
        call_command('mock_lists')

        print(f"{GREEN}Setup complete!{RESET}") 