#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_DiagnosticReport(models.Model):
    basedOn_CarePlan = models.ManyToManyField("FHIR_CarePlan", related_name="DiagnosticReport_basedOn", blank=True)
    basedOn_ImmunizationRecommendation = models.ManyToManyField("FHIR_ImmunizationRecommendation", related_name="DiagnosticReport_basedOn", blank=True)
    basedOn_MedicationRequest = models.ManyToManyField("FHIR_MedicationRequest", related_name="DiagnosticReport_basedOn", blank=True)
    basedOn_NutritionOrder = models.ManyToManyField("FHIR_NutritionOrder", related_name="DiagnosticReport_basedOn", blank=True)
    basedOn_ServiceRequest = models.ManyToManyField("FHIR_ServiceRequest", related_name="DiagnosticReport_basedOn", blank=True)
    class StatusChoices(models.TextChoices): REGISTERED = 'registered', 'Registered'; PARTIAL = 'partial', 'Partial'; PRELIMINARY = 'preliminary', 'Preliminary'; MODIFIED = 'modified', 'Modified'; FINAL = 'final', 'Final'; AMENDED = 'amended', 'Amended'; CORRECTED = 'corrected', 'Corrected'; APPENDED = 'appended', 'Appended'; CANCELLED = 'cancelled', 'Cancelled'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    BINDING_code = "https://build.fhir.org/valueset-report-codes.html"
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='DiagnosticReport_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    subject_Patient = models.ForeignKey("FHIR_Patient", related_name="DiagnosticReport_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Group = models.ForeignKey("FHIR_Group", related_name="DiagnosticReport_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Device = models.ForeignKey("FHIR_Device", related_name="DiagnosticReport_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Location = models.ForeignKey("FHIR_Location", related_name="DiagnosticReport_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Organization = models.ForeignKey("FHIR_Organization", related_name="DiagnosticReport_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="DiagnosticReport_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Medication = models.ForeignKey("FHIR_Medication", related_name="DiagnosticReport_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Substance = models.ForeignKey("FHIR_Substance", related_name="DiagnosticReport_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_BiologicallyDerivedProduct = models.ForeignKey("FHIR_BiologicallyDerivedProduct", related_name="DiagnosticReport_subject", null=True, blank=True, on_delete=models.SET_NULL)
    encounter = models.ForeignKey("FHIR_Encounter", related_name="DiagnosticReport_encounter", null=True, blank=True, on_delete=models.SET_NULL)
    effective_dateTime = FHIR_primitive_DateTimeField(null=True, blank=True, )
    effective_Period = models.OneToOneField("FHIR_GP_Period", related_name='DiagnosticReport_effective_Period', null=True, blank=True, on_delete=models.SET_NULL)
    issued = FHIR_primitive_InstantField(null=True, blank=True, )
    procedure = models.ManyToManyField("FHIR_Procedure", related_name="DiagnosticReport_procedure", blank=True)
    performer_Practitioner = models.ManyToManyField("FHIR_Practitioner", related_name="DiagnosticReport_performer", blank=True)
    performer_PractitionerRole = models.ManyToManyField("FHIR_PractitionerRole", related_name="DiagnosticReport_performer", blank=True)
    performer_Organization = models.ManyToManyField("FHIR_Organization", related_name="DiagnosticReport_performer", blank=True)
    performer_CareTeam = models.ManyToManyField("FHIR_CareTeam", related_name="DiagnosticReport_performer", blank=True)
    performer_HealthcareService = models.ManyToManyField("FHIR_HealthcareService", related_name="DiagnosticReport_performer", blank=True)
    performer_Device = models.ManyToManyField("FHIR_Device", related_name="DiagnosticReport_performer", blank=True)
    resultsInterpreter_Practitioner = models.ManyToManyField("FHIR_Practitioner", related_name="DiagnosticReport_resultsInterpreter", blank=True)
    resultsInterpreter_PractitionerRole = models.ManyToManyField("FHIR_PractitionerRole", related_name="DiagnosticReport_resultsInterpreter", blank=True)
    resultsInterpreter_Organization = models.ManyToManyField("FHIR_Organization", related_name="DiagnosticReport_resultsInterpreter", blank=True)
    resultsInterpreter_CareTeam = models.ManyToManyField("FHIR_CareTeam", related_name="DiagnosticReport_resultsInterpreter", blank=True)
    specimen = models.ManyToManyField("FHIR_Specimen", related_name="DiagnosticReport_specimen", blank=True)
    result = models.ManyToManyField("FHIR_Observation", related_name="DiagnosticReport_result", blank=True)
    study_GenomicStudy = models.ManyToManyField("FHIR_GenomicStudy", related_name="DiagnosticReport_study", blank=True)
    study_ImagingStudy = models.ManyToManyField("FHIR_ImagingStudy", related_name="DiagnosticReport_study", blank=True)
    composition = models.ForeignKey("FHIR_Composition", related_name="DiagnosticReport_composition", null=True, blank=True, on_delete=models.SET_NULL)
    conclusion = FHIR_primitive_MarkdownField(null=True, blank=True, )
    communication = models.ManyToManyField("FHIR_Communication", related_name="DiagnosticReport_communication", blank=True)

class FHIR_DiagnosticReport_identifier(FHIR_GP_Identifier):
    DiagnosticReport = models.ForeignKey(FHIR_DiagnosticReport, related_name='DiagnosticReport_identifier', null=False, on_delete=models.CASCADE)

class FHIR_DiagnosticReport_category(models.Model):
    DiagnosticReport = models.ForeignKey(FHIR_DiagnosticReport, related_name='DiagnosticReport_category', null=False, on_delete=models.CASCADE)
    BINDING_category = "TODO"
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='DiagnosticReport_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_DiagnosticReport_note(FHIR_GP_Annotation):
    DiagnosticReport = models.ForeignKey(FHIR_DiagnosticReport, related_name='DiagnosticReport_note', null=False, on_delete=models.CASCADE)

class FHIR_DiagnosticReport_supportingInfo(models.Model):
    DiagnosticReport = models.ForeignKey(FHIR_DiagnosticReport, related_name='DiagnosticReport_supportingInfo', null=False, on_delete=models.CASCADE)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='DiagnosticReport_supportingInfo_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    reference_ImagingStudy = models.ForeignKey("FHIR_ImagingStudy", related_name="DiagnosticReport_supportingInfo_reference", null=True, blank=True, on_delete=models.SET_NULL)
    reference_Procedure = models.ForeignKey("FHIR_Procedure", related_name="DiagnosticReport_supportingInfo_reference", null=True, blank=True, on_delete=models.SET_NULL)
    reference_Observation = models.ForeignKey("FHIR_Observation", related_name="DiagnosticReport_supportingInfo_reference", null=True, blank=True, on_delete=models.SET_NULL)
    reference_DiagnosticReport = models.ForeignKey("FHIR_DiagnosticReport", related_name="DiagnosticReport_supportingInfo_reference", null=True, blank=True, on_delete=models.SET_NULL)
    reference_Citation = models.ForeignKey("FHIR_Citation", related_name="DiagnosticReport_supportingInfo_reference", null=True, blank=True, on_delete=models.SET_NULL)
    reference_FamilyMemberHistory = models.ForeignKey("FHIR_FamilyMemberHistory", related_name="DiagnosticReport_supportingInfo_reference", null=True, blank=True, on_delete=models.SET_NULL)
    reference_AllergyIntolerance = models.ForeignKey("FHIR_AllergyIntolerance", related_name="DiagnosticReport_supportingInfo_reference", null=True, blank=True, on_delete=models.SET_NULL)
    reference_DeviceUsage = models.ForeignKey("FHIR_DeviceUsage", related_name="DiagnosticReport_supportingInfo_reference", null=True, blank=True, on_delete=models.SET_NULL)
    reference_Condition = models.ForeignKey("FHIR_Condition", related_name="DiagnosticReport_supportingInfo_reference", null=True, blank=True, on_delete=models.SET_NULL)
    reference_GenomicStudy = models.ForeignKey("FHIR_GenomicStudy", related_name="DiagnosticReport_supportingInfo_reference", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_DiagnosticReport_media(models.Model):
    DiagnosticReport = models.ForeignKey(FHIR_DiagnosticReport, related_name='DiagnosticReport_media', null=False, on_delete=models.CASCADE)
    comment = FHIR_primitive_StringField(null=True, blank=True, )
    link = models.ForeignKey("FHIR_DocumentReference", related_name="DiagnosticReport_media_link", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_DiagnosticReport_conclusionCode(models.Model):
    DiagnosticReport = models.ForeignKey(FHIR_DiagnosticReport, related_name='DiagnosticReport_conclusionCode', null=False, on_delete=models.CASCADE)
    BINDING_conclusionCode = "https://www.hl7.org/fhir/valueset-clinical-findings.html"
    conclusionCode_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_conclusionCode}, related_name='DiagnosticReport_conclusionCode', blank=True)
    conclusionCode_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    conclusionCode_Observation_ref = models.ForeignKey("FHIR_Observation", related_name="DiagnosticReport_conclusionCode_Observation", null=True, blank=True, on_delete=models.SET_NULL)
    conclusionCode_Condition_ref = models.ForeignKey("FHIR_Condition", related_name="DiagnosticReport_conclusionCode_Condition", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_DiagnosticReport_recomendation(models.Model):
    DiagnosticReport = models.ForeignKey(FHIR_DiagnosticReport, related_name='DiagnosticReport_recomendation', null=False, on_delete=models.CASCADE)
    BINDING_recomendation = "TODO"
    recomendation_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_recomendation}, related_name='DiagnosticReport_recomendation', blank=True)
    recomendation_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_DiagnosticReport_presentedForm(FHIR_GP_Attachment):
    DiagnosticReport = models.ForeignKey(FHIR_DiagnosticReport, related_name='DiagnosticReport_presentedForm', null=False, on_delete=models.CASCADE)
