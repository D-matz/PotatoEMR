from django.core.management.base import BaseCommand
from potato.models import *


class Command(BaseCommand):

    def handle(self, *args, **options):
        for binding in FHIR_GP_Binding.objects.all().order_by('binding_rule'):
            print(binding.binding_rule,
                  FHIR_GP_Coding.objects.filter(codings__binding_rule=binding.binding_rule).count())
