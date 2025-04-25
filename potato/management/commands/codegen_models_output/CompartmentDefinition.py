
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_CompartmentDefinition(models.Model):
    url = FHIR_primitive_URIField(null=True, blank=True, )
    version = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = models.OneToOneField("FHIR_GP_Coding", related_name='CompartmentDefinition_versionAlgorithm', null=True, blank=True, on_delete=models.SET_NULL)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    title = FHIR_primitive_StringField(null=True, blank=True, )
    class StatusChoices(models.TextChoices): DRAFT = 'draft', 'Draft'; ACTIVE = 'active', 'Active'; RETIRED = 'retired', 'Retired'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    experimental = FHIR_primitive_BooleanField(null=True, blank=True, )
    date = FHIR_primitive_DateTimeField(null=True, blank=True, )
    publisher = FHIR_primitive_StringField(null=True, blank=True, )
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    purpose = FHIR_primitive_MarkdownField(null=True, blank=True, )
    class CodeChoices(models.TextChoices): PATIENT = 'Patient', 'Patient'; ENCOUNTER = 'Encounter', 'Encounter'; RELATEDPERSON = 'RelatedPerson', 'Relatedperson'; PRACTITIONER = 'Practitioner', 'Practitioner'; DEVICE = 'Device', 'Device'; EPISODEOFCARE = 'EpisodeOfCare', 'Episodeofcare'; 
    code = FHIR_primitive_CodeField(choices=CodeChoices.choices, null=True, blank=True, )
    search = FHIR_primitive_BooleanField(null=True, blank=True, )

class FHIR_CompartmentDefinition_resource(models.Model):
    CompartmentDefinition = models.ForeignKey(FHIR_CompartmentDefinition, related_name='CompartmentDefinition_resource', null=False, on_delete=models.CASCADE)
    class CodeChoices(models.TextChoices): NAME_OF_RESOURCE_TYPE = 'Name of resource type', 'Name of resource type'; 
    code = FHIR_primitive_CodeField(choices=CodeChoices.choices, null=True, blank=True, )
    documentation = FHIR_primitive_StringField(null=True, blank=True, )
    startParam = FHIR_primitive_URIField(null=True, blank=True, )
    endParam = FHIR_primitive_URIField(null=True, blank=True, )

class FHIR_CompartmentDefinition_resource_param(models.Model):
    CompartmentDefinition_resource = models.ForeignKey(FHIR_CompartmentDefinition_resource, related_name='CompartmentDefinition_resource_param', null=False, on_delete=models.CASCADE)
    
    param = FHIR_primitive_StringField(null=True, blank=True, )
    