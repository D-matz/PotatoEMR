#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Measure(models.Model):
    url = FHIR_primitive_URIField(null=True, blank=True, )
    version = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = models.OneToOneField("FHIR_GP_Coding", related_name='Measure_versionAlgorithm', null=True, blank=True, on_delete=models.SET_NULL)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    title = FHIR_primitive_StringField(null=True, blank=True, )
    subtitle = FHIR_primitive_StringField(null=True, blank=True, )
    class StatusChoices(models.TextChoices): DRAFT = 'draft', 'Draft'; ACTIVE = 'active', 'Active'; RETIRED = 'retired', 'Retired'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    experimental = FHIR_primitive_BooleanField(null=True, blank=True, )
    BINDING_subject = "TODO"
    subject_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_subject}, related_name='Measure_subject', blank=True)
    subject_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    subject = models.ForeignKey("FHIR_Group", related_name="Measure_subject", null=True, blank=True, on_delete=models.SET_NULL)
    class BasisChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    basis = FHIR_primitive_CodeField(choices=BasisChoices.choices, null=True, blank=True, )
    date = FHIR_primitive_DateTimeField(null=True, blank=True, )
    publisher = FHIR_primitive_StringField(null=True, blank=True, )
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    purpose = FHIR_primitive_MarkdownField(null=True, blank=True, )
    usage = FHIR_primitive_MarkdownField(null=True, blank=True, )
    copyright = FHIR_primitive_MarkdownField(null=True, blank=True, )
    copyrightLabel = FHIR_primitive_StringField(null=True, blank=True, )
    approvalDate = FHIR_primitive_DateField(null=True, blank=True, )
    lastReviewDate = FHIR_primitive_DateField(null=True, blank=True, )
    effectivePeriod = models.OneToOneField("FHIR_GP_Period", related_name='Measure_effectivePeriod', null=True, blank=True, on_delete=models.SET_NULL)
    reportingFrequency = models.OneToOneField("FHIR_GP_Quantity", related_name='Measure_reportingFrequency', null=True, blank=True, on_delete=models.SET_NULL)
    disclaimer = FHIR_primitive_MarkdownField(null=True, blank=True, )
    BINDING_scoring = "TODO"
    scoring_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_scoring}, related_name='Measure_scoring', blank=True)
    scoring_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_scoringUnit = "TODO"
    scoringUnit_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_scoringUnit}, related_name='Measure_scoringUnit', blank=True)
    scoringUnit_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    scoringPrecision = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    BINDING_compositeScoring = "TODO"
    compositeScoring_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_compositeScoring}, related_name='Measure_compositeScoring', blank=True)
    compositeScoring_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    riskAdjustment = FHIR_primitive_MarkdownField(null=True, blank=True, )
    rateAggregation = FHIR_primitive_MarkdownField(null=True, blank=True, )
    rationale = FHIR_primitive_MarkdownField(null=True, blank=True, )
    clinicalRecommendationStatement = FHIR_primitive_MarkdownField(null=True, blank=True, )
    BINDING_improvementNotation = "TODO"
    improvementNotation_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_improvementNotation}, related_name='Measure_improvementNotation', blank=True)
    improvementNotation_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    improvementNotationGuidance = FHIR_primitive_MarkdownField(null=True, blank=True, )
    guidance = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_Measure_identifier(FHIR_GP_Identifier):
    Measure = models.ForeignKey(FHIR_Measure, related_name='Measure_identifier', null=False, on_delete=models.CASCADE)

class FHIR_Measure_jurisdiction(models.Model):
    Measure = models.ForeignKey(FHIR_Measure, related_name='Measure_jurisdiction', null=False, on_delete=models.CASCADE)
    BINDING_jurisdiction = "TODO"
    jurisdiction_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_jurisdiction}, related_name='Measure_jurisdiction', blank=True)
    jurisdiction_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Measure_topic(models.Model):
    Measure = models.ForeignKey(FHIR_Measure, related_name='Measure_topic', null=False, on_delete=models.CASCADE)
    BINDING_topic = "TODO"
    topic_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_topic}, related_name='Measure_topic', blank=True)
    topic_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Measure_library(models.Model):
    Measure = models.ForeignKey(FHIR_Measure, related_name='Measure_library', null=False, on_delete=models.CASCADE)
    
    library = FHIR_primitive_CanonicalField(null=True, blank=True, )
    
class FHIR_Measure_type(models.Model):
    Measure = models.ForeignKey(FHIR_Measure, related_name='Measure_type', null=False, on_delete=models.CASCADE)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Measure_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Measure_term(models.Model):
    Measure = models.ForeignKey(FHIR_Measure, related_name='Measure_term', null=False, on_delete=models.CASCADE)
    BINDING_code = "TODO"
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='Measure_term_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    definition = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_Measure_group(models.Model):
    Measure = models.ForeignKey(FHIR_Measure, related_name='Measure_group', null=False, on_delete=models.CASCADE)
    linkId = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_code = "TODO"
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='Measure_group_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    BINDING_subject = "TODO"
    subject_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_subject}, related_name='Measure_group_subject', blank=True)
    subject_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    subject = models.ForeignKey("FHIR_Group", related_name="Measure_group_subject", null=True, blank=True, on_delete=models.SET_NULL)
    class BasisChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    basis = FHIR_primitive_CodeField(choices=BasisChoices.choices, null=True, blank=True, )
    BINDING_scoring = "TODO"
    scoring_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_scoring}, related_name='Measure_group_scoring', blank=True)
    scoring_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_scoringUnit = "TODO"
    scoringUnit_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_scoringUnit}, related_name='Measure_group_scoringUnit', blank=True)
    scoringUnit_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    scoringPrecision = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    BINDING_compositeScoring = "TODO"
    compositeScoring_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_compositeScoring}, related_name='Measure_group_compositeScoring', blank=True)
    compositeScoring_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    rateAggregation = FHIR_primitive_MarkdownField(null=True, blank=True, )
    BINDING_improvementNotation = "TODO"
    improvementNotation_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_improvementNotation}, related_name='Measure_group_improvementNotation', blank=True)
    improvementNotation_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    improvementNotationGuidance = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_Measure_group_type(models.Model):
    Measure_group = models.ForeignKey(FHIR_Measure_group, related_name='Measure_group_type', null=False, on_delete=models.CASCADE)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Measure_group_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Measure_group_component(models.Model):
    Measure_group = models.ForeignKey(FHIR_Measure_group, related_name='Measure_group_component', null=False, on_delete=models.CASCADE)
    measure = FHIR_primitive_CanonicalField(null=True, blank=True, )
    groupId = FHIR_primitive_StringField(null=True, blank=True, )
    weight = FHIR_primitive_DecimalField(null=True, blank=True, )

class FHIR_Measure_group_library(models.Model):
    Measure_group = models.ForeignKey(FHIR_Measure_group, related_name='Measure_group_library', null=False, on_delete=models.CASCADE)
    
    library = FHIR_primitive_CanonicalField(null=True, blank=True, )
    
class FHIR_Measure_group_population(models.Model):
    Measure_group = models.ForeignKey(FHIR_Measure_group, related_name='Measure_group_population', null=False, on_delete=models.CASCADE)
    linkId = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_code = "TODO"
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='Measure_group_population_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    groupDefinition = models.ForeignKey("FHIR_Group", related_name="Measure_group_population_groupDefinition", null=True, blank=True, on_delete=models.SET_NULL)
    inputPopulationId = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_aggregateMethod = "TODO"
    aggregateMethod_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_aggregateMethod}, related_name='Measure_group_population_aggregateMethod', blank=True)
    aggregateMethod_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_Measure_group_stratifier(models.Model):
    Measure_group = models.ForeignKey(FHIR_Measure_group, related_name='Measure_group_stratifier', null=False, on_delete=models.CASCADE)
    linkId = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_code = "TODO"
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='Measure_group_stratifier_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    groupDefinition = models.ForeignKey("FHIR_Group", related_name="Measure_group_stratifier_groupDefinition", null=True, blank=True, on_delete=models.SET_NULL)
    valueSet = FHIR_primitive_CanonicalField(null=True, blank=True, )
    unit = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_Measure_group_stratifier_component(models.Model):
    Measure_group_stratifier = models.ForeignKey(FHIR_Measure_group_stratifier, related_name='Measure_group_stratifier_component', null=False, on_delete=models.CASCADE)
    linkId = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_code = "TODO"
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='Measure_group_stratifier_component_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    groupDefinition = models.ForeignKey("FHIR_Group", related_name="Measure_group_stratifier_component_groupDefinition", null=True, blank=True, on_delete=models.SET_NULL)
    valueSet = FHIR_primitive_CanonicalField(null=True, blank=True, )
    unit = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_Measure_supplementalData(models.Model):
    Measure = models.ForeignKey(FHIR_Measure, related_name='Measure_supplementalData', null=False, on_delete=models.CASCADE)
    linkId = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_code = "TODO"
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='Measure_supplementalData_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    valueSet = FHIR_primitive_CanonicalField(null=True, blank=True, )
    unit = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_Measure_supplementalData_usage(models.Model):
    Measure_supplementalData = models.ForeignKey(FHIR_Measure_supplementalData, related_name='Measure_supplementalData_usage', null=False, on_delete=models.CASCADE)
    BINDING_usage = "TODO"
    usage_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_usage}, related_name='Measure_supplementalData_usage', blank=True)
    usage_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    