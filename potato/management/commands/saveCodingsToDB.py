from django.core.management.base import BaseCommand
from ...FHIR_DataTypes.FHIR_generalpurpose import FHIR_GP_Coding, FHIR_GP_Binding
import os, importlib

import requests
from bs4 import BeautifulSoup
#this is just used to copy FHIR webpages into FHIR_Codings codings
import sys

def getCodingsFromFHIRValueSet(binding_url):
    response = requests.get(binding_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    codes_table = soup.find('table', {'class': 'codes'})

    codings = {}
    if codes_table:
        table = ""
        header_row = codes_table.find_all('tr')[0]
        headers = [header.get_text(strip=True) for header in header_row]
        print("headers: " + str(headers))
        rows = codes_table.find_all('tr')[1:]  # Skip header row
        for row in rows:
            cols = row.find_all('td')
            item = {}
            coding_in_system = "error system not found"
            
            for i, header in enumerate(headers):
                if header == "Code":
                    item['code'] = cols[i].get_text(strip=True)
                elif header == "System":
                    coding_in_system = cols[i].get_text(strip=True)
    #printing system then each code in it, so no need to print system in each code too
                elif header == "Display":
                    item['display'] = cols[i].get_text(strip=True)
                elif header == "Definition":
                    item['definition'] = cols[i].get_text(strip=True)

            if coding_in_system in codings:
                codings[coding_in_system].append(item)
            else:
                codings[coding_in_system] = [item]

    else:
        print("Could not find codes table on the page")

    writeCodingFile = "potato/FHIR_Codings_and_Bindings/" + binding_url.replace("http://www.", "").replace("https://www.", "").replace("/", "_").replace("-", "_").replace(".", "_") + ".py"
    print("write file: " + writeCodingFile)
    coding_file = open(writeCodingFile, 'w', encoding='utf-8')
    coding_file.write("binding = \"" + binding_url + "\"\n")
    coding_file.write("codings = [\n")
    for coding_system in codings:
        print("write system: " + coding_system)
        coding_file.write("{\n")
        coding_file.write("\"system\" : \"" + coding_system + "\",\n")
        coding_file.write("\"version\" : \"???\",\n")
        coding_file.write("\"coding\" : " + str(codings[coding_system]) + "\n")
        coding_file.write("},\n")
    coding_file.write("]\n")



class Command(BaseCommand):
    help = 'Save FHIR codings from potato/FHIR_Codings_and_Bindings'

    def add_arguments(self, parser):
        parser.add_argument('binding_url', type=str, nargs='?', default=None)

    def handle(self, *args, **options):
        binding_url = options['binding_url']
        if binding_url:
            getCodingsFromFHIRValueSet(binding_url)

        codings_dir = 'potato/FHIR_Codings_and_Bindings'
        for filename in os.listdir(codings_dir):
            if filename.endswith('.py') and not filename.startswith('__'):
                module_name = filename[:-3]
                codingfile = importlib.import_module(f"potato.FHIR_Codings_and_Bindings.{module_name}")
                #this file has a binding_rule, which could be just a url to a valueset, a rule, whatever, some string
                #also has a list of codings, each with system, version, and list of [{'code': '...', 'display': '...', 'definition': '...'}]

                binding_model, created = FHIR_GP_Binding.objects.get_or_create(binding_rule=codingfile.binding)

                #save each coding in coding file, if the coding doesnt exist already
                numCodingsCreated = 0
                for coding_system in codingfile.codings:
                    for coding_data in coding_system['coding']:
                        coding_model, created = FHIR_GP_Coding.objects.get_or_create(
                            system=coding_system['system'],
                            version=coding_system['version'],
                            code=coding_data['code'],
                            display=coding_data['display'],
                            userSelected=False,
                        )
                        #print(coding_model, binding_model)
                        binding_model.binding_codings.add(coding_model)
                        
                        if created:
                            numCodingsCreated += 1                    

                print(f"Created {numCodingsCreated} codings for {module_name}")

