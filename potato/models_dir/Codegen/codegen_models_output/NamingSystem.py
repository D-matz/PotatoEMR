#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_NamingSystem(models.Model):
    url = FHIR_primitive_URIField(null=True, blank=True, )
    version = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = models.OneToOneField("FHIR_GP_Coding", related_name='NamingSystem_versionAlgorithm', null=True, blank=True, on_delete=models.SET_NULL)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    title = FHIR_primitive_StringField(null=True, blank=True, )
    class StatusChoices(models.TextChoices): DRAFT = 'draft', 'Draft'; ACTIVE = 'active', 'Active'; RETIRED = 'retired', 'Retired'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    class KindChoices(models.TextChoices): CODESYSTEM = 'codesystem', 'Codesystem'; IDENTIFIER = 'identifier', 'Identifier'; ROOT = 'root', 'Root'; 
    kind = FHIR_primitive_CodeField(choices=KindChoices.choices, null=True, blank=True, )
    experimental = FHIR_primitive_BooleanField(null=True, blank=True, )
    date = FHIR_primitive_DateTimeField(null=True, blank=True, )
    publisher = FHIR_primitive_StringField(null=True, blank=True, )
    responsible = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='NamingSystem_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    purpose = FHIR_primitive_MarkdownField(null=True, blank=True, )
    copyright = FHIR_primitive_MarkdownField(null=True, blank=True, )
    copyrightLabel = FHIR_primitive_StringField(null=True, blank=True, )
    approvalDate = FHIR_primitive_DateField(null=True, blank=True, )
    lastReviewDate = FHIR_primitive_DateField(null=True, blank=True, )
    effectivePeriod = models.OneToOneField("FHIR_GP_Period", related_name='NamingSystem_effectivePeriod', null=True, blank=True, on_delete=models.SET_NULL)
    usage = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_NamingSystem_identifier(FHIR_GP_Identifier):
    NamingSystem = models.ForeignKey(FHIR_NamingSystem, related_name='NamingSystem_identifier', null=False, on_delete=models.CASCADE)

class FHIR_NamingSystem_jurisdiction(models.Model):
    NamingSystem = models.ForeignKey(FHIR_NamingSystem, related_name='NamingSystem_jurisdiction', null=False, on_delete=models.CASCADE)
    BINDING_jurisdiction = "TODO"
    jurisdiction_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_jurisdiction}, related_name='NamingSystem_jurisdiction', blank=True)
    jurisdiction_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_NamingSystem_topic(models.Model):
    NamingSystem = models.ForeignKey(FHIR_NamingSystem, related_name='NamingSystem_topic', null=False, on_delete=models.CASCADE)
    BINDING_topic = "TODO"
    topic_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_topic}, related_name='NamingSystem_topic', blank=True)
    topic_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_NamingSystem_uniqueId(models.Model):
    NamingSystem = models.ForeignKey(FHIR_NamingSystem, related_name='NamingSystem_uniqueId', null=False, on_delete=models.CASCADE)
    class TypeChoices(models.TextChoices): OID = 'oid', 'Oid'; UUID = 'uuid', 'Uuid'; URI = 'uri', 'Uri'; IRI_STEM = 'iri-stem', 'Iri-stem'; V2CSMNEMONIC = 'v2csmnemonic', 'V2csmnemonic'; OTHER = 'other', 'Other'; 
    type = FHIR_primitive_CodeField(choices=TypeChoices.choices, null=True, blank=True, )
    value = FHIR_primitive_StringField(null=True, blank=True, )
    preferred = FHIR_primitive_BooleanField(null=True, blank=True, )
    comment = FHIR_primitive_StringField(null=True, blank=True, )
    period = models.OneToOneField("FHIR_GP_Period", related_name='NamingSystem_uniqueId_period', null=True, blank=True, on_delete=models.SET_NULL)
    authoritative = FHIR_primitive_BooleanField(null=True, blank=True, )
