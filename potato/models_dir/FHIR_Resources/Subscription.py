#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Subscription(models.Model):
    name = FHIR_primitive_StringField(null=True, blank=True, )
    class StatusChoices(models.TextChoices): REQUESTED = 'requested', 'Requested'; ACTIVE = 'active', 'Active'; ERROR = 'error', 'Error'; OFF = 'off', 'Off'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    topic = FHIR_primitive_CanonicalField(null=True, blank=True, )
    end = FHIR_primitive_InstantField(null=True, blank=True, )
    managingEntity_CareTeam = models.ForeignKey("FHIR_CareTeam", related_name="Subscription_managingEntity", null=True, blank=True, on_delete=models.SET_NULL)
    managingEntity_HealthcareService = models.ForeignKey("FHIR_HealthcareService", related_name="Subscription_managingEntity", null=True, blank=True, on_delete=models.SET_NULL)
    managingEntity_Organization = models.ForeignKey("FHIR_Organization", related_name="Subscription_managingEntity", null=True, blank=True, on_delete=models.SET_NULL)
    managingEntity_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="Subscription_managingEntity", null=True, blank=True, on_delete=models.SET_NULL)
    managingEntity_Patient = models.ForeignKey("FHIR_Patient", related_name="Subscription_managingEntity", null=True, blank=True, on_delete=models.SET_NULL)
    managingEntity_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="Subscription_managingEntity", null=True, blank=True, on_delete=models.SET_NULL)
    managingEntity_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="Subscription_managingEntity", null=True, blank=True, on_delete=models.SET_NULL)
    reason = FHIR_primitive_StringField(null=True, blank=True, )
    channelType = models.OneToOneField("FHIR_GP_Coding", related_name='Subscription_channelType', null=True, blank=True, on_delete=models.SET_NULL)
    endpoint = FHIR_primitive_URLField(null=True, blank=True, )
    heartbeatPeriod = FHIR_primitive_UnsignedIntField(null=True, blank=True, )
    timeout = FHIR_primitive_UnsignedIntField(null=True, blank=True, )
    class ContenttypeChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    contentType = FHIR_primitive_CodeField(choices=ContenttypeChoices.choices, null=True, blank=True, )
    class ContentChoices(models.TextChoices): EMPTY = 'empty', 'Empty'; ID_ONLY = 'id-only', 'Id-only'; FULL_RESOURCE = 'full-resource', 'Full-resource'; 
    content = FHIR_primitive_CodeField(choices=ContentChoices.choices, null=True, blank=True, )
    maxCount = FHIR_primitive_PositiveIntField(null=True, blank=True, )

class FHIR_Subscription_identifier(FHIR_GP_Identifier):
    Subscription = models.ForeignKey(FHIR_Subscription, related_name='Subscription_identifier', null=False, on_delete=models.CASCADE)

class FHIR_Subscription_contact(FHIR_GP_ContactPoint):
    Subscription = models.ForeignKey(FHIR_Subscription, related_name='Subscription_contact', null=False, on_delete=models.CASCADE)

class FHIR_Subscription_filterBy(models.Model):
    Subscription = models.ForeignKey(FHIR_Subscription, related_name='Subscription_filterBy', null=False, on_delete=models.CASCADE)
    resource = FHIR_primitive_URIField(null=True, blank=True, )
    filterParameter = FHIR_primitive_StringField(null=True, blank=True, )
    class ComparatorChoices(models.TextChoices): EQ = 'eq', 'Eq'; NE = 'ne', 'Ne'; GT = 'gt', 'Gt'; LT = 'lt', 'Lt'; GE = 'ge', 'Ge'; LE = 'le', 'Le'; SA = 'sa', 'Sa'; EB = 'eb', 'Eb'; AP = 'ap', 'Ap'; 
    comparator = FHIR_primitive_CodeField(choices=ComparatorChoices.choices, null=True, blank=True, )
    class ModifierChoices(models.TextChoices): MISSING = 'missing', 'Missing'; EXACT = 'exact', 'Exact'; CONTAINS = 'contains', 'Contains'; NOT = 'not', 'Not'; TEXT = 'text', 'Text'; IN = 'in', 'In'; NOT_IN = 'not-in', 'Not-in'; BELOW = 'below', 'Below'; ABOVE = 'above', 'Above'; TYPE = 'type', 'Type'; IDENTIFIER = 'identifier', 'Identifier'; OF_TYPE = 'of-type', 'Of-type'; CODE_TEXT = 'code-text', 'Code-text'; TEXT_ADVANCED = 'text-advanced', 'Text-advanced'; ITERATE = 'iterate', 'Iterate'; 
    modifier = FHIR_primitive_CodeField(choices=ModifierChoices.choices, null=True, blank=True, )
    value = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_Subscription_filterBy_event(models.Model):
    Subscription_filterBy = models.ForeignKey(FHIR_Subscription_filterBy, related_name='Subscription_filterBy_event', null=False, on_delete=models.CASCADE)
    BINDING_event = 'TODO'
    event_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_event}, related_name='Subscription_filterBy_event', blank=True)
    event_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Subscription_parameter(models.Model):
    Subscription = models.ForeignKey(FHIR_Subscription, related_name='Subscription_parameter', null=False, on_delete=models.CASCADE)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    value = FHIR_primitive_StringField(null=True, blank=True, )
