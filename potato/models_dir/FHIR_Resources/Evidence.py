#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Evidence(models.Model):
    url = FHIR_primitive_URIField(null=True, blank=True, )
    version = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = models.OneToOneField("FHIR_GP_Coding", related_name='Evidence_versionAlgorithm', null=True, blank=True, on_delete=models.SET_NULL)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    title = FHIR_primitive_StringField(null=True, blank=True, )
    citeAs = FHIR_primitive_MarkdownField(null=True, blank=True, )
    class StatusChoices(models.TextChoices): DRAFT = 'draft', 'Draft'; ACTIVE = 'active', 'Active'; RETIRED = 'retired', 'Retired'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    experimental = FHIR_primitive_BooleanField(null=True, blank=True, )
    date = FHIR_primitive_DateTimeField(null=True, blank=True, )
    approvalDate = FHIR_primitive_DateField(null=True, blank=True, )
    lastReviewDate = FHIR_primitive_DateField(null=True, blank=True, )
    publisher = FHIR_primitive_StringField(null=True, blank=True, )
    purpose = FHIR_primitive_MarkdownField(null=True, blank=True, )
    copyright = FHIR_primitive_MarkdownField(null=True, blank=True, )
    copyrightLabel = FHIR_primitive_StringField(null=True, blank=True, )
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    assertion = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_Evidence_identifier(FHIR_GP_Identifier):
    Evidence = models.ForeignKey(FHIR_Evidence, related_name='Evidence_identifier', null=False, on_delete=models.CASCADE)

class FHIR_Evidence_relatesTo(models.Model):
    Evidence = models.ForeignKey(FHIR_Evidence, related_name='Evidence_relatesTo', null=False, on_delete=models.CASCADE)
    class TypeChoices(models.TextChoices): DOCUMENTATION = 'documentation', 'Documentation'; JUSTIFICATION = 'justification', 'Justification'; PREDECESSOR = 'predecessor', 'Predecessor'; SUCCESSOR = 'successor', 'Successor'; DERIVED_FROM = 'derived-from', 'Derived-from'; DEPENDS_ON = 'depends-on', 'Depends-on'; COMPOSED_OF = 'composed-of', 'Composed-of'; PART_OF = 'part-of', 'Part-of'; AMENDS = 'amends', 'Amends'; AMENDED_WITH = 'amended-with', 'Amended-with'; APPENDS = 'appends', 'Appends'; APPENDED_WITH = 'appended-with', 'Appended-with'; CITES = 'cites', 'Cites'; CITED_BY = 'cited-by', 'Cited-by'; COMMENTS_ON = 'comments-on', 'Comments-on'; COMMENT_IN = 'comment-in', 'Comment-in'; CONTAINS = 'contains', 'Contains'; CONTAINED_IN = 'contained-in', 'Contained-in'; CORRECTS = 'corrects', 'Corrects'; CORRECTION_IN = 'correction-in', 'Correction-in'; REPLACES = 'replaces', 'Replaces'; REPLACED_WITH = 'replaced-with', 'Replaced-with'; RETRACTS = 'retracts', 'Retracts'; RETRACTED_BY = 'retracted-by', 'Retracted-by'; SIGNS = 'signs', 'Signs'; SIMILAR_TO = 'similar-to', 'Similar-to'; SUPPORTS = 'supports', 'Supports'; SUPPORTED_WITH = 'supported-with', 'Supported-with'; TRANSFORMS = 'transforms', 'Transforms'; TRANSFORMED_INTO = 'transformed-into', 'Transformed-into'; TRANSFORMED_WITH = 'transformed-with', 'Transformed-with'; SPECIFICATION_OF = 'specification-of', 'Specification-of'; CREATED_WITH = 'created-with', 'Created-with'; CITE_AS = 'cite-as', 'Cite-as'; SUMMARIZES = 'summarizes', 'Summarizes'; 
    type = FHIR_primitive_CodeField(choices=TypeChoices.choices, null=True, blank=True, )
    target = FHIR_primitive_URIField(null=True, blank=True, )
    target = models.OneToOneField("FHIR_GP_Attachment", related_name='Evidence_relatesTo_target', null=True, blank=True, on_delete=models.SET_NULL)
    target = FHIR_primitive_CanonicalField(null=True, blank=True, )
    target = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_Evidence_note(FHIR_GP_Annotation):
    Evidence = models.ForeignKey(FHIR_Evidence, related_name='Evidence_note', null=False, on_delete=models.CASCADE)

class FHIR_Evidence_variableDefinition(models.Model):
    Evidence = models.ForeignKey(FHIR_Evidence, related_name='Evidence_variableDefinition', null=False, on_delete=models.CASCADE)
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    class VariableroleChoices(models.TextChoices): POPULATION = 'population', 'Population'; EXPOSURE = 'exposure', 'Exposure'; OUTCOME = 'outcome', 'Outcome'; COVARIATE = 'covariate', 'Covariate'; 
    variableRole = FHIR_primitive_CodeField(choices=VariableroleChoices.choices, null=True, blank=True, )
    BINDING_roleSubtype = 'TODO'
    roleSubtype_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_roleSubtype}, related_name='Evidence_variableDefinition_roleSubtype', blank=True)
    roleSubtype_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    comparatorCategory = FHIR_primitive_StringField(null=True, blank=True, )
    observed_Group = models.ForeignKey("FHIR_Group", related_name="Evidence_variableDefinition_observed", null=True, blank=True, on_delete=models.SET_NULL)
    observed_EvidenceVariable = models.ForeignKey("FHIR_EvidenceVariable", related_name="Evidence_variableDefinition_observed", null=True, blank=True, on_delete=models.SET_NULL)
    intended_Group = models.ForeignKey("FHIR_Group", related_name="Evidence_variableDefinition_intended", null=True, blank=True, on_delete=models.SET_NULL)
    intended_EvidenceVariable = models.ForeignKey("FHIR_EvidenceVariable", related_name="Evidence_variableDefinition_intended", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_directnessMatch = 'TODO'
    directnessMatch_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_directnessMatch}, related_name='Evidence_variableDefinition_directnessMatch', blank=True)
    directnessMatch_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_Evidence_variableDefinition_note(FHIR_GP_Annotation):
    Evidence_variableDefinition = models.ForeignKey(FHIR_Evidence_variableDefinition, related_name='Evidence_variableDefinition_note', null=False, on_delete=models.CASCADE)

class FHIR_Evidence_synthesisType(models.Model):
    Evidence = models.ForeignKey(FHIR_Evidence, related_name='Evidence_synthesisType', null=False, on_delete=models.CASCADE)
    BINDING_synthesisType = 'TODO'
    synthesisType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_synthesisType}, related_name='Evidence_synthesisType', blank=True)
    synthesisType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Evidence_studyDesign(models.Model):
    Evidence = models.ForeignKey(FHIR_Evidence, related_name='Evidence_studyDesign', null=False, on_delete=models.CASCADE)
    BINDING_studyDesign = 'TODO'
    studyDesign_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_studyDesign}, related_name='Evidence_studyDesign', blank=True)
    studyDesign_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Evidence_statistic(models.Model):
    Evidence = models.ForeignKey(FHIR_Evidence, related_name='Evidence_statistic', null=False, on_delete=models.CASCADE)
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    BINDING_statisticType = 'TODO'
    statisticType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_statisticType}, related_name='Evidence_statistic_statisticType', blank=True)
    statisticType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_category = 'TODO'
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='Evidence_statistic_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='Evidence_statistic_quantity', null=True, blank=True, on_delete=models.SET_NULL)
    numberOfEvents = FHIR_primitive_UnsignedIntField(null=True, blank=True, )
    numberAffected = FHIR_primitive_UnsignedIntField(null=True, blank=True, )

class FHIR_Evidence_statistic_note(FHIR_GP_Annotation):
    Evidence_statistic = models.ForeignKey(FHIR_Evidence_statistic, related_name='Evidence_statistic_note', null=False, on_delete=models.CASCADE)

class FHIR_Evidence_statistic_sampleSize(models.Model):
    Evidence_statistic = models.ForeignKey(FHIR_Evidence_statistic, related_name='Evidence_statistic_sampleSize', null=False, on_delete=models.CASCADE)
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    numberOfStudies = FHIR_primitive_UnsignedIntField(null=True, blank=True, )
    numberOfParticipants = FHIR_primitive_UnsignedIntField(null=True, blank=True, )
    knownDataCount = FHIR_primitive_UnsignedIntField(null=True, blank=True, )

class FHIR_Evidence_statistic_sampleSize_note(FHIR_GP_Annotation):
    Evidence_statistic_sampleSize = models.ForeignKey(FHIR_Evidence_statistic_sampleSize, related_name='Evidence_statistic_sampleSize_note', null=False, on_delete=models.CASCADE)

class FHIR_Evidence_statistic_attributeEstimate(models.Model):
    Evidence_statistic = models.ForeignKey(FHIR_Evidence_statistic, related_name='Evidence_statistic_attributeEstimate', null=False, on_delete=models.CASCADE)
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Evidence_statistic_attributeEstimate_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='Evidence_statistic_attributeEstimate_quantity', null=True, blank=True, on_delete=models.SET_NULL)
    level = FHIR_primitive_DecimalField(null=True, blank=True, )
    range = models.OneToOneField("FHIR_GP_Range", related_name='Evidence_statistic_attributeEstimate_range', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Evidence_statistic_attributeEstimate_note(FHIR_GP_Annotation):
    Evidence_statistic_attributeEstimate = models.ForeignKey(FHIR_Evidence_statistic_attributeEstimate, related_name='Evidence_statistic_attributeEstimate_note', null=False, on_delete=models.CASCADE)

class FHIR_Evidence_statistic_modelCharacteristic(models.Model):
    Evidence_statistic = models.ForeignKey(FHIR_Evidence_statistic, related_name='Evidence_statistic_modelCharacteristic', null=False, on_delete=models.CASCADE)
    BINDING_code = 'TODO'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='Evidence_statistic_modelCharacteristic_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value = models.OneToOneField("FHIR_GP_Quantity", related_name='Evidence_statistic_modelCharacteristic_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_Range", related_name='Evidence_statistic_modelCharacteristic_value', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_value = 'TODO'
    value_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_value}, related_name='Evidence_statistic_modelCharacteristic_value', blank=True)
    value_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    intended = FHIR_primitive_BooleanField(null=True, blank=True, )
    applied = FHIR_primitive_BooleanField(null=True, blank=True, )

class FHIR_Evidence_statistic_modelCharacteristic_variable(models.Model):
    Evidence_statistic_modelCharacteristic = models.ForeignKey(FHIR_Evidence_statistic_modelCharacteristic, related_name='Evidence_statistic_modelCharacteristic_variable', null=False, on_delete=models.CASCADE)
    variableDefinition_Group = models.ForeignKey("FHIR_Group", related_name="Evidence_statistic_modelCharacteristic_variable_variableDefinition", null=True, blank=True, on_delete=models.SET_NULL)
    variableDefinition_EvidenceVariable = models.ForeignKey("FHIR_EvidenceVariable", related_name="Evidence_statistic_modelCharacteristic_variable_variableDefinition", null=True, blank=True, on_delete=models.SET_NULL)
    class HandlingChoices(models.TextChoices): BOOLEAN = 'boolean', 'Boolean'; CONTINUOUS = 'continuous', 'Continuous'; DICHOTOMOUS = 'dichotomous', 'Dichotomous'; ORDINAL = 'ordinal', 'Ordinal'; POLYCHOTOMOUS = 'polychotomous', 'Polychotomous'; EXTENSION = 'extension', 'Extension'; 
    handling = FHIR_primitive_CodeField(choices=HandlingChoices.choices, null=True, blank=True, )

class FHIR_Evidence_statistic_modelCharacteristic_variable_valueCategory(models.Model):
    Evidence_statistic_modelCharacteristic_variable = models.ForeignKey(FHIR_Evidence_statistic_modelCharacteristic_variable, related_name='Evidence_statistic_modelCharacteristic_variable_valueCategory', null=False, on_delete=models.CASCADE)
    BINDING_valueCategory = 'TODO'
    valueCategory_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_valueCategory}, related_name='Evidence_statistic_modelCharacteristic_variable_valueCategory', blank=True)
    valueCategory_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Evidence_statistic_modelCharacteristic_variable_valueQuantity(FHIR_GP_Quantity):
    Evidence_statistic_modelCharacteristic_variable = models.ForeignKey(FHIR_Evidence_statistic_modelCharacteristic_variable, related_name='Evidence_statistic_modelCharacteristic_variable_valueQuantity', null=False, on_delete=models.CASCADE)

class FHIR_Evidence_statistic_modelCharacteristic_variable_valueRange(FHIR_GP_Range):
    Evidence_statistic_modelCharacteristic_variable = models.ForeignKey(FHIR_Evidence_statistic_modelCharacteristic_variable, related_name='Evidence_statistic_modelCharacteristic_variable_valueRange', null=False, on_delete=models.CASCADE)

class FHIR_Evidence_certainty(models.Model):
    Evidence = models.ForeignKey(FHIR_Evidence, related_name='Evidence_certainty', null=False, on_delete=models.CASCADE)
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Evidence_certainty_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_rating = 'TODO'
    rating_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_rating}, related_name='Evidence_certainty_rating', blank=True)
    rating_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_Evidence_certainty_note(FHIR_GP_Annotation):
    Evidence_certainty = models.ForeignKey(FHIR_Evidence_certainty, related_name='Evidence_certainty_note', null=False, on_delete=models.CASCADE)

class FHIR_Evidence_certainty_rater(models.Model):
    Evidence_certainty = models.ForeignKey(FHIR_Evidence_certainty, related_name='Evidence_certainty_rater', null=False, on_delete=models.CASCADE)
    
    rater = FHIR_primitive_StringField(null=True, blank=True, )
    