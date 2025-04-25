
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Communication(models.Model):
    basedOn_CarePlan = models.ManyToManyField("FHIR_CarePlan", related_name="Communication_basedOn", blank=True)
    basedOn_CommunicationRequest = models.ManyToManyField("FHIR_CommunicationRequest", related_name="Communication_basedOn", blank=True)
    basedOn_DeviceRequest = models.ManyToManyField("FHIR_DeviceRequest", related_name="Communication_basedOn", blank=True)
    basedOn_ImmunizationRecommendation = models.ManyToManyField("FHIR_ImmunizationRecommendation", related_name="Communication_basedOn", blank=True)
    basedOn_MedicationRequest = models.ManyToManyField("FHIR_MedicationRequest", related_name="Communication_basedOn", blank=True)
    basedOn_NutritionOrder = models.ManyToManyField("FHIR_NutritionOrder", related_name="Communication_basedOn", blank=True)
    basedOn_ServiceRequest = models.ManyToManyField("FHIR_ServiceRequest", related_name="Communication_basedOn", blank=True)
    basedOn_Task = models.ManyToManyField("FHIR_Task", related_name="Communication_basedOn", blank=True)
    basedOn_VisionPrescription = models.ManyToManyField("FHIR_VisionPrescription", related_name="Communication_basedOn", blank=True)
    inResponseTo = models.ManyToManyField("FHIR_Communication", related_name="Communication_inResponseTo", blank=True)
    class StatusChoices(models.TextChoices): PREPARATION = 'preparation', 'Preparation'; IN_PROGRESS = 'in-progress', 'In-progress'; NOT_DONE = 'not-done', 'Not-done'; ON_HOLD = 'on-hold', 'On-hold'; STOPPED = 'stopped', 'Stopped'; COMPLETED = 'completed', 'Completed'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    BINDING_statusReason = 'TODO'
    statusReason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_statusReason}, related_name='Communication_statusReason', blank=True)
    statusReason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    class PriorityChoices(models.TextChoices): ROUTINE = 'routine', 'Routine'; URGENT = 'urgent', 'Urgent'; ASAP = 'asap', 'Asap'; STAT = 'stat', 'Stat'; 
    priority = FHIR_primitive_CodeField(choices=PriorityChoices.choices, null=True, blank=True, )
    subject_Patient = models.ForeignKey("FHIR_Patient", related_name="Communication_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Group = models.ForeignKey("FHIR_Group", related_name="Communication_subject", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_topic = 'TODO'
    topic_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_topic}, related_name='Communication_topic', blank=True)
    topic_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    encounter = models.ForeignKey("FHIR_Encounter", related_name="Communication_encounter", null=True, blank=True, on_delete=models.SET_NULL)
    sent = FHIR_primitive_DateTimeField(null=True, blank=True, )
    received = FHIR_primitive_DateTimeField(null=True, blank=True, )
    recipient_CareTeam = models.ManyToManyField("FHIR_CareTeam", related_name="Communication_recipient", blank=True)
    recipient_Device = models.ManyToManyField("FHIR_Device", related_name="Communication_recipient", blank=True)
    recipient_Group = models.ManyToManyField("FHIR_Group", related_name="Communication_recipient", blank=True)
    recipient_HealthcareService = models.ManyToManyField("FHIR_HealthcareService", related_name="Communication_recipient", blank=True)
    recipient_Location = models.ManyToManyField("FHIR_Location", related_name="Communication_recipient", blank=True)
    recipient_Organization = models.ManyToManyField("FHIR_Organization", related_name="Communication_recipient", blank=True)
    recipient_Patient = models.ManyToManyField("FHIR_Patient", related_name="Communication_recipient", blank=True)
    recipient_Practitioner = models.ManyToManyField("FHIR_Practitioner", related_name="Communication_recipient", blank=True)
    recipient_PractitionerRole = models.ManyToManyField("FHIR_PractitionerRole", related_name="Communication_recipient", blank=True)
    recipient_RelatedPerson = models.ManyToManyField("FHIR_RelatedPerson", related_name="Communication_recipient", blank=True)
    recipient_Endpoint = models.ManyToManyField("FHIR_Endpoint", related_name="Communication_recipient", blank=True)
    sender_Device = models.ForeignKey("FHIR_Device", related_name="Communication_sender", null=True, blank=True, on_delete=models.SET_NULL)
    sender_Organization = models.ForeignKey("FHIR_Organization", related_name="Communication_sender", null=True, blank=True, on_delete=models.SET_NULL)
    sender_Patient = models.ForeignKey("FHIR_Patient", related_name="Communication_sender", null=True, blank=True, on_delete=models.SET_NULL)
    sender_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="Communication_sender", null=True, blank=True, on_delete=models.SET_NULL)
    sender_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="Communication_sender", null=True, blank=True, on_delete=models.SET_NULL)
    sender_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="Communication_sender", null=True, blank=True, on_delete=models.SET_NULL)
    sender_HealthcareService = models.ForeignKey("FHIR_HealthcareService", related_name="Communication_sender", null=True, blank=True, on_delete=models.SET_NULL)
    sender_Endpoint = models.ForeignKey("FHIR_Endpoint", related_name="Communication_sender", null=True, blank=True, on_delete=models.SET_NULL)
    sender_CareTeam = models.ForeignKey("FHIR_CareTeam", related_name="Communication_sender", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Communication_identifier(FHIR_GP_Identifier):
    Communication = models.ForeignKey(FHIR_Communication, related_name='Communication_identifier', null=False, on_delete=models.CASCADE)

class FHIR_Communication_category(models.Model):
    Communication = models.ForeignKey(FHIR_Communication, related_name='Communication_category', null=False, on_delete=models.CASCADE)
    BINDING_category = 'TODO'
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='Communication_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Communication_medium(models.Model):
    Communication = models.ForeignKey(FHIR_Communication, related_name='Communication_medium', null=False, on_delete=models.CASCADE)
    BINDING_medium = 'TODO'
    medium_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_medium}, related_name='Communication_medium', blank=True)
    medium_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Communication_reason(models.Model):
    Communication = models.ForeignKey(FHIR_Communication, related_name='Communication_reason', null=False, on_delete=models.CASCADE)
    BINDING_reason = 'TODO'
    reason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_reason}, related_name='Communication_reason', blank=True)
    reason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_Communication_payload(models.Model):
    Communication = models.ForeignKey(FHIR_Communication, related_name='Communication_payload', null=False, on_delete=models.CASCADE)
    content = models.OneToOneField("FHIR_GP_Attachment", related_name='Communication_payload_content', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_content = 'TODO'
    content_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_content}, related_name='Communication_payload_content', blank=True)
    content_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_Communication_note(FHIR_GP_Annotation):
    Communication = models.ForeignKey(FHIR_Communication, related_name='Communication_note', null=False, on_delete=models.CASCADE)
