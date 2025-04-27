#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_SearchParameter(models.Model):
    url = FHIR_primitive_URIField(null=True, blank=True, )
    version = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm_string = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm_Coding = models.OneToOneField("FHIR_GP_Coding", related_name='SearchParameter_versionAlgorithm_Coding', null=True, blank=True, on_delete=models.SET_NULL)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    title = FHIR_primitive_StringField(null=True, blank=True, )
    derivedFrom = FHIR_primitive_CanonicalField(null=True, blank=True, )
    class StatusChoices(models.TextChoices): DRAFT = 'draft', 'Draft'; ACTIVE = 'active', 'Active'; RETIRED = 'retired', 'Retired'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    experimental = FHIR_primitive_BooleanField(null=True, blank=True, )
    date = FHIR_primitive_DateTimeField(null=True, blank=True, )
    publisher = FHIR_primitive_StringField(null=True, blank=True, )
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    purpose = FHIR_primitive_MarkdownField(null=True, blank=True, )
    copyright = FHIR_primitive_MarkdownField(null=True, blank=True, )
    copyrightLabel = FHIR_primitive_StringField(null=True, blank=True, )
    class CodeChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    code = FHIR_primitive_CodeField(choices=CodeChoices.choices, null=True, blank=True, )
    class TypeChoices(models.TextChoices): NUMBER = 'number', 'Number'; DATE = 'date', 'Date'; STRING = 'string', 'String'; TOKEN = 'token', 'Token'; REFERENCE = 'reference', 'Reference'; COMPOSITE = 'composite', 'Composite'; QUANTITY = 'quantity', 'Quantity'; URI = 'uri', 'Uri'; SPECIAL = 'special', 'Special'; RESOURCE = 'resource', 'Resource'; 
    type = FHIR_primitive_CodeField(choices=TypeChoices.choices, null=True, blank=True, )
    expression = FHIR_primitive_StringField(null=True, blank=True, )
    class ProcessingmodeChoices(models.TextChoices): NORMAL = 'normal', 'Normal'; PHONETIC = 'phonetic', 'Phonetic'; OTHER = 'other', 'Other'; 
    processingMode = FHIR_primitive_CodeField(choices=ProcessingmodeChoices.choices, null=True, blank=True, )
    constraint = FHIR_primitive_StringField(null=True, blank=True, )
    multipleOr = FHIR_primitive_BooleanField(null=True, blank=True, )
    multipleAnd = FHIR_primitive_BooleanField(null=True, blank=True, )

class FHIR_SearchParameter_identifier(FHIR_GP_Identifier):
    SearchParameter = models.ForeignKey(FHIR_SearchParameter, related_name='SearchParameter_identifier', null=False, on_delete=models.CASCADE)

class FHIR_SearchParameter_jurisdiction(models.Model):
    SearchParameter = models.ForeignKey(FHIR_SearchParameter, related_name='SearchParameter_jurisdiction', null=False, on_delete=models.CASCADE)
    BINDING_jurisdiction = "TODO"
    jurisdiction_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_jurisdiction}, related_name='SearchParameter_jurisdiction', blank=True)
    jurisdiction_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_SearchParameter_aliasCode(models.Model):
    SearchParameter = models.ForeignKey(FHIR_SearchParameter, related_name='SearchParameter_aliasCode', null=False, on_delete=models.CASCADE)
    
    class AliascodeChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    aliasCode = FHIR_primitive_CodeField(choices=AliascodeChoices.choices, null=True, blank=True, )
    
class FHIR_SearchParameter_base(models.Model):
    SearchParameter = models.ForeignKey(FHIR_SearchParameter, related_name='SearchParameter_base', null=False, on_delete=models.CASCADE)
    
    class BaseChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    base = FHIR_primitive_CodeField(choices=BaseChoices.choices, null=True, blank=True, )
    
class FHIR_SearchParameter_target(models.Model):
    SearchParameter = models.ForeignKey(FHIR_SearchParameter, related_name='SearchParameter_target', null=False, on_delete=models.CASCADE)
    
    class TargetChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    target = FHIR_primitive_CodeField(choices=TargetChoices.choices, null=True, blank=True, )
    
class FHIR_SearchParameter_comparator(models.Model):
    SearchParameter = models.ForeignKey(FHIR_SearchParameter, related_name='SearchParameter_comparator', null=False, on_delete=models.CASCADE)
    
    class ComparatorChoices(models.TextChoices): EQ = 'eq', 'Eq'; NE = 'ne', 'Ne'; GT = 'gt', 'Gt'; LT = 'lt', 'Lt'; GE = 'ge', 'Ge'; LE = 'le', 'Le'; SA = 'sa', 'Sa'; EB = 'eb', 'Eb'; AP = 'ap', 'Ap'; 
    comparator = FHIR_primitive_CodeField(choices=ComparatorChoices.choices, null=True, blank=True, )
    
class FHIR_SearchParameter_modifier(models.Model):
    SearchParameter = models.ForeignKey(FHIR_SearchParameter, related_name='SearchParameter_modifier', null=False, on_delete=models.CASCADE)
    
    class ModifierChoices(models.TextChoices): MISSING = 'missing', 'Missing'; EXACT = 'exact', 'Exact'; CONTAINS = 'contains', 'Contains'; NOT = 'not', 'Not'; TEXT = 'text', 'Text'; IN = 'in', 'In'; NOT_IN = 'not-in', 'Not-in'; BELOW = 'below', 'Below'; ABOVE = 'above', 'Above'; TYPE = 'type', 'Type'; IDENTIFIER = 'identifier', 'Identifier'; OF_TYPE = 'of-type', 'Of-type'; CODE_TEXT = 'code-text', 'Code-text'; TEXT_ADVANCED = 'text-advanced', 'Text-advanced'; ITERATE = 'iterate', 'Iterate'; 
    modifier = FHIR_primitive_CodeField(choices=ModifierChoices.choices, null=True, blank=True, )
    
class FHIR_SearchParameter_chain(models.Model):
    SearchParameter = models.ForeignKey(FHIR_SearchParameter, related_name='SearchParameter_chain', null=False, on_delete=models.CASCADE)
    
    chain = FHIR_primitive_StringField(null=True, blank=True, )
    
class FHIR_SearchParameter_component(models.Model):
    SearchParameter = models.ForeignKey(FHIR_SearchParameter, related_name='SearchParameter_component', null=False, on_delete=models.CASCADE)
    definition = FHIR_primitive_CanonicalField(null=True, blank=True, )
    expression = FHIR_primitive_StringField(null=True, blank=True, )
