#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Procedure(models.Model):
    basedOn_CarePlan = models.ManyToManyField("FHIR_CarePlan", related_name="Procedure_basedOn", blank=True)
    basedOn_ServiceRequest = models.ManyToManyField("FHIR_ServiceRequest", related_name="Procedure_basedOn", blank=True)
    basedOn_MedicationRequest = models.ManyToManyField("FHIR_MedicationRequest", related_name="Procedure_basedOn", blank=True)
    partOf_Procedure = models.ManyToManyField("FHIR_Procedure", related_name="Procedure_partOf", blank=True)
    partOf_Observation = models.ManyToManyField("FHIR_Observation", related_name="Procedure_partOf", blank=True)
    partOf_MedicationAdministration = models.ManyToManyField("FHIR_MedicationAdministration", related_name="Procedure_partOf", blank=True)
    class StatusChoices(models.TextChoices): PREPARATION = 'preparation', 'Preparation'; IN_PROGRESS = 'in-progress', 'In-progress'; NOT_DONE = 'not-done', 'Not-done'; ON_HOLD = 'on-hold', 'On-hold'; STOPPED = 'stopped', 'Stopped'; COMPLETED = 'completed', 'Completed'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    BINDING_statusReason = 'TODO'
    statusReason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_statusReason}, related_name='Procedure_statusReason', blank=True)
    statusReason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_code = 'TODO'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='Procedure_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    subject_Patient = models.ForeignKey("FHIR_Patient", related_name="Procedure_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Group = models.ForeignKey("FHIR_Group", related_name="Procedure_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Device = models.ForeignKey("FHIR_Device", related_name="Procedure_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="Procedure_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Organization = models.ForeignKey("FHIR_Organization", related_name="Procedure_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Location = models.ForeignKey("FHIR_Location", related_name="Procedure_subject", null=True, blank=True, on_delete=models.SET_NULL)
    focus_Patient = models.ForeignKey("FHIR_Patient", related_name="Procedure_focus", null=True, blank=True, on_delete=models.SET_NULL)
    focus_Group = models.ForeignKey("FHIR_Group", related_name="Procedure_focus", null=True, blank=True, on_delete=models.SET_NULL)
    focus_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="Procedure_focus", null=True, blank=True, on_delete=models.SET_NULL)
    focus_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="Procedure_focus", null=True, blank=True, on_delete=models.SET_NULL)
    focus_Organization = models.ForeignKey("FHIR_Organization", related_name="Procedure_focus", null=True, blank=True, on_delete=models.SET_NULL)
    focus_CareTeam = models.ForeignKey("FHIR_CareTeam", related_name="Procedure_focus", null=True, blank=True, on_delete=models.SET_NULL)
    focus_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="Procedure_focus", null=True, blank=True, on_delete=models.SET_NULL)
    focus_Specimen = models.ForeignKey("FHIR_Specimen", related_name="Procedure_focus", null=True, blank=True, on_delete=models.SET_NULL)
    encounter = models.ForeignKey("FHIR_Encounter", related_name="Procedure_encounter", null=True, blank=True, on_delete=models.SET_NULL)
    occurrence = FHIR_primitive_DateTimeField(null=True, blank=True, )
    occurrence = models.OneToOneField("FHIR_GP_Period", related_name='Procedure_occurrence', null=True, blank=True, on_delete=models.SET_NULL)
    occurrence = FHIR_primitive_StringField(null=True, blank=True, )
    occurrence = models.OneToOneField("FHIR_GP_Quantity_Age", related_name='Procedure_occurrence', null=True, blank=True, on_delete=models.SET_NULL)
    occurrence = models.OneToOneField("FHIR_GP_Range", related_name='Procedure_occurrence', null=True, blank=True, on_delete=models.SET_NULL)
    occurrence = models.OneToOneField("FHIR_GP_Timing", related_name='Procedure_occurrence', null=True, blank=True, on_delete=models.SET_NULL)
    recorded = FHIR_primitive_DateTimeField(null=True, blank=True, )
    recorder_Patient = models.ForeignKey("FHIR_Patient", related_name="Procedure_recorder", null=True, blank=True, on_delete=models.SET_NULL)
    recorder_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="Procedure_recorder", null=True, blank=True, on_delete=models.SET_NULL)
    recorder_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="Procedure_recorder", null=True, blank=True, on_delete=models.SET_NULL)
    recorder_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="Procedure_recorder", null=True, blank=True, on_delete=models.SET_NULL)
    reported = FHIR_primitive_BooleanField(null=True, blank=True, )
    reported_Patient = models.ForeignKey("FHIR_Patient", related_name="Procedure_reported", null=True, blank=True, on_delete=models.SET_NULL)
    reported_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="Procedure_reported", null=True, blank=True, on_delete=models.SET_NULL)
    reported_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="Procedure_reported", null=True, blank=True, on_delete=models.SET_NULL)
    reported_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="Procedure_reported", null=True, blank=True, on_delete=models.SET_NULL)
    reported_Organization = models.ForeignKey("FHIR_Organization", related_name="Procedure_reported", null=True, blank=True, on_delete=models.SET_NULL)
    location = models.ForeignKey("FHIR_Location", related_name="Procedure_location", null=True, blank=True, on_delete=models.SET_NULL)
    bodyStructure = models.ManyToManyField("FHIR_BodyStructure", related_name="Procedure_bodyStructure", blank=True)
    report_DiagnosticReport = models.ManyToManyField("FHIR_DiagnosticReport", related_name="Procedure_report", blank=True)
    report_DocumentReference = models.ManyToManyField("FHIR_DocumentReference", related_name="Procedure_report", blank=True)
    report_Composition = models.ManyToManyField("FHIR_Composition", related_name="Procedure_report", blank=True)

class FHIR_Procedure_identifier(FHIR_GP_Identifier):
    Procedure = models.ForeignKey(FHIR_Procedure, related_name='Procedure_identifier', null=False, on_delete=models.CASCADE)

class FHIR_Procedure_category(models.Model):
    Procedure = models.ForeignKey(FHIR_Procedure, related_name='Procedure_category', null=False, on_delete=models.CASCADE)
    BINDING_category = 'TODO'
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='Procedure_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Procedure_performer(models.Model):
    Procedure = models.ForeignKey(FHIR_Procedure, related_name='Procedure_performer', null=False, on_delete=models.CASCADE)
    BINDING_function = 'TODO'
    function_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_function}, related_name='Procedure_performer_function', blank=True)
    function_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    actor_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="Procedure_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="Procedure_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Organization = models.ForeignKey("FHIR_Organization", related_name="Procedure_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Patient = models.ForeignKey("FHIR_Patient", related_name="Procedure_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="Procedure_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Device = models.ForeignKey("FHIR_Device", related_name="Procedure_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_CareTeam = models.ForeignKey("FHIR_CareTeam", related_name="Procedure_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_HealthcareService = models.ForeignKey("FHIR_HealthcareService", related_name="Procedure_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    onBehalfOf = models.ForeignKey("FHIR_Organization", related_name="Procedure_performer_onBehalfOf", null=True, blank=True, on_delete=models.SET_NULL)
    period = models.OneToOneField("FHIR_GP_Period", related_name='Procedure_performer_period', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Procedure_reason(models.Model):
    Procedure = models.ForeignKey(FHIR_Procedure, related_name='Procedure_reason', null=False, on_delete=models.CASCADE)
    BINDING_reason = 'TODO'
    reason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_reason}, related_name='Procedure_reason', blank=True)
    reason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    reason_Condition_ref = models.ForeignKey("FHIR_Condition", related_name="Procedure_reason_Condition", null=True, blank=True, on_delete=models.SET_NULL)
    reason_Observation_ref = models.ForeignKey("FHIR_Observation", related_name="Procedure_reason_Observation", null=True, blank=True, on_delete=models.SET_NULL)
    reason_Procedure_ref = models.ForeignKey("FHIR_Procedure", related_name="Procedure_reason_Procedure", null=True, blank=True, on_delete=models.SET_NULL)
    reason_DiagnosticReport_ref = models.ForeignKey("FHIR_DiagnosticReport", related_name="Procedure_reason_DiagnosticReport", null=True, blank=True, on_delete=models.SET_NULL)
    reason_DocumentReference_ref = models.ForeignKey("FHIR_DocumentReference", related_name="Procedure_reason_DocumentReference", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Procedure_bodySite(models.Model):
    Procedure = models.ForeignKey(FHIR_Procedure, related_name='Procedure_bodySite', null=False, on_delete=models.CASCADE)
    BINDING_bodySite = 'TODO'
    bodySite_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_bodySite}, related_name='Procedure_bodySite', blank=True)
    bodySite_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Procedure_outcome(models.Model):
    Procedure = models.ForeignKey(FHIR_Procedure, related_name='Procedure_outcome', null=False, on_delete=models.CASCADE)
    BINDING_outcome = 'TODO'
    outcome_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_outcome}, related_name='Procedure_outcome', blank=True)
    outcome_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    outcome_Observation_ref = models.ForeignKey("FHIR_Observation", related_name="Procedure_outcome_Observation", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Procedure_complication(models.Model):
    Procedure = models.ForeignKey(FHIR_Procedure, related_name='Procedure_complication', null=False, on_delete=models.CASCADE)
    BINDING_complication = 'TODO'
    complication_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_complication}, related_name='Procedure_complication', blank=True)
    complication_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    complication_Condition_ref = models.ForeignKey("FHIR_Condition", related_name="Procedure_complication_Condition", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Procedure_followUp(models.Model):
    Procedure = models.ForeignKey(FHIR_Procedure, related_name='Procedure_followUp', null=False, on_delete=models.CASCADE)
    BINDING_followUp = 'TODO'
    followUp_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_followUp}, related_name='Procedure_followUp', blank=True)
    followUp_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    followUp_ServiceRequest_ref = models.ForeignKey("FHIR_ServiceRequest", related_name="Procedure_followUp_ServiceRequest", null=True, blank=True, on_delete=models.SET_NULL)
    followUp_PlanDefinition_ref = models.ForeignKey("FHIR_PlanDefinition", related_name="Procedure_followUp_PlanDefinition", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Procedure_note(FHIR_GP_Annotation):
    Procedure = models.ForeignKey(FHIR_Procedure, related_name='Procedure_note', null=False, on_delete=models.CASCADE)

class FHIR_Procedure_focalDevice(models.Model):
    Procedure = models.ForeignKey(FHIR_Procedure, related_name='Procedure_focalDevice', null=False, on_delete=models.CASCADE)
    BINDING_action = 'TODO'
    action_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_action}, related_name='Procedure_focalDevice_action', blank=True)
    action_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    manipulated = models.ForeignKey("FHIR_Device", related_name="Procedure_focalDevice_manipulated", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Procedure_used(models.Model):
    Procedure = models.ForeignKey(FHIR_Procedure, related_name='Procedure_used', null=False, on_delete=models.CASCADE)
    BINDING_used = 'TODO'
    used_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_used}, related_name='Procedure_used', blank=True)
    used_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    used_Device_ref = models.ForeignKey("FHIR_Device", related_name="Procedure_used_Device", null=True, blank=True, on_delete=models.SET_NULL)
    used_Medication_ref = models.ForeignKey("FHIR_Medication", related_name="Procedure_used_Medication", null=True, blank=True, on_delete=models.SET_NULL)
    used_Substance_ref = models.ForeignKey("FHIR_Substance", related_name="Procedure_used_Substance", null=True, blank=True, on_delete=models.SET_NULL)
    used_BiologicallyDerivedProduct_ref = models.ForeignKey("FHIR_BiologicallyDerivedProduct", related_name="Procedure_used_BiologicallyDerivedProduct", null=True, blank=True, on_delete=models.SET_NULL)
