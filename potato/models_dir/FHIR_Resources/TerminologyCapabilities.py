#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_TerminologyCapabilities(models.Model):
    url = FHIR_primitive_URIField(null=True, blank=True, )
    version = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm_string = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm_Coding = models.OneToOneField("FHIR_GP_Coding", related_name='TerminologyCapabilities_versionAlgorithm_Coding', null=True, blank=True, on_delete=models.SET_NULL)
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
    class KindChoices(models.TextChoices): INSTANCE = 'instance', 'Instance'; CAPABILITY = 'capability', 'Capability'; REQUIREMENTS = 'requirements', 'Requirements'; 
    kind = FHIR_primitive_CodeField(choices=KindChoices.choices, null=True, blank=True, )
    lockedDate = FHIR_primitive_BooleanField(null=True, blank=True, )
    class CodesearchChoices(models.TextChoices): IN_COMPOSE = 'in-compose', 'In-compose'; IN_EXPANSION = 'in-expansion', 'In-expansion'; IN_COMPOSE_OR_EXPANSION = 'in-compose-or-expansion', 'In-compose-or-expansion'; 
    codeSearch = FHIR_primitive_CodeField(choices=CodesearchChoices.choices, null=True, blank=True, )

class FHIR_TerminologyCapabilities_identifier(FHIR_GP_Identifier):
    TerminologyCapabilities = models.ForeignKey(FHIR_TerminologyCapabilities, related_name='TerminologyCapabilities_identifier', null=False, on_delete=models.CASCADE)

class FHIR_TerminologyCapabilities_jurisdiction(models.Model):
    TerminologyCapabilities = models.ForeignKey(FHIR_TerminologyCapabilities, related_name='TerminologyCapabilities_jurisdiction', null=False, on_delete=models.CASCADE)
    BINDING_jurisdiction = "TODO"
    jurisdiction_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_jurisdiction}, related_name='TerminologyCapabilities_jurisdiction', blank=True)
    jurisdiction_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_TerminologyCapabilities_software(models.Model):
    TerminologyCapabilities = models.ForeignKey(FHIR_TerminologyCapabilities, related_name='TerminologyCapabilities_software', null=False, on_delete=models.CASCADE)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    version = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_TerminologyCapabilities_implementation(models.Model):
    TerminologyCapabilities = models.ForeignKey(FHIR_TerminologyCapabilities, related_name='TerminologyCapabilities_implementation', null=False, on_delete=models.CASCADE)
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    url = FHIR_primitive_URLField(null=True, blank=True, )

class FHIR_TerminologyCapabilities_codeSystem(models.Model):
    TerminologyCapabilities = models.ForeignKey(FHIR_TerminologyCapabilities, related_name='TerminologyCapabilities_codeSystem', null=False, on_delete=models.CASCADE)
    uri = FHIR_primitive_CanonicalField(null=True, blank=True, )
    class ContentChoices(models.TextChoices): NOT_PRESENT = 'not-present', 'Not-present'; EXAMPLE = 'example', 'Example'; FRAGMENT = 'fragment', 'Fragment'; COMPLETE = 'complete', 'Complete'; SUPPLEMENT = 'supplement', 'Supplement'; 
    content = FHIR_primitive_CodeField(choices=ContentChoices.choices, null=True, blank=True, )
    subsumption = FHIR_primitive_BooleanField(null=True, blank=True, )

class FHIR_TerminologyCapabilities_codeSystem_version(models.Model):
    TerminologyCapabilities_codeSystem = models.ForeignKey(FHIR_TerminologyCapabilities_codeSystem, related_name='TerminologyCapabilities_codeSystem_version', null=False, on_delete=models.CASCADE)
    code = FHIR_primitive_StringField(null=True, blank=True, )
    isDefault = FHIR_primitive_BooleanField(null=True, blank=True, )
    compositional = FHIR_primitive_BooleanField(null=True, blank=True, )

class FHIR_TerminologyCapabilities_codeSystem_version_language(models.Model):
    TerminologyCapabilities_codeSystem_version = models.ForeignKey(FHIR_TerminologyCapabilities_codeSystem_version, related_name='TerminologyCapabilities_codeSystem_version_language', null=False, on_delete=models.CASCADE)
    
    class LanguageChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    language = FHIR_primitive_CodeField(choices=LanguageChoices.choices, null=True, blank=True, )
    
class FHIR_TerminologyCapabilities_codeSystem_version_filter(models.Model):
    TerminologyCapabilities_codeSystem_version = models.ForeignKey(FHIR_TerminologyCapabilities_codeSystem_version, related_name='TerminologyCapabilities_codeSystem_version_filter', null=False, on_delete=models.CASCADE)
    class CodeChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    code = FHIR_primitive_CodeField(choices=CodeChoices.choices, null=True, blank=True, )

class FHIR_TerminologyCapabilities_codeSystem_version_filter_op(models.Model):
    TerminologyCapabilities_codeSystem_version_filter = models.ForeignKey(FHIR_TerminologyCapabilities_codeSystem_version_filter, related_name='TerminologyCapabilities_codeSystem_version_filter_op', null=False, on_delete=models.CASCADE)
    
    class OpChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    op = FHIR_primitive_CodeField(choices=OpChoices.choices, null=True, blank=True, )
    
class FHIR_TerminologyCapabilities_codeSystem_version_property(models.Model):
    TerminologyCapabilities_codeSystem_version = models.ForeignKey(FHIR_TerminologyCapabilities_codeSystem_version, related_name='TerminologyCapabilities_codeSystem_version_property', null=False, on_delete=models.CASCADE)
    
    class PropertyChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    property = FHIR_primitive_CodeField(choices=PropertyChoices.choices, null=True, blank=True, )
    
class FHIR_TerminologyCapabilities_supplements(models.Model):
    TerminologyCapabilities = models.ForeignKey(FHIR_TerminologyCapabilities, related_name='TerminologyCapabilities_supplements', null=False, on_delete=models.CASCADE)
    class GlobalsChoices(models.TextChoices): NOT_SUPPORTED = 'not-supported', 'Not-supported'; EXPLICIT = 'explicit', 'Explicit'; IMPLICIT = 'implicit', 'Implicit'; 
    globals = FHIR_primitive_CodeField(choices=GlobalsChoices.choices, null=True, blank=True, )

class FHIR_TerminologyCapabilities_expansion(models.Model):
    TerminologyCapabilities = models.ForeignKey(FHIR_TerminologyCapabilities, related_name='TerminologyCapabilities_expansion', null=False, on_delete=models.CASCADE)
    hierarchical = FHIR_primitive_BooleanField(null=True, blank=True, )
    paging = FHIR_primitive_BooleanField(null=True, blank=True, )
    incomplete = FHIR_primitive_BooleanField(null=True, blank=True, )
    textFilter = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_TerminologyCapabilities_expansion_parameter(models.Model):
    TerminologyCapabilities_expansion = models.ForeignKey(FHIR_TerminologyCapabilities_expansion, related_name='TerminologyCapabilities_expansion_parameter', null=False, on_delete=models.CASCADE)
    class NameChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    name = FHIR_primitive_CodeField(choices=NameChoices.choices, null=True, blank=True, )
    documentation = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_TerminologyCapabilities_validateCode(models.Model):
    TerminologyCapabilities = models.ForeignKey(FHIR_TerminologyCapabilities, related_name='TerminologyCapabilities_validateCode', null=False, on_delete=models.CASCADE)
    translations = FHIR_primitive_BooleanField(null=True, blank=True, )

class FHIR_TerminologyCapabilities_translation(models.Model):
    TerminologyCapabilities = models.ForeignKey(FHIR_TerminologyCapabilities, related_name='TerminologyCapabilities_translation', null=False, on_delete=models.CASCADE)
    needsMap = FHIR_primitive_BooleanField(null=True, blank=True, )

class FHIR_TerminologyCapabilities_closure(models.Model):
    TerminologyCapabilities = models.ForeignKey(FHIR_TerminologyCapabilities, related_name='TerminologyCapabilities_closure', null=False, on_delete=models.CASCADE)
    translation = FHIR_primitive_BooleanField(null=True, blank=True, )
