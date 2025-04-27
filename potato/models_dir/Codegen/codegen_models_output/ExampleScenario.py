#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_ExampleScenario(models.Model):
    url = FHIR_primitive_URIField(null=True, blank=True, )
    version = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = models.OneToOneField("FHIR_GP_Coding", related_name='ExampleScenario_versionAlgorithm', null=True, blank=True, on_delete=models.SET_NULL)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    title = FHIR_primitive_StringField(null=True, blank=True, )
    class StatusChoices(models.TextChoices): DRAFT = 'draft', 'Draft'; ACTIVE = 'active', 'Active'; RETIRED = 'retired', 'Retired'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    experimental = FHIR_primitive_BooleanField(null=True, blank=True, )
    date = FHIR_primitive_DateTimeField(null=True, blank=True, )
    publisher = FHIR_primitive_StringField(null=True, blank=True, )
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    purpose = FHIR_primitive_MarkdownField(null=True, blank=True, )
    copyright = FHIR_primitive_MarkdownField(null=True, blank=True, )
    copyrightLabel = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_ExampleScenario_identifier(FHIR_GP_Identifier):
    ExampleScenario = models.ForeignKey(FHIR_ExampleScenario, related_name='ExampleScenario_identifier', null=False, on_delete=models.CASCADE)

class FHIR_ExampleScenario_jurisdiction(models.Model):
    ExampleScenario = models.ForeignKey(FHIR_ExampleScenario, related_name='ExampleScenario_jurisdiction', null=False, on_delete=models.CASCADE)
    BINDING_jurisdiction = "TODO"
    jurisdiction_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_jurisdiction}, related_name='ExampleScenario_jurisdiction', blank=True)
    jurisdiction_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ExampleScenario_actor(models.Model):
    ExampleScenario = models.ForeignKey(FHIR_ExampleScenario, related_name='ExampleScenario_actor', null=False, on_delete=models.CASCADE)
    key = FHIR_primitive_StringField(null=True, blank=True, )
    class TypeChoices(models.TextChoices): SYSTEM = 'system', 'System'; NON_SYSTEM = 'non-system', 'Non-system'; INDIVIDUAL = 'individual', 'Individual'; PATIENT = 'patient', 'Patient'; PRACTITIONER = 'practitioner', 'Practitioner'; RELATED_PERSON = 'related-person', 'Related-person'; DEVICE = 'device', 'Device'; COLLECTIVE = 'collective', 'Collective'; CARE_TEAM = 'care-team', 'Care-team'; GROUP = 'group', 'Group'; HEALTHCARE_SERVICE = 'healthcare-service', 'Healthcare-service'; ORGANIZATION = 'organization', 'Organization'; 
    type = FHIR_primitive_CodeField(choices=TypeChoices.choices, null=True, blank=True, )
    title = FHIR_primitive_StringField(null=True, blank=True, )
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    definition = FHIR_primitive_CanonicalField(null=True, blank=True, )

class FHIR_ExampleScenario_instance(models.Model):
    ExampleScenario = models.ForeignKey(FHIR_ExampleScenario, related_name='ExampleScenario_instance', null=False, on_delete=models.CASCADE)
    key = FHIR_primitive_StringField(null=True, blank=True, )
    structureType = models.OneToOneField("FHIR_GP_Coding", related_name='ExampleScenario_instance_structureType', null=True, blank=True, on_delete=models.SET_NULL)
    structureVersion = FHIR_primitive_StringField(null=True, blank=True, )
    structureProfile = FHIR_primitive_CanonicalField(null=True, blank=True, )
    structureProfile = FHIR_primitive_URIField(null=True, blank=True, )
    title = FHIR_primitive_StringField(null=True, blank=True, )
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_ExampleScenario_instance_version(models.Model):
    ExampleScenario_instance = models.ForeignKey(FHIR_ExampleScenario_instance, related_name='ExampleScenario_instance_version', null=False, on_delete=models.CASCADE)
    key = FHIR_primitive_StringField(null=True, blank=True, )
    title = FHIR_primitive_StringField(null=True, blank=True, )
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_ExampleScenario_instance_containedInstance(models.Model):
    ExampleScenario_instance = models.ForeignKey(FHIR_ExampleScenario_instance, related_name='ExampleScenario_instance_containedInstance', null=False, on_delete=models.CASCADE)
    instanceReference = FHIR_primitive_StringField(null=True, blank=True, )
    versionReference = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_ExampleScenario_process(models.Model):
    ExampleScenario = models.ForeignKey(FHIR_ExampleScenario, related_name='ExampleScenario_process', null=False, on_delete=models.CASCADE)
    title = FHIR_primitive_StringField(null=True, blank=True, )
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    preConditions = FHIR_primitive_MarkdownField(null=True, blank=True, )
    postConditions = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_ExampleScenario_process_step(models.Model):
    ExampleScenario_process = models.ForeignKey(FHIR_ExampleScenario_process, related_name='ExampleScenario_process_step', null=False, on_delete=models.CASCADE)
    number = FHIR_primitive_StringField(null=True, blank=True, )
    workflow = FHIR_primitive_CanonicalField(null=True, blank=True, )
    pause = FHIR_primitive_BooleanField(null=True, blank=True, )

class FHIR_ExampleScenario_process_step_operation(models.Model):
    ExampleScenario_process_step = models.ForeignKey(FHIR_ExampleScenario_process_step, related_name='ExampleScenario_process_step_operation', null=False, on_delete=models.CASCADE)
    type = models.OneToOneField("FHIR_GP_Coding", related_name='ExampleScenario_process_step_operation_type', null=True, blank=True, on_delete=models.SET_NULL)
    title = FHIR_primitive_StringField(null=True, blank=True, )
    initiator = FHIR_primitive_StringField(null=True, blank=True, )
    receiver = FHIR_primitive_StringField(null=True, blank=True, )
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    initiatorActive = FHIR_primitive_BooleanField(null=True, blank=True, )
    receiverActive = FHIR_primitive_BooleanField(null=True, blank=True, )

class FHIR_ExampleScenario_process_step_alternative(models.Model):
    ExampleScenario_process_step = models.ForeignKey(FHIR_ExampleScenario_process_step, related_name='ExampleScenario_process_step_alternative', null=False, on_delete=models.CASCADE)
    title = FHIR_primitive_StringField(null=True, blank=True, )
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
