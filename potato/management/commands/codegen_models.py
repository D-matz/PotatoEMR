from django.core.management.base import BaseCommand
import requests
import json

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

#codegen in PotatoEMR/potato/management/commands/codegen_models.py
#run with: python manage.py codegen_models

print_model_start = '''
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_replace_classname(replace_model):
'''


def elementArray_to_ModelString(element_array):
    #print("call with num elements", len(element_array))
    this_model_lines = ""
    related_model_lines = ""

    i = 0 #looping like this to skip backbone elements and recurse for them
    while i < len(element_array):
        field = element_array[i]
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

        if use_id == None:
            i = i + 1
            continue
        id_split = use_id.split('.')
        #print(i, use_type, id_split)
        if len(id_split) < 2:
            i = i + 1
            continue #element name itself
        elif id_split[1].lower() in ["id", "meta", "implicitrules", "language", "text", "contained"]:
            #not using stuff not in narrative before identifier
            i = i + 1
            continue
        elif use_type in ["extension", "modifierextension", "http://hl7.org/fhirpath/system.string"]:
            i = i + 1
            #not using stuff in backboneElement beginning
            continue
        else:
            #a field we want to use
            field_name = id_split[-1]
            if use_type == "backboneelement":
                related_model_lines += f'''
class FHIR_{"_".join(id_split)}(models.Model):
    {field_name} = models.ForeignKey(FHIR_{"_".join(id_split[:-1])}, related_name='{field_name}', null=False, on_delete=models.CASCADE')'''
                backbone_min_len = len(id_split) + 1
                backbone_array = []
                i = i + 1
                while(i < len(element_array) and len(element_array[i]['id'].split('.')) >= backbone_min_len):
                    backbone_array.append(element_array[i])
                    i = i + 1
                #recurse for all elements in backbone
                all_model_lines_in_backbone = elementArray_to_ModelString(backbone_array)
                #print("backbone", all_model_lines_in_backbone)
                related_model_lines += all_model_lines_in_backbone
                continue
            elif use_type in FHIR_to_Model_primitive:
                if use_max == '*':
                    related_model_lines += f'''
class FHIR_{"_".join(id_split)}(models.Model):
    {field_name} = models.ForeignKey(FHIR_{"_".join(id_split[:-1])}, related_name='{field_name}', null=False, on_delete=models.CASCADE)
'''
                else:
                    options = ""
                    this_model_lines += f'''
    {field_name} = {FHIR_to_Model_primitive[use_type]}({options})'''
            elif use_type in FHIR_to_Model_generalpurpose:
                use_type_model = FHIR_to_Model_generalpurpose[use_type]
                if use_max == '*':
                    related_model_lines += f'''
class FHIR_{"_".join(id_split)}({use_type_model}):
    {field_name} = models.ForeignKey({"_".join(id_split[:-1])}, related_name='{field_name}', null=False, on_delete=models.CASCADE')
'''
                else:
                    this_model_lines += f'''
    {field_name} = models.OneToOneField({use_type_model}, related_name='{field_name}', null=True, blank=True, on_delete=models.SET_NULL)'''
            elif use_type == "reference":
                reference_targets =  field['type'][0]['targetProfile']
                for ref_target in reference_targets:
                    model_target = ref_target.replace("http://hl7.org/fhir/StructureDefinition/", "")
                    if use_max == '*':
                        this_model_lines += f'''
    {field_name}_{model_target} = models.ManyToManyField("FHIR_{model_target}", related_name="{field_name}_{model_target}", blank=True)'''
                    else:
                        this_model_lines += f'''
    {field_name}_{model_target} = models.ForeignKey("FHIR_{model_target}", related_name="{field_name}_{model_target}", null=True, blank=True, on_delete=models.SET_NULL)'''

        i = i + 1

    return this_model_lines + "\n" + related_model_lines

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("generating FHIR Resource models")
        # URL of the FHIR MedicationRequest profile JSON

        FHIR_Resource_name = "MedicationRequest"

        print("codegen: " +FHIR_Resource_name)

        url = "https://build.fhir.org/" + FHIR_Resource_name.lower() + ".profile.canonical.json"

        # Download the JSON content
        response = requests.get(url)
        response.raise_for_status()  # Raise exception if request failed

        # Parse the JSON
        data = response.json()
        FHIR_Resource = data['snapshot']['element']


        #0..* or 1..* elements can have multiple
        #need to put 0..* elements at end, in own model with foreign key to this model
        #but if backboneElement is 0..*, need to recurse for all elements in it


        all_model_lines = elementArray_to_ModelString(FHIR_Resource)
        print("result", all_model_lines)