#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Condition(models.Model):
    BINDING_clinicalStatus = "https://build.fhir.org/valueset-condition-clinical.html"
    clinicalStatus_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_clinicalStatus}, related_name='Condition_clinicalStatus', blank=True)
    clinicalStatus_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_verificationStatus = "http://hl7.org/fhir/ValueSet/condition-ver-status.html"
    verificationStatus_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_verificationStatus}, related_name='Condition_verificationStatus', blank=True)
    verificationStatus_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_severity = "https://build.fhir.org/valueset-condition-severity.html"
    severity_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_severity}, related_name='Condition_severity', blank=True)
    severity_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_code = "https://build.fhir.org/valueset-condition-code.html"
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='Condition_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    bodyStructure = models.ForeignKey("FHIR_BodyStructure", related_name="Condition_bodyStructure", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Patient = models.ForeignKey("FHIR_Patient", related_name="Condition_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Group = models.ForeignKey("FHIR_Group", related_name="Condition_subject", null=True, blank=True, on_delete=models.SET_NULL)
    encounter = models.ForeignKey("FHIR_Encounter", related_name="Condition_encounter", null=True, blank=True, on_delete=models.SET_NULL)
    onset_dateTime = FHIR_primitive_DateTimeField(null=True, blank=True, )
    onset_Age = models.OneToOneField("FHIR_GP_Quantity_Age", related_name='Condition_onset_Age', null=True, blank=True, on_delete=models.SET_NULL)
    onset_Period = models.OneToOneField("FHIR_GP_Period", related_name='Condition_onset_Period', null=True, blank=True, on_delete=models.SET_NULL)
    onset_Range = models.OneToOneField("FHIR_GP_Range", related_name='Condition_onset_Range', null=True, blank=True, on_delete=models.SET_NULL)
    onset_string = FHIR_primitive_StringField(null=True, blank=True, )
    abatement_dateTime = FHIR_primitive_DateTimeField(null=True, blank=True, )
    abatement_Age = models.OneToOneField("FHIR_GP_Quantity_Age", related_name='Condition_abatement_Age', null=True, blank=True, on_delete=models.SET_NULL)
    abatement_Period = models.OneToOneField("FHIR_GP_Period", related_name='Condition_abatement_Period', null=True, blank=True, on_delete=models.SET_NULL)
    abatement_Range = models.OneToOneField("FHIR_GP_Range", related_name='Condition_abatement_Range', null=True, blank=True, on_delete=models.SET_NULL)
    abatement_string = FHIR_primitive_StringField(null=True, blank=True, )
    recordedDate = FHIR_primitive_DateTimeField(null=True, blank=True, )
    recorder_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="Condition_recorder", null=True, blank=True, on_delete=models.SET_NULL)
    recorder_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="Condition_recorder", null=True, blank=True, on_delete=models.SET_NULL)
    recorder_Patient = models.ForeignKey("FHIR_Patient", related_name="Condition_recorder", null=True, blank=True, on_delete=models.SET_NULL)
    recorder_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="Condition_recorder", null=True, blank=True, on_delete=models.SET_NULL)
    asserter_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="Condition_asserter", null=True, blank=True, on_delete=models.SET_NULL)
    asserter_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="Condition_asserter", null=True, blank=True, on_delete=models.SET_NULL)
    asserter_Patient = models.ForeignKey("FHIR_Patient", related_name="Condition_asserter", null=True, blank=True, on_delete=models.SET_NULL)
    asserter_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="Condition_asserter", null=True, blank=True, on_delete=models.SET_NULL)
    asserter_Device = models.ForeignKey("FHIR_Device", related_name="Condition_asserter", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Condition_identifier(FHIR_GP_Identifier):
    Condition = models.ForeignKey(FHIR_Condition, related_name='Condition_identifier', null=False, on_delete=models.CASCADE)

class FHIR_Condition_category(models.Model):
    Condition = models.ForeignKey(FHIR_Condition, related_name='Condition_category', null=False, on_delete=models.CASCADE)
    BINDING_category = "TODO"
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='Condition_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Condition_bodySite(models.Model):
    Condition = models.ForeignKey(FHIR_Condition, related_name='Condition_bodySite', null=False, on_delete=models.CASCADE)
    BINDING_bodySite = "TODO"
    bodySite_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_bodySite}, related_name='Condition_bodySite', blank=True)
    bodySite_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Condition_stage(models.Model):
    Condition = models.ForeignKey(FHIR_Condition, related_name='Condition_stage', null=False, on_delete=models.CASCADE)
    BINDING_summary = "TODO"
    summary_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_summary}, related_name='Condition_stage_summary', blank=True)
    summary_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    assessment_ClinicalAssessment = models.ManyToManyField("FHIR_ClinicalAssessment", related_name="Condition_stage_assessment", blank=True)
    assessment_DiagnosticReport = models.ManyToManyField("FHIR_DiagnosticReport", related_name="Condition_stage_assessment", blank=True)
    assessment_Observation = models.ManyToManyField("FHIR_Observation", related_name="Condition_stage_assessment", blank=True)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Condition_stage_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_Condition_evidence(models.Model):
    Condition = models.ForeignKey(FHIR_Condition, related_name='Condition_evidence', null=False, on_delete=models.CASCADE)
    BINDING_evidence = "TODO"
    evidence_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_evidence}, related_name='Condition_evidence', blank=True)
    evidence_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_Condition_note(FHIR_GP_Annotation):
    Condition = models.ForeignKey(FHIR_Condition, related_name='Condition_note', null=False, on_delete=models.CASCADE)
