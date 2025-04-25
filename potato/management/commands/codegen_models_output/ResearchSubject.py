
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_ResearchSubject(models.Model):
    class StatusChoices(models.TextChoices): DRAFT = 'draft', 'Draft'; ACTIVE = 'active', 'Active'; RETIRED = 'retired', 'Retired'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    period = models.OneToOneField("FHIR_GP_Period", related_name='ResearchSubject_period', null=True, blank=True, on_delete=models.SET_NULL)
    study = models.ForeignKey("FHIR_ResearchStudy", related_name="ResearchSubject_study", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Patient = models.ForeignKey("FHIR_Patient", related_name="ResearchSubject_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Group = models.ForeignKey("FHIR_Group", related_name="ResearchSubject_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Specimen = models.ForeignKey("FHIR_Specimen", related_name="ResearchSubject_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Device = models.ForeignKey("FHIR_Device", related_name="ResearchSubject_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Medication = models.ForeignKey("FHIR_Medication", related_name="ResearchSubject_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Substance = models.ForeignKey("FHIR_Substance", related_name="ResearchSubject_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_SubstanceDefinition = models.ForeignKey("FHIR_SubstanceDefinition", related_name="ResearchSubject_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_BiologicallyDerivedProduct = models.ForeignKey("FHIR_BiologicallyDerivedProduct", related_name="ResearchSubject_subject", null=True, blank=True, on_delete=models.SET_NULL)
    assignedComparisonGroup = FHIR_primitive_IdField(null=True, blank=True, )
    actualComparisonGroup = FHIR_primitive_IdField(null=True, blank=True, )
    consent = models.ManyToManyField("FHIR_Consent", related_name="ResearchSubject_consent", blank=True)

class FHIR_ResearchSubject_identifier(FHIR_GP_Identifier):
    ResearchSubject = models.ForeignKey(FHIR_ResearchSubject, related_name='ResearchSubject_identifier', null=False, on_delete=models.CASCADE)

class FHIR_ResearchSubject_subjectState(models.Model):
    ResearchSubject = models.ForeignKey(FHIR_ResearchSubject, related_name='ResearchSubject_subjectState', null=False, on_delete=models.CASCADE)
    BINDING_code = 'TODO'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='ResearchSubject_subjectState_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    startDate = FHIR_primitive_DateTimeField(null=True, blank=True, )
    endDate = FHIR_primitive_DateTimeField(null=True, blank=True, )
    BINDING_reason = 'TODO'
    reason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_reason}, related_name='ResearchSubject_subjectState_reason', blank=True)
    reason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_ResearchSubject_subjectMilestone(models.Model):
    ResearchSubject = models.ForeignKey(FHIR_ResearchSubject, related_name='ResearchSubject_subjectMilestone', null=False, on_delete=models.CASCADE)
    date = FHIR_primitive_DateTimeField(null=True, blank=True, )
    BINDING_reason = 'TODO'
    reason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_reason}, related_name='ResearchSubject_subjectMilestone_reason', blank=True)
    reason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_ResearchSubject_subjectMilestone_milestone(models.Model):
    ResearchSubject_subjectMilestone = models.ForeignKey(FHIR_ResearchSubject_subjectMilestone, related_name='ResearchSubject_subjectMilestone_milestone', null=False, on_delete=models.CASCADE)
    BINDING_milestone = 'TODO'
    milestone_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_milestone}, related_name='ResearchSubject_subjectMilestone_milestone', blank=True)
    milestone_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    