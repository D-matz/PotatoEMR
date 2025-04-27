#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_DetectedIssue(models.Model):
    class StatusChoices(models.TextChoices): PRELIMINARY = 'preliminary', 'Preliminary'; FINAL = 'final', 'Final'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; UNKNOWN = 'unknown', 'Unknown'; MITIGATED = 'mitigated', 'Mitigated'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    BINDING_code = 'TODO'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='DetectedIssue_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_severity = 'TODO'
    severity_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_severity}, related_name='DetectedIssue_severity', blank=True)
    severity_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    subject_Patient = models.ForeignKey("FHIR_Patient", related_name="DetectedIssue_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Group = models.ForeignKey("FHIR_Group", related_name="DetectedIssue_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Device = models.ForeignKey("FHIR_Device", related_name="DetectedIssue_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Location = models.ForeignKey("FHIR_Location", related_name="DetectedIssue_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Organization = models.ForeignKey("FHIR_Organization", related_name="DetectedIssue_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Procedure = models.ForeignKey("FHIR_Procedure", related_name="DetectedIssue_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="DetectedIssue_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Medication = models.ForeignKey("FHIR_Medication", related_name="DetectedIssue_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Substance = models.ForeignKey("FHIR_Substance", related_name="DetectedIssue_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_BiologicallyDerivedProduct = models.ForeignKey("FHIR_BiologicallyDerivedProduct", related_name="DetectedIssue_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_NutritionProduct = models.ForeignKey("FHIR_NutritionProduct", related_name="DetectedIssue_subject", null=True, blank=True, on_delete=models.SET_NULL)
    encounter = models.ForeignKey("FHIR_Encounter", related_name="DetectedIssue_encounter", null=True, blank=True, on_delete=models.SET_NULL)
    identified = FHIR_primitive_DateTimeField(null=True, blank=True, )
    identified = models.OneToOneField("FHIR_GP_Period", related_name='DetectedIssue_identified', null=True, blank=True, on_delete=models.SET_NULL)
    identified = models.OneToOneField("FHIR_GP_Timing", related_name='DetectedIssue_identified', null=True, blank=True, on_delete=models.SET_NULL)
    author_Patient = models.ForeignKey("FHIR_Patient", related_name="DetectedIssue_author", null=True, blank=True, on_delete=models.SET_NULL)
    author_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="DetectedIssue_author", null=True, blank=True, on_delete=models.SET_NULL)
    author_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="DetectedIssue_author", null=True, blank=True, on_delete=models.SET_NULL)
    author_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="DetectedIssue_author", null=True, blank=True, on_delete=models.SET_NULL)
    author_Device = models.ForeignKey("FHIR_Device", related_name="DetectedIssue_author", null=True, blank=True, on_delete=models.SET_NULL)
    detail = FHIR_primitive_MarkdownField(null=True, blank=True, )
    reference = FHIR_primitive_URIField(null=True, blank=True, )
    BINDING_qualityOfEvidence = 'TODO'
    qualityOfEvidence_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_qualityOfEvidence}, related_name='DetectedIssue_qualityOfEvidence', blank=True)
    qualityOfEvidence_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_managementCode = 'TODO'
    managementCode_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_managementCode}, related_name='DetectedIssue_managementCode', blank=True)
    managementCode_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_DetectedIssue_identifier(FHIR_GP_Identifier):
    DetectedIssue = models.ForeignKey(FHIR_DetectedIssue, related_name='DetectedIssue_identifier', null=False, on_delete=models.CASCADE)

class FHIR_DetectedIssue_category(models.Model):
    DetectedIssue = models.ForeignKey(FHIR_DetectedIssue, related_name='DetectedIssue_category', null=False, on_delete=models.CASCADE)
    BINDING_category = 'TODO'
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='DetectedIssue_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_DetectedIssue_evidence(models.Model):
    DetectedIssue = models.ForeignKey(FHIR_DetectedIssue, related_name='DetectedIssue_evidence', null=False, on_delete=models.CASCADE)

class FHIR_DetectedIssue_evidence_code(models.Model):
    DetectedIssue_evidence = models.ForeignKey(FHIR_DetectedIssue_evidence, related_name='DetectedIssue_evidence_code', null=False, on_delete=models.CASCADE)
    BINDING_code = 'TODO'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='DetectedIssue_evidence_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_DetectedIssue_mitigation(models.Model):
    DetectedIssue = models.ForeignKey(FHIR_DetectedIssue, related_name='DetectedIssue_mitigation', null=False, on_delete=models.CASCADE)
    BINDING_action = 'TODO'
    action_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_action}, related_name='DetectedIssue_mitigation_action', blank=True)
    action_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    date = FHIR_primitive_DateTimeField(null=True, blank=True, )
    author_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="DetectedIssue_mitigation_author", null=True, blank=True, on_delete=models.SET_NULL)
    author_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="DetectedIssue_mitigation_author", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_DetectedIssue_mitigation_note(FHIR_GP_Annotation):
    DetectedIssue_mitigation = models.ForeignKey(FHIR_DetectedIssue_mitigation, related_name='DetectedIssue_mitigation_note', null=False, on_delete=models.CASCADE)
