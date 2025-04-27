#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_MessageDefinition(models.Model):
    url = FHIR_primitive_URIField(null=True, blank=True, )
    version = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = models.OneToOneField("FHIR_GP_Coding", related_name='MessageDefinition_versionAlgorithm', null=True, blank=True, on_delete=models.SET_NULL)
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
    base = FHIR_primitive_CanonicalField(null=True, blank=True, )
    event = models.OneToOneField("FHIR_GP_Coding", related_name='MessageDefinition_event', null=True, blank=True, on_delete=models.SET_NULL)
    event = FHIR_primitive_URIField(null=True, blank=True, )
    class CategoryChoices(models.TextChoices): CONSEQUENCE = 'consequence', 'Consequence'; CURRENCY = 'currency', 'Currency'; NOTIFICATION = 'notification', 'Notification'; 
    category = FHIR_primitive_CodeField(choices=CategoryChoices.choices, null=True, blank=True, )
    class ResponserequiredChoices(models.TextChoices): ALWAYS = 'always', 'Always'; ON_ERROR = 'on-error', 'On-error'; NEVER = 'never', 'Never'; ON_SUCCESS = 'on-success', 'On-success'; 
    responseRequired = FHIR_primitive_CodeField(choices=ResponserequiredChoices.choices, null=True, blank=True, )
    graph = FHIR_primitive_CanonicalField(null=True, blank=True, )

class FHIR_MessageDefinition_identifier(FHIR_GP_Identifier):
    MessageDefinition = models.ForeignKey(FHIR_MessageDefinition, related_name='MessageDefinition_identifier', null=False, on_delete=models.CASCADE)

class FHIR_MessageDefinition_replaces(models.Model):
    MessageDefinition = models.ForeignKey(FHIR_MessageDefinition, related_name='MessageDefinition_replaces', null=False, on_delete=models.CASCADE)
    
    replaces = FHIR_primitive_CanonicalField(null=True, blank=True, )
    
class FHIR_MessageDefinition_jurisdiction(models.Model):
    MessageDefinition = models.ForeignKey(FHIR_MessageDefinition, related_name='MessageDefinition_jurisdiction', null=False, on_delete=models.CASCADE)
    BINDING_jurisdiction = 'TODO'
    jurisdiction_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_jurisdiction}, related_name='MessageDefinition_jurisdiction', blank=True)
    jurisdiction_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_MessageDefinition_parent(models.Model):
    MessageDefinition = models.ForeignKey(FHIR_MessageDefinition, related_name='MessageDefinition_parent', null=False, on_delete=models.CASCADE)
    
    parent = FHIR_primitive_CanonicalField(null=True, blank=True, )
    
class FHIR_MessageDefinition_focus(models.Model):
    MessageDefinition = models.ForeignKey(FHIR_MessageDefinition, related_name='MessageDefinition_focus', null=False, on_delete=models.CASCADE)
    class CodeChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    code = FHIR_primitive_CodeField(choices=CodeChoices.choices, null=True, blank=True, )
    profile = FHIR_primitive_CanonicalField(null=True, blank=True, )
    min = FHIR_primitive_UnsignedIntField(null=True, blank=True, )
    max = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_MessageDefinition_allowedResponse(models.Model):
    MessageDefinition = models.ForeignKey(FHIR_MessageDefinition, related_name='MessageDefinition_allowedResponse', null=False, on_delete=models.CASCADE)
    message = FHIR_primitive_CanonicalField(null=True, blank=True, )
    situation = FHIR_primitive_MarkdownField(null=True, blank=True, )
