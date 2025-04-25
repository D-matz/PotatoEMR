
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Flag(models.Model):
    class StatusChoices(models.TextChoices): ACTIVE = 'active', 'Active'; INACTIVE = 'inactive', 'Inactive'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    BINDING_code = 'TODO'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='Flag_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    subject_Patient = models.ForeignKey("FHIR_Patient", related_name="Flag_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="Flag_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Location = models.ForeignKey("FHIR_Location", related_name="Flag_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Group = models.ForeignKey("FHIR_Group", related_name="Flag_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Organization = models.ForeignKey("FHIR_Organization", related_name="Flag_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="Flag_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="Flag_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_PlanDefinition = models.ForeignKey("FHIR_PlanDefinition", related_name="Flag_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Medication = models.ForeignKey("FHIR_Medication", related_name="Flag_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Procedure = models.ForeignKey("FHIR_Procedure", related_name="Flag_subject", null=True, blank=True, on_delete=models.SET_NULL)
    period = models.OneToOneField("FHIR_GP_Period", related_name='Flag_period', null=True, blank=True, on_delete=models.SET_NULL)
    encounter = models.ForeignKey("FHIR_Encounter", related_name="Flag_encounter", null=True, blank=True, on_delete=models.SET_NULL)
    author_Device = models.ForeignKey("FHIR_Device", related_name="Flag_author", null=True, blank=True, on_delete=models.SET_NULL)
    author_Organization = models.ForeignKey("FHIR_Organization", related_name="Flag_author", null=True, blank=True, on_delete=models.SET_NULL)
    author_Patient = models.ForeignKey("FHIR_Patient", related_name="Flag_author", null=True, blank=True, on_delete=models.SET_NULL)
    author_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="Flag_author", null=True, blank=True, on_delete=models.SET_NULL)
    author_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="Flag_author", null=True, blank=True, on_delete=models.SET_NULL)
    author_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="Flag_author", null=True, blank=True, on_delete=models.SET_NULL)
    supportingInfo_Condition = models.ManyToManyField("FHIR_Condition", related_name="Flag_supportingInfo", blank=True)
    supportingInfo_Procedure = models.ManyToManyField("FHIR_Procedure", related_name="Flag_supportingInfo", blank=True)
    supportingInfo_AllergyIntolerance = models.ManyToManyField("FHIR_AllergyIntolerance", related_name="Flag_supportingInfo", blank=True)
    supportingInfo_Observation = models.ManyToManyField("FHIR_Observation", related_name="Flag_supportingInfo", blank=True)
    supportingInfo_RiskAssessment = models.ManyToManyField("FHIR_RiskAssessment", related_name="Flag_supportingInfo", blank=True)

class FHIR_Flag_identifier(FHIR_GP_Identifier):
    Flag = models.ForeignKey(FHIR_Flag, related_name='Flag_identifier', null=False, on_delete=models.CASCADE)

class FHIR_Flag_category(models.Model):
    Flag = models.ForeignKey(FHIR_Flag, related_name='Flag_category', null=False, on_delete=models.CASCADE)
    BINDING_category = 'TODO'
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='Flag_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    