from django.core.management.base import BaseCommand
import requests
import json


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("generating FHIR Resource models")
        # URL of the FHIR MedicationRequest profile JSON

        FHIR_Resource_name = "MedicationRequest"

        print("codegen: " +FHIR_Resource_name)

        url = "https://www.hl7.org/fhir/" + FHIR_Resource_name + ".profile.canonical.json"

        # Download the JSON content
        response = requests.get(url)
        response.raise_for_status()  # Raise exception if request failed

        # Parse the JSON
        data = response.json()
        element = data['snapshot']['element']

        FHIR_to_Model_primitive = {
            #primitive types from PotatoEMR\potato\models_dir\FHIR_DataTypes\FHIR_primitive.py
            'Base64Binary' : 'FHIR_primitive_Base64BinaryField',
            'boolean' : 'FHIR_primitive_BooleanField',
            'canonical' : 'FHIR_primitive_CanonicalField',
            'code' : 'FHIR_primitive_CodeField',
            'date' : 'FHIR_primitive_DateField',
            'dateTime' : 'FHIR_primitive_DateTimeField',
            'DateTimeField': 'FHIR_primitive_DateTimeField',
            'Decimal' : 'FHIR_primitive_DecimalField',
            'id' : 'FHIR_primitive_IdField',
            'instant' : 'FHIR_primitive_InstantField',
            'signedInt64' : 'FHIR_primitive_SignedInt64Field',
            'signedInt' : 'FHIR_primitive_SignedIntField',
            'markdown' : 'FHIR_primitive_MarkdownField',
            'oid' : 'FHIR_primitive_OID_Field',
            'string' : 'FHIR_primitive_StringField',
            'positiveInt' : 'FHIR_primitive_PositiveIntField',
            'time' : 'FHIR_primitive_TimeField',
            'UnsignedInt' : 'FHIR_primitive_UnsignedIntField',
            'URI' : 'FHIR_primitive_URIField',
            'URL' : 'FHIR_primitive_URLField',
            'UUID' : 'FHIR_primitive_UUIDField',
        }
        FHIR_to_Model_generalpurpose = {
            #general purpose types from PotatoEMR\potato\models_dir\FHIR_DataTypes\FHIR_generalpurpose.py
            'Attachment' : 'FHIR_GP_Attachment',
            'coding' : 'FHIR_GP_Coding',
            'quantity' : 'FHIR_GP_Quantity',
            'distance' : 'FHIR_GP_Quantity_Distance',
            'time' : 'FHIR_GP_Quantity_Time',
            'age' : 'FHIR_GP_Quantity_Age',
            'duration' : 'FHIR_GP_Quantity_Duration',
            'simpleQuantity' : 'FHIR_GP_Quantity_Simple',
            'money' : 'FHIR_GP_Quantity_Money',
            'Range' : 'FHIR_GP_Range',
            'Ratio' : 'FHIR_GP_Ratio',
            'Ratio_Range' : 'FHIR_GP_Ratio_Range',
            'period' : 'FHIR_GP_Period',
            'sampledData' : 'FHIR_GP_SampledData',
            'identifier' : 'FHIR_GP_Identifier',
            'humanName' : 'FHIR_GP_HumanName',
            'address' : 'FHIR_GP_Address',
            'contactPoint' : 'FHIR_GP_ContactPoint',
            'signature' : 'FHIR_GP_Signature',
            'Annotation' : 'FHIR_GP_Annotation',
            'Timing' : 'FHIR_GP_Timing',

            #special purpose types from PotatoEMR\potato\models_dir\FHIR_DataTypes\FHIR_specialpurpose.py
            'Meta' : 'FHIR_SP_Meta',
            'Meta_Profile' : 'FHIR_SP_Meta_Profile',
            'Meta_Security' : 'FHIR_SP_Meta_Security',
            'Meta_Tag' : 'FHIR_SP_Meta_Tag',
            'Dosage' : 'FHIR_SP_Dosage',

            #metadata types from PotatoEMR\potato\models_dir\FHIR_DataTypes\FHIR_metadata.py
            'ExtendedContactDetail' : 'FHIR_meta_ExtendedContactDetail',
            'VirtualServiceDetail' : 'FHIR_meta_VirtualServiceDetail',

            #reference to another FHIR resource
            'Reference' : 'models.ForeignKey(replace_resource, blank=replace_blank, null=replace_null, on_delete=models.replace_delete)',

            #codeableconcept and codeablereference
        }
        lower_FHIR_to_Model_primitive = {k.lower(): v for k, v in FHIR_to_Model_primitive.items()}
        lower_FHIR_to_Model_generalpurpose = {k.lower(): v for k, v in FHIR_to_Model_generalpurpose.items()}

        model_template_zero_one = "replace_field = models.OneToOneField(replace_model, related_name='replace_related', null=True, on_delete=models.SET_NULL)\n"
        model_template_one_one  = "replace_field = models.OneToOneField(replace_model, related_name='replace_related', null=False, on_delete=models.CASCADE)\n"
        model_template_many = '''
class FHIR_replace_classname(replace_model):
    replace_field = models.ForeignKey(replace_resource, related_name='replace_related', null=False, on_delete=models.CASCADE')
'''

        primitive_template_zero_one = "replace_field = replace_primitive(replace_options, blank=True, Null=True)\n"
        primitive_template_one_one = "replace_field = replace_primitive(replace_options, blank=False, Null=False)\n"
        primitive_template_many = '''
class FHIR_replace_classname(replace_model):
    replace_field = replace_primitive(replace_options, blank=False, Null=False)
'''

        ignoringEverythingBeforeIdentifier = True
        ignoringThreeAfterBackbone = 0

        currently_in_backbone = None
        #tricky thing is if the backbone element is 0..*
        #will need to make a new class with this backbone fields, and put it after the model

        print_lines = '''
#codegen in PotatoEMR/potato/management/commands/codegen_models.py
#run with: python manage.py codegen_models

from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_replace_classname(replace_model):
'''

        print_lines_after = []

        for field in element:
            use_id = None
            use_type = None
            use_min = None
            use_max = None
            if 'id' in field:
                use_id = field['id']
            if 'min' in field:
                use_min = field['min']
            if 'max' in field:
                use_max = field['max']
            if 'type' in field:
                field_type = field['type']
                if len(field_type ) > 0:
                    first_type = field_type[0]
                    if 'code' in first_type:
                        use_type = first_type['code'].lower()
            
            if use_id == None: continue
            if use_id.lower() == FHIR_Resource_name.lower(): continue
            id_split = use_id.split('.')[1:]

            if id_split[0] == "identifier":
                ignoringEverythingBeforeIdentifier = False
            if ignoringEverythingBeforeIdentifier:
                #not using stuff not in narrative before identifier
                continue
            if ignoringThreeAfterBackbone > 0:
                #not using stuff not in narrative after backbone element
                #you can tell where stuff belongs in backbone by its split id
                ignoringThreeAfterBackbone -= 1
                continue


            if use_type == "backboneelement":
                ignoringThreeAfterBackbone = 3
                continue

            elif use_type in lower_FHIR_to_Model_primitive:
                field_name = id_split[0]
                if use_max == '*':
                    template_str = primitive_template_many
                    template_str = template_str.replace("replace_field", field_name)
                    template_str = template_str.replace("replace_options", "")
                    print_lines += template_str
                else:
                    if use_min == '0':
                        template_str = primitive_template_zero_one
                    else:
                        template_str = primitive_template_one_one
                    template_str = template_str.replace("replace_field", field_name)
                    template_str = template_str.replace("replace_options", "")
                    print_lines += template_str

            elif use_type in lower_FHIR_to_Model_generalpurpose:
                print("generalpurpose", id_split, lower_FHIR_to_Model_generalpurpose[use_type], use_min, use_max)
                field_name = id_split[0]
                if use_max == '*':
                    template_str = model_template_many
                else:
                    template_str = model_template_one_one
                template_str = template_str.replace("replace_field", field_name)
                template_str = template_str.replace("replace_model", "FHIR_" + FHIR_Resource_name)
                template_str = template_str.replace("replace_resource", "FHIR_" + FHIR_Resource_name)
                print_lines += template_str

            elif use_type == "codeableconcept":
                #print(id_split, "CodeableConcept", use_min, use_max)
                pass
            elif use_type == "codeablereference":
                #print(id_split, "CodeableReference", use_min, use_max)
                pass
            else:
                print(use_type, id_split[0], "unknown type")


        print(print_lines)