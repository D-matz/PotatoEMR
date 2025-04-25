
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_ValueSet(models.Model):
    url = FHIR_primitive_URIField(null=True, blank=True, )
    version = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = models.OneToOneField("FHIR_GP_Coding", related_name='ValueSet_versionAlgorithm', null=True, blank=True, on_delete=models.SET_NULL)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    title = FHIR_primitive_StringField(null=True, blank=True, )
    class StatusChoices(models.TextChoices): DRAFT = 'draft', 'Draft'; ACTIVE = 'active', 'Active'; RETIRED = 'retired', 'Retired'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    experimental = FHIR_primitive_BooleanField(null=True, blank=True, )
    date = FHIR_primitive_DateTimeField(null=True, blank=True, )
    publisher = FHIR_primitive_StringField(null=True, blank=True, )
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    immutable = FHIR_primitive_BooleanField(null=True, blank=True, )
    purpose = FHIR_primitive_MarkdownField(null=True, blank=True, )
    copyright = FHIR_primitive_MarkdownField(null=True, blank=True, )
    copyrightLabel = FHIR_primitive_StringField(null=True, blank=True, )
    approvalDate = FHIR_primitive_DateField(null=True, blank=True, )
    lastReviewDate = FHIR_primitive_DateField(null=True, blank=True, )
    effectivePeriod = models.OneToOneField("FHIR_GP_Period", related_name='ValueSet_effectivePeriod', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ValueSet_identifier(FHIR_GP_Identifier):
    ValueSet = models.ForeignKey(FHIR_ValueSet, related_name='ValueSet_identifier', null=False, on_delete=models.CASCADE)

class FHIR_ValueSet_jurisdiction(models.Model):
    ValueSet = models.ForeignKey(FHIR_ValueSet, related_name='ValueSet_jurisdiction', null=False, on_delete=models.CASCADE)
    BINDING_jurisdiction = 'TODO'
    jurisdiction_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_jurisdiction}, related_name='ValueSet_jurisdiction', blank=True)
    jurisdiction_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ValueSet_topic(models.Model):
    ValueSet = models.ForeignKey(FHIR_ValueSet, related_name='ValueSet_topic', null=False, on_delete=models.CASCADE)
    BINDING_topic = 'TODO'
    topic_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_topic}, related_name='ValueSet_topic', blank=True)
    topic_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ValueSet_compose(models.Model):
    ValueSet = models.ForeignKey(FHIR_ValueSet, related_name='ValueSet_compose', null=False, on_delete=models.CASCADE)
    lockedDate = FHIR_primitive_DateField(null=True, blank=True, )
    inactive = FHIR_primitive_BooleanField(null=True, blank=True, )

class FHIR_ValueSet_compose_include(models.Model):
    ValueSet_compose = models.ForeignKey(FHIR_ValueSet_compose, related_name='ValueSet_compose_include', null=False, on_delete=models.CASCADE)
    system = FHIR_primitive_URIField(null=True, blank=True, )
    version = FHIR_primitive_StringField(null=True, blank=True, )
    copyright = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_ValueSet_compose_include_concept(models.Model):
    ValueSet_compose_include = models.ForeignKey(FHIR_ValueSet_compose_include, related_name='ValueSet_compose_include_concept', null=False, on_delete=models.CASCADE)
    class CodeChoices(models.TextChoices): CODE_OR_EXPRESSION_FROM_SYSTEM = 'Code or expression from system', 'Code or expression from system'; 
    code = FHIR_primitive_CodeField(choices=CodeChoices.choices, null=True, blank=True, )
    display = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_ValueSet_compose_include_concept_designation(models.Model):
    ValueSet_compose_include_concept = models.ForeignKey(FHIR_ValueSet_compose_include_concept, related_name='ValueSet_compose_include_concept_designation', null=False, on_delete=models.CASCADE)
    class LanguageChoices(models.TextChoices): HUMAN_LANGUAGE_OF_THE_DESIGNATION = 'Human language of the designation', 'Human language of the designation'; 
    language = FHIR_primitive_CodeField(choices=LanguageChoices.choices, null=True, blank=True, )
    use = models.OneToOneField("FHIR_GP_Coding", related_name='ValueSet_compose_include_concept_designation_use', null=True, blank=True, on_delete=models.SET_NULL)
    value = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_ValueSet_compose_include_concept_designation_additionalUse(FHIR_GP_Coding):
    ValueSet_compose_include_concept_designation = models.ForeignKey(FHIR_ValueSet_compose_include_concept_designation, related_name='ValueSet_compose_include_concept_designation_additionalUse', null=False, on_delete=models.CASCADE)

class FHIR_ValueSet_compose_include_filter(models.Model):
    ValueSet_compose_include = models.ForeignKey(FHIR_ValueSet_compose_include, related_name='ValueSet_compose_include_filter', null=False, on_delete=models.CASCADE)
    class PropertyChoices(models.TextChoices): A_PROPERTY/FILTER_DEFINED_BY_THE_CODE_SYSTEM = 'A property/filter defined by the code system', 'A property/filter defined by the code system'; 
    property = FHIR_primitive_CodeField(choices=PropertyChoices.choices, null=True, blank=True, )
    class OpChoices(models.TextChoices): = = '=', '='; IS_A = 'is-a', 'Is-a'; DESCENDENT_OF = 'descendent-of', 'Descendent-of'; IS_NOT_A = 'is-not-a', 'Is-not-a'; REGEX = 'regex', 'Regex'; IN = 'in', 'In'; NOT_IN = 'not-in', 'Not-in'; GENERALIZES = 'generalizes', 'Generalizes'; CHILD_OF = 'child-of', 'Child-of'; DESCENDENT_LEAF = 'descendent-leaf', 'Descendent-leaf'; EXISTS = 'exists', 'Exists'; 
    op = FHIR_primitive_CodeField(choices=OpChoices.choices, null=True, blank=True, )
    value = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_ValueSet_compose_include_valueSet(models.Model):
    ValueSet_compose_include = models.ForeignKey(FHIR_ValueSet_compose_include, related_name='ValueSet_compose_include_valueSet', null=False, on_delete=models.CASCADE)
    
    valueSet = FHIR_primitive_CanonicalField(null=True, blank=True, )
    
class FHIR_ValueSet_compose_property(models.Model):
    ValueSet_compose = models.ForeignKey(FHIR_ValueSet_compose, related_name='ValueSet_compose_property', null=False, on_delete=models.CASCADE)
    
    property = FHIR_primitive_StringField(null=True, blank=True, )
    
class FHIR_ValueSet_expansion(models.Model):
    ValueSet = models.ForeignKey(FHIR_ValueSet, related_name='ValueSet_expansion', null=False, on_delete=models.CASCADE)
    identifier = FHIR_primitive_URIField(null=True, blank=True, )
    next = FHIR_primitive_URIField(null=True, blank=True, )
    timestamp = FHIR_primitive_DateTimeField(null=True, blank=True, )

class FHIR_ValueSet_expansion_parameter(models.Model):
    ValueSet_expansion = models.ForeignKey(FHIR_ValueSet_expansion, related_name='ValueSet_expansion_parameter', null=False, on_delete=models.CASCADE)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    value = FHIR_primitive_StringField(null=True, blank=True, )
    value = FHIR_primitive_BooleanField(null=True, blank=True, )
    value = FHIR_primitive_DecimalField(null=True, blank=True, )
    value = FHIR_primitive_URIField(null=True, blank=True, )
    class ValueChoices(models.TextChoices): VALUE_OF_THE_NAMED_PARAMETER = 'Value of the named parameter', 'Value of the named parameter'; 
    value = FHIR_primitive_CodeField(choices=ValueChoices.choices, null=True, blank=True, )
    value = FHIR_primitive_DateTimeField(null=True, blank=True, )

class FHIR_ValueSet_expansion_property(models.Model):
    ValueSet_expansion = models.ForeignKey(FHIR_ValueSet_expansion, related_name='ValueSet_expansion_property', null=False, on_delete=models.CASCADE)
    class CodeChoices(models.TextChoices): IDENTIFIES_THE_PROPERTY_ON_THE_CONCEPTS,_AND_WHEN_REFERRED_TO_IN_OPERATIONS = 'Identifies the property on the concepts, and when referred to in operations', 'Identifies the property on the concepts, and when referred to in operations'; 
    code = FHIR_primitive_CodeField(choices=CodeChoices.choices, null=True, blank=True, )
    uri = FHIR_primitive_URIField(null=True, blank=True, )

class FHIR_ValueSet_expansion_contains(models.Model):
    ValueSet_expansion = models.ForeignKey(FHIR_ValueSet_expansion, related_name='ValueSet_expansion_contains', null=False, on_delete=models.CASCADE)
    system = FHIR_primitive_URIField(null=True, blank=True, )
    abstract = FHIR_primitive_BooleanField(null=True, blank=True, )
    inactive = FHIR_primitive_BooleanField(null=True, blank=True, )
    version = FHIR_primitive_StringField(null=True, blank=True, )
    class CodeChoices(models.TextChoices): CODE___IF_BLANK,_THIS_IS_NOT_A_SELECTABLE_CODE = 'Code - if blank, this is not a selectable code', 'Code - if blank, this is not a selectable code'; 
    code = FHIR_primitive_CodeField(choices=CodeChoices.choices, null=True, blank=True, )
    display = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_ValueSet_expansion_contains_property(models.Model):
    ValueSet_expansion_contains = models.ForeignKey(FHIR_ValueSet_expansion_contains, related_name='ValueSet_expansion_contains_property', null=False, on_delete=models.CASCADE)
    class CodeChoices(models.TextChoices): REFERENCE_TO_VALUESET.EXPANSION.PROPERTY.CODE = 'Reference to ValueSet.expansion.property.code', 'Reference to valueset.expansion.property.code'; 
    code = FHIR_primitive_CodeField(choices=CodeChoices.choices, null=True, blank=True, )
    class ValueChoices(models.TextChoices): VALUE_OF_THE_PROPERTY_FOR_THIS_CONCEPT = 'Value of the property for this concept', 'Value of the property for this concept'; 
    value = FHIR_primitive_CodeField(choices=ValueChoices.choices, null=True, blank=True, )
    value = models.OneToOneField("FHIR_GP_Coding", related_name='ValueSet_expansion_contains_property_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = FHIR_primitive_StringField(null=True, blank=True, )
    value = FHIR_primitive_BooleanField(null=True, blank=True, )
    value = FHIR_primitive_DateTimeField(null=True, blank=True, )
    value = FHIR_primitive_DecimalField(null=True, blank=True, )

class FHIR_ValueSet_expansion_contains_property_subProperty(models.Model):
    ValueSet_expansion_contains_property = models.ForeignKey(FHIR_ValueSet_expansion_contains_property, related_name='ValueSet_expansion_contains_property_subProperty', null=False, on_delete=models.CASCADE)
    class CodeChoices(models.TextChoices): REFERENCE_TO_VALUESET.EXPANSION.PROPERTY.CODE = 'Reference to ValueSet.expansion.property.code', 'Reference to valueset.expansion.property.code'; 
    code = FHIR_primitive_CodeField(choices=CodeChoices.choices, null=True, blank=True, )
    class ValueChoices(models.TextChoices): VALUE_OF_THE_SUBPROPERTY_FOR_THIS_CONCEPT = 'Value of the subproperty for this concept', 'Value of the subproperty for this concept'; 
    value = FHIR_primitive_CodeField(choices=ValueChoices.choices, null=True, blank=True, )
    value = models.OneToOneField("FHIR_GP_Coding", related_name='ValueSet_expansion_contains_property_subProperty_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = FHIR_primitive_StringField(null=True, blank=True, )
    value = FHIR_primitive_BooleanField(null=True, blank=True, )
    value = FHIR_primitive_DateTimeField(null=True, blank=True, )
    value = FHIR_primitive_DecimalField(null=True, blank=True, )

class FHIR_ValueSet_scope(models.Model):
    ValueSet = models.ForeignKey(FHIR_ValueSet, related_name='ValueSet_scope', null=False, on_delete=models.CASCADE)
    inclusionCriteria = FHIR_primitive_MarkdownField(null=True, blank=True, )
    exclusionCriteria = FHIR_primitive_MarkdownField(null=True, blank=True, )
