#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_SubscriptionStatus(models.Model):
    class StatusChoices(models.TextChoices): REQUESTED = 'requested', 'Requested'; ACTIVE = 'active', 'Active'; ERROR = 'error', 'Error'; OFF = 'off', 'Off'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    class TypeChoices(models.TextChoices): HANDSHAKE = 'handshake', 'Handshake'; HEARTBEAT = 'heartbeat', 'Heartbeat'; EVENT_NOTIFICATION = 'event-notification', 'Event-notification'; QUERY_STATUS = 'query-status', 'Query-status'; QUERY_EVENT = 'query-event', 'Query-event'; 
    type = FHIR_primitive_CodeField(choices=TypeChoices.choices, null=True, blank=True, )
    subscription = models.ForeignKey("FHIR_Subscription", related_name="SubscriptionStatus_subscription", null=True, blank=True, on_delete=models.SET_NULL)
    topic = FHIR_primitive_CanonicalField(null=True, blank=True, )

class FHIR_SubscriptionStatus_notificationEvent(models.Model):
    SubscriptionStatus = models.ForeignKey(FHIR_SubscriptionStatus, related_name='SubscriptionStatus_notificationEvent', null=False, on_delete=models.CASCADE)
    timestamp = FHIR_primitive_InstantField(null=True, blank=True, )

class FHIR_SubscriptionStatus_notificationEvent_triggerEvent(models.Model):
    SubscriptionStatus_notificationEvent = models.ForeignKey(FHIR_SubscriptionStatus_notificationEvent, related_name='SubscriptionStatus_notificationEvent_triggerEvent', null=False, on_delete=models.CASCADE)
    BINDING_triggerEvent = 'TODO'
    triggerEvent_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_triggerEvent}, related_name='SubscriptionStatus_notificationEvent_triggerEvent', blank=True)
    triggerEvent_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_SubscriptionStatus_notificationEvent_relatedQuery(models.Model):
    SubscriptionStatus_notificationEvent = models.ForeignKey(FHIR_SubscriptionStatus_notificationEvent, related_name='SubscriptionStatus_notificationEvent_relatedQuery', null=False, on_delete=models.CASCADE)
    queryType = models.OneToOneField("FHIR_GP_Coding", related_name='SubscriptionStatus_notificationEvent_relatedQuery_queryType', null=True, blank=True, on_delete=models.SET_NULL)
    query = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_SubscriptionStatus_error(models.Model):
    SubscriptionStatus = models.ForeignKey(FHIR_SubscriptionStatus, related_name='SubscriptionStatus_error', null=False, on_delete=models.CASCADE)
    BINDING_error = 'TODO'
    error_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_error}, related_name='SubscriptionStatus_error', blank=True)
    error_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    