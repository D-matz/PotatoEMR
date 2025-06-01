from django.core.management.base import BaseCommand
from potato.models import *
import os, importlib

import requests
from bs4 import BeautifulSoup

#use to get codings from fhir page and save to db:
#python manage.py saveCodingsToDB https://hl7.org/fhir/valueset-condition-clinical.html
class Command(BaseCommand):
    help = f'''Save FHIR codings from potato/FHIR_Codings_and_Bindings,
add argument such as https://hl7.org/fhir/valueset-condition-clinical.html'''

    def add_arguments(self, parser):
        parser.add_argument('binding_url', type=str, nargs='?', default=None)

    def handle(self, *args, **options):
        binding_url = options['binding_url']
        response = requests.get(binding_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        codes_table = soup.find('table', {'class': 'codes'})

        if not codes_table:
            print("Could not find codes table on the page")
            return

        binding_model, created = FHIR_GP_Binding.objects.get_or_create(binding_rule=binding_url)
        numCodingsCreated = 0

        header_row = codes_table.find_all('tr')[0]
        headers = [header.get_text(strip=True) for header in header_row]
        print("headers: " + str(headers))
        
        current_system = None
        for row in codes_table.find_all('tr')[1:]:  # Skip header row
            cols = row.find_all('td')
            code = display = definition = None
            
            for i, header in enumerate(headers):
                if header == "Code":
                    code = cols[i].get_text(strip=True)
                elif header == "System":
                    current_system = cols[i].get_text(strip=True)
                elif header == "Display":
                    display = cols[i].get_text(strip=True)
                elif header == "Definition":
                    definition = cols[i].get_text(strip=True)
            
            if code and current_system:
                coding_model, created = FHIR_GP_Coding.objects.get_or_create(
                    system=current_system,
                    version="???",  # Keeping the same version placeholder
                    code=code,
                    display=display or "",
                    userSelected=False,
                )
                binding_model.binding_codings.add(coding_model)
                
                if created:
                    numCodingsCreated += 1
                    
        print(f"Created {numCodingsCreated} codings for {binding_url}")