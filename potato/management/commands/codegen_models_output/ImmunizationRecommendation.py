
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_ImmunizationRecommendation(models.Model):
    patient = models.ForeignKey("FHIR_Patient", related_name="ImmunizationRecommendation_patient", null=True, blank=True, on_delete=models.SET_NULL)
    date = FHIR_primitive_DateTimeField(null=True, blank=True, )
    authority = models.ForeignKey("FHIR_Organization", related_name="ImmunizationRecommendation_authority", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ImmunizationRecommendation_identifier(FHIR_GP_Identifier):
    ImmunizationRecommendation = models.ForeignKey(FHIR_ImmunizationRecommendation, related_name='ImmunizationRecommendation_identifier', null=False, on_delete=models.CASCADE)

class FHIR_ImmunizationRecommendation_recommendation(models.Model):
    ImmunizationRecommendation = models.ForeignKey(FHIR_ImmunizationRecommendation, related_name='ImmunizationRecommendation_recommendation', null=False, on_delete=models.CASCADE)
    BINDING_forecastStatus = 'TODO'
    forecastStatus_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_forecastStatus}, related_name='ImmunizationRecommendation_recommendation_forecastStatus', blank=True)
    forecastStatus_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    series = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_doseNumber = 'TODO'
    doseNumber_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_doseNumber}, related_name='ImmunizationRecommendation_recommendation_doseNumber', blank=True)
    doseNumber_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_seriesDoses = 'TODO'
    seriesDoses_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_seriesDoses}, related_name='ImmunizationRecommendation_recommendation_seriesDoses', blank=True)
    seriesDoses_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    supportingImmunization_Immunization = models.ManyToManyField("FHIR_Immunization", related_name="ImmunizationRecommendation_recommendation_supportingImmunization", blank=True)
    supportingImmunization_ImmunizationEvaluation = models.ManyToManyField("FHIR_ImmunizationEvaluation", related_name="ImmunizationRecommendation_recommendation_supportingImmunization", blank=True)

class FHIR_ImmunizationRecommendation_recommendation_vaccineCode(models.Model):
    ImmunizationRecommendation_recommendation = models.ForeignKey(FHIR_ImmunizationRecommendation_recommendation, related_name='ImmunizationRecommendation_recommendation_vaccineCode', null=False, on_delete=models.CASCADE)
    BINDING_vaccineCode = 'TODO'
    vaccineCode_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_vaccineCode}, related_name='ImmunizationRecommendation_recommendation_vaccineCode', blank=True)
    vaccineCode_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ImmunizationRecommendation_recommendation_targetDisease(models.Model):
    ImmunizationRecommendation_recommendation = models.ForeignKey(FHIR_ImmunizationRecommendation_recommendation, related_name='ImmunizationRecommendation_recommendation_targetDisease', null=False, on_delete=models.CASCADE)
    BINDING_targetDisease = 'TODO'
    targetDisease_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_targetDisease}, related_name='ImmunizationRecommendation_recommendation_targetDisease', blank=True)
    targetDisease_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ImmunizationRecommendation_recommendation_contraindicatedVaccineCode(models.Model):
    ImmunizationRecommendation_recommendation = models.ForeignKey(FHIR_ImmunizationRecommendation_recommendation, related_name='ImmunizationRecommendation_recommendation_contraindicatedVaccineCode', null=False, on_delete=models.CASCADE)
    BINDING_contraindicatedVaccineCode = 'TODO'
    contraindicatedVaccineCode_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_contraindicatedVaccineCode}, related_name='ImmunizationRecommendation_recommendation_contraindicatedVaccineCode', blank=True)
    contraindicatedVaccineCode_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ImmunizationRecommendation_recommendation_forecastReason(models.Model):
    ImmunizationRecommendation_recommendation = models.ForeignKey(FHIR_ImmunizationRecommendation_recommendation, related_name='ImmunizationRecommendation_recommendation_forecastReason', null=False, on_delete=models.CASCADE)
    BINDING_forecastReason = 'TODO'
    forecastReason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_forecastReason}, related_name='ImmunizationRecommendation_recommendation_forecastReason', blank=True)
    forecastReason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ImmunizationRecommendation_recommendation_dateCriterion(models.Model):
    ImmunizationRecommendation_recommendation = models.ForeignKey(FHIR_ImmunizationRecommendation_recommendation, related_name='ImmunizationRecommendation_recommendation_dateCriterion', null=False, on_delete=models.CASCADE)
    BINDING_code = 'TODO'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='ImmunizationRecommendation_recommendation_dateCriterion_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value = FHIR_primitive_DateTimeField(null=True, blank=True, )
