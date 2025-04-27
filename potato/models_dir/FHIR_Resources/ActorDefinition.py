#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_ActorDefinition(models.Model):
    url = FHIR_primitive_URIField(null=True, blank=True, )
    version = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = models.OneToOneField("FHIR_GP_Coding", related_name='ActorDefinition_versionAlgorithm', null=True, blank=True, on_delete=models.SET_NULL)
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
    class TypeChoices(models.TextChoices): SYSTEM = 'system', 'System'; NON_SYSTEM = 'non-system', 'Non-system'; INDIVIDUAL = 'individual', 'Individual'; PATIENT = 'patient', 'Patient'; PRACTITIONER = 'practitioner', 'Practitioner'; RELATED_PERSON = 'related-person', 'Related-person'; DEVICE = 'device', 'Device'; COLLECTIVE = 'collective', 'Collective'; CARE_TEAM = 'care-team', 'Care-team'; GROUP = 'group', 'Group'; HEALTHCARE_SERVICE = 'healthcare-service', 'Healthcare-service'; ORGANIZATION = 'organization', 'Organization'; 
    type = FHIR_primitive_CodeField(choices=TypeChoices.choices, null=True, blank=True, )
    documentation = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_ActorDefinition_identifier(FHIR_GP_Identifier):
    ActorDefinition = models.ForeignKey(FHIR_ActorDefinition, related_name='ActorDefinition_identifier', null=False, on_delete=models.CASCADE)

class FHIR_ActorDefinition_jurisdiction(models.Model):
    ActorDefinition = models.ForeignKey(FHIR_ActorDefinition, related_name='ActorDefinition_jurisdiction', null=False, on_delete=models.CASCADE)
    BINDING_jurisdiction = 'TODO'
    jurisdiction_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_jurisdiction}, related_name='ActorDefinition_jurisdiction', blank=True)
    jurisdiction_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ActorDefinition_reference(models.Model):
    ActorDefinition = models.ForeignKey(FHIR_ActorDefinition, related_name='ActorDefinition_reference', null=False, on_delete=models.CASCADE)
    
    reference = FHIR_primitive_URLField(null=True, blank=True, )
    
class FHIR_ActorDefinition_baseDefinition(models.Model):
    ActorDefinition = models.ForeignKey(FHIR_ActorDefinition, related_name='ActorDefinition_baseDefinition', null=False, on_delete=models.CASCADE)
    
    baseDefinition = FHIR_primitive_CanonicalField(null=True, blank=True, )
    