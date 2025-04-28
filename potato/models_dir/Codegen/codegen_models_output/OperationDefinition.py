#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_OperationDefinition(models.Model):
    url = FHIR_primitive_URIField(null=True, blank=True, )
    version = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm_string = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm_Coding = models.OneToOneField("FHIR_GP_Coding", related_name='OperationDefinition_versionAlgorithm_Coding', null=True, blank=True, on_delete=models.SET_NULL)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    title = FHIR_primitive_StringField(null=True, blank=True, )
    class StatusChoices(models.TextChoices): DRAFT = 'draft', 'Draft'; ACTIVE = 'active', 'Active'; RETIRED = 'retired', 'Retired'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    class KindChoices(models.TextChoices): OPERATION = 'operation', 'Operation'; QUERY = 'query', 'Query'; 
    kind = FHIR_primitive_CodeField(choices=KindChoices.choices, null=True, blank=True, )
    experimental = FHIR_primitive_BooleanField(null=True, blank=True, )
    date = FHIR_primitive_DateTimeField(null=True, blank=True, )
    publisher = FHIR_primitive_StringField(null=True, blank=True, )
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    purpose = FHIR_primitive_MarkdownField(null=True, blank=True, )
    copyright = FHIR_primitive_MarkdownField(null=True, blank=True, )
    copyrightLabel = FHIR_primitive_StringField(null=True, blank=True, )
    affectsState = FHIR_primitive_BooleanField(null=True, blank=True, )
    class SynchronicityChoices(models.TextChoices): SYNCHRONOUS = 'synchronous', 'Synchronous'; ASYNCHRONOUS = 'asynchronous', 'Asynchronous'; EITHER = 'either', 'Either'; 
    synchronicity = FHIR_primitive_CodeField(choices=SynchronicityChoices.choices, null=True, blank=True, )
    class CodeChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    code = FHIR_primitive_CodeField(choices=CodeChoices.choices, null=True, blank=True, )
    comment = FHIR_primitive_MarkdownField(null=True, blank=True, )
    base = FHIR_primitive_CanonicalField(null=True, blank=True, )
    system = FHIR_primitive_BooleanField(null=True, blank=True, )
    type = FHIR_primitive_BooleanField(null=True, blank=True, )
    instance = FHIR_primitive_BooleanField(null=True, blank=True, )
    inputProfile = FHIR_primitive_CanonicalField(null=True, blank=True, )
    outputProfile = FHIR_primitive_CanonicalField(null=True, blank=True, )

class FHIR_OperationDefinition_identifier(FHIR_GP_Identifier):
    OperationDefinition = models.ForeignKey(FHIR_OperationDefinition, related_name='OperationDefinition_identifier', null=False, on_delete=models.CASCADE)

class FHIR_OperationDefinition_jurisdiction(models.Model):
    OperationDefinition = models.ForeignKey(FHIR_OperationDefinition, related_name='OperationDefinition_jurisdiction', null=False, on_delete=models.CASCADE)
    BINDING_jurisdiction = "TODO"
    jurisdiction_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_jurisdiction}, related_name='OperationDefinition_jurisdiction', blank=True)
    jurisdiction_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_OperationDefinition_resource(models.Model):
    OperationDefinition = models.ForeignKey(FHIR_OperationDefinition, related_name='OperationDefinition_resource', null=False, on_delete=models.CASCADE)
    
    class ResourceChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    resource = FHIR_primitive_CodeField(choices=ResourceChoices.choices, null=True, blank=True, )
    
class FHIR_OperationDefinition_parameter(models.Model):
    OperationDefinition = models.ForeignKey(FHIR_OperationDefinition, related_name='OperationDefinition_parameter', null=False, on_delete=models.CASCADE)
    class NameChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    name = FHIR_primitive_CodeField(choices=NameChoices.choices, null=True, blank=True, )
    class UseChoices(models.TextChoices): IN = 'in', 'In'; OUT = 'out', 'Out'; 
    use = FHIR_primitive_CodeField(choices=UseChoices.choices, null=True, blank=True, )
    min = FHIR_primitive_UnsignedIntField(null=True, blank=True, )
    max = FHIR_primitive_StringField(null=True, blank=True, )
    documentation = FHIR_primitive_MarkdownField(null=True, blank=True, )
    class TypeChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    type = FHIR_primitive_CodeField(choices=TypeChoices.choices, null=True, blank=True, )
    class SearchtypeChoices(models.TextChoices): NUMBER = 'number', 'Number'; DATE = 'date', 'Date'; STRING = 'string', 'String'; TOKEN = 'token', 'Token'; REFERENCE = 'reference', 'Reference'; COMPOSITE = 'composite', 'Composite'; QUANTITY = 'quantity', 'Quantity'; URI = 'uri', 'Uri'; SPECIAL = 'special', 'Special'; RESOURCE = 'resource', 'Resource'; 
    searchType = FHIR_primitive_CodeField(choices=SearchtypeChoices.choices, null=True, blank=True, )

class FHIR_OperationDefinition_parameter_scope(models.Model):
    OperationDefinition_parameter = models.ForeignKey(FHIR_OperationDefinition_parameter, related_name='OperationDefinition_parameter_scope', null=False, on_delete=models.CASCADE)
    
    class ScopeChoices(models.TextChoices): INSTANCE = 'instance', 'Instance'; TYPE = 'type', 'Type'; SYSTEM = 'system', 'System'; 
    scope = FHIR_primitive_CodeField(choices=ScopeChoices.choices, null=True, blank=True, )
    
class FHIR_OperationDefinition_parameter_allowedType(models.Model):
    OperationDefinition_parameter = models.ForeignKey(FHIR_OperationDefinition_parameter, related_name='OperationDefinition_parameter_allowedType', null=False, on_delete=models.CASCADE)
    
    class AllowedtypeChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    allowedType = FHIR_primitive_CodeField(choices=AllowedtypeChoices.choices, null=True, blank=True, )
    
class FHIR_OperationDefinition_parameter_targetProfile(models.Model):
    OperationDefinition_parameter = models.ForeignKey(FHIR_OperationDefinition_parameter, related_name='OperationDefinition_parameter_targetProfile', null=False, on_delete=models.CASCADE)
    
    targetProfile = FHIR_primitive_CanonicalField(null=True, blank=True, )
    
class FHIR_OperationDefinition_parameter_binding(models.Model):
    OperationDefinition_parameter = models.ForeignKey(FHIR_OperationDefinition_parameter, related_name='OperationDefinition_parameter_binding', null=False, on_delete=models.CASCADE)
    class StrengthChoices(models.TextChoices): REQUIRED = 'required', 'Required'; EXTENSIBLE = 'extensible', 'Extensible'; PREFERRED = 'preferred', 'Preferred'; EXAMPLE = 'example', 'Example'; DESCRIPTIVE = 'descriptive', 'Descriptive'; 
    strength = FHIR_primitive_CodeField(choices=StrengthChoices.choices, null=True, blank=True, )
    valueSet = FHIR_primitive_CanonicalField(null=True, blank=True, )

class FHIR_OperationDefinition_parameter_referencedFrom(models.Model):
    OperationDefinition_parameter = models.ForeignKey(FHIR_OperationDefinition_parameter, related_name='OperationDefinition_parameter_referencedFrom', null=False, on_delete=models.CASCADE)
    source = FHIR_primitive_StringField(null=True, blank=True, )
    sourceId = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_OperationDefinition_overload(models.Model):
    OperationDefinition = models.ForeignKey(FHIR_OperationDefinition, related_name='OperationDefinition_overload', null=False, on_delete=models.CASCADE)
    comment = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_OperationDefinition_overload_parameterName(models.Model):
    OperationDefinition_overload = models.ForeignKey(FHIR_OperationDefinition_overload, related_name='OperationDefinition_overload_parameterName', null=False, on_delete=models.CASCADE)
    
    parameterName = FHIR_primitive_StringField(null=True, blank=True, )
    