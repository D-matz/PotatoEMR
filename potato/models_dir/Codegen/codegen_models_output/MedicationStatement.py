#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_MedicationStatement(models.Model):
    partOf_Procedure = models.ManyToManyField("FHIR_Procedure", related_name="MedicationStatement_partOf", blank=True)
    partOf_MedicationStatement = models.ManyToManyField("FHIR_MedicationStatement", related_name="MedicationStatement_partOf", blank=True)
    class StatusChoices(models.TextChoices): RECORDED = 'recorded', 'Recorded'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; DRAFT = 'draft', 'Draft'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    BINDING_medication = "TODO"
    medication_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_medication}, related_name='MedicationStatement_medication', blank=True)
    medication_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    medication_Medication_ref = models.ForeignKey("FHIR_Medication", related_name="MedicationStatement_medication_Medication", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Patient = models.ForeignKey("FHIR_Patient", related_name="MedicationStatement_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Group = models.ForeignKey("FHIR_Group", related_name="MedicationStatement_subject", null=True, blank=True, on_delete=models.SET_NULL)
    encounter = models.ForeignKey("FHIR_Encounter", related_name="MedicationStatement_encounter", null=True, blank=True, on_delete=models.SET_NULL)
    effective_dateTime = FHIR_primitive_DateTimeField(null=True, blank=True, )
    effective_Period = models.OneToOneField("FHIR_GP_Period", related_name='MedicationStatement_effective_Period', null=True, blank=True, on_delete=models.SET_NULL)
    effective_Timing = models.OneToOneField("FHIR_GP_Timing", related_name='MedicationStatement_effective_Timing', null=True, blank=True, on_delete=models.SET_NULL)
    dateAsserted = FHIR_primitive_DateTimeField(null=True, blank=True, )
    author_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="MedicationStatement_author", null=True, blank=True, on_delete=models.SET_NULL)
    author_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="MedicationStatement_author", null=True, blank=True, on_delete=models.SET_NULL)
    author_Organization = models.ForeignKey("FHIR_Organization", related_name="MedicationStatement_author", null=True, blank=True, on_delete=models.SET_NULL)
    author_Patient = models.ForeignKey("FHIR_Patient", related_name="MedicationStatement_author", null=True, blank=True, on_delete=models.SET_NULL)
    author_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="MedicationStatement_author", null=True, blank=True, on_delete=models.SET_NULL)
    author_Device = models.ForeignKey("FHIR_Device", related_name="MedicationStatement_author", null=True, blank=True, on_delete=models.SET_NULL)
    informationSource_Device = models.ManyToManyField("FHIR_Device", related_name="MedicationStatement_informationSource", blank=True)
    informationSource_Patient = models.ManyToManyField("FHIR_Patient", related_name="MedicationStatement_informationSource", blank=True)
    informationSource_Practitioner = models.ManyToManyField("FHIR_Practitioner", related_name="MedicationStatement_informationSource", blank=True)
    informationSource_PractitionerRole = models.ManyToManyField("FHIR_PractitionerRole", related_name="MedicationStatement_informationSource", blank=True)
    informationSource_RelatedPerson = models.ManyToManyField("FHIR_RelatedPerson", related_name="MedicationStatement_informationSource", blank=True)
    informationSource_Organization = models.ManyToManyField("FHIR_Organization", related_name="MedicationStatement_informationSource", blank=True)
    informationSource_Group = models.ManyToManyField("FHIR_Group", related_name="MedicationStatement_informationSource", blank=True)
    relatedClinicalInformation_Observation = models.ManyToManyField("FHIR_Observation", related_name="MedicationStatement_relatedClinicalInformation", blank=True)
    relatedClinicalInformation_Condition = models.ManyToManyField("FHIR_Condition", related_name="MedicationStatement_relatedClinicalInformation", blank=True)
    renderedDosageInstruction = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_MedicationStatement_identifier(FHIR_GP_Identifier):
    MedicationStatement = models.ForeignKey(FHIR_MedicationStatement, related_name='MedicationStatement_identifier', null=False, on_delete=models.CASCADE)

class FHIR_MedicationStatement_category(models.Model):
    MedicationStatement = models.ForeignKey(FHIR_MedicationStatement, related_name='MedicationStatement_category', null=False, on_delete=models.CASCADE)
    BINDING_category = "TODO"
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='MedicationStatement_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_MedicationStatement_reason(models.Model):
    MedicationStatement = models.ForeignKey(FHIR_MedicationStatement, related_name='MedicationStatement_reason', null=False, on_delete=models.CASCADE)
    BINDING_reason = "TODO"
    reason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_reason}, related_name='MedicationStatement_reason', blank=True)
    reason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    reason_Condition_ref = models.ForeignKey("FHIR_Condition", related_name="MedicationStatement_reason_Condition", null=True, blank=True, on_delete=models.SET_NULL)
    reason_Observation_ref = models.ForeignKey("FHIR_Observation", related_name="MedicationStatement_reason_Observation", null=True, blank=True, on_delete=models.SET_NULL)
    reason_DiagnosticReport_ref = models.ForeignKey("FHIR_DiagnosticReport", related_name="MedicationStatement_reason_DiagnosticReport", null=True, blank=True, on_delete=models.SET_NULL)
    reason_Procedure_ref = models.ForeignKey("FHIR_Procedure", related_name="MedicationStatement_reason_Procedure", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_MedicationStatement_note(FHIR_GP_Annotation):
    MedicationStatement = models.ForeignKey(FHIR_MedicationStatement, related_name='MedicationStatement_note', null=False, on_delete=models.CASCADE)

class FHIR_MedicationStatement_dosage(FHIR_SP_Dosage):
    MedicationStatement = models.ForeignKey(FHIR_MedicationStatement, related_name='MedicationStatement_dosage', null=False, on_delete=models.CASCADE)

class FHIR_MedicationStatement_adherence(models.Model):
    MedicationStatement = models.ForeignKey(FHIR_MedicationStatement, related_name='MedicationStatement_adherence', null=False, on_delete=models.CASCADE)
    BINDING_code = "TODO"
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='MedicationStatement_adherence_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_reason = "TODO"
    reason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_reason}, related_name='MedicationStatement_adherence_reason', blank=True)
    reason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
