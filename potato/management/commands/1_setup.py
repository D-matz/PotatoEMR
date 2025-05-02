from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Runs CodingsBindingsLoad followed by mock to set up initial data'

    def handle(self, *args, **options):
        GREEN = '\033[92m'
        RESET = '\033[0m'

        print(f"{GREEN}Loading codings and bindings...{RESET}")
        call_command('CodingsBindingsLoad')

        print(f"{GREEN}Creating mock data...{RESET}")
        call_command('mock')

        print(f"{GREEN}Setup complete!{RESET}") 