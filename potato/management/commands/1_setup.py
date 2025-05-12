from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Runs CodingsBindingsLoad followed by mock to set up initial data'

    def handle(self, *args, **options):
        GREEN = '\033[92m'
        RESET = '\033[0m'

        print(f"{GREEN}Loading codings and bindings...{RESET}")
        call_command('CodingsBindingsLoad')

        print(f"{GREEN}Creating patients with conditions, appointments, practitioners, locations...{RESET}")
        call_command('mock_data')

        print(f"{GREEN}Creating LOTR patients with photos...{RESET}")
        call_command('mock_pics')

        print(f"{GREEN}Setup complete!{RESET}") 