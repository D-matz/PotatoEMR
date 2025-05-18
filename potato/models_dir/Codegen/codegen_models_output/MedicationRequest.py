#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_MedicationRequest(models.Model):
    basedOn_CarePlan = models.ManyToManyField("FHIR_CarePlan", related_name="MedicationRequest_basedOn", blank=True)
    basedOn_MedicationRequest = models.ManyToManyField("FHIR_MedicationRequest", related_name="MedicationRequest_basedOn", blank=True)
    basedOn_ServiceRequest = models.ManyToManyField("FHIR_ServiceRequest", related_name="MedicationRequest_basedOn", blank=True)
    basedOn_ImmunizationRecommendation = models.ManyToManyField("FHIR_ImmunizationRecommendation", related_name="MedicationRequest_basedOn", blank=True)
    basedOn_RequestOrchestration = models.ManyToManyField("FHIR_RequestOrchestration", related_name="MedicationRequest_basedOn", blank=True)
    priorPrescription = models.ForeignKey("FHIR_MedicationRequest", related_name="MedicationRequest_priorPrescription", null=True, blank=True, on_delete=models.SET_NULL)
    groupIdentifier = models.OneToOneField("FHIR_GP_Identifier", related_name='MedicationRequest_groupIdentifier', null=True, blank=True, on_delete=models.SET_NULL)
    class StatusChoices(models.TextChoices): ACTIVE = 'active', 'Active'; ON_HOLD = 'on-hold', 'On-hold'; ENDED = 'ended', 'Ended'; STOPPED = 'stopped', 'Stopped'; COMPLETED = 'completed', 'Completed'; CANCELLED = 'cancelled', 'Cancelled'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; DRAFT = 'draft', 'Draft'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    BINDING_statusReason = "TODO"
    statusReason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_statusReason}, related_name='MedicationRequest_statusReason', blank=True)
    statusReason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    statusChanged = FHIR_primitive_DateTimeField(null=True, blank=True, )
    class IntentChoices(models.TextChoices): PROPOSAL = 'proposal', 'Proposal'; PLAN = 'plan', 'Plan'; ORDER = 'order', 'Order'; ORIGINAL_ORDER = 'original-order', 'Original-order'; REFLEX_ORDER = 'reflex-order', 'Reflex-order'; FILLER_ORDER = 'filler-order', 'Filler-order'; INSTANCE_ORDER = 'instance-order', 'Instance-order'; OPTION = 'option', 'Option'; 
    intent = FHIR_primitive_CodeField(choices=IntentChoices.choices, null=True, blank=True, )
    class PriorityChoices(models.TextChoices): ROUTINE = 'routine', 'Routine'; URGENT = 'urgent', 'Urgent'; ASAP = 'asap', 'Asap'; STAT = 'stat', 'Stat'; 
    priority = FHIR_primitive_CodeField(choices=PriorityChoices.choices, null=True, blank=True, )
    doNotPerform = FHIR_primitive_BooleanField(null=True, blank=True, )
    BINDING_medication = "TODO"
    medication_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_medication}, related_name='MedicationRequest_medication', blank=True)
    medication_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    medication_Medication_ref = models.ForeignKey("FHIR_Medication", related_name="MedicationRequest_medication_Medication", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Patient = models.ForeignKey("FHIR_Patient", related_name="MedicationRequest_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Group = models.ForeignKey("FHIR_Group", related_name="MedicationRequest_subject", null=True, blank=True, on_delete=models.SET_NULL)
    informationSource_Patient = models.ManyToManyField("FHIR_Patient", related_name="MedicationRequest_informationSource", blank=True)
    informationSource_Practitioner = models.ManyToManyField("FHIR_Practitioner", related_name="MedicationRequest_informationSource", blank=True)
    informationSource_PractitionerRole = models.ManyToManyField("FHIR_PractitionerRole", related_name="MedicationRequest_informationSource", blank=True)
    informationSource_RelatedPerson = models.ManyToManyField("FHIR_RelatedPerson", related_name="MedicationRequest_informationSource", blank=True)
    informationSource_Organization = models.ManyToManyField("FHIR_Organization", related_name="MedicationRequest_informationSource", blank=True)
    informationSource_Group = models.ManyToManyField("FHIR_Group", related_name="MedicationRequest_informationSource", blank=True)
    encounter = models.ForeignKey("FHIR_Encounter", related_name="MedicationRequest_encounter", null=True, blank=True, on_delete=models.SET_NULL)
                            #skipping Reference(Any) for field supportingInformation as MedicationRequest supportingInformation not in referenceAny_targets
    authoredOn = FHIR_primitive_DateTimeField(null=True, blank=True, )
    requester_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="MedicationRequest_requester", null=True, blank=True, on_delete=models.SET_NULL)
    requester_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="MedicationRequest_requester", null=True, blank=True, on_delete=models.SET_NULL)
    requester_Organization = models.ForeignKey("FHIR_Organization", related_name="MedicationRequest_requester", null=True, blank=True, on_delete=models.SET_NULL)
    requester_Patient = models.ForeignKey("FHIR_Patient", related_name="MedicationRequest_requester", null=True, blank=True, on_delete=models.SET_NULL)
    requester_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="MedicationRequest_requester", null=True, blank=True, on_delete=models.SET_NULL)
    requester_Device = models.ForeignKey("FHIR_Device", related_name="MedicationRequest_requester", null=True, blank=True, on_delete=models.SET_NULL)
    reported = FHIR_primitive_BooleanField(null=True, blank=True, )
    BINDING_performerType = "TODO"
    performerType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_performerType}, related_name='MedicationRequest_performerType', blank=True)
    performerType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    performer_Practitioner = models.ManyToManyField("FHIR_Practitioner", related_name="MedicationRequest_performer", blank=True)
    performer_PractitionerRole = models.ManyToManyField("FHIR_PractitionerRole", related_name="MedicationRequest_performer", blank=True)
    performer_Organization = models.ManyToManyField("FHIR_Organization", related_name="MedicationRequest_performer", blank=True)
    performer_Patient = models.ManyToManyField("FHIR_Patient", related_name="MedicationRequest_performer", blank=True)
    performer_DeviceDefinition = models.ManyToManyField("FHIR_DeviceDefinition", related_name="MedicationRequest_performer", blank=True)
    performer_RelatedPerson = models.ManyToManyField("FHIR_RelatedPerson", related_name="MedicationRequest_performer", blank=True)
    performer_CareTeam = models.ManyToManyField("FHIR_CareTeam", related_name="MedicationRequest_performer", blank=True)
    performer_HealthcareService = models.ManyToManyField("FHIR_HealthcareService", related_name="MedicationRequest_performer", blank=True)
    performer_Group = models.ManyToManyField("FHIR_Group", related_name="MedicationRequest_performer", blank=True)
    recorder_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="MedicationRequest_recorder", null=True, blank=True, on_delete=models.SET_NULL)
    recorder_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="MedicationRequest_recorder", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_courseOfTherapyType = "TODO"
    courseOfTherapyType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_courseOfTherapyType}, related_name='MedicationRequest_courseOfTherapyType', blank=True)
    courseOfTherapyType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    insurance_Coverage = models.ManyToManyField("FHIR_Coverage", related_name="MedicationRequest_insurance", blank=True)
    insurance_ClaimResponse = models.ManyToManyField("FHIR_ClaimResponse", related_name="MedicationRequest_insurance", blank=True)
    renderedDosageInstruction = FHIR_primitive_MarkdownField(null=True, blank=True, )
    effectiveDosePeriod = models.OneToOneField("FHIR_GP_Period", related_name='MedicationRequest_effectiveDosePeriod', null=True, blank=True, on_delete=models.SET_NULL)
    eventHistory = models.ManyToManyField("FHIR_Provenance", related_name="MedicationRequest_eventHistory", blank=True)

class FHIR_MedicationRequest_identifier(FHIR_GP_Identifier):
    MedicationRequest = models.ForeignKey(FHIR_MedicationRequest, related_name='MedicationRequest_identifier', null=False, on_delete=models.CASCADE)

class FHIR_MedicationRequest_category(models.Model):
    MedicationRequest = models.ForeignKey(FHIR_MedicationRequest, related_name='MedicationRequest_category', null=False, on_delete=models.CASCADE)
    BINDING_category = "TODO"
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='MedicationRequest_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_MedicationRequest_device(models.Model):
    MedicationRequest = models.ForeignKey(FHIR_MedicationRequest, related_name='MedicationRequest_device', null=False, on_delete=models.CASCADE)
    BINDING_device = "TODO"
    device_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_device}, related_name='MedicationRequest_device', blank=True)
    device_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    device_DeviceDefinition_ref = models.ForeignKey("FHIR_DeviceDefinition", related_name="MedicationRequest_device_DeviceDefinition", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_MedicationRequest_reason(models.Model):
    MedicationRequest = models.ForeignKey(FHIR_MedicationRequest, related_name='MedicationRequest_reason', null=False, on_delete=models.CASCADE)
    BINDING_reason = "TODO"
    reason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_reason}, related_name='MedicationRequest_reason', blank=True)
    reason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    reason_Condition_ref = models.ForeignKey("FHIR_Condition", related_name="MedicationRequest_reason_Condition", null=True, blank=True, on_delete=models.SET_NULL)
    reason_Observation_ref = models.ForeignKey("FHIR_Observation", related_name="MedicationRequest_reason_Observation", null=True, blank=True, on_delete=models.SET_NULL)
    reason_DiagnosticReport_ref = models.ForeignKey("FHIR_DiagnosticReport", related_name="MedicationRequest_reason_DiagnosticReport", null=True, blank=True, on_delete=models.SET_NULL)
    reason_Procedure_ref = models.ForeignKey("FHIR_Procedure", related_name="MedicationRequest_reason_Procedure", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_MedicationRequest_note(FHIR_GP_Annotation):
    MedicationRequest = models.ForeignKey(FHIR_MedicationRequest, related_name='MedicationRequest_note', null=False, on_delete=models.CASCADE)

class FHIR_MedicationRequest_dosageInstruction(FHIR_SP_Dosage):
    MedicationRequest = models.ForeignKey(FHIR_MedicationRequest, related_name='MedicationRequest_dosageInstruction', null=False, on_delete=models.CASCADE)

class FHIR_MedicationRequest_dispenseRequest(models.Model):
    MedicationRequest = models.ForeignKey(FHIR_MedicationRequest, related_name='MedicationRequest_dispenseRequest', null=False, on_delete=models.CASCADE)
    dispenseInterval = models.OneToOneField("FHIR_GP_Quantity_Duration", related_name='MedicationRequest_dispenseRequest_dispenseInterval', null=True, blank=True, on_delete=models.SET_NULL)
    validityPeriod = models.OneToOneField("FHIR_GP_Period", related_name='MedicationRequest_dispenseRequest_validityPeriod', null=True, blank=True, on_delete=models.SET_NULL)
    numberOfRepeatsAllowed = FHIR_primitive_UnsignedIntField(null=True, blank=True, )
    quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='MedicationRequest_dispenseRequest_quantity', null=True, blank=True, on_delete=models.SET_NULL)
    expectedSupplyDuration = models.OneToOneField("FHIR_GP_Quantity_Duration", related_name='MedicationRequest_dispenseRequest_expectedSupplyDuration', null=True, blank=True, on_delete=models.SET_NULL)
    dispenser = models.ForeignKey("FHIR_Organization", related_name="MedicationRequest_dispenseRequest_dispenser", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_doseAdministrationAid = "TODO"
    doseAdministrationAid_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_doseAdministrationAid}, related_name='MedicationRequest_dispenseRequest_doseAdministrationAid', blank=True)
    doseAdministrationAid_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_MedicationRequest_dispenseRequest_initialFill(models.Model):
    MedicationRequest_dispenseRequest = models.ForeignKey(FHIR_MedicationRequest_dispenseRequest, related_name='MedicationRequest_dispenseRequest_initialFill', null=False, on_delete=models.CASCADE)
    quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='MedicationRequest_dispenseRequest_initialFill_quantity', null=True, blank=True, on_delete=models.SET_NULL)
    duration = models.OneToOneField("FHIR_GP_Quantity_Duration", related_name='MedicationRequest_dispenseRequest_initialFill_duration', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_MedicationRequest_dispenseRequest_dispenserInstruction(FHIR_GP_Annotation):
    MedicationRequest_dispenseRequest = models.ForeignKey(FHIR_MedicationRequest_dispenseRequest, related_name='MedicationRequest_dispenseRequest_dispenserInstruction', null=False, on_delete=models.CASCADE)

class FHIR_MedicationRequest_substitution(models.Model):
    MedicationRequest = models.ForeignKey(FHIR_MedicationRequest, related_name='MedicationRequest_substitution', null=False, on_delete=models.CASCADE)
    allowed_boolean = FHIR_primitive_BooleanField(null=True, blank=True, )
    BINDING_allowed_CodeableConcept = "TODO"
    allowed_CodeableConcept_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_allowed_CodeableConcept}, related_name='MedicationRequest_substitution_allowed_CodeableConcept', blank=True)
    allowed_CodeableConcept_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_reason = "TODO"
    reason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_reason}, related_name='MedicationRequest_substitution_reason', blank=True)
    reason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
