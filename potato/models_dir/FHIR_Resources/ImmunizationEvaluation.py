#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_ImmunizationEvaluation(models.Model):
    class StatusChoices(models.TextChoices): COMPLETED = 'completed', 'Completed'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    patient = models.ForeignKey("FHIR_Patient", related_name="ImmunizationEvaluation_patient", null=True, blank=True, on_delete=models.SET_NULL)
    date = FHIR_primitive_DateTimeField(null=True, blank=True, )
    authority = models.ForeignKey("FHIR_Organization", related_name="ImmunizationEvaluation_authority", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_targetDisease = 'TODO'
    targetDisease_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_targetDisease}, related_name='ImmunizationEvaluation_targetDisease', blank=True)
    targetDisease_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    immunizationEvent = models.ForeignKey("FHIR_Immunization", related_name="ImmunizationEvaluation_immunizationEvent", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_doseStatus = 'TODO'
    doseStatus_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_doseStatus}, related_name='ImmunizationEvaluation_doseStatus', blank=True)
    doseStatus_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    series = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_doseNumber = 'TODO'
    doseNumber_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_doseNumber}, related_name='ImmunizationEvaluation_doseNumber', blank=True)
    doseNumber_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_seriesDoses = 'TODO'
    seriesDoses_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_seriesDoses}, related_name='ImmunizationEvaluation_seriesDoses', blank=True)
    seriesDoses_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_ImmunizationEvaluation_identifier(FHIR_GP_Identifier):
    ImmunizationEvaluation = models.ForeignKey(FHIR_ImmunizationEvaluation, related_name='ImmunizationEvaluation_identifier', null=False, on_delete=models.CASCADE)

class FHIR_ImmunizationEvaluation_doseStatusReason(models.Model):
    ImmunizationEvaluation = models.ForeignKey(FHIR_ImmunizationEvaluation, related_name='ImmunizationEvaluation_doseStatusReason', null=False, on_delete=models.CASCADE)
    BINDING_doseStatusReason = 'TODO'
    doseStatusReason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_doseStatusReason}, related_name='ImmunizationEvaluation_doseStatusReason', blank=True)
    doseStatusReason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    