
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_ServiceRequest(models.Model):
    basedOn_CarePlan = models.ManyToManyField("FHIR_CarePlan", related_name="ServiceRequest_basedOn", blank=True)
    basedOn_ServiceRequest = models.ManyToManyField("FHIR_ServiceRequest", related_name="ServiceRequest_basedOn", blank=True)
    basedOn_MedicationRequest = models.ManyToManyField("FHIR_MedicationRequest", related_name="ServiceRequest_basedOn", blank=True)
    basedOn_RequestOrchestration = models.ManyToManyField("FHIR_RequestOrchestration", related_name="ServiceRequest_basedOn", blank=True)
    basedOn_NutritionOrder = models.ManyToManyField("FHIR_NutritionOrder", related_name="ServiceRequest_basedOn", blank=True)
    replaces = models.ManyToManyField("FHIR_ServiceRequest", related_name="ServiceRequest_replaces", blank=True)
    requisition = models.OneToOneField("FHIR_GP_Identifier", related_name='ServiceRequest_requisition', null=True, blank=True, on_delete=models.SET_NULL)
    class StatusChoices(models.TextChoices): DRAFT = 'draft', 'Draft'; ACTIVE = 'active', 'Active'; ON_HOLD = 'on-hold', 'On-hold'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; ENDED = 'ended', 'Ended'; COMPLETED = 'completed', 'Completed'; REVOKED = 'revoked', 'Revoked'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    class IntentChoices(models.TextChoices): PROPOSAL = 'proposal', 'Proposal'; PLAN = 'plan', 'Plan'; DIRECTIVE = 'directive', 'Directive'; ORDER_+ = 'order +', 'Order +'; 
    intent = FHIR_primitive_CodeField(choices=IntentChoices.choices, null=True, blank=True, )
    class PriorityChoices(models.TextChoices): ROUTINE = 'routine', 'Routine'; URGENT = 'urgent', 'Urgent'; ASAP = 'asap', 'Asap'; STAT = 'stat', 'Stat'; 
    priority = FHIR_primitive_CodeField(choices=PriorityChoices.choices, null=True, blank=True, )
    doNotPerform = FHIR_primitive_BooleanField(null=True, blank=True, )
    BINDING_code = 'TODO'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='ServiceRequest_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    code_ActivityDefinition_ref = models.ForeignKey("FHIR_ActivityDefinition", related_name="ServiceRequest_code", null=True, blank=True, on_delete=models.SET_NULL)
    code_PlanDefinition_ref = models.ForeignKey("FHIR_PlanDefinition", related_name="ServiceRequest_code", null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='ServiceRequest_quantity', null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.OneToOneField("FHIR_GP_Ratio", related_name='ServiceRequest_quantity', null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.OneToOneField("FHIR_GP_Range", related_name='ServiceRequest_quantity', null=True, blank=True, on_delete=models.SET_NULL)
    subject_Patient = models.ForeignKey("FHIR_Patient", related_name="ServiceRequest_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Group = models.ForeignKey("FHIR_Group", related_name="ServiceRequest_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Location = models.ForeignKey("FHIR_Location", related_name="ServiceRequest_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Device = models.ForeignKey("FHIR_Device", related_name="ServiceRequest_subject", null=True, blank=True, on_delete=models.SET_NULL)
    encounter = models.ForeignKey("FHIR_Encounter", related_name="ServiceRequest_encounter", null=True, blank=True, on_delete=models.SET_NULL)
    occurrence = FHIR_primitive_DateTimeField(null=True, blank=True, )
    occurrence = models.OneToOneField("FHIR_GP_Period", related_name='ServiceRequest_occurrence', null=True, blank=True, on_delete=models.SET_NULL)
    occurrence = models.OneToOneField("FHIR_GP_Timing", related_name='ServiceRequest_occurrence', null=True, blank=True, on_delete=models.SET_NULL)
    asNeeded = FHIR_primitive_BooleanField(null=True, blank=True, )
    authoredOn = FHIR_primitive_DateTimeField(null=True, blank=True, )
    requester_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="ServiceRequest_requester", null=True, blank=True, on_delete=models.SET_NULL)
    requester_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="ServiceRequest_requester", null=True, blank=True, on_delete=models.SET_NULL)
    requester_Organization = models.ForeignKey("FHIR_Organization", related_name="ServiceRequest_requester", null=True, blank=True, on_delete=models.SET_NULL)
    requester_Patient = models.ForeignKey("FHIR_Patient", related_name="ServiceRequest_requester", null=True, blank=True, on_delete=models.SET_NULL)
    requester_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="ServiceRequest_requester", null=True, blank=True, on_delete=models.SET_NULL)
    requester_Device = models.ForeignKey("FHIR_Device", related_name="ServiceRequest_requester", null=True, blank=True, on_delete=models.SET_NULL)
    requester_Group = models.ForeignKey("FHIR_Group", related_name="ServiceRequest_requester", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_performerType = 'TODO'
    performerType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_performerType}, related_name='ServiceRequest_performerType', blank=True)
    performerType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    performer_Practitioner = models.ManyToManyField("FHIR_Practitioner", related_name="ServiceRequest_performer", blank=True)
    performer_PractitionerRole = models.ManyToManyField("FHIR_PractitionerRole", related_name="ServiceRequest_performer", blank=True)
    performer_Organization = models.ManyToManyField("FHIR_Organization", related_name="ServiceRequest_performer", blank=True)
    performer_CareTeam = models.ManyToManyField("FHIR_CareTeam", related_name="ServiceRequest_performer", blank=True)
    performer_HealthcareService = models.ManyToManyField("FHIR_HealthcareService", related_name="ServiceRequest_performer", blank=True)
    performer_Patient = models.ManyToManyField("FHIR_Patient", related_name="ServiceRequest_performer", blank=True)
    performer_Device = models.ManyToManyField("FHIR_Device", related_name="ServiceRequest_performer", blank=True)
    performer_RelatedPerson = models.ManyToManyField("FHIR_RelatedPerson", related_name="ServiceRequest_performer", blank=True)
    performer_Group = models.ManyToManyField("FHIR_Group", related_name="ServiceRequest_performer", blank=True)
    insurance_Coverage = models.ManyToManyField("FHIR_Coverage", related_name="ServiceRequest_insurance", blank=True)
    insurance_ClaimResponse = models.ManyToManyField("FHIR_ClaimResponse", related_name="ServiceRequest_insurance", blank=True)
    specimen = models.ManyToManyField("FHIR_Specimen", related_name="ServiceRequest_specimen", blank=True)
    bodyStructure = models.ForeignKey("FHIR_BodyStructure", related_name="ServiceRequest_bodyStructure", null=True, blank=True, on_delete=models.SET_NULL)
    relevantHistory = models.ManyToManyField("FHIR_Provenance", related_name="ServiceRequest_relevantHistory", blank=True)

class FHIR_ServiceRequest_identifier(FHIR_GP_Identifier):
    ServiceRequest = models.ForeignKey(FHIR_ServiceRequest, related_name='ServiceRequest_identifier', null=False, on_delete=models.CASCADE)

class FHIR_ServiceRequest_instantiatesCanonical(models.Model):
    ServiceRequest = models.ForeignKey(FHIR_ServiceRequest, related_name='ServiceRequest_instantiatesCanonical', null=False, on_delete=models.CASCADE)
    
    instantiatesCanonical = FHIR_primitive_CanonicalField(null=True, blank=True, )
    
class FHIR_ServiceRequest_instantiatesUri(models.Model):
    ServiceRequest = models.ForeignKey(FHIR_ServiceRequest, related_name='ServiceRequest_instantiatesUri', null=False, on_delete=models.CASCADE)
    
    instantiatesUri = FHIR_primitive_URIField(null=True, blank=True, )
    
class FHIR_ServiceRequest_category(models.Model):
    ServiceRequest = models.ForeignKey(FHIR_ServiceRequest, related_name='ServiceRequest_category', null=False, on_delete=models.CASCADE)
    BINDING_category = 'TODO'
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='ServiceRequest_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ServiceRequest_orderDetail(models.Model):
    ServiceRequest = models.ForeignKey(FHIR_ServiceRequest, related_name='ServiceRequest_orderDetail', null=False, on_delete=models.CASCADE)
    BINDING_parameterFocus = 'TODO'
    parameterFocus_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_parameterFocus}, related_name='ServiceRequest_orderDetail_parameterFocus', blank=True)
    parameterFocus_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    parameterFocus_Device_ref = models.ForeignKey("FHIR_Device", related_name="ServiceRequest_orderDetail_parameterFocus", null=True, blank=True, on_delete=models.SET_NULL)
    parameterFocus_DeviceDefinition_ref = models.ForeignKey("FHIR_DeviceDefinition", related_name="ServiceRequest_orderDetail_parameterFocus", null=True, blank=True, on_delete=models.SET_NULL)
    parameterFocus_DeviceRequest_ref = models.ForeignKey("FHIR_DeviceRequest", related_name="ServiceRequest_orderDetail_parameterFocus", null=True, blank=True, on_delete=models.SET_NULL)
    parameterFocus_SupplyRequest_ref = models.ForeignKey("FHIR_SupplyRequest", related_name="ServiceRequest_orderDetail_parameterFocus", null=True, blank=True, on_delete=models.SET_NULL)
    parameterFocus_Medication_ref = models.ForeignKey("FHIR_Medication", related_name="ServiceRequest_orderDetail_parameterFocus", null=True, blank=True, on_delete=models.SET_NULL)
    parameterFocus_MedicationRequest_ref = models.ForeignKey("FHIR_MedicationRequest", related_name="ServiceRequest_orderDetail_parameterFocus", null=True, blank=True, on_delete=models.SET_NULL)
    parameterFocus_BiologicallyDerivedProduct_ref = models.ForeignKey("FHIR_BiologicallyDerivedProduct", related_name="ServiceRequest_orderDetail_parameterFocus", null=True, blank=True, on_delete=models.SET_NULL)
    parameterFocus_Substance_ref = models.ForeignKey("FHIR_Substance", related_name="ServiceRequest_orderDetail_parameterFocus", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ServiceRequest_orderDetail_parameter(models.Model):
    ServiceRequest_orderDetail = models.ForeignKey(FHIR_ServiceRequest_orderDetail, related_name='ServiceRequest_orderDetail_parameter', null=False, on_delete=models.CASCADE)
    BINDING_code = 'TODO'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='ServiceRequest_orderDetail_parameter_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value = models.OneToOneField("FHIR_GP_Quantity", related_name='ServiceRequest_orderDetail_parameter_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_Ratio", related_name='ServiceRequest_orderDetail_parameter_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_Range", related_name='ServiceRequest_orderDetail_parameter_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = FHIR_primitive_BooleanField(null=True, blank=True, )
    BINDING_value = 'TODO'
    value_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_value}, related_name='ServiceRequest_orderDetail_parameter_value', blank=True)
    value_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value = FHIR_primitive_StringField(null=True, blank=True, )
    value = models.OneToOneField("FHIR_GP_Period", related_name='ServiceRequest_orderDetail_parameter_value', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ServiceRequest_asNeededFor(models.Model):
    ServiceRequest = models.ForeignKey(FHIR_ServiceRequest, related_name='ServiceRequest_asNeededFor', null=False, on_delete=models.CASCADE)
    BINDING_asNeededFor = 'TODO'
    asNeededFor_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_asNeededFor}, related_name='ServiceRequest_asNeededFor', blank=True)
    asNeededFor_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ServiceRequest_location(models.Model):
    ServiceRequest = models.ForeignKey(FHIR_ServiceRequest, related_name='ServiceRequest_location', null=False, on_delete=models.CASCADE)
    BINDING_location = 'TODO'
    location_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_location}, related_name='ServiceRequest_location', blank=True)
    location_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    location_Location_ref = models.ForeignKey("FHIR_Location", related_name="ServiceRequest_location", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ServiceRequest_reason(models.Model):
    ServiceRequest = models.ForeignKey(FHIR_ServiceRequest, related_name='ServiceRequest_reason', null=False, on_delete=models.CASCADE)
    BINDING_reason = 'TODO'
    reason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_reason}, related_name='ServiceRequest_reason', blank=True)
    reason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    reason_Condition_ref = models.ForeignKey("FHIR_Condition", related_name="ServiceRequest_reason", null=True, blank=True, on_delete=models.SET_NULL)
    reason_Observation_ref = models.ForeignKey("FHIR_Observation", related_name="ServiceRequest_reason", null=True, blank=True, on_delete=models.SET_NULL)
    reason_DiagnosticReport_ref = models.ForeignKey("FHIR_DiagnosticReport", related_name="ServiceRequest_reason", null=True, blank=True, on_delete=models.SET_NULL)
    reason_DocumentReference_ref = models.ForeignKey("FHIR_DocumentReference", related_name="ServiceRequest_reason", null=True, blank=True, on_delete=models.SET_NULL)
    reason_DetectedIssue_ref = models.ForeignKey("FHIR_DetectedIssue", related_name="ServiceRequest_reason", null=True, blank=True, on_delete=models.SET_NULL)
    reason_Procedure_ref = models.ForeignKey("FHIR_Procedure", related_name="ServiceRequest_reason", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ServiceRequest_supportingInfo(models.Model):
    ServiceRequest = models.ForeignKey(FHIR_ServiceRequest, related_name='ServiceRequest_supportingInfo', null=False, on_delete=models.CASCADE)
    BINDING_supportingInfo = 'TODO'
    supportingInfo_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_supportingInfo}, related_name='ServiceRequest_supportingInfo', blank=True)
    supportingInfo_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_ServiceRequest_bodySite(models.Model):
    ServiceRequest = models.ForeignKey(FHIR_ServiceRequest, related_name='ServiceRequest_bodySite', null=False, on_delete=models.CASCADE)
    BINDING_bodySite = 'TODO'
    bodySite_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_bodySite}, related_name='ServiceRequest_bodySite', blank=True)
    bodySite_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ServiceRequest_note(FHIR_GP_Annotation):
    ServiceRequest = models.ForeignKey(FHIR_ServiceRequest, related_name='ServiceRequest_note', null=False, on_delete=models.CASCADE)

class FHIR_ServiceRequest_patientInstruction(models.Model):
    ServiceRequest = models.ForeignKey(FHIR_ServiceRequest, related_name='ServiceRequest_patientInstruction', null=False, on_delete=models.CASCADE)
    instruction = FHIR_primitive_MarkdownField(null=True, blank=True, )
    instruction = models.ForeignKey("FHIR_DocumentReference", related_name="ServiceRequest_patientInstruction_instruction", null=True, blank=True, on_delete=models.SET_NULL)
