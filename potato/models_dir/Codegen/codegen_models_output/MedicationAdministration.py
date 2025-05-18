#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_MedicationAdministration(models.Model):
    basedOn = models.ManyToManyField("FHIR_CarePlan", related_name="MedicationAdministration_basedOn", blank=True)
    partOf_MedicationAdministration = models.ManyToManyField("FHIR_MedicationAdministration", related_name="MedicationAdministration_partOf", blank=True)
    partOf_Procedure = models.ManyToManyField("FHIR_Procedure", related_name="MedicationAdministration_partOf", blank=True)
    partOf_MedicationDispense = models.ManyToManyField("FHIR_MedicationDispense", related_name="MedicationAdministration_partOf", blank=True)
    class StatusChoices(models.TextChoices): IN_PROGRESS = 'in-progress', 'In-progress'; NOT_DONE = 'not-done', 'Not-done'; ON_HOLD = 'on-hold', 'On-hold'; COMPLETED = 'completed', 'Completed'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; STOPPED = 'stopped', 'Stopped'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    BINDING_medication = "TODO"
    medication_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_medication}, related_name='MedicationAdministration_medication', blank=True)
    medication_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    medication_Medication_ref = models.ForeignKey("FHIR_Medication", related_name="MedicationAdministration_medication_Medication", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Patient = models.ForeignKey("FHIR_Patient", related_name="MedicationAdministration_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Group = models.ForeignKey("FHIR_Group", related_name="MedicationAdministration_subject", null=True, blank=True, on_delete=models.SET_NULL)
    encounter = models.ForeignKey("FHIR_Encounter", related_name="MedicationAdministration_encounter", null=True, blank=True, on_delete=models.SET_NULL)
                            #skipping Reference(Any) for field supportingInformation as MedicationAdministration supportingInformation not in referenceAny_targets
    occurrence_dateTime = FHIR_primitive_DateTimeField(null=True, blank=True, )
    occurrence_Period = models.OneToOneField("FHIR_GP_Period", related_name='MedicationAdministration_occurrence_Period', null=True, blank=True, on_delete=models.SET_NULL)
    occurrence_Timing = models.OneToOneField("FHIR_GP_Timing", related_name='MedicationAdministration_occurrence_Timing', null=True, blank=True, on_delete=models.SET_NULL)
    recorded = FHIR_primitive_DateTimeField(null=True, blank=True, )
    isSubPotent = FHIR_primitive_BooleanField(null=True, blank=True, )
    request = models.ForeignKey("FHIR_MedicationRequest", related_name="MedicationAdministration_request", null=True, blank=True, on_delete=models.SET_NULL)
    eventHistory = models.ManyToManyField("FHIR_Provenance", related_name="MedicationAdministration_eventHistory", blank=True)

class FHIR_MedicationAdministration_identifier(FHIR_GP_Identifier):
    MedicationAdministration = models.ForeignKey(FHIR_MedicationAdministration, related_name='MedicationAdministration_identifier', null=False, on_delete=models.CASCADE)

class FHIR_MedicationAdministration_statusReason(models.Model):
    MedicationAdministration = models.ForeignKey(FHIR_MedicationAdministration, related_name='MedicationAdministration_statusReason', null=False, on_delete=models.CASCADE)
    BINDING_statusReason = "TODO"
    statusReason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_statusReason}, related_name='MedicationAdministration_statusReason', blank=True)
    statusReason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_MedicationAdministration_category(models.Model):
    MedicationAdministration = models.ForeignKey(FHIR_MedicationAdministration, related_name='MedicationAdministration_category', null=False, on_delete=models.CASCADE)
    BINDING_category = "TODO"
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='MedicationAdministration_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_MedicationAdministration_subPotentReason(models.Model):
    MedicationAdministration = models.ForeignKey(FHIR_MedicationAdministration, related_name='MedicationAdministration_subPotentReason', null=False, on_delete=models.CASCADE)
    BINDING_subPotentReason = "TODO"
    subPotentReason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_subPotentReason}, related_name='MedicationAdministration_subPotentReason', blank=True)
    subPotentReason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_MedicationAdministration_performer(models.Model):
    MedicationAdministration = models.ForeignKey(FHIR_MedicationAdministration, related_name='MedicationAdministration_performer', null=False, on_delete=models.CASCADE)
    BINDING_function = "TODO"
    function_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_function}, related_name='MedicationAdministration_performer_function', blank=True)
    function_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_actor = "TODO"
    actor_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_actor}, related_name='MedicationAdministration_performer_actor', blank=True)
    actor_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    actor_Practitioner_ref = models.ForeignKey("FHIR_Practitioner", related_name="MedicationAdministration_performer_actor_Practitioner", null=True, blank=True, on_delete=models.SET_NULL)
    actor_PractitionerRole_ref = models.ForeignKey("FHIR_PractitionerRole", related_name="MedicationAdministration_performer_actor_PractitionerRole", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Patient_ref = models.ForeignKey("FHIR_Patient", related_name="MedicationAdministration_performer_actor_Patient", null=True, blank=True, on_delete=models.SET_NULL)
    actor_RelatedPerson_ref = models.ForeignKey("FHIR_RelatedPerson", related_name="MedicationAdministration_performer_actor_RelatedPerson", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Device_ref = models.ForeignKey("FHIR_Device", related_name="MedicationAdministration_performer_actor_Device", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Group_ref = models.ForeignKey("FHIR_Group", related_name="MedicationAdministration_performer_actor_Group", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_MedicationAdministration_reason(models.Model):
    MedicationAdministration = models.ForeignKey(FHIR_MedicationAdministration, related_name='MedicationAdministration_reason', null=False, on_delete=models.CASCADE)
    BINDING_reason = "TODO"
    reason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_reason}, related_name='MedicationAdministration_reason', blank=True)
    reason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    reason_Condition_ref = models.ForeignKey("FHIR_Condition", related_name="MedicationAdministration_reason_Condition", null=True, blank=True, on_delete=models.SET_NULL)
    reason_Observation_ref = models.ForeignKey("FHIR_Observation", related_name="MedicationAdministration_reason_Observation", null=True, blank=True, on_delete=models.SET_NULL)
    reason_DiagnosticReport_ref = models.ForeignKey("FHIR_DiagnosticReport", related_name="MedicationAdministration_reason_DiagnosticReport", null=True, blank=True, on_delete=models.SET_NULL)
    reason_Procedure_ref = models.ForeignKey("FHIR_Procedure", related_name="MedicationAdministration_reason_Procedure", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_MedicationAdministration_device(models.Model):
    MedicationAdministration = models.ForeignKey(FHIR_MedicationAdministration, related_name='MedicationAdministration_device', null=False, on_delete=models.CASCADE)
    BINDING_device = "TODO"
    device_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_device}, related_name='MedicationAdministration_device', blank=True)
    device_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    device_Device_ref = models.ForeignKey("FHIR_Device", related_name="MedicationAdministration_device_Device", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_MedicationAdministration_note(FHIR_GP_Annotation):
    MedicationAdministration = models.ForeignKey(FHIR_MedicationAdministration, related_name='MedicationAdministration_note', null=False, on_delete=models.CASCADE)

class FHIR_MedicationAdministration_dosage(models.Model):
    MedicationAdministration = models.ForeignKey(FHIR_MedicationAdministration, related_name='MedicationAdministration_dosage', null=False, on_delete=models.CASCADE)
    text = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_site = "TODO"
    site_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_site}, related_name='MedicationAdministration_dosage_site', blank=True)
    site_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_route = "TODO"
    route_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_route}, related_name='MedicationAdministration_dosage_route', blank=True)
    route_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_method = "TODO"
    method_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_method}, related_name='MedicationAdministration_dosage_method', blank=True)
    method_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    dose = models.OneToOneField("FHIR_GP_Quantity", related_name='MedicationAdministration_dosage_dose', null=True, blank=True, on_delete=models.SET_NULL)
    rate_Ratio = models.OneToOneField("FHIR_GP_Ratio", related_name='MedicationAdministration_dosage_rate_Ratio', null=True, blank=True, on_delete=models.SET_NULL)
    rate_Quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='MedicationAdministration_dosage_rate_Quantity', null=True, blank=True, on_delete=models.SET_NULL)
