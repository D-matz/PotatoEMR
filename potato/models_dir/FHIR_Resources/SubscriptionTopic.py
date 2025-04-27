#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_SubscriptionTopic(models.Model):
    url = FHIR_primitive_URIField(null=True, blank=True, )
    version = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = models.OneToOneField("FHIR_GP_Coding", related_name='SubscriptionTopic_versionAlgorithm', null=True, blank=True, on_delete=models.SET_NULL)
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
    approvalDate = FHIR_primitive_DateField(null=True, blank=True, )
    lastReviewDate = FHIR_primitive_DateField(null=True, blank=True, )
    effectivePeriod = models.OneToOneField("FHIR_GP_Period", related_name='SubscriptionTopic_effectivePeriod', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_SubscriptionTopic_identifier(FHIR_GP_Identifier):
    SubscriptionTopic = models.ForeignKey(FHIR_SubscriptionTopic, related_name='SubscriptionTopic_identifier', null=False, on_delete=models.CASCADE)

class FHIR_SubscriptionTopic_derivedFrom(models.Model):
    SubscriptionTopic = models.ForeignKey(FHIR_SubscriptionTopic, related_name='SubscriptionTopic_derivedFrom', null=False, on_delete=models.CASCADE)
    
    derivedFrom = FHIR_primitive_CanonicalField(null=True, blank=True, )
    
class FHIR_SubscriptionTopic_jurisdiction(models.Model):
    SubscriptionTopic = models.ForeignKey(FHIR_SubscriptionTopic, related_name='SubscriptionTopic_jurisdiction', null=False, on_delete=models.CASCADE)
    BINDING_jurisdiction = 'TODO'
    jurisdiction_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_jurisdiction}, related_name='SubscriptionTopic_jurisdiction', blank=True)
    jurisdiction_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_SubscriptionTopic_trigger(models.Model):
    SubscriptionTopic = models.ForeignKey(FHIR_SubscriptionTopic, related_name='SubscriptionTopic_trigger', null=False, on_delete=models.CASCADE)
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    resource = FHIR_primitive_URIField(null=True, blank=True, )
    fhirPathCriteria = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_event = 'TODO'
    event_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_event}, related_name='SubscriptionTopic_trigger_event', blank=True)
    event_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_SubscriptionTopic_trigger_supportedInteraction(models.Model):
    SubscriptionTopic_trigger = models.ForeignKey(FHIR_SubscriptionTopic_trigger, related_name='SubscriptionTopic_trigger_supportedInteraction', null=False, on_delete=models.CASCADE)
    
    class SupportedinteractionChoices(models.TextChoices): CREATE = 'create', 'Create'; UPDATE = 'update', 'Update'; DELETE = 'delete', 'Delete'; 
    supportedInteraction = FHIR_primitive_CodeField(choices=SupportedinteractionChoices.choices, null=True, blank=True, )
    
class FHIR_SubscriptionTopic_trigger_queryCriteria(models.Model):
    SubscriptionTopic_trigger = models.ForeignKey(FHIR_SubscriptionTopic_trigger, related_name='SubscriptionTopic_trigger_queryCriteria', null=False, on_delete=models.CASCADE)
    previous = FHIR_primitive_StringField(null=True, blank=True, )
    class ResultforcreateChoices(models.TextChoices): TEST_PASSES = 'test-passes', 'Test-passes'; TEST_FAILS = 'test-fails', 'Test-fails'; 
    resultForCreate = FHIR_primitive_CodeField(choices=ResultforcreateChoices.choices, null=True, blank=True, )
    current = FHIR_primitive_StringField(null=True, blank=True, )
    class ResultfordeleteChoices(models.TextChoices): TEST_PASSES = 'test-passes', 'Test-passes'; TEST_FAILS = 'test-fails', 'Test-fails'; 
    resultForDelete = FHIR_primitive_CodeField(choices=ResultfordeleteChoices.choices, null=True, blank=True, )
    requireBoth = FHIR_primitive_BooleanField(null=True, blank=True, )

class FHIR_SubscriptionTopic_trigger_canFilterBy(models.Model):
    SubscriptionTopic_trigger = models.ForeignKey(FHIR_SubscriptionTopic_trigger, related_name='SubscriptionTopic_trigger_canFilterBy', null=False, on_delete=models.CASCADE)
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    resource = FHIR_primitive_URIField(null=True, blank=True, )
    filterParameter = FHIR_primitive_StringField(null=True, blank=True, )
    filterDefinition = FHIR_primitive_URIField(null=True, blank=True, )

class FHIR_SubscriptionTopic_trigger_canFilterBy_comparator(models.Model):
    SubscriptionTopic_trigger_canFilterBy = models.ForeignKey(FHIR_SubscriptionTopic_trigger_canFilterBy, related_name='SubscriptionTopic_trigger_canFilterBy_comparator', null=False, on_delete=models.CASCADE)
    
    class ComparatorChoices(models.TextChoices): EQ = 'eq', 'Eq'; NE = 'ne', 'Ne'; GT = 'gt', 'Gt'; LT = 'lt', 'Lt'; GE = 'ge', 'Ge'; LE = 'le', 'Le'; SA = 'sa', 'Sa'; EB = 'eb', 'Eb'; AP = 'ap', 'Ap'; 
    comparator = FHIR_primitive_CodeField(choices=ComparatorChoices.choices, null=True, blank=True, )
    
class FHIR_SubscriptionTopic_trigger_canFilterBy_modifier(models.Model):
    SubscriptionTopic_trigger_canFilterBy = models.ForeignKey(FHIR_SubscriptionTopic_trigger_canFilterBy, related_name='SubscriptionTopic_trigger_canFilterBy_modifier', null=False, on_delete=models.CASCADE)
    
    class ModifierChoices(models.TextChoices): MISSING = 'missing', 'Missing'; EXACT = 'exact', 'Exact'; CONTAINS = 'contains', 'Contains'; NOT = 'not', 'Not'; TEXT = 'text', 'Text'; IN = 'in', 'In'; NOT_IN = 'not-in', 'Not-in'; BELOW = 'below', 'Below'; ABOVE = 'above', 'Above'; TYPE = 'type', 'Type'; IDENTIFIER = 'identifier', 'Identifier'; OF_TYPE = 'of-type', 'Of-type'; CODE_TEXT = 'code-text', 'Code-text'; TEXT_ADVANCED = 'text-advanced', 'Text-advanced'; ITERATE = 'iterate', 'Iterate'; 
    modifier = FHIR_primitive_CodeField(choices=ModifierChoices.choices, null=True, blank=True, )
    
class FHIR_SubscriptionTopic_trigger_notificationShape(models.Model):
    SubscriptionTopic_trigger = models.ForeignKey(FHIR_SubscriptionTopic_trigger, related_name='SubscriptionTopic_trigger_notificationShape', null=False, on_delete=models.CASCADE)
    resource = FHIR_primitive_URIField(null=True, blank=True, )

class FHIR_SubscriptionTopic_trigger_notificationShape_include(models.Model):
    SubscriptionTopic_trigger_notificationShape = models.ForeignKey(FHIR_SubscriptionTopic_trigger_notificationShape, related_name='SubscriptionTopic_trigger_notificationShape_include', null=False, on_delete=models.CASCADE)
    
    include = FHIR_primitive_StringField(null=True, blank=True, )
    
class FHIR_SubscriptionTopic_trigger_notificationShape_revInclude(models.Model):
    SubscriptionTopic_trigger_notificationShape = models.ForeignKey(FHIR_SubscriptionTopic_trigger_notificationShape, related_name='SubscriptionTopic_trigger_notificationShape_revInclude', null=False, on_delete=models.CASCADE)
    
    revInclude = FHIR_primitive_StringField(null=True, blank=True, )
    
class FHIR_SubscriptionTopic_trigger_notificationShape_relatedQuery(models.Model):
    SubscriptionTopic_trigger_notificationShape = models.ForeignKey(FHIR_SubscriptionTopic_trigger_notificationShape, related_name='SubscriptionTopic_trigger_notificationShape_relatedQuery', null=False, on_delete=models.CASCADE)
    queryType = models.OneToOneField("FHIR_GP_Coding", related_name='SubscriptionTopic_trigger_notificationShape_relatedQuery_queryType', null=True, blank=True, on_delete=models.SET_NULL)
    query = FHIR_primitive_StringField(null=True, blank=True, )
