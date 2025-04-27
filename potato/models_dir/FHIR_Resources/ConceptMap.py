#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_ConceptMap(models.Model):
    url = FHIR_primitive_URIField(null=True, blank=True, )
    version = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = models.OneToOneField("FHIR_GP_Coding", related_name='ConceptMap_versionAlgorithm', null=True, blank=True, on_delete=models.SET_NULL)
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
    effectivePeriod = models.OneToOneField("FHIR_GP_Period", related_name='ConceptMap_effectivePeriod', null=True, blank=True, on_delete=models.SET_NULL)
    sourceScope = FHIR_primitive_URIField(null=True, blank=True, )
    sourceScope = FHIR_primitive_CanonicalField(null=True, blank=True, )
    targetScope = FHIR_primitive_URIField(null=True, blank=True, )
    targetScope = FHIR_primitive_CanonicalField(null=True, blank=True, )

class FHIR_ConceptMap_identifier(FHIR_GP_Identifier):
    ConceptMap = models.ForeignKey(FHIR_ConceptMap, related_name='ConceptMap_identifier', null=False, on_delete=models.CASCADE)

class FHIR_ConceptMap_jurisdiction(models.Model):
    ConceptMap = models.ForeignKey(FHIR_ConceptMap, related_name='ConceptMap_jurisdiction', null=False, on_delete=models.CASCADE)
    BINDING_jurisdiction = 'TODO'
    jurisdiction_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_jurisdiction}, related_name='ConceptMap_jurisdiction', blank=True)
    jurisdiction_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ConceptMap_topic(models.Model):
    ConceptMap = models.ForeignKey(FHIR_ConceptMap, related_name='ConceptMap_topic', null=False, on_delete=models.CASCADE)
    BINDING_topic = 'TODO'
    topic_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_topic}, related_name='ConceptMap_topic', blank=True)
    topic_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ConceptMap_property(models.Model):
    ConceptMap = models.ForeignKey(FHIR_ConceptMap, related_name='ConceptMap_property', null=False, on_delete=models.CASCADE)
    class CodeChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    code = FHIR_primitive_CodeField(choices=CodeChoices.choices, null=True, blank=True, )
    uri = FHIR_primitive_URIField(null=True, blank=True, )
    description = FHIR_primitive_StringField(null=True, blank=True, )
    class TypeChoices(models.TextChoices): CODING = 'Coding', 'Coding'; STRING = 'string', 'String'; INTEGER = 'integer', 'Integer'; BOOLEAN = 'boolean', 'Boolean'; DATETIME = 'dateTime', 'Datetime'; DECIMAL = 'decimal', 'Decimal'; CODE = 'code', 'Code'; 
    type = FHIR_primitive_CodeField(choices=TypeChoices.choices, null=True, blank=True, )
    system = FHIR_primitive_CanonicalField(null=True, blank=True, )

class FHIR_ConceptMap_additionalAttribute(models.Model):
    ConceptMap = models.ForeignKey(FHIR_ConceptMap, related_name='ConceptMap_additionalAttribute', null=False, on_delete=models.CASCADE)
    class CodeChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    code = FHIR_primitive_CodeField(choices=CodeChoices.choices, null=True, blank=True, )
    uri = FHIR_primitive_URIField(null=True, blank=True, )
    description = FHIR_primitive_StringField(null=True, blank=True, )
    class TypeChoices(models.TextChoices): CODE = 'code', 'Code'; CODING = 'Coding', 'Coding'; STRING = 'string', 'String'; BOOLEAN = 'boolean', 'Boolean'; QUANTITY = 'Quantity', 'Quantity'; 
    type = FHIR_primitive_CodeField(choices=TypeChoices.choices, null=True, blank=True, )

class FHIR_ConceptMap_group(models.Model):
    ConceptMap = models.ForeignKey(FHIR_ConceptMap, related_name='ConceptMap_group', null=False, on_delete=models.CASCADE)
    source = FHIR_primitive_CanonicalField(null=True, blank=True, )
    target = FHIR_primitive_CanonicalField(null=True, blank=True, )

class FHIR_ConceptMap_group_element(models.Model):
    ConceptMap_group = models.ForeignKey(FHIR_ConceptMap_group, related_name='ConceptMap_group_element', null=False, on_delete=models.CASCADE)
    class CodeChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    code = FHIR_primitive_CodeField(choices=CodeChoices.choices, null=True, blank=True, )
    display = FHIR_primitive_StringField(null=True, blank=True, )
    valueSet = FHIR_primitive_CanonicalField(null=True, blank=True, )
    noMap = FHIR_primitive_BooleanField(null=True, blank=True, )

class FHIR_ConceptMap_group_element_target(models.Model):
    ConceptMap_group_element = models.ForeignKey(FHIR_ConceptMap_group_element, related_name='ConceptMap_group_element_target', null=False, on_delete=models.CASCADE)
    class CodeChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    code = FHIR_primitive_CodeField(choices=CodeChoices.choices, null=True, blank=True, )
    display = FHIR_primitive_StringField(null=True, blank=True, )
    valueSet = FHIR_primitive_CanonicalField(null=True, blank=True, )
    class RelationshipChoices(models.TextChoices): RELATED_TO = 'related-to', 'Related-to'; EQUIVALENT = 'equivalent', 'Equivalent'; SOURCE_IS_NARROWER_THAN_TARGET = 'source-is-narrower-than-target', 'Source-is-narrower-than-target'; SOURCE_IS_BROADER_THAN_TARGET = 'source-is-broader-than-target', 'Source-is-broader-than-target'; NOT_RELATED_TO = 'not-related-to', 'Not-related-to'; 
    relationship = FHIR_primitive_CodeField(choices=RelationshipChoices.choices, null=True, blank=True, )
    comment = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_ConceptMap_group_element_target_property(models.Model):
    ConceptMap_group_element_target = models.ForeignKey(FHIR_ConceptMap_group_element_target, related_name='ConceptMap_group_element_target_property', null=False, on_delete=models.CASCADE)
    class CodeChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    code = FHIR_primitive_CodeField(choices=CodeChoices.choices, null=True, blank=True, )
    value = models.OneToOneField("FHIR_GP_Coding", related_name='ConceptMap_group_element_target_property_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = FHIR_primitive_StringField(null=True, blank=True, )
    value = FHIR_primitive_BooleanField(null=True, blank=True, )
    value = FHIR_primitive_DateTimeField(null=True, blank=True, )
    value = FHIR_primitive_DecimalField(null=True, blank=True, )
    class ValueChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    value = FHIR_primitive_CodeField(choices=ValueChoices.choices, null=True, blank=True, )

class FHIR_ConceptMap_group_element_target_dependsOn(models.Model):
    ConceptMap_group_element_target = models.ForeignKey(FHIR_ConceptMap_group_element_target, related_name='ConceptMap_group_element_target_dependsOn', null=False, on_delete=models.CASCADE)
    class AttributeChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    attribute = FHIR_primitive_CodeField(choices=AttributeChoices.choices, null=True, blank=True, )
    class ValueChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    value = FHIR_primitive_CodeField(choices=ValueChoices.choices, null=True, blank=True, )
    value = models.OneToOneField("FHIR_GP_Coding", related_name='ConceptMap_group_element_target_dependsOn_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = FHIR_primitive_StringField(null=True, blank=True, )
    value = FHIR_primitive_BooleanField(null=True, blank=True, )
    value = models.OneToOneField("FHIR_GP_Quantity", related_name='ConceptMap_group_element_target_dependsOn_value', null=True, blank=True, on_delete=models.SET_NULL)
    valueSet = FHIR_primitive_CanonicalField(null=True, blank=True, )

class FHIR_ConceptMap_group_unmapped(models.Model):
    ConceptMap_group = models.ForeignKey(FHIR_ConceptMap_group, related_name='ConceptMap_group_unmapped', null=False, on_delete=models.CASCADE)
    class ModeChoices(models.TextChoices): USE_SOURCE_CODE = 'use-source-code', 'Use-source-code'; FIXED = 'fixed', 'Fixed'; OTHER_MAP = 'other-map', 'Other-map'; 
    mode = FHIR_primitive_CodeField(choices=ModeChoices.choices, null=True, blank=True, )
    class CodeChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    code = FHIR_primitive_CodeField(choices=CodeChoices.choices, null=True, blank=True, )
    display = FHIR_primitive_StringField(null=True, blank=True, )
    valueSet = FHIR_primitive_CanonicalField(null=True, blank=True, )
    class RelationshipChoices(models.TextChoices): RELATED_TO = 'related-to', 'Related-to'; EQUIVALENT = 'equivalent', 'Equivalent'; SOURCE_IS_NARROWER_THAN_TARGET = 'source-is-narrower-than-target', 'Source-is-narrower-than-target'; SOURCE_IS_BROADER_THAN_TARGET = 'source-is-broader-than-target', 'Source-is-broader-than-target'; NOT_RELATED_TO = 'not-related-to', 'Not-related-to'; 
    relationship = FHIR_primitive_CodeField(choices=RelationshipChoices.choices, null=True, blank=True, )
    otherMap = FHIR_primitive_CanonicalField(null=True, blank=True, )
