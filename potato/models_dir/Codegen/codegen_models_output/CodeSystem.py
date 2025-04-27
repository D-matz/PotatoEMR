#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_CodeSystem(models.Model):
    url = FHIR_primitive_URIField(null=True, blank=True, )
    version = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = models.OneToOneField("FHIR_GP_Coding", related_name='CodeSystem_versionAlgorithm', null=True, blank=True, on_delete=models.SET_NULL)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    title = FHIR_primitive_StringField(null=True, blank=True, )
    class StatusChoices(models.TextChoices): DRAFT = 'draft', 'Draft'; ACTIVE = 'active', 'Active'; RETIRED = 'retired', 'Retired'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    experimental = FHIR_primitive_BooleanField(null=True, blank=True, )
    date = FHIR_primitive_DateTimeField(null=True, blank=True, )
    publisher = FHIR_primitive_StringField(null=True, blank=True, )
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    purpose = FHIR_primitive_MarkdownField(null=True, blank=True, )
    copyright = FHIR_primitive_MarkdownField(null=True, blank=True, )
    copyrightLabel = FHIR_primitive_StringField(null=True, blank=True, )
    approvalDate = FHIR_primitive_DateField(null=True, blank=True, )
    lastReviewDate = FHIR_primitive_DateField(null=True, blank=True, )
    effectivePeriod = models.OneToOneField("FHIR_GP_Period", related_name='CodeSystem_effectivePeriod', null=True, blank=True, on_delete=models.SET_NULL)
    caseSensitive = FHIR_primitive_BooleanField(null=True, blank=True, )
    valueSet = FHIR_primitive_CanonicalField(null=True, blank=True, )
    class HierarchymeaningChoices(models.TextChoices): GROUPED_BY = 'grouped-by', 'Grouped-by'; IS_A = 'is-a', 'Is-a'; PART_OF = 'part-of', 'Part-of'; CLASSIFIED_WITH = 'classified-with', 'Classified-with'; 
    hierarchyMeaning = FHIR_primitive_CodeField(choices=HierarchymeaningChoices.choices, null=True, blank=True, )
    compositional = FHIR_primitive_BooleanField(null=True, blank=True, )
    versionNeeded = FHIR_primitive_BooleanField(null=True, blank=True, )
    class ContentChoices(models.TextChoices): NOT_PRESENT = 'not-present', 'Not-present'; EXAMPLE = 'example', 'Example'; FRAGMENT = 'fragment', 'Fragment'; COMPLETE = 'complete', 'Complete'; SUPPLEMENT = 'supplement', 'Supplement'; 
    content = FHIR_primitive_CodeField(choices=ContentChoices.choices, null=True, blank=True, )
    supplements = FHIR_primitive_CanonicalField(null=True, blank=True, )
    count = FHIR_primitive_UnsignedIntField(null=True, blank=True, )

class FHIR_CodeSystem_identifier(FHIR_GP_Identifier):
    CodeSystem = models.ForeignKey(FHIR_CodeSystem, related_name='CodeSystem_identifier', null=False, on_delete=models.CASCADE)

class FHIR_CodeSystem_jurisdiction(models.Model):
    CodeSystem = models.ForeignKey(FHIR_CodeSystem, related_name='CodeSystem_jurisdiction', null=False, on_delete=models.CASCADE)
    BINDING_jurisdiction = "TODO"
    jurisdiction_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_jurisdiction}, related_name='CodeSystem_jurisdiction', blank=True)
    jurisdiction_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_CodeSystem_topic(models.Model):
    CodeSystem = models.ForeignKey(FHIR_CodeSystem, related_name='CodeSystem_topic', null=False, on_delete=models.CASCADE)
    BINDING_topic = "TODO"
    topic_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_topic}, related_name='CodeSystem_topic', blank=True)
    topic_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_CodeSystem_filter(models.Model):
    CodeSystem = models.ForeignKey(FHIR_CodeSystem, related_name='CodeSystem_filter', null=False, on_delete=models.CASCADE)
    class CodeChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    code = FHIR_primitive_CodeField(choices=CodeChoices.choices, null=True, blank=True, )
    description = FHIR_primitive_StringField(null=True, blank=True, )
    value = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_CodeSystem_filter_operator(models.Model):
    CodeSystem_filter = models.ForeignKey(FHIR_CodeSystem_filter, related_name='CodeSystem_filter_operator', null=False, on_delete=models.CASCADE)
    
    class OperatorChoices(models.TextChoices): EQUALS = '=', '='; IS_A = 'is-a', 'Is-a'; DESCENDENT_OF = 'descendent-of', 'Descendent-of'; IS_NOT_A = 'is-not-a', 'Is-not-a'; REGEX = 'regex', 'Regex'; IN = 'in', 'In'; NOT_IN = 'not-in', 'Not-in'; GENERALIZES = 'generalizes', 'Generalizes'; CHILD_OF = 'child-of', 'Child-of'; DESCENDENT_LEAF = 'descendent-leaf', 'Descendent-leaf'; EXISTS = 'exists', 'Exists'; 
    operator = FHIR_primitive_CodeField(choices=OperatorChoices.choices, null=True, blank=True, )
    
class FHIR_CodeSystem_property(models.Model):
    CodeSystem = models.ForeignKey(FHIR_CodeSystem, related_name='CodeSystem_property', null=False, on_delete=models.CASCADE)
    class CodeChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    code = FHIR_primitive_CodeField(choices=CodeChoices.choices, null=True, blank=True, )
    uri = FHIR_primitive_URIField(null=True, blank=True, )
    description = FHIR_primitive_StringField(null=True, blank=True, )
    class TypeChoices(models.TextChoices): CODE = 'code', 'Code'; CODING = 'Coding', 'Coding'; STRING = 'string', 'String'; INTEGER = 'integer', 'Integer'; BOOLEAN = 'boolean', 'Boolean'; DATETIME = 'dateTime', 'Datetime'; DECIMAL = 'decimal', 'Decimal'; 
    type = FHIR_primitive_CodeField(choices=TypeChoices.choices, null=True, blank=True, )

class FHIR_CodeSystem_concept(models.Model):
    CodeSystem = models.ForeignKey(FHIR_CodeSystem, related_name='CodeSystem_concept', null=False, on_delete=models.CASCADE)
    class CodeChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    code = FHIR_primitive_CodeField(choices=CodeChoices.choices, null=True, blank=True, )
    display = FHIR_primitive_StringField(null=True, blank=True, )
    definition = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_CodeSystem_concept_designation(models.Model):
    CodeSystem_concept = models.ForeignKey(FHIR_CodeSystem_concept, related_name='CodeSystem_concept_designation', null=False, on_delete=models.CASCADE)
    class LanguageChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    language = FHIR_primitive_CodeField(choices=LanguageChoices.choices, null=True, blank=True, )
    use = models.OneToOneField("FHIR_GP_Coding", related_name='CodeSystem_concept_designation_use', null=True, blank=True, on_delete=models.SET_NULL)
    value = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_CodeSystem_concept_designation_additionalUse(FHIR_GP_Coding):
    CodeSystem_concept_designation = models.ForeignKey(FHIR_CodeSystem_concept_designation, related_name='CodeSystem_concept_designation_additionalUse', null=False, on_delete=models.CASCADE)

class FHIR_CodeSystem_concept_property(models.Model):
    CodeSystem_concept = models.ForeignKey(FHIR_CodeSystem_concept, related_name='CodeSystem_concept_property', null=False, on_delete=models.CASCADE)
    class CodeChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    code = FHIR_primitive_CodeField(choices=CodeChoices.choices, null=True, blank=True, )
    class ValueChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    value = FHIR_primitive_CodeField(choices=ValueChoices.choices, null=True, blank=True, )
    value = models.OneToOneField("FHIR_GP_Coding", related_name='CodeSystem_concept_property_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = FHIR_primitive_StringField(null=True, blank=True, )
    value = FHIR_primitive_BooleanField(null=True, blank=True, )
    value = FHIR_primitive_DateTimeField(null=True, blank=True, )
    value = FHIR_primitive_DecimalField(null=True, blank=True, )
