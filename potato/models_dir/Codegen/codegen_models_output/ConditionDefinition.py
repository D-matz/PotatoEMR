#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_ConditionDefinition(models.Model):
    url = FHIR_primitive_URIField(null=True, blank=True, )
    version = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = models.OneToOneField("FHIR_GP_Coding", related_name='ConditionDefinition_versionAlgorithm', null=True, blank=True, on_delete=models.SET_NULL)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    title = FHIR_primitive_StringField(null=True, blank=True, )
    subtitle = FHIR_primitive_StringField(null=True, blank=True, )
    class StatusChoices(models.TextChoices): DRAFT = 'draft', 'Draft'; ACTIVE = 'active', 'Active'; RETIRED = 'retired', 'Retired'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    experimental = FHIR_primitive_BooleanField(null=True, blank=True, )
    date = FHIR_primitive_DateTimeField(null=True, blank=True, )
    publisher = FHIR_primitive_StringField(null=True, blank=True, )
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    BINDING_code = "TODO"
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='ConditionDefinition_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_severity = "TODO"
    severity_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_severity}, related_name='ConditionDefinition_severity', blank=True)
    severity_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_bodySite = "TODO"
    bodySite_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_bodySite}, related_name='ConditionDefinition_bodySite', blank=True)
    bodySite_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_stage = "TODO"
    stage_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_stage}, related_name='ConditionDefinition_stage', blank=True)
    stage_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    hasSeverity = FHIR_primitive_BooleanField(null=True, blank=True, )
    hasBodySite = FHIR_primitive_BooleanField(null=True, blank=True, )
    hasStage = FHIR_primitive_BooleanField(null=True, blank=True, )
    team = models.ManyToManyField("FHIR_CareTeam", related_name="ConditionDefinition_team", blank=True)

class FHIR_ConditionDefinition_identifier(FHIR_GP_Identifier):
    ConditionDefinition = models.ForeignKey(FHIR_ConditionDefinition, related_name='ConditionDefinition_identifier', null=False, on_delete=models.CASCADE)

class FHIR_ConditionDefinition_jurisdiction(models.Model):
    ConditionDefinition = models.ForeignKey(FHIR_ConditionDefinition, related_name='ConditionDefinition_jurisdiction', null=False, on_delete=models.CASCADE)
    BINDING_jurisdiction = "TODO"
    jurisdiction_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_jurisdiction}, related_name='ConditionDefinition_jurisdiction', blank=True)
    jurisdiction_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ConditionDefinition_definition(models.Model):
    ConditionDefinition = models.ForeignKey(FHIR_ConditionDefinition, related_name='ConditionDefinition_definition', null=False, on_delete=models.CASCADE)
    
    definition = FHIR_primitive_URIField(null=True, blank=True, )
    
class FHIR_ConditionDefinition_observation(models.Model):
    ConditionDefinition = models.ForeignKey(FHIR_ConditionDefinition, related_name='ConditionDefinition_observation', null=False, on_delete=models.CASCADE)
    
    observation = FHIR_primitive_CanonicalField(null=True, blank=True, )
    
class FHIR_ConditionDefinition_medication(models.Model):
    ConditionDefinition = models.ForeignKey(FHIR_ConditionDefinition, related_name='ConditionDefinition_medication', null=False, on_delete=models.CASCADE)
    BINDING_category = "TODO"
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='ConditionDefinition_medication_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_code = "TODO"
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='ConditionDefinition_medication_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_ConditionDefinition_precondition(models.Model):
    ConditionDefinition = models.ForeignKey(FHIR_ConditionDefinition, related_name='ConditionDefinition_precondition', null=False, on_delete=models.CASCADE)
    class TypeChoices(models.TextChoices): SENSITIVE = 'sensitive', 'Sensitive'; SPECIFIC = 'specific', 'Specific'; 
    type = FHIR_primitive_CodeField(choices=TypeChoices.choices, null=True, blank=True, )
    BINDING_code = "TODO"
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='ConditionDefinition_precondition_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_value = "TODO"
    value_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_value}, related_name='ConditionDefinition_precondition_value', blank=True)
    value_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value = models.OneToOneField("FHIR_GP_Quantity", related_name='ConditionDefinition_precondition_value', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ConditionDefinition_questionnaire(models.Model):
    ConditionDefinition = models.ForeignKey(FHIR_ConditionDefinition, related_name='ConditionDefinition_questionnaire', null=False, on_delete=models.CASCADE)
    class PurposeChoices(models.TextChoices): PREADMIT = 'preadmit', 'Preadmit'; DIFF_DIAGNOSIS = 'diff-diagnosis', 'Diff-diagnosis'; OUTCOME = 'outcome', 'Outcome'; 
    purpose = FHIR_primitive_CodeField(choices=PurposeChoices.choices, null=True, blank=True, )
    reference = models.ForeignKey("FHIR_Questionnaire", related_name="ConditionDefinition_questionnaire_reference", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ConditionDefinition_plan(models.Model):
    ConditionDefinition = models.ForeignKey(FHIR_ConditionDefinition, related_name='ConditionDefinition_plan', null=False, on_delete=models.CASCADE)
    BINDING_role = "TODO"
    role_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_role}, related_name='ConditionDefinition_plan_role', blank=True)
    role_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    reference = models.ForeignKey("FHIR_PlanDefinition", related_name="ConditionDefinition_plan_reference", null=True, blank=True, on_delete=models.SET_NULL)
