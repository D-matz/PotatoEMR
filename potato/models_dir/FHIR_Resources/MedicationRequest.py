from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_MedicationRequest(models.Model):
	#Identifier ForeignKey to this, related_name=medicationRequest_identifiers
	basedOn_CarePlan = models.ManyToManyField("FHIR_CarePlan", related_name="mr_basedOn_CarePlan", blank=True)
	basedOn_MedicationRequest = models.ManyToManyField("FHIR_MedicationRequest", related_name="mr_basedOn_MedicationRequest", blank=True)
	basedOn_ServiceRequest = models.ManyToManyField("FHIR_ServiceRequest", related_name="mr_basedOn_ServiceRequest", blank=True)
	basedOn_ImmunizationRecommendation = models.ManyToManyField("FHIR_ImmunizationRecommendation", related_name="mr_basedOn_ImmunizationRecommendation", blank=True)
	basedOn_RequestOrchestration = models.ManyToManyField("FHIR_RequestOrchestration", related_name="mr_basedOn_RequestOrchestration", blank=True)

	priorPrescription = models.ForeignKey("FHIR_MedicationRequest", null=True, blank=True, on_delete=models.SET_NULL)
	groupIdentifier = models.ForeignKey("FHIR_GP_Identifier", null=True, blank=True, on_delete=models.SET_NULL)

	BINDING_RULE_STATUS_REASON = "todo"
	statusReason_cc =  models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={'codings__binding_rule': BINDING_RULE_STATUS_REASON }, related_name="status_reason", blank=True)
	statusReason_cctext = FHIR_primitive_StringField(max_length=255, null=True, blank=True)

	class IntentChoices(models.TextChoices): PROPOSAL = 'proposal', 'Proposal'; PLAN = 'plan', 'Plan'; ORDER = 'order', 'Order'; ORIGINAL_ORDER = 'original-order', 'Original Order'; REFLEX_ORDER = 'reflex-order', 'Reflex Order'; FILLER_ORDER = 'filler-order', 'Filler Order'; INSTANCE_ORDER = 'instance-order', 'Instance Order'; OPTION = 'option', 'Option'
	intent = FHIR_primitive_CodeField(max_length=16, choices=IntentChoices.choices, null=False)

	#catgory foreign key to this

	class PriorityChoices(models.TextChoices): ROUTINE = 'routine', 'Routine'; URGENT = 'urgent', 'Urgent'; ASAP = 'asap', 'ASAP'; STAT = 'stat', 'Stat'
	priority = FHIR_primitive_CodeField(max_length=10, choices=PriorityChoices.choices, null=True)

	doNotPerform = FHIR_primitive_BooleanField(default=False)

	BINDING_RULE_MEDICATION = "todo"
	medication_cc =  models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={'codings__binding_rule': BINDING_RULE_MEDICATION }, related_name="medication_request_medication", blank=True)
	medication_cctext = FHIR_primitive_StringField(max_length=255, null=True, blank=True)
	medication_ref = models.ForeignKey('FHIR_Medication', related_name="medication", null=True, on_delete=models.SET_NULL)

	subject_patient = models.ForeignKey('FHIR_Patient', related_name="mr_subject_patient", null=True, on_delete=models.SET_NULL)
	subject_group = models.ForeignKey('FHIR_Patient', related_name="mr_subject_group", null=True, on_delete=models.SET_NULL)

	informationSource_patient = models.ManyToManyField('FHIR_Medication', related_name="informationSource_patient", blank=True)
	informationSource_practitioner = models.ManyToManyField('FHIR_Medication', related_name="informationSource_practitioner", blank=True)
	informationSource_practitionerRole = models.ManyToManyField('FHIR_Medication', related_name="informationSource_practitionerRole", blank=True)
	informationSource_relatedPerson = models.ManyToManyField('FHIR_Medication', related_name="informationSource_relatedPerson", blank=True)
	informationSource_organization = models.ManyToManyField('FHIR_Medication', related_name="informationSource_organization", blank=True)
	informationSource_group = models.ManyToManyField('FHIR_Medication', related_name="informationSource_group", blank=True)

	encounter = models.ForeignKey('FHIR_Encounter', related_name="encounter", null=True, on_delete=models.SET_NULL)

	#TODO supportingInformation ref to any idk

	authoredOn = FHIR_primitive_DateTimeField(null=True, blank=True)

	requester_practitioner = models.ForeignKey('FHIR_Practitioner', related_name="requester_practitioner", null=True, on_delete=models.SET_NULL)
	requester_practitionerRole = models.ForeignKey('FHIR_PractitionerRole', related_name="requester_practitionerRole", null=True, on_delete=models.SET_NULL)
	requester_organization = models.ForeignKey('FHIR_Organization', related_name="requester_organization", null=True, on_delete=models.SET_NULL)
	requester_patient = models.ForeignKey('FHIR_Patient', related_name="requester_patient", null=True, on_delete=models.SET_NULL)
	requester_relatedPerson = models.ForeignKey('FHIR_RelatedPerson', related_name="requester_relatedPerson", null=True, on_delete=models.SET_NULL)
	requester_device = models.ForeignKey('FHIR_Device', related_name="requester_device", null=True, on_delete=models.SET_NULL)

	reported = FHIR_primitive_BooleanField()

	BINDING_RULE_PERFORMER_TYPE = "idk"
	performerType_cc =  models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={'codings__binding_rule': BINDING_RULE_PERFORMER_TYPE }, related_name="performer_type", blank=True)
	performerType_cctext = FHIR_primitive_StringField(max_length=255, null=True, blank=True)

	performer_practitioner = models.ManyToManyField('FHIR_Practitioner', related_name="performer_practitioner", blank=True)
	performer_practitionerRole = models.ManyToManyField('FHIR_PractitionerRole', related_name="performer_practitionerRole", blank=True)
	performer_organization = models.ManyToManyField('FHIR_Organization', related_name="performer_organization", blank=True)
	performer_patient = models.ManyToManyField('FHIR_Patient', related_name="performer_patient", blank=True)
	performer_deviceDefinition = models.ManyToManyField('FHIR_DeviceDefinition', related_name="performer_deviceDefinition", blank=True)
	performer_relatedPerson = models.ManyToManyField('FHIR_RelatedPerson', related_name="performer_relatedPerson", blank=True)
	performer_careTeam = models.ManyToManyField('FHIR_CareTeam', related_name="performer_careTeam", blank=True)
	performer_healthcareService = models.ManyToManyField('FHIR_HealthcareService', related_name="performer_healthcareService", blank=True)
	performer_group = models.ManyToManyField('FHIR_Group', related_name="performer_group", blank=True)

	#device foreign key to this


	recorder_practitioner = models.ForeignKey('FHIR_Practitioner', related_name="recorder_practitioner", null=True, on_delete=models.SET_NULL)
	recorder_practitionerRole = models.ForeignKey('FHIR_PractitionerRole', related_name="recorder_practitionerRole", null=True, on_delete=models.SET_NULL)


	BINDING_RULE_COURSE_OF_THERAPY = ""
	courseOfTherapyType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={'codings__binding_rule': BINDING_RULE_COURSE_OF_THERAPY }, blank=True, related_name="course_of_therapy_type")
	courseOfTherapyType_cctext = FHIR_primitive_StringField(max_length=255, null=True, blank=True)

	insurance_coverage = models.ManyToManyField("FHIR_Coverage", blank=True)
	insurance_claimResponse = models.ManyToManyField("FHIR_ClaimResponse", blank=True)

	#note - annotation foreign key to this

	renderedDosageInstruction = FHIR_primitive_MarkdownField()
	effectiveDosagePeriod = models.OneToOneField(FHIR_GP_Period, on_delete=models.SET_NULL, null=True, blank=True)

	#dosageInstruction dosage foreign key to this (create special purpose data types)

	#dispenseRequest backbone
	#initialFill backbone
	dispenseRequest_initialFill_quantity = FHIR_GP_Quantity_Simple()
	dispenseRequest_initialFill_duration = FHIR_GP_Quantity_Duration()
	dispenseRequest_dispenseInterval = FHIR_GP_Quantity_Duration()
	dispenseRequest_validityPeriod = models.OneToOneField(FHIR_GP_Period, on_delete=models.SET_NULL, related_name="mr_dispenseRequest_validityPeriod", null=True, blank=True)
	dispenseRequest_numberOfRepeatsAllowed = FHIR_primitive_UnsignedIntField(default=0)
	dispenseRequest_quantity = FHIR_GP_Quantity_Simple()
	dispenseRequest_expectedSupplyDuration = FHIR_GP_Quantity_Duration()
	dispenseRequest_dispenser = models.ForeignKey("FHIR_Organization", null=True, on_delete=models.SET_NULL)
	#dispenserInstruction foreign key to this
	BINDING_RULE_DOSE_AIDS = ""
	dispenseRequest_doseAdministrationAid_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={'codings__binding_rule': BINDING_RULE_DOSE_AIDS}, blank=True, related_name="dose_administration_aid")
	dispenseRequest_doseAdministrationAid_cctext = FHIR_primitive_StringField(max_length=255, null=True, blank=True)

	#substitution backbone
	substitution_allowed = FHIR_primitive_BooleanField()
	#TODO not sure what allowedCodeableConcept means, no binding rule
	BINDING_RULE_SUBSTANCE_ADMIN_SUBSTITUTION_REASON = ""
	substitution_reason_cc= models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={'codings__binding_rule': BINDING_RULE_SUBSTANCE_ADMIN_SUBSTITUTION_REASON}, blank=True, related_name="substitution_reason")
	substitution_reason_cctext = FHIR_primitive_StringField(max_length=255, null=True, blank=True)

	eventHistory = models.ManyToManyField("FHIR_Provenance")	

class FHIR_MedicationRequest_Category(models.Model):
    medicationRequest = models.ForeignKey(FHIR_MedicationRequest, null=False, on_delete=models.CASCADE)
    BINDING_RULE_CATEGORY = "todo"
    category_cc =  models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={'codings__binding_rule': BINDING_RULE_CATEGORY })
    category_cctext = FHIR_primitive_StringField(max_length=255, null=True, blank=True)

class FHIR_MedicationRequest_Device(models.Model):
    BINDING_RULE_DEVICE_DEFINITION = "todo"
    device_cc =  models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={'codings__binding_rule': BINDING_RULE_DEVICE_DEFINITION })
    device_cctext = FHIR_primitive_StringField(max_length=255, null=True, blank=True)
    device_ref = models.ForeignKey('FHIR_DeviceDefinition', related_name="medication", null=True, on_delete=models.SET_NULL)
	
class FHIR_MedicationRequest_Reason_Condition(models.Model):
    medicationRequest = models.ForeignKey(FHIR_MedicationRequest, null=False, on_delete=models.CASCADE)
    BINDING_RULE_CONDITION = ""
    reason_condition_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={'codings__binding_rule': BINDING_RULE_CONDITION}, blank=True)
    reason_condition_cctext = FHIR_primitive_StringField(max_length=255, null=True, blank=True)
    reason_condition_ref = models.ForeignKey('FHIR_Condition', related_name="reason_condition", null=True, on_delete=models.SET_NULL)

class FHIR_MedicationRequest_Reason_Observation(models.Model):
    medicationRequest = models.ForeignKey(FHIR_MedicationRequest, null=False, on_delete=models.CASCADE)
    BINDING_RULE_OBSERVATION  = ""
    reason_observation_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={'codings__binding_rule': BINDING_RULE_OBSERVATION}, blank=True)
    reason_observation_cctext = FHIR_primitive_StringField(max_length=255, null=True, blank=True)
    reason_observation_ref = models.ForeignKey('FHIR_Observation', related_name="reason_observation", null=True, on_delete=models.SET_NULL)
	
class FHIR_MedicationRequest_Reason_DiagnosticReport(models.Model):
    medicationRequest = models.ForeignKey(FHIR_MedicationRequest, null=False, on_delete=models.CASCADE)
    BINDING_RULE_DIAGNOSTIC_REPORT = ""
    reason_diagnosticReport_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={'codings__binding_rule': BINDING_RULE_DIAGNOSTIC_REPORT}, blank=True)
    reason_diagnosticReport_cctext = FHIR_primitive_StringField(max_length=255, null=True, blank=True)
    reason_diagnosticReport_ref = models.ForeignKey('FHIR_DiagnosticReport', related_name="reason_diagnosticReport", null=True, on_delete=models.SET_NULL)

class FHIR_MedicationRequest_Reason_Procedure(models.Model):
    medicationRequest = models.ForeignKey(FHIR_MedicationRequest, null=False, on_delete=models.CASCADE)
    BINDING_RULE_PROCEDURE = ""
    reason_procedure_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={'codings__binding_rule': BINDING_RULE_PROCEDURE}, blank=True)
    reason_procedure_cctext = FHIR_primitive_StringField(max_length=255, null=True, blank=True)
    reason_procedure_ref = models.ForeignKey('FHIR_Procedure', related_name="reason_procedure", null=True, on_delete=models.SET_NULL)




class FHIR_MedicationRequest_Note(FHIR_GP_Annotation):
    medicationRequest = models.ForeignKey(FHIR_MedicationRequest, on_delete=models.CASCADE, related_name='mr_notes')

class FHIR_MedicationRequest_DosageInstruction(FHIR_SP_Dosage):
    medicationRequest = models.ForeignKey(FHIR_MedicationRequest, on_delete=models.CASCADE, related_name='mr_dosageInstruction')     
