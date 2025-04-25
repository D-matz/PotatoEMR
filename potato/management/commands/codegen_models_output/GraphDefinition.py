
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_GraphDefinition(models.Model):
    url = FHIR_primitive_URIField(null=True, blank=True, )
    version = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = models.OneToOneField("FHIR_GP_Coding", related_name='GraphDefinition_versionAlgorithm', null=True, blank=True, on_delete=models.SET_NULL)
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
    start = FHIR_primitive_IdField(null=True, blank=True, )

class FHIR_GraphDefinition_identifier(FHIR_GP_Identifier):
    GraphDefinition = models.ForeignKey(FHIR_GraphDefinition, related_name='GraphDefinition_identifier', null=False, on_delete=models.CASCADE)

class FHIR_GraphDefinition_jurisdiction(models.Model):
    GraphDefinition = models.ForeignKey(FHIR_GraphDefinition, related_name='GraphDefinition_jurisdiction', null=False, on_delete=models.CASCADE)
    BINDING_jurisdiction = 'TODO'
    jurisdiction_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_jurisdiction}, related_name='GraphDefinition_jurisdiction', blank=True)
    jurisdiction_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_GraphDefinition_node(models.Model):
    GraphDefinition = models.ForeignKey(FHIR_GraphDefinition, related_name='GraphDefinition_node', null=False, on_delete=models.CASCADE)
    nodeId = FHIR_primitive_IdField(null=True, blank=True, )
    description = FHIR_primitive_StringField(null=True, blank=True, )
    class TypeChoices(models.TextChoices): TYPE_OF_RESOURCE_THIS_LINK_REFERS_TO = 'Type of resource this link refers to', 'Type of resource this link refers to'; 
    type = FHIR_primitive_CodeField(choices=TypeChoices.choices, null=True, blank=True, )
    profile = FHIR_primitive_CanonicalField(null=True, blank=True, )

class FHIR_GraphDefinition_link(models.Model):
    GraphDefinition = models.ForeignKey(FHIR_GraphDefinition, related_name='GraphDefinition_link', null=False, on_delete=models.CASCADE)
    description = FHIR_primitive_StringField(null=True, blank=True, )
    max = FHIR_primitive_StringField(null=True, blank=True, )
    sourceId = FHIR_primitive_IdField(null=True, blank=True, )
    path = FHIR_primitive_StringField(null=True, blank=True, )
    sliceName = FHIR_primitive_StringField(null=True, blank=True, )
    targetId = FHIR_primitive_IdField(null=True, blank=True, )
    params = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_GraphDefinition_link_compartment(models.Model):
    GraphDefinition_link = models.ForeignKey(FHIR_GraphDefinition_link, related_name='GraphDefinition_link_compartment', null=False, on_delete=models.CASCADE)
    class UseChoices(models.TextChoices): WHERE = 'where', 'Where'; REQUIRES = 'requires', 'Requires'; 
    use = FHIR_primitive_CodeField(choices=UseChoices.choices, null=True, blank=True, )
    class RuleChoices(models.TextChoices): IDENTICAL = 'identical', 'Identical'; MATCHING = 'matching', 'Matching'; DIFFERENT = 'different', 'Different'; CUSTOM = 'custom', 'Custom'; 
    rule = FHIR_primitive_CodeField(choices=RuleChoices.choices, null=True, blank=True, )
    class CodeChoices(models.TextChoices): PATIENT = 'Patient', 'Patient'; ENCOUNTER = 'Encounter', 'Encounter'; RELATEDPERSON = 'RelatedPerson', 'Relatedperson'; PRACTITIONER = 'Practitioner', 'Practitioner'; DEVICE = 'Device', 'Device'; EPISODEOFCARE = 'EpisodeOfCare', 'Episodeofcare'; 
    code = FHIR_primitive_CodeField(choices=CodeChoices.choices, null=True, blank=True, )
    expression = FHIR_primitive_StringField(null=True, blank=True, )
    description = FHIR_primitive_StringField(null=True, blank=True, )
