#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_CommunicationRequest(models.Model):
                            #skipping Reference(Any) for field basedOn as CommunicationRequest basedOn not in referenceAny_targets
    replaces = models.ManyToManyField("FHIR_CommunicationRequest", related_name="CommunicationRequest_replaces", blank=True)
    groupIdentifier = models.OneToOneField("FHIR_GP_Identifier", related_name='CommunicationRequest_groupIdentifier', null=True, blank=True, on_delete=models.SET_NULL)
    class StatusChoices(models.TextChoices): DRAFT = 'draft', 'Draft'; ACTIVE = 'active', 'Active'; ON_HOLD = 'on-hold', 'On-hold'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; ENDED = 'ended', 'Ended'; COMPLETED = 'completed', 'Completed'; REVOKED = 'revoked', 'Revoked'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    BINDING_statusReason = "TODO"
    statusReason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_statusReason}, related_name='CommunicationRequest_statusReason', blank=True)
    statusReason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    class IntentChoices(models.TextChoices): PROPOSAL = 'proposal', 'Proposal'; PLAN = 'plan', 'Plan'; DIRECTIVE = 'directive', 'Directive'; ORDER = 'order', 'Order'; ORIGINAL_ORDER = 'original-order', 'Original-order'; REFLEX_ORDER = 'reflex-order', 'Reflex-order'; FILLER_ORDER = 'filler-order', 'Filler-order'; INSTANCE_ORDER = 'instance-order', 'Instance-order'; OPTION = 'option', 'Option'; 
    intent = FHIR_primitive_CodeField(choices=IntentChoices.choices, null=True, blank=True, )
    class PriorityChoices(models.TextChoices): ROUTINE = 'routine', 'Routine'; URGENT = 'urgent', 'Urgent'; ASAP = 'asap', 'Asap'; STAT = 'stat', 'Stat'; 
    priority = FHIR_primitive_CodeField(choices=PriorityChoices.choices, null=True, blank=True, )
    doNotPerform = FHIR_primitive_BooleanField(null=True, blank=True, )
    subject_Patient = models.ForeignKey("FHIR_Patient", related_name="CommunicationRequest_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Group = models.ForeignKey("FHIR_Group", related_name="CommunicationRequest_subject", null=True, blank=True, on_delete=models.SET_NULL)
                            #skipping Reference(Any) for field about as CommunicationRequest about not in referenceAny_targets
    encounter = models.ForeignKey("FHIR_Encounter", related_name="CommunicationRequest_encounter", null=True, blank=True, on_delete=models.SET_NULL)
    occurrence_dateTime = FHIR_primitive_DateTimeField(null=True, blank=True, )
    occurrence_Period = models.OneToOneField("FHIR_GP_Period", related_name='CommunicationRequest_occurrence_Period', null=True, blank=True, on_delete=models.SET_NULL)
    authoredOn = FHIR_primitive_DateTimeField(null=True, blank=True, )
    requester_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="CommunicationRequest_requester", null=True, blank=True, on_delete=models.SET_NULL)
    requester_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="CommunicationRequest_requester", null=True, blank=True, on_delete=models.SET_NULL)
    requester_Organization = models.ForeignKey("FHIR_Organization", related_name="CommunicationRequest_requester", null=True, blank=True, on_delete=models.SET_NULL)
    requester_Patient = models.ForeignKey("FHIR_Patient", related_name="CommunicationRequest_requester", null=True, blank=True, on_delete=models.SET_NULL)
    requester_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="CommunicationRequest_requester", null=True, blank=True, on_delete=models.SET_NULL)
    requester_Device = models.ForeignKey("FHIR_Device", related_name="CommunicationRequest_requester", null=True, blank=True, on_delete=models.SET_NULL)
    requester_Group = models.ForeignKey("FHIR_Group", related_name="CommunicationRequest_requester", null=True, blank=True, on_delete=models.SET_NULL)
    recipient_Device = models.ManyToManyField("FHIR_Device", related_name="CommunicationRequest_recipient", blank=True)
    recipient_Organization = models.ManyToManyField("FHIR_Organization", related_name="CommunicationRequest_recipient", blank=True)
    recipient_Patient = models.ManyToManyField("FHIR_Patient", related_name="CommunicationRequest_recipient", blank=True)
    recipient_Practitioner = models.ManyToManyField("FHIR_Practitioner", related_name="CommunicationRequest_recipient", blank=True)
    recipient_PractitionerRole = models.ManyToManyField("FHIR_PractitionerRole", related_name="CommunicationRequest_recipient", blank=True)
    recipient_RelatedPerson = models.ManyToManyField("FHIR_RelatedPerson", related_name="CommunicationRequest_recipient", blank=True)
    recipient_Group = models.ManyToManyField("FHIR_Group", related_name="CommunicationRequest_recipient", blank=True)
    recipient_CareTeam = models.ManyToManyField("FHIR_CareTeam", related_name="CommunicationRequest_recipient", blank=True)
    recipient_HealthcareService = models.ManyToManyField("FHIR_HealthcareService", related_name="CommunicationRequest_recipient", blank=True)
    recipient_Endpoint = models.ManyToManyField("FHIR_Endpoint", related_name="CommunicationRequest_recipient", blank=True)
    informationProvider_Device = models.ManyToManyField("FHIR_Device", related_name="CommunicationRequest_informationProvider", blank=True)
    informationProvider_Organization = models.ManyToManyField("FHIR_Organization", related_name="CommunicationRequest_informationProvider", blank=True)
    informationProvider_Patient = models.ManyToManyField("FHIR_Patient", related_name="CommunicationRequest_informationProvider", blank=True)
    informationProvider_Practitioner = models.ManyToManyField("FHIR_Practitioner", related_name="CommunicationRequest_informationProvider", blank=True)
    informationProvider_PractitionerRole = models.ManyToManyField("FHIR_PractitionerRole", related_name="CommunicationRequest_informationProvider", blank=True)
    informationProvider_RelatedPerson = models.ManyToManyField("FHIR_RelatedPerson", related_name="CommunicationRequest_informationProvider", blank=True)
    informationProvider_HealthcareService = models.ManyToManyField("FHIR_HealthcareService", related_name="CommunicationRequest_informationProvider", blank=True)
    informationProvider_Endpoint = models.ManyToManyField("FHIR_Endpoint", related_name="CommunicationRequest_informationProvider", blank=True)
    informationProvider_Group = models.ManyToManyField("FHIR_Group", related_name="CommunicationRequest_informationProvider", blank=True)

class FHIR_CommunicationRequest_identifier(FHIR_GP_Identifier):
    CommunicationRequest = models.ForeignKey(FHIR_CommunicationRequest, related_name='CommunicationRequest_identifier', null=False, on_delete=models.CASCADE)

class FHIR_CommunicationRequest_category(models.Model):
    CommunicationRequest = models.ForeignKey(FHIR_CommunicationRequest, related_name='CommunicationRequest_category', null=False, on_delete=models.CASCADE)
    BINDING_category = "TODO"
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='CommunicationRequest_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_CommunicationRequest_medium(models.Model):
    CommunicationRequest = models.ForeignKey(FHIR_CommunicationRequest, related_name='CommunicationRequest_medium', null=False, on_delete=models.CASCADE)
    BINDING_medium = "TODO"
    medium_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_medium}, related_name='CommunicationRequest_medium', blank=True)
    medium_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_CommunicationRequest_payload(models.Model):
    CommunicationRequest = models.ForeignKey(FHIR_CommunicationRequest, related_name='CommunicationRequest_payload', null=False, on_delete=models.CASCADE)
    content_Attachment = models.OneToOneField("FHIR_GP_Attachment", related_name='CommunicationRequest_payload_content_Attachment', null=True, blank=True, on_delete=models.SET_NULL)
                            #skipping Reference(Any) for field content_Reference as CommunicationRequest content_Reference not in referenceAny_targets
    BINDING_content_CodeableConcept = "TODO"
    content_CodeableConcept_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_content_CodeableConcept}, related_name='CommunicationRequest_payload_content_CodeableConcept', blank=True)
    content_CodeableConcept_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_CommunicationRequest_reason(models.Model):
    CommunicationRequest = models.ForeignKey(FHIR_CommunicationRequest, related_name='CommunicationRequest_reason', null=False, on_delete=models.CASCADE)
    BINDING_reason = "TODO"
    reason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_reason}, related_name='CommunicationRequest_reason', blank=True)
    reason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_CommunicationRequest_note(FHIR_GP_Annotation):
    CommunicationRequest = models.ForeignKey(FHIR_CommunicationRequest, related_name='CommunicationRequest_note', null=False, on_delete=models.CASCADE)
