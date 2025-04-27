#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_StructureDefinition(models.Model):
    url = FHIR_primitive_URIField(null=True, blank=True, )
    version = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = models.OneToOneField("FHIR_GP_Coding", related_name='StructureDefinition_versionAlgorithm', null=True, blank=True, on_delete=models.SET_NULL)
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
    class FhirversionChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    fhirVersion = FHIR_primitive_CodeField(choices=FhirversionChoices.choices, null=True, blank=True, )
    class KindChoices(models.TextChoices): PRIMITIVE_TYPE = 'primitive-type', 'Primitive-type'; COMPLEX_TYPE = 'complex-type', 'Complex-type'; RESOURCE = 'resource', 'Resource'; LOGICAL = 'logical', 'Logical'; 
    kind = FHIR_primitive_CodeField(choices=KindChoices.choices, null=True, blank=True, )
    abstract = FHIR_primitive_BooleanField(null=True, blank=True, )
    type = FHIR_primitive_URIField(null=True, blank=True, )
    baseDefinition = FHIR_primitive_CanonicalField(null=True, blank=True, )
    class DerivationChoices(models.TextChoices): SPECIALIZATION = 'specialization', 'Specialization'; CONSTRAINT___HOW_RELATES_TO_BASE_DEFINITION = 'constraint - How relates to base definition', 'Constraint - how relates to base definition'; 
    derivation = FHIR_primitive_CodeField(choices=DerivationChoices.choices, null=True, blank=True, )

class FHIR_StructureDefinition_identifier(FHIR_GP_Identifier):
    StructureDefinition = models.ForeignKey(FHIR_StructureDefinition, related_name='StructureDefinition_identifier', null=False, on_delete=models.CASCADE)

class FHIR_StructureDefinition_jurisdiction(models.Model):
    StructureDefinition = models.ForeignKey(FHIR_StructureDefinition, related_name='StructureDefinition_jurisdiction', null=False, on_delete=models.CASCADE)
    BINDING_jurisdiction = 'TODO'
    jurisdiction_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_jurisdiction}, related_name='StructureDefinition_jurisdiction', blank=True)
    jurisdiction_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_StructureDefinition_keyword(FHIR_GP_Coding):
    StructureDefinition = models.ForeignKey(FHIR_StructureDefinition, related_name='StructureDefinition_keyword', null=False, on_delete=models.CASCADE)

class FHIR_StructureDefinition_mapping(models.Model):
    StructureDefinition = models.ForeignKey(FHIR_StructureDefinition, related_name='StructureDefinition_mapping', null=False, on_delete=models.CASCADE)
    identity = FHIR_primitive_IdField(null=True, blank=True, )
    uri = FHIR_primitive_URIField(null=True, blank=True, )
    name = FHIR_primitive_StringField(null=True, blank=True, )
    comment = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_StructureDefinition_context(models.Model):
    StructureDefinition = models.ForeignKey(FHIR_StructureDefinition, related_name='StructureDefinition_context', null=False, on_delete=models.CASCADE)
    class TypeChoices(models.TextChoices): FHIRPATH = 'fhirpath', 'Fhirpath'; ELEMENT = 'element', 'Element'; EXTENSION = 'extension', 'Extension'; 
    type = FHIR_primitive_CodeField(choices=TypeChoices.choices, null=True, blank=True, )
    expression = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_StructureDefinition_contextInvariant(models.Model):
    StructureDefinition = models.ForeignKey(FHIR_StructureDefinition, related_name='StructureDefinition_contextInvariant', null=False, on_delete=models.CASCADE)
    
    contextInvariant = FHIR_primitive_StringField(null=True, blank=True, )
    
class FHIR_StructureDefinition_snapshot(models.Model):
    StructureDefinition = models.ForeignKey(FHIR_StructureDefinition, related_name='StructureDefinition_snapshot', null=False, on_delete=models.CASCADE)

class FHIR_StructureDefinition_differential(models.Model):
    StructureDefinition = models.ForeignKey(FHIR_StructureDefinition, related_name='StructureDefinition_differential', null=False, on_delete=models.CASCADE)
