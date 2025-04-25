
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_ImplementationGuide(models.Model):
    url = FHIR_primitive_URIField(null=True, blank=True, )
    version = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = models.OneToOneField("FHIR_GP_Coding", related_name='ImplementationGuide_versionAlgorithm', null=True, blank=True, on_delete=models.SET_NULL)
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
    packageId = FHIR_primitive_IdField(null=True, blank=True, )
    class LicenseChoices(models.TextChoices): SPDX_LICENSE_CODE_FOR_THIS_IG_OR_NOT_OPEN_SOURCE = 'SPDX license code for this IG (or not-open-source)', 'Spdx license code for this ig (or not-open-source)'; 
    license = FHIR_primitive_CodeField(choices=LicenseChoices.choices, null=True, blank=True, )

class FHIR_ImplementationGuide_identifier(FHIR_GP_Identifier):
    ImplementationGuide = models.ForeignKey(FHIR_ImplementationGuide, related_name='ImplementationGuide_identifier', null=False, on_delete=models.CASCADE)

class FHIR_ImplementationGuide_jurisdiction(models.Model):
    ImplementationGuide = models.ForeignKey(FHIR_ImplementationGuide, related_name='ImplementationGuide_jurisdiction', null=False, on_delete=models.CASCADE)
    BINDING_jurisdiction = 'TODO'
    jurisdiction_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_jurisdiction}, related_name='ImplementationGuide_jurisdiction', blank=True)
    jurisdiction_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ImplementationGuide_fhirVersion(models.Model):
    ImplementationGuide = models.ForeignKey(FHIR_ImplementationGuide, related_name='ImplementationGuide_fhirVersion', null=False, on_delete=models.CASCADE)
    
    class FhirversionChoices(models.TextChoices): FHIR_VERSIONS_THIS_IMPLEMENTATION_GUIDE_TARGETS = 'FHIR Version(s) this Implementation Guide targets', 'Fhir version(s) this implementation guide targets'; 
    fhirVersion = FHIR_primitive_CodeField(choices=FhirversionChoices.choices, null=True, blank=True, )
    
class FHIR_ImplementationGuide_dependsOn(models.Model):
    ImplementationGuide = models.ForeignKey(FHIR_ImplementationGuide, related_name='ImplementationGuide_dependsOn', null=False, on_delete=models.CASCADE)
    uri = FHIR_primitive_CanonicalField(null=True, blank=True, )
    packageId = FHIR_primitive_IdField(null=True, blank=True, )
    version = FHIR_primitive_StringField(null=True, blank=True, )
    reason = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_ImplementationGuide_global(models.Model):
    ImplementationGuide = models.ForeignKey(FHIR_ImplementationGuide, related_name='ImplementationGuide_global', null=False, on_delete=models.CASCADE)
    class TypeChoices(models.TextChoices): TYPE_THIS_PROFILE_APPLIES_TO = 'Type this profile applies to', 'Type this profile applies to'; 
    type = FHIR_primitive_CodeField(choices=TypeChoices.choices, null=True, blank=True, )
    profile = FHIR_primitive_CanonicalField(null=True, blank=True, )

class FHIR_ImplementationGuide_definition(models.Model):
    ImplementationGuide = models.ForeignKey(FHIR_ImplementationGuide, related_name='ImplementationGuide_definition', null=False, on_delete=models.CASCADE)

class FHIR_ImplementationGuide_definition_grouping(models.Model):
    ImplementationGuide_definition = models.ForeignKey(FHIR_ImplementationGuide_definition, related_name='ImplementationGuide_definition_grouping', null=False, on_delete=models.CASCADE)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_ImplementationGuide_definition_resource(models.Model):
    ImplementationGuide_definition = models.ForeignKey(FHIR_ImplementationGuide_definition, related_name='ImplementationGuide_definition_resource', null=False, on_delete=models.CASCADE)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    isExample = FHIR_primitive_BooleanField(null=True, blank=True, )
    groupingId = FHIR_primitive_IdField(null=True, blank=True, )

class FHIR_ImplementationGuide_definition_resource_fhirVersion(models.Model):
    ImplementationGuide_definition_resource = models.ForeignKey(FHIR_ImplementationGuide_definition_resource, related_name='ImplementationGuide_definition_resource_fhirVersion', null=False, on_delete=models.CASCADE)
    
    class FhirversionChoices(models.TextChoices): VERSIONS_THIS_APPLIES_TO_IF_DIFFERENT_TO_IG = 'Versions this applies to (if different to IG)', 'Versions this applies to (if different to ig)'; 
    fhirVersion = FHIR_primitive_CodeField(choices=FhirversionChoices.choices, null=True, blank=True, )
    
class FHIR_ImplementationGuide_definition_resource_profile(models.Model):
    ImplementationGuide_definition_resource = models.ForeignKey(FHIR_ImplementationGuide_definition_resource, related_name='ImplementationGuide_definition_resource_profile', null=False, on_delete=models.CASCADE)
    
    profile = FHIR_primitive_CanonicalField(null=True, blank=True, )
    
class FHIR_ImplementationGuide_definition_page(models.Model):
    ImplementationGuide_definition = models.ForeignKey(FHIR_ImplementationGuide_definition, related_name='ImplementationGuide_definition_page', null=False, on_delete=models.CASCADE)
    source = FHIR_primitive_URLField(null=True, blank=True, )
    source = FHIR_primitive_StringField(null=True, blank=True, )
    source = FHIR_primitive_MarkdownField(null=True, blank=True, )
    name = FHIR_primitive_URLField(null=True, blank=True, )
    title = FHIR_primitive_StringField(null=True, blank=True, )
    class GenerationChoices(models.TextChoices): HTML = 'html', 'Html'; MARKDOWN = 'markdown', 'Markdown'; XML = 'xml', 'Xml'; GENERATED = 'generated', 'Generated'; 
    generation = FHIR_primitive_CodeField(choices=GenerationChoices.choices, null=True, blank=True, )

class FHIR_ImplementationGuide_definition_parameter(models.Model):
    ImplementationGuide_definition = models.ForeignKey(FHIR_ImplementationGuide_definition, related_name='ImplementationGuide_definition_parameter', null=False, on_delete=models.CASCADE)
    code = models.OneToOneField("FHIR_GP_Coding", related_name='ImplementationGuide_definition_parameter_code', null=True, blank=True, on_delete=models.SET_NULL)
    value = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_ImplementationGuide_definition_template(models.Model):
    ImplementationGuide_definition = models.ForeignKey(FHIR_ImplementationGuide_definition, related_name='ImplementationGuide_definition_template', null=False, on_delete=models.CASCADE)
    class CodeChoices(models.TextChoices): TYPE_OF_TEMPLATE_SPECIFIED = 'Type of template specified', 'Type of template specified'; 
    code = FHIR_primitive_CodeField(choices=CodeChoices.choices, null=True, blank=True, )
    source = FHIR_primitive_StringField(null=True, blank=True, )
    scope = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_ImplementationGuide_manifest(models.Model):
    ImplementationGuide = models.ForeignKey(FHIR_ImplementationGuide, related_name='ImplementationGuide_manifest', null=False, on_delete=models.CASCADE)
    rendering = FHIR_primitive_URLField(null=True, blank=True, )

class FHIR_ImplementationGuide_manifest_resource(models.Model):
    ImplementationGuide_manifest = models.ForeignKey(FHIR_ImplementationGuide_manifest, related_name='ImplementationGuide_manifest_resource', null=False, on_delete=models.CASCADE)
    isExample = FHIR_primitive_BooleanField(null=True, blank=True, )
    relativePath = FHIR_primitive_URLField(null=True, blank=True, )

class FHIR_ImplementationGuide_manifest_resource_profile(models.Model):
    ImplementationGuide_manifest_resource = models.ForeignKey(FHIR_ImplementationGuide_manifest_resource, related_name='ImplementationGuide_manifest_resource_profile', null=False, on_delete=models.CASCADE)
    
    profile = FHIR_primitive_CanonicalField(null=True, blank=True, )
    
class FHIR_ImplementationGuide_manifest_page(models.Model):
    ImplementationGuide_manifest = models.ForeignKey(FHIR_ImplementationGuide_manifest, related_name='ImplementationGuide_manifest_page', null=False, on_delete=models.CASCADE)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    title = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_ImplementationGuide_manifest_page_anchor(models.Model):
    ImplementationGuide_manifest_page = models.ForeignKey(FHIR_ImplementationGuide_manifest_page, related_name='ImplementationGuide_manifest_page_anchor', null=False, on_delete=models.CASCADE)
    
    anchor = FHIR_primitive_StringField(null=True, blank=True, )
    
class FHIR_ImplementationGuide_manifest_image(models.Model):
    ImplementationGuide_manifest = models.ForeignKey(FHIR_ImplementationGuide_manifest, related_name='ImplementationGuide_manifest_image', null=False, on_delete=models.CASCADE)
    
    image = FHIR_primitive_StringField(null=True, blank=True, )
    
class FHIR_ImplementationGuide_manifest_other(models.Model):
    ImplementationGuide_manifest = models.ForeignKey(FHIR_ImplementationGuide_manifest, related_name='ImplementationGuide_manifest_other', null=False, on_delete=models.CASCADE)
    
    other = FHIR_primitive_StringField(null=True, blank=True, )
    