
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_ClinicalAssessment(models.Model):
    class StatusChoices(models.TextChoices): PREPARATION = 'preparation', 'Preparation'; IN_PROGRESS = 'in-progress', 'In-progress'; NOT_DONE = 'not-done', 'Not-done'; ON_HOLD = 'on-hold', 'On-hold'; STOPPED = 'stopped', 'Stopped'; COMPLETED = 'completed', 'Completed'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    BINDING_statusReason = 'TODO'
    statusReason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_statusReason}, related_name='ClinicalAssessment_statusReason', blank=True)
    statusReason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    description = FHIR_primitive_StringField(null=True, blank=True, )
    subject_Patient = models.ForeignKey("FHIR_Patient", related_name="ClinicalAssessment_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Group = models.ForeignKey("FHIR_Group", related_name="ClinicalAssessment_subject", null=True, blank=True, on_delete=models.SET_NULL)
    encounter = models.ForeignKey("FHIR_Encounter", related_name="ClinicalAssessment_encounter", null=True, blank=True, on_delete=models.SET_NULL)
    effective = FHIR_primitive_DateTimeField(null=True, blank=True, )
    effective = models.OneToOneField("FHIR_GP_Period", related_name='ClinicalAssessment_effective', null=True, blank=True, on_delete=models.SET_NULL)
    date = FHIR_primitive_DateTimeField(null=True, blank=True, )
    performer_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="ClinicalAssessment_performer", null=True, blank=True, on_delete=models.SET_NULL)
    performer_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="ClinicalAssessment_performer", null=True, blank=True, on_delete=models.SET_NULL)
    previous = models.ForeignKey("FHIR_ClinicalAssessment", related_name="ClinicalAssessment_previous", null=True, blank=True, on_delete=models.SET_NULL)
    problem_Condition = models.ManyToManyField("FHIR_Condition", related_name="ClinicalAssessment_problem", blank=True)
    problem_AllergyIntolerance = models.ManyToManyField("FHIR_AllergyIntolerance", related_name="ClinicalAssessment_problem", blank=True)
    BINDING_changePattern = 'TODO'
    changePattern_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_changePattern}, related_name='ClinicalAssessment_changePattern', blank=True)
    changePattern_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    summary = FHIR_primitive_MarkdownField(null=True, blank=True, )
    prognosisReference = models.ManyToManyField("FHIR_RiskAssessment", related_name="ClinicalAssessment_prognosisReference", blank=True)

class FHIR_ClinicalAssessment_identifier(FHIR_GP_Identifier):
    ClinicalAssessment = models.ForeignKey(FHIR_ClinicalAssessment, related_name='ClinicalAssessment_identifier', null=False, on_delete=models.CASCADE)

class FHIR_ClinicalAssessment_protocol(models.Model):
    ClinicalAssessment = models.ForeignKey(FHIR_ClinicalAssessment, related_name='ClinicalAssessment_protocol', null=False, on_delete=models.CASCADE)
    
    protocol = FHIR_primitive_URIField(null=True, blank=True, )
    
class FHIR_ClinicalAssessment_finding(models.Model):
    ClinicalAssessment = models.ForeignKey(FHIR_ClinicalAssessment, related_name='ClinicalAssessment_finding', null=False, on_delete=models.CASCADE)
    BINDING_item = 'TODO'
    item_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_item}, related_name='ClinicalAssessment_finding_item', blank=True)
    item_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    item_Condition_ref = models.ForeignKey("FHIR_Condition", related_name="ClinicalAssessment_finding_item", null=True, blank=True, on_delete=models.SET_NULL)
    item_Observation_ref = models.ForeignKey("FHIR_Observation", related_name="ClinicalAssessment_finding_item", null=True, blank=True, on_delete=models.SET_NULL)
    item_DocumentReference_ref = models.ForeignKey("FHIR_DocumentReference", related_name="ClinicalAssessment_finding_item", null=True, blank=True, on_delete=models.SET_NULL)
    basis = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_ClinicalAssessment_prognosisCodeableConcept(models.Model):
    ClinicalAssessment = models.ForeignKey(FHIR_ClinicalAssessment, related_name='ClinicalAssessment_prognosisCodeableConcept', null=False, on_delete=models.CASCADE)
    BINDING_prognosisCodeableConcept = 'TODO'
    prognosisCodeableConcept_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_prognosisCodeableConcept}, related_name='ClinicalAssessment_prognosisCodeableConcept', blank=True)
    prognosisCodeableConcept_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ClinicalAssessment_note(FHIR_GP_Annotation):
    ClinicalAssessment = models.ForeignKey(FHIR_ClinicalAssessment, related_name='ClinicalAssessment_note', null=False, on_delete=models.CASCADE)
