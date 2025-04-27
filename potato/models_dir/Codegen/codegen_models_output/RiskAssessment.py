#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_RiskAssessment(models.Model):
    class StatusChoices(models.TextChoices): REGISTERED = 'registered', 'Registered'; SPECIMEN_IN_PROCESS = 'specimen-in-process', 'Specimen-in-process'; PRELIMINARY = 'preliminary', 'Preliminary'; FINAL = 'final', 'Final'; AMENDED = 'amended', 'Amended'; CORRECTED = 'corrected', 'Corrected'; APPENDED = 'appended', 'Appended'; CANCELLED = 'cancelled', 'Cancelled'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; UNKNOWN = 'unknown', 'Unknown'; CANNOT_BE_OBTAINED = 'cannot-be-obtained', 'Cannot-be-obtained'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    BINDING_method = "TODO"
    method_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_method}, related_name='RiskAssessment_method', blank=True)
    method_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_code = "TODO"
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='RiskAssessment_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    subject_Patient = models.ForeignKey("FHIR_Patient", related_name="RiskAssessment_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Group = models.ForeignKey("FHIR_Group", related_name="RiskAssessment_subject", null=True, blank=True, on_delete=models.SET_NULL)
    encounter = models.ForeignKey("FHIR_Encounter", related_name="RiskAssessment_encounter", null=True, blank=True, on_delete=models.SET_NULL)
    occurrence = FHIR_primitive_DateTimeField(null=True, blank=True, )
    occurrence = models.OneToOneField("FHIR_GP_Period", related_name='RiskAssessment_occurrence', null=True, blank=True, on_delete=models.SET_NULL)
    condition = models.ForeignKey("FHIR_Condition", related_name="RiskAssessment_condition", null=True, blank=True, on_delete=models.SET_NULL)
    performer_Patient = models.ForeignKey("FHIR_Patient", related_name="RiskAssessment_performer", null=True, blank=True, on_delete=models.SET_NULL)
    performer_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="RiskAssessment_performer", null=True, blank=True, on_delete=models.SET_NULL)
    performer_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="RiskAssessment_performer", null=True, blank=True, on_delete=models.SET_NULL)
    performer_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="RiskAssessment_performer", null=True, blank=True, on_delete=models.SET_NULL)
    performer_Device = models.ForeignKey("FHIR_Device", related_name="RiskAssessment_performer", null=True, blank=True, on_delete=models.SET_NULL)
    mitigation = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_RiskAssessment_identifier(FHIR_GP_Identifier):
    RiskAssessment = models.ForeignKey(FHIR_RiskAssessment, related_name='RiskAssessment_identifier', null=False, on_delete=models.CASCADE)

class FHIR_RiskAssessment_reason(models.Model):
    RiskAssessment = models.ForeignKey(FHIR_RiskAssessment, related_name='RiskAssessment_reason', null=False, on_delete=models.CASCADE)
    BINDING_reason = "TODO"
    reason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_reason}, related_name='RiskAssessment_reason', blank=True)
    reason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    reason_Condition_ref = models.ForeignKey("FHIR_Condition", related_name="RiskAssessment_reason_Condition", null=True, blank=True, on_delete=models.SET_NULL)
    reason_Observation_ref = models.ForeignKey("FHIR_Observation", related_name="RiskAssessment_reason_Observation", null=True, blank=True, on_delete=models.SET_NULL)
    reason_DiagnosticReport_ref = models.ForeignKey("FHIR_DiagnosticReport", related_name="RiskAssessment_reason_DiagnosticReport", null=True, blank=True, on_delete=models.SET_NULL)
    reason_DocumentReference_ref = models.ForeignKey("FHIR_DocumentReference", related_name="RiskAssessment_reason_DocumentReference", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_RiskAssessment_prediction(models.Model):
    RiskAssessment = models.ForeignKey(FHIR_RiskAssessment, related_name='RiskAssessment_prediction', null=False, on_delete=models.CASCADE)
    BINDING_outcome = "TODO"
    outcome_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_outcome}, related_name='RiskAssessment_prediction_outcome', blank=True)
    outcome_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    probability = FHIR_primitive_DecimalField(null=True, blank=True, )
    probability = models.OneToOneField("FHIR_GP_Range", related_name='RiskAssessment_prediction_probability', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_qualitativeRisk = "TODO"
    qualitativeRisk_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_qualitativeRisk}, related_name='RiskAssessment_prediction_qualitativeRisk', blank=True)
    qualitativeRisk_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    relativeRisk = FHIR_primitive_DecimalField(null=True, blank=True, )
    when = models.OneToOneField("FHIR_GP_Period", related_name='RiskAssessment_prediction_when', null=True, blank=True, on_delete=models.SET_NULL)
    when = models.OneToOneField("FHIR_GP_Range", related_name='RiskAssessment_prediction_when', null=True, blank=True, on_delete=models.SET_NULL)
    rationale = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_RiskAssessment_note(FHIR_GP_Annotation):
    RiskAssessment = models.ForeignKey(FHIR_RiskAssessment, related_name='RiskAssessment_note', null=False, on_delete=models.CASCADE)
