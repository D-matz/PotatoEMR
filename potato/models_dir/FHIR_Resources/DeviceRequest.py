#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_DeviceRequest(models.Model):
    replaces = models.ManyToManyField("FHIR_DeviceRequest", related_name="DeviceRequest_replaces", blank=True)
    groupIdentifier = models.OneToOneField("FHIR_GP_Identifier", related_name='DeviceRequest_groupIdentifier', null=True, blank=True, on_delete=models.SET_NULL)
    class StatusChoices(models.TextChoices): DRAFT = 'draft', 'Draft'; ACTIVE = 'active', 'Active'; ON_HOLD = 'on-hold', 'On-hold'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; ENDED = 'ended', 'Ended'; COMPLETED = 'completed', 'Completed'; REVOKED = 'revoked', 'Revoked'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    class IntentChoices(models.TextChoices): PROPOSAL = 'proposal', 'Proposal'; PLAN = 'plan', 'Plan'; DIRECTIVE = 'directive', 'Directive'; ORDER = 'order', 'Order'; ORIGINAL_ORDER = 'original-order', 'Original-order'; REFLEX_ORDER = 'reflex-order', 'Reflex-order'; FILLER_ORDER = 'filler-order', 'Filler-order'; INSTANCE_ORDER = 'instance-order', 'Instance-order'; OPTION = 'option', 'Option'; 
    intent = FHIR_primitive_CodeField(choices=IntentChoices.choices, null=True, blank=True, )
    class PriorityChoices(models.TextChoices): ROUTINE = 'routine', 'Routine'; URGENT = 'urgent', 'Urgent'; ASAP = 'asap', 'Asap'; STAT = 'stat', 'Stat'; 
    priority = FHIR_primitive_CodeField(choices=PriorityChoices.choices, null=True, blank=True, )
    doNotPerform = FHIR_primitive_BooleanField(null=True, blank=True, )
    BINDING_code = 'TODO'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='DeviceRequest_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    code_Device_ref = models.ForeignKey("FHIR_Device", related_name="DeviceRequest_code_Device", null=True, blank=True, on_delete=models.SET_NULL)
    code_DeviceDefinition_ref = models.ForeignKey("FHIR_DeviceDefinition", related_name="DeviceRequest_code_DeviceDefinition", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Patient = models.ForeignKey("FHIR_Patient", related_name="DeviceRequest_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Group = models.ForeignKey("FHIR_Group", related_name="DeviceRequest_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Location = models.ForeignKey("FHIR_Location", related_name="DeviceRequest_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Device = models.ForeignKey("FHIR_Device", related_name="DeviceRequest_subject", null=True, blank=True, on_delete=models.SET_NULL)
    encounter = models.ForeignKey("FHIR_Encounter", related_name="DeviceRequest_encounter", null=True, blank=True, on_delete=models.SET_NULL)
    occurrence = FHIR_primitive_DateTimeField(null=True, blank=True, )
    occurrence = models.OneToOneField("FHIR_GP_Period", related_name='DeviceRequest_occurrence', null=True, blank=True, on_delete=models.SET_NULL)
    occurrence = models.OneToOneField("FHIR_GP_Timing", related_name='DeviceRequest_occurrence', null=True, blank=True, on_delete=models.SET_NULL)
    authoredOn = FHIR_primitive_DateTimeField(null=True, blank=True, )
    requester_Device = models.ForeignKey("FHIR_Device", related_name="DeviceRequest_requester", null=True, blank=True, on_delete=models.SET_NULL)
    requester_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="DeviceRequest_requester", null=True, blank=True, on_delete=models.SET_NULL)
    requester_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="DeviceRequest_requester", null=True, blank=True, on_delete=models.SET_NULL)
    requester_Organization = models.ForeignKey("FHIR_Organization", related_name="DeviceRequest_requester", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_performer = 'TODO'
    performer_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_performer}, related_name='DeviceRequest_performer', blank=True)
    performer_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    performer_Practitioner_ref = models.ForeignKey("FHIR_Practitioner", related_name="DeviceRequest_performer_Practitioner", null=True, blank=True, on_delete=models.SET_NULL)
    performer_PractitionerRole_ref = models.ForeignKey("FHIR_PractitionerRole", related_name="DeviceRequest_performer_PractitionerRole", null=True, blank=True, on_delete=models.SET_NULL)
    performer_Organization_ref = models.ForeignKey("FHIR_Organization", related_name="DeviceRequest_performer_Organization", null=True, blank=True, on_delete=models.SET_NULL)
    performer_CareTeam_ref = models.ForeignKey("FHIR_CareTeam", related_name="DeviceRequest_performer_CareTeam", null=True, blank=True, on_delete=models.SET_NULL)
    performer_HealthcareService_ref = models.ForeignKey("FHIR_HealthcareService", related_name="DeviceRequest_performer_HealthcareService", null=True, blank=True, on_delete=models.SET_NULL)
    performer_Patient_ref = models.ForeignKey("FHIR_Patient", related_name="DeviceRequest_performer_Patient", null=True, blank=True, on_delete=models.SET_NULL)
    performer_Device_ref = models.ForeignKey("FHIR_Device", related_name="DeviceRequest_performer_Device", null=True, blank=True, on_delete=models.SET_NULL)
    performer_RelatedPerson_ref = models.ForeignKey("FHIR_RelatedPerson", related_name="DeviceRequest_performer_RelatedPerson", null=True, blank=True, on_delete=models.SET_NULL)
    asNeeded = FHIR_primitive_BooleanField(null=True, blank=True, )
    BINDING_asNeededFor = 'TODO'
    asNeededFor_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_asNeededFor}, related_name='DeviceRequest_asNeededFor', blank=True)
    asNeededFor_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    insurance_Coverage = models.ManyToManyField("FHIR_Coverage", related_name="DeviceRequest_insurance", blank=True)
    insurance_ClaimResponse = models.ManyToManyField("FHIR_ClaimResponse", related_name="DeviceRequest_insurance", blank=True)
    relevantHistory = models.ManyToManyField("FHIR_Provenance", related_name="DeviceRequest_relevantHistory", blank=True)

class FHIR_DeviceRequest_identifier(FHIR_GP_Identifier):
    DeviceRequest = models.ForeignKey(FHIR_DeviceRequest, related_name='DeviceRequest_identifier', null=False, on_delete=models.CASCADE)

class FHIR_DeviceRequest_instantiatesCanonical(models.Model):
    DeviceRequest = models.ForeignKey(FHIR_DeviceRequest, related_name='DeviceRequest_instantiatesCanonical', null=False, on_delete=models.CASCADE)
    
    instantiatesCanonical = FHIR_primitive_CanonicalField(null=True, blank=True, )
    
class FHIR_DeviceRequest_instantiatesUri(models.Model):
    DeviceRequest = models.ForeignKey(FHIR_DeviceRequest, related_name='DeviceRequest_instantiatesUri', null=False, on_delete=models.CASCADE)
    
    instantiatesUri = FHIR_primitive_URIField(null=True, blank=True, )
    
class FHIR_DeviceRequest_parameter(models.Model):
    DeviceRequest = models.ForeignKey(FHIR_DeviceRequest, related_name='DeviceRequest_parameter', null=False, on_delete=models.CASCADE)
    BINDING_code = 'TODO'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='DeviceRequest_parameter_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_value = 'TODO'
    value_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_value}, related_name='DeviceRequest_parameter_value', blank=True)
    value_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value = models.OneToOneField("FHIR_GP_Quantity", related_name='DeviceRequest_parameter_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_Range", related_name='DeviceRequest_parameter_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = FHIR_primitive_BooleanField(null=True, blank=True, )

class FHIR_DeviceRequest_reason(models.Model):
    DeviceRequest = models.ForeignKey(FHIR_DeviceRequest, related_name='DeviceRequest_reason', null=False, on_delete=models.CASCADE)
    BINDING_reason = 'TODO'
    reason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_reason}, related_name='DeviceRequest_reason', blank=True)
    reason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    reason_Condition_ref = models.ForeignKey("FHIR_Condition", related_name="DeviceRequest_reason_Condition", null=True, blank=True, on_delete=models.SET_NULL)
    reason_Observation_ref = models.ForeignKey("FHIR_Observation", related_name="DeviceRequest_reason_Observation", null=True, blank=True, on_delete=models.SET_NULL)
    reason_DiagnosticReport_ref = models.ForeignKey("FHIR_DiagnosticReport", related_name="DeviceRequest_reason_DiagnosticReport", null=True, blank=True, on_delete=models.SET_NULL)
    reason_DocumentReference_ref = models.ForeignKey("FHIR_DocumentReference", related_name="DeviceRequest_reason_DocumentReference", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_DeviceRequest_note(FHIR_GP_Annotation):
    DeviceRequest = models.ForeignKey(FHIR_DeviceRequest, related_name='DeviceRequest_note', null=False, on_delete=models.CASCADE)
