from django.core.management.base import BaseCommand
from potato.models import *

class Command(BaseCommand):

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        for a in FHIR_AllergyIntolerance.objects.all():
            a.delete()