#python potato/models_dir/Codegen/codegen_models.py -overwrite
#writes to potato/models_dir/Codegen/codegen_models_output,
#add -overwrite to directly overwrite models in potato/models_dir/Codegen/FHIR_Resources

from django.core.management.base import BaseCommand
import requests
import json
import os
import sys

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
    #codeableconcept and codeablereference
}
lower_FHIR_to_Model_primitive = {k.lower(): v for k, v in FHIR_to_Model_primitive.items()}
lower_FHIR_to_Model_generalpurpose = {k.lower(): v for k, v in FHIR_to_Model_generalpurpose.items()}

default_bindings = {
    "AllergyIntolerance": {
        "BINDING_clinicalStatus": 'https://www.hl7.org/fhir/valueset-allergyintolerance-clinical.html',
        "BINDING_verificationStatus": 'https://www.hl7.org/fhir/valueset-allergyintolerance-verification.html',
        "BINDING_type": 'https://www.hl7.org/fhir/valueset-allergy-intolerance-type.html',
        "BINDING_code": 'https://www.hl7.org/fhir/valueset-allergyintolerance-code.html',
        "BINDING_substance": 'https://www.hl7.org/fhir/valueset-substance-code.html',
        "BINDING_exposureRoute": 'https://www.hl7.org/fhir/valueset-route-codes.html',
        "BINDING_manifestation": 'https://www.hl7.org/fhir/valueset-clinical-findings.html',
    },
    "Condition":{
        "BINDING_clinicalStatus": 'https://hl7.org/fhir/valueset-condition-clinical.html',
        "BINDING_verificationStatus": 'http://hl7.org/fhir/valueset-condition-ver-status.html',
        "BINDING_severity": 'https://build.fhir.org/valueset-condition-severity.html',
        "BINDING_code": 'https://build.fhir.org/valueset-condition-code.html',
    }
}

default_strs = {
    "FHIR_Patient": "patient_names = [name.text for name in self.Patient_name.all() if name.text]; return ', '.join(patient_names) if patient_names else 'Unnamed Patient'"
}

def elementArray_to_ModelString(element_array, FHIR_Resource_name):
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

            #in cases like allowed[x] one field can have multiple types
            #split these into multiple fields
            if len(field_type) > 1:
                new_fields = []
                for possible_type in field_type:
                    new_field = field.copy()
                    new_field['type'] = [possible_type]
                    new_field['id'] = new_field['id'][:-3] + "_" + possible_type['code']
                    #onset[x] to onset_dateTime, onset_Age, etc
                    new_fields.append(new_field)
                element_array[i+1:i+1] = new_fields
                i = i + 1
                continue

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
            if field_name.endswith('[x]'):
                field_name = field_name[:-3]
                #TODO maybe dont need this
                #we already split cases like allowed[x] into multiple fields
            related_name = use_id.replace('.', '_')
            if related_name.endswith('[x]'):
                related_name = related_name[:-3]
            if use_type == "backboneelement":
                related_model_lines += f'''
class FHIR_{"_".join(id_split)}(models.Model):
    {"_".join(id_split[:-1])} = models.ForeignKey(FHIR_{"_".join(id_split[:-1])}, related_name='{related_name}', null=False, on_delete=models.CASCADE)'''
                backbone_min_len = len(id_split) + 1
                backbone_array = []
                i = i + 1
                while(i < len(element_array) and len(element_array[i]['id'].split('.')) >= backbone_min_len):
                    backbone_array.append(element_array[i])
                    i = i + 1
                #recurse for all elements in backbone
                all_model_lines_in_backbone = elementArray_to_ModelString(backbone_array, FHIR_Resource_name)
                #print("backbone", all_model_lines_in_backbone)
                related_model_lines += all_model_lines_in_backbone
                continue

            #primitive types implemented as a single field
            elif use_type in lower_FHIR_to_Model_primitive:
                code_choices = ""
                field_options = ""
                field_null = "null=True, blank=True, "
                if use_min == '1':
                    field_null = "null=False, blank=False, "
                if use_type == 'code':
                    field_options += f'''choices={field_name.capitalize()}Choices.choices, '''
                    if '|' in field['short']:
                        code_list = field['short'].split(' | ')
                    else:
                        code_list = ['TODO']
                    code_choices = f'''
    class {field_name.capitalize()}Choices(models.TextChoices): '''
                    for code in code_list:
                        code_choices += f"{code.replace('>=', 'GREATER_THAN_OR_EQUALS').replace('<=', 'LESS_THAN_OR_EQUALS').replace('>', 'GREATER_THAN').replace('<', 'LESS_THAN').replace('!=', 'NOT_EQUALS').replace('=', 'EQUALS').replace('+', 'PLUS').replace('-', '_').replace(' ', '_').replace('(', '').replace(')', '').upper()} = '{code}', '{code.capitalize()}'; "
                if use_max == '*':
                    related_model_lines += f'''
class FHIR_{"_".join(id_split)}(models.Model):
    {"_".join(id_split[:-1])} = models.ForeignKey(FHIR_{"_".join(id_split[:-1])}, related_name='{related_name}', null=False, on_delete=models.CASCADE)
    {code_choices}
    {field_name} = {lower_FHIR_to_Model_primitive[use_type]}({field_options}{field_null})
    '''
                else:
                    this_model_lines += f'''{code_choices}
    {field_name} = {lower_FHIR_to_Model_primitive[use_type]}({field_options}{field_null})'''

            #general purpose types implemented as a model
            elif use_type in lower_FHIR_to_Model_generalpurpose:
                use_type_model = lower_FHIR_to_Model_generalpurpose[use_type]
                oneToOne_null = "null=True, blank=True, on_delete=models.SET_NULL"
                if use_min == '1':
                    oneToOne_null = "null=False, blank=False, on_delete=models.CASCADE"
                if use_max == '*':
                    related_model_lines += f'''
class FHIR_{"_".join(id_split)}({use_type_model}):
    {"_".join(id_split[:-1])} = models.ForeignKey(FHIR_{"_".join(id_split[:-1])}, related_name='{related_name}', null=False, on_delete=models.CASCADE)
'''
                else:
                    this_model_lines += f'''
    {field_name} = models.OneToOneField("{use_type_model}", related_name='{related_name}', {oneToOne_null})'''

            #reference to another model representing a FHIR resource
            elif use_type == "reference":
                #not going to do anything with Reference(<no target resource here)
                if 'targetProfile' in field['type'][0]:
                    reference_targets =  field['type'][0]['targetProfile']
                    for ref_target in reference_targets:
                        model_target = ref_target.replace("http://hl7.org/fhir/StructureDefinition/", "")
                        if model_target == "Resource": continue #skip "Any" fields that can be any fhir resource
                        ref_field_name = field_name + "_" + model_target #add model target in case field can be actor_Patient, actor_Group, etc
                        if len(reference_targets) == 1:
                            ref_field_name = field_name #dumb looking to have actor_Patient if actor can only be Patient, then just actor is good
                        if use_max == '*':
                            this_model_lines += f'''
    {ref_field_name} = models.ManyToManyField("FHIR_{model_target}", related_name="{related_name}", blank=True)'''
                        else:
                            this_model_lines += f'''
    {ref_field_name} = models.ForeignKey("FHIR_{model_target}", related_name="{related_name}", null=True, blank=True, on_delete=models.SET_NULL)'''

            #codeableconcept has set of codings from its binding set, and a text field
            #codeablereference has that plus reference(s) to another model representing a FHIR resource
            elif use_type == "codeableconcept" or use_type == "codeablereference":
                binding_str = "BINDING_" + field_name
                binding_chosen = "TODO"
                if FHIR_Resource_name in default_bindings and binding_str in default_bindings[FHIR_Resource_name]:
                    binding_chosen = default_bindings[FHIR_Resource_name][binding_str]
                cc = f'''
    {binding_str} = "{binding_chosen}"
    {field_name}_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={{"codings__binding_rule": BINDING_{field_name}}}, related_name='{related_name}', blank=True)
    {field_name}_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)'''
                if use_type == 'codeableconcept':
                    if use_max == '*':
                        related_model_lines += f'''
class FHIR_{"_".join(id_split)}(models.Model):
    {"_".join(id_split[:-1])} = models.ForeignKey(FHIR_{"_".join(id_split[:-1])}, related_name='{related_name}', null=False, on_delete=models.CASCADE){cc}
    '''
                    else:
                        this_model_lines += cc
                elif use_type == "codeablereference":
                    #not going to do anything with Reference(<no target resource here)
                    if 'targetProfile' in field['type'][0]:
                        reference_targets =  field['type'][0]['targetProfile']
                        reference_list = ""
                        for ref_target in reference_targets:
                            model_target = ref_target.replace("http://hl7.org/fhir/StructureDefinition/", "")
                            if model_target == "Resource": continue #skip "Any" fields that can be any fhir resource
                            reference_list += f'''
    {field_name}_{model_target}_ref = models.ForeignKey("FHIR_{model_target}", related_name="{related_name}_{model_target}", null=True, blank=True, on_delete=models.SET_NULL)'''

                        if use_max == '*':
                            related_model_lines += f'''
class FHIR_{"_".join(id_split)}(models.Model):
    {"_".join(id_split[:-1])} = models.ForeignKey(FHIR_{"_".join(id_split[:-1])}, related_name='{related_name}', null=False, on_delete=models.CASCADE){cc}''' + reference_list + "\n"
                        else:
                            this_model_lines += (cc + reference_list)

            else:
                print("unknown type", use_type, field_name)

        i = i + 1

    return this_model_lines + "\n" + related_model_lines


overwrite = "-overwrite" in sys.argv
base_dir = "potato/models_dir"
output_dir = os.path.join("potato/models_dir", "FHIR_Resources" if overwrite else "Codegen/codegen_models_output")
print("generating FHIR Resource models")

FHIR_resource_list = ['Account', 'ActivityDefinition', 'ActorDefinition', 'AdministrableProductDefinition', 'AdverseEvent', 'AllergyIntolerance', 'Appointment', 'AppointmentResponse', 'ArtifactAssessment', 'AuditEvent', 'Basic', 'Binary', 'BiologicallyDerivedProduct', 'BiologicallyDerivedProductDispense', 'BodyStructure', 'Bundle', 'CapabilityStatement', 'CarePlan', 'CareTeam', 'ChargeItem', 'ChargeItemDefinition', 'Citation', 'Claim', 'ClaimResponse', 'ClinicalAssessment', 'ClinicalUseDefinition', 'CodeSystem', 'Communication', 'CommunicationRequest', 'CompartmentDefinition', 'Composition', 'ConceptMap', 'Condition', 'ConditionDefinition', 'Consent', 'Contract', 'Coverage', 'CoverageEligibilityRequest', 'CoverageEligibilityResponse', 'DetectedIssue', 'Device', 'DeviceAlert', 'DeviceAssociation', 'DeviceDefinition', 'DeviceDispense', 'DeviceMetric', 'DeviceRequest', 'DeviceUsage', 'DiagnosticReport', 'DocumentReference', 'Encounter', 'EncounterHistory', 'Endpoint', 'EnrollmentRequest', 'EnrollmentResponse', 'EpisodeOfCare', 'EventDefinition', 'Evidence', 'EvidenceVariable', 'ExampleScenario', 'ExplanationOfBenefit', 'FamilyMemberHistory', 'Flag', 'FormularyItem', 'GenomicStudy', 'Goal', 'GraphDefinition', 'Group', 'GuidanceResponse', 'HealthcareService', 'ImagingSelection', 'ImagingStudy', 'Immunization', 'ImmunizationEvaluation', 'ImmunizationRecommendation', 'ImplementationGuide', 'Ingredient', 'InsurancePlan', 'InsuranceProduct', 'InventoryItem', 'InventoryReport', 'Invoice', 'Library', 'Linkage', 'List', 'Location', 'ManufacturedItemDefinition', 'Measure', 'MeasureReport', 'Medication', 'MedicationAdministration', 'MedicationDispense', 'MedicationKnowledge', 'MedicationRequest', 'MedicationStatement', 'MedicinalProductDefinition', 'MessageDefinition', 'MessageHeader', 'MolecularDefinition', 'MolecularSequence', 'NamingSystem', 'NutritionIntake', 'NutritionOrder', 'NutritionProduct', 'Observation', 'ObservationDefinition', 'OperationDefinition', 'OperationOutcome', 'Organization', 'OrganizationAffiliation', 'PackagedProductDefinition', 'Parameters', 'Patient', 'PaymentNotice', 'PaymentReconciliation', 'Permission', 'Person', 'PersonalRelationship', 'PlanDefinition', 'Practitioner', 'PractitionerRole', 'Procedure', 'Provenance', 'Questionnaire', 'QuestionnaireResponse', 'RegulatedAuthorization', 'RelatedPerson', 'RequestOrchestration', 'Requirements', 'ResearchStudy', 'ResearchSubject', 'RiskAssessment', 'Schedule', 'SearchParameter', 'ServiceRequest', 'Slot', 'Specimen', 'SpecimenDefinition', 'StructureDefinition', 'StructureMap', 'Subscription', 'SubscriptionStatus', 'SubscriptionTopic', 'Substance', 'SubstanceDefinition', 'SubstanceNucleicAcid', 'SubstancePolymer', 'SubstanceProtein', 'SubstanceReferenceInformation', 'SubstanceSourceMaterial', 'SupplyDelivery', 'SupplyRequest', 'Task', 'TerminologyCapabilities', 'TestPlan', 'TestReport', 'TestScript', 'Transport', 'ValueSet', 'VerificationResult', 'VisionPrescription']
for FHIR_Resource_name in FHIR_resource_list:

    url = "https://build.fhir.org/" + FHIR_Resource_name.lower() + ".profile.canonical.json"

    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    FHIR_Resource = data['snapshot']['element']

    #0..* or 1..* elements can have multiple
    #need to put 0..* elements at end, in own model with foreign key to this model
    #but if backboneElement is 0..*, need to recurse for all elements in it

    all_model_lines = elementArray_to_ModelString(FHIR_Resource, FHIR_Resource_name)

    if FHIR_Resource_name in ["OperationOutcome", "Parameters"]:
        all_model_lines = "pass" + all_model_lines
    #These are empty on top level
    #can't make all empty classes pass because empty backbone elements have foreign key in them
    all_model_lines = all_model_lines.replace("import = ", "import_field = ").replace("check = ", "check_field = ")

    all_model_lines = all_model_lines.replace(f'''    observation = models.ForeignKey("FHIR_Observation", related_name="Observation_triggeredBy_observation", null=True, blank=True, on_delete=models.SET_NULL)''',
                                              f'''    triggeredBy_observation = models.ForeignKey("FHIR_Observation", related_name="Observation_triggeredBy_observation", null=True, blank=True, on_delete=models.SET_NULL)''')
    #case where backbone element has foreign key to resource type
    #and field has same name as that resource type

    strdef = "" #might need to do strs for backbone elements too idk
    if "FHIR_" + FHIR_Resource_name in default_strs:
        strdef = f'''
    def __str__(self):
        {default_strs["FHIR_" + FHIR_Resource_name]}'''

    #TODO maybe also print diffs vs models_dir/FHIR_Resources/FHIR_Resource_name.py
    output_file = os.path.join(output_dir, f"{FHIR_Resource_name}.py")
    print("writing", output_file)
    with open(output_file, 'w') as f:
        f.write(f'''#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_{FHIR_Resource_name}(models.Model):{strdef}{all_model_lines}''')
