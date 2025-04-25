
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_DeviceDispense(models.Model):
    basedOn_CarePlan = models.ManyToManyField("FHIR_CarePlan", related_name="DeviceDispense_basedOn", blank=True)
    basedOn_DeviceRequest = models.ManyToManyField("FHIR_DeviceRequest", related_name="DeviceDispense_basedOn", blank=True)
    partOf = models.ManyToManyField("FHIR_Procedure", related_name="DeviceDispense_partOf", blank=True)
    class StatusChoices(models.TextChoices): PREPARATION = 'preparation', 'Preparation'; IN_PROGRESS = 'in-progress', 'In-progress'; CANCELLED = 'cancelled', 'Cancelled'; ON_HOLD = 'on-hold', 'On-hold'; COMPLETED = 'completed', 'Completed'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; STOPPED = 'stopped', 'Stopped'; DECLINED = 'declined', 'Declined'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    BINDING_statusReason = 'TODO'
    statusReason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_statusReason}, related_name='DeviceDispense_statusReason', blank=True)
    statusReason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    statusReason_DetectedIssue_ref = models.ForeignKey("FHIR_DetectedIssue", related_name="DeviceDispense_statusReason", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_device = 'TODO'
    device_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_device}, related_name='DeviceDispense_device', blank=True)
    device_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    device_Device_ref = models.ForeignKey("FHIR_Device", related_name="DeviceDispense_device", null=True, blank=True, on_delete=models.SET_NULL)
    device_DeviceDefinition_ref = models.ForeignKey("FHIR_DeviceDefinition", related_name="DeviceDispense_device", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Patient = models.ForeignKey("FHIR_Patient", related_name="DeviceDispense_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="DeviceDispense_subject", null=True, blank=True, on_delete=models.SET_NULL)
    receiver_Patient = models.ForeignKey("FHIR_Patient", related_name="DeviceDispense_receiver", null=True, blank=True, on_delete=models.SET_NULL)
    receiver_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="DeviceDispense_receiver", null=True, blank=True, on_delete=models.SET_NULL)
    receiver_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="DeviceDispense_receiver", null=True, blank=True, on_delete=models.SET_NULL)
    receiver_Location = models.ForeignKey("FHIR_Location", related_name="DeviceDispense_receiver", null=True, blank=True, on_delete=models.SET_NULL)
    receiver_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="DeviceDispense_receiver", null=True, blank=True, on_delete=models.SET_NULL)
    encounter = models.ForeignKey("FHIR_Encounter", related_name="DeviceDispense_encounter", null=True, blank=True, on_delete=models.SET_NULL)
    location = models.ForeignKey("FHIR_Location", related_name="DeviceDispense_location", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='DeviceDispense_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='DeviceDispense_quantity', null=True, blank=True, on_delete=models.SET_NULL)
    preparedDate = FHIR_primitive_DateTimeField(null=True, blank=True, )
    whenHandedOver = FHIR_primitive_DateTimeField(null=True, blank=True, )
    destination = models.ForeignKey("FHIR_Location", related_name="DeviceDispense_destination", null=True, blank=True, on_delete=models.SET_NULL)
    usageInstruction = FHIR_primitive_MarkdownField(null=True, blank=True, )
    eventHistory = models.ManyToManyField("FHIR_Provenance", related_name="DeviceDispense_eventHistory", blank=True)

class FHIR_DeviceDispense_identifier(FHIR_GP_Identifier):
    DeviceDispense = models.ForeignKey(FHIR_DeviceDispense, related_name='DeviceDispense_identifier', null=False, on_delete=models.CASCADE)

class FHIR_DeviceDispense_category(models.Model):
    DeviceDispense = models.ForeignKey(FHIR_DeviceDispense, related_name='DeviceDispense_category', null=False, on_delete=models.CASCADE)
    BINDING_category = 'TODO'
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='DeviceDispense_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_DeviceDispense_performer(models.Model):
    DeviceDispense = models.ForeignKey(FHIR_DeviceDispense, related_name='DeviceDispense_performer', null=False, on_delete=models.CASCADE)
    BINDING_function = 'TODO'
    function_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_function}, related_name='DeviceDispense_performer_function', blank=True)
    function_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    actor_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="DeviceDispense_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="DeviceDispense_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Organization = models.ForeignKey("FHIR_Organization", related_name="DeviceDispense_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Patient = models.ForeignKey("FHIR_Patient", related_name="DeviceDispense_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Device = models.ForeignKey("FHIR_Device", related_name="DeviceDispense_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="DeviceDispense_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_CareTeam = models.ForeignKey("FHIR_CareTeam", related_name="DeviceDispense_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_DeviceDispense_note(FHIR_GP_Annotation):
    DeviceDispense = models.ForeignKey(FHIR_DeviceDispense, related_name='DeviceDispense_note', null=False, on_delete=models.CASCADE)
