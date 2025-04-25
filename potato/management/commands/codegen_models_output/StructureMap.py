
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_StructureMap(models.Model):
    url = FHIR_primitive_URIField(null=True, blank=True, )
    version = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = models.OneToOneField("FHIR_GP_Coding", related_name='StructureMap_versionAlgorithm', null=True, blank=True, on_delete=models.SET_NULL)
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

class FHIR_StructureMap_identifier(FHIR_GP_Identifier):
    StructureMap = models.ForeignKey(FHIR_StructureMap, related_name='StructureMap_identifier', null=False, on_delete=models.CASCADE)

class FHIR_StructureMap_jurisdiction(models.Model):
    StructureMap = models.ForeignKey(FHIR_StructureMap, related_name='StructureMap_jurisdiction', null=False, on_delete=models.CASCADE)
    BINDING_jurisdiction = 'TODO'
    jurisdiction_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_jurisdiction}, related_name='StructureMap_jurisdiction', blank=True)
    jurisdiction_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_StructureMap_structure(models.Model):
    StructureMap = models.ForeignKey(FHIR_StructureMap, related_name='StructureMap_structure', null=False, on_delete=models.CASCADE)
    url = FHIR_primitive_CanonicalField(null=True, blank=True, )
    class ModeChoices(models.TextChoices): SOURCE = 'source', 'Source'; QUERIED = 'queried', 'Queried'; TARGET = 'target', 'Target'; PRODUCED = 'produced', 'Produced'; 
    mode = FHIR_primitive_CodeField(choices=ModeChoices.choices, null=True, blank=True, )
    alias = FHIR_primitive_StringField(null=True, blank=True, )
    documentation = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_StructureMap_import(models.Model):
    StructureMap = models.ForeignKey(FHIR_StructureMap, related_name='StructureMap_import', null=False, on_delete=models.CASCADE)
    
    import = FHIR_primitive_CanonicalField(null=True, blank=True, )
    
class FHIR_StructureMap_const(models.Model):
    StructureMap = models.ForeignKey(FHIR_StructureMap, related_name='StructureMap_const', null=False, on_delete=models.CASCADE)
    name = FHIR_primitive_IdField(null=True, blank=True, )
    value = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_StructureMap_group(models.Model):
    StructureMap = models.ForeignKey(FHIR_StructureMap, related_name='StructureMap_group', null=False, on_delete=models.CASCADE)
    name = FHIR_primitive_IdField(null=True, blank=True, )
    extends = FHIR_primitive_IdField(null=True, blank=True, )
    class TypemodeChoices(models.TextChoices): TYPES = 'types', 'Types'; TYPE_AND_TYPES = 'type-and-types', 'Type-and-types'; 
    typeMode = FHIR_primitive_CodeField(choices=TypemodeChoices.choices, null=True, blank=True, )
    documentation = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_StructureMap_group_input(models.Model):
    StructureMap_group = models.ForeignKey(FHIR_StructureMap_group, related_name='StructureMap_group_input', null=False, on_delete=models.CASCADE)
    name = FHIR_primitive_IdField(null=True, blank=True, )
    type = FHIR_primitive_StringField(null=True, blank=True, )
    class ModeChoices(models.TextChoices): SOURCE = 'source', 'Source'; TARGET = 'target', 'Target'; 
    mode = FHIR_primitive_CodeField(choices=ModeChoices.choices, null=True, blank=True, )
    documentation = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_StructureMap_group_rule(models.Model):
    StructureMap_group = models.ForeignKey(FHIR_StructureMap_group, related_name='StructureMap_group_rule', null=False, on_delete=models.CASCADE)
    name = FHIR_primitive_IdField(null=True, blank=True, )
    documentation = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_StructureMap_group_rule_source(models.Model):
    StructureMap_group_rule = models.ForeignKey(FHIR_StructureMap_group_rule, related_name='StructureMap_group_rule_source', null=False, on_delete=models.CASCADE)
    context = FHIR_primitive_IdField(null=True, blank=True, )
    min = FHIR_primitive_UnsignedIntField(null=True, blank=True, )
    max = FHIR_primitive_StringField(null=True, blank=True, )
    type = FHIR_primitive_StringField(null=True, blank=True, )
    defaultValue = FHIR_primitive_StringField(null=True, blank=True, )
    element = FHIR_primitive_StringField(null=True, blank=True, )
    class ListmodeChoices(models.TextChoices): FIRST = 'first', 'First'; NOT_FIRST = 'not_first', 'Not_first'; LAST = 'last', 'Last'; NOT_LAST = 'not_last', 'Not_last'; ONLY_ONE = 'only_one', 'Only_one'; 
    listMode = FHIR_primitive_CodeField(choices=ListmodeChoices.choices, null=True, blank=True, )
    variable = FHIR_primitive_IdField(null=True, blank=True, )
    condition = FHIR_primitive_StringField(null=True, blank=True, )
    check = FHIR_primitive_StringField(null=True, blank=True, )
    logMessage = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_StructureMap_group_rule_target(models.Model):
    StructureMap_group_rule = models.ForeignKey(FHIR_StructureMap_group_rule, related_name='StructureMap_group_rule_target', null=False, on_delete=models.CASCADE)
    context = FHIR_primitive_StringField(null=True, blank=True, )
    element = FHIR_primitive_StringField(null=True, blank=True, )
    variable = FHIR_primitive_IdField(null=True, blank=True, )
    listRuleId = FHIR_primitive_IdField(null=True, blank=True, )
    class TransformChoices(models.TextChoices): CREATE = 'create', 'Create'; COPY_+ = 'copy +', 'Copy +'; 
    transform = FHIR_primitive_CodeField(choices=TransformChoices.choices, null=True, blank=True, )

class FHIR_StructureMap_group_rule_target_listMode(models.Model):
    StructureMap_group_rule_target = models.ForeignKey(FHIR_StructureMap_group_rule_target, related_name='StructureMap_group_rule_target_listMode', null=False, on_delete=models.CASCADE)
    
    class ListmodeChoices(models.TextChoices): FIRST = 'first', 'First'; SHARE = 'share', 'Share'; LAST = 'last', 'Last'; SINGLE = 'single', 'Single'; 
    listMode = FHIR_primitive_CodeField(choices=ListmodeChoices.choices, null=True, blank=True, )
    
class FHIR_StructureMap_group_rule_target_parameter(models.Model):
    StructureMap_group_rule_target = models.ForeignKey(FHIR_StructureMap_group_rule_target, related_name='StructureMap_group_rule_target_parameter', null=False, on_delete=models.CASCADE)
    value = FHIR_primitive_IdField(null=True, blank=True, )
    value = FHIR_primitive_StringField(null=True, blank=True, )
    value = FHIR_primitive_BooleanField(null=True, blank=True, )
    value = FHIR_primitive_DecimalField(null=True, blank=True, )
    value = FHIR_primitive_DateField(null=True, blank=True, )
    value = FHIR_primitive_TimeField(null=True, blank=True, )
    value = FHIR_primitive_DateTimeField(null=True, blank=True, )

class FHIR_StructureMap_group_rule_dependent(models.Model):
    StructureMap_group_rule = models.ForeignKey(FHIR_StructureMap_group_rule, related_name='StructureMap_group_rule_dependent', null=False, on_delete=models.CASCADE)
    name = FHIR_primitive_IdField(null=True, blank=True, )
