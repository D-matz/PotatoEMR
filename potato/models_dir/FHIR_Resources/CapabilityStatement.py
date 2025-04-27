#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_CapabilityStatement(models.Model):
    url = FHIR_primitive_URIField(null=True, blank=True, )
    version = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm_string = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm_Coding = models.OneToOneField("FHIR_GP_Coding", related_name='CapabilityStatement_versionAlgorithm_Coding', null=True, blank=True, on_delete=models.SET_NULL)
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
    class FhirversionChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    fhirVersion = FHIR_primitive_CodeField(choices=FhirversionChoices.choices, null=True, blank=True, )

class FHIR_CapabilityStatement_identifier(FHIR_GP_Identifier):
    CapabilityStatement = models.ForeignKey(FHIR_CapabilityStatement, related_name='CapabilityStatement_identifier', null=False, on_delete=models.CASCADE)

class FHIR_CapabilityStatement_actorDefinition(models.Model):
    CapabilityStatement = models.ForeignKey(FHIR_CapabilityStatement, related_name='CapabilityStatement_actorDefinition', null=False, on_delete=models.CASCADE)
    
    actorDefinition = FHIR_primitive_CanonicalField(null=True, blank=True, )
    
class FHIR_CapabilityStatement_jurisdiction(models.Model):
    CapabilityStatement = models.ForeignKey(FHIR_CapabilityStatement, related_name='CapabilityStatement_jurisdiction', null=False, on_delete=models.CASCADE)
    BINDING_jurisdiction = "TODO"
    jurisdiction_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_jurisdiction}, related_name='CapabilityStatement_jurisdiction', blank=True)
    jurisdiction_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_CapabilityStatement_instantiates(models.Model):
    CapabilityStatement = models.ForeignKey(FHIR_CapabilityStatement, related_name='CapabilityStatement_instantiates', null=False, on_delete=models.CASCADE)
    
    instantiates = FHIR_primitive_CanonicalField(null=True, blank=True, )
    
class FHIR_CapabilityStatement_imports(models.Model):
    CapabilityStatement = models.ForeignKey(FHIR_CapabilityStatement, related_name='CapabilityStatement_imports', null=False, on_delete=models.CASCADE)
    
    imports = FHIR_primitive_CanonicalField(null=True, blank=True, )
    
class FHIR_CapabilityStatement_software(models.Model):
    CapabilityStatement = models.ForeignKey(FHIR_CapabilityStatement, related_name='CapabilityStatement_software', null=False, on_delete=models.CASCADE)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    version = FHIR_primitive_StringField(null=True, blank=True, )
    releaseDate = FHIR_primitive_DateTimeField(null=True, blank=True, )

class FHIR_CapabilityStatement_implementation(models.Model):
    CapabilityStatement = models.ForeignKey(FHIR_CapabilityStatement, related_name='CapabilityStatement_implementation', null=False, on_delete=models.CASCADE)
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    url = FHIR_primitive_URLField(null=True, blank=True, )
    custodian = models.ForeignKey("FHIR_Organization", related_name="CapabilityStatement_implementation_custodian", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_CapabilityStatement_format(models.Model):
    CapabilityStatement = models.ForeignKey(FHIR_CapabilityStatement, related_name='CapabilityStatement_format', null=False, on_delete=models.CASCADE)
    
    class FormatChoices(models.TextChoices): FORMATS_SUPPORTED_XML = 'formats supported (xml', 'Formats supported (xml'; JSON = 'json', 'Json'; TTL = 'ttl', 'Ttl'; MIME_TYPE = 'mime type)', 'Mime type)'; 
    format = FHIR_primitive_CodeField(choices=FormatChoices.choices, null=True, blank=True, )
    
class FHIR_CapabilityStatement_patchFormat(models.Model):
    CapabilityStatement = models.ForeignKey(FHIR_CapabilityStatement, related_name='CapabilityStatement_patchFormat', null=False, on_delete=models.CASCADE)
    
    class PatchformatChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    patchFormat = FHIR_primitive_CodeField(choices=PatchformatChoices.choices, null=True, blank=True, )
    
class FHIR_CapabilityStatement_acceptLanguage(models.Model):
    CapabilityStatement = models.ForeignKey(FHIR_CapabilityStatement, related_name='CapabilityStatement_acceptLanguage', null=False, on_delete=models.CASCADE)
    
    class AcceptlanguageChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    acceptLanguage = FHIR_primitive_CodeField(choices=AcceptlanguageChoices.choices, null=True, blank=True, )
    
class FHIR_CapabilityStatement_implementationGuide(models.Model):
    CapabilityStatement = models.ForeignKey(FHIR_CapabilityStatement, related_name='CapabilityStatement_implementationGuide', null=False, on_delete=models.CASCADE)
    
    implementationGuide = FHIR_primitive_CanonicalField(null=True, blank=True, )
    
class FHIR_CapabilityStatement_rest(models.Model):
    CapabilityStatement = models.ForeignKey(FHIR_CapabilityStatement, related_name='CapabilityStatement_rest', null=False, on_delete=models.CASCADE)
    class ModeChoices(models.TextChoices): CLIENT = 'client', 'Client'; SERVER = 'server', 'Server'; 
    mode = FHIR_primitive_CodeField(choices=ModeChoices.choices, null=True, blank=True, )
    documentation = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_CapabilityStatement_rest_security(models.Model):
    CapabilityStatement_rest = models.ForeignKey(FHIR_CapabilityStatement_rest, related_name='CapabilityStatement_rest_security', null=False, on_delete=models.CASCADE)
    cors = FHIR_primitive_BooleanField(null=True, blank=True, )
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_CapabilityStatement_rest_security_service(models.Model):
    CapabilityStatement_rest_security = models.ForeignKey(FHIR_CapabilityStatement_rest_security, related_name='CapabilityStatement_rest_security_service', null=False, on_delete=models.CASCADE)
    BINDING_service = "TODO"
    service_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_service}, related_name='CapabilityStatement_rest_security_service', blank=True)
    service_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_CapabilityStatement_rest_resource(models.Model):
    CapabilityStatement_rest = models.ForeignKey(FHIR_CapabilityStatement_rest, related_name='CapabilityStatement_rest_resource', null=False, on_delete=models.CASCADE)
    class TypeChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    type = FHIR_primitive_CodeField(choices=TypeChoices.choices, null=True, blank=True, )
    definition = FHIR_primitive_CanonicalField(null=True, blank=True, )
    profile = FHIR_primitive_CanonicalField(null=True, blank=True, )
    documentation = FHIR_primitive_MarkdownField(null=True, blank=True, )
    class VersioningChoices(models.TextChoices): NO_VERSION = 'no-version', 'No-version'; VERSIONED = 'versioned', 'Versioned'; VERSIONED_UPDATE = 'versioned-update', 'Versioned-update'; 
    versioning = FHIR_primitive_CodeField(choices=VersioningChoices.choices, null=True, blank=True, )
    readHistory = FHIR_primitive_BooleanField(null=True, blank=True, )
    updateCreate = FHIR_primitive_BooleanField(null=True, blank=True, )
    conditionalCreate = FHIR_primitive_BooleanField(null=True, blank=True, )
    class ConditionalreadChoices(models.TextChoices): NOT_SUPPORTED = 'not-supported', 'Not-supported'; MODIFIED_SINCE = 'modified-since', 'Modified-since'; NOT_MATCH = 'not-match', 'Not-match'; FULL_SUPPORT = 'full-support', 'Full-support'; 
    conditionalRead = FHIR_primitive_CodeField(choices=ConditionalreadChoices.choices, null=True, blank=True, )
    conditionalUpdate = FHIR_primitive_BooleanField(null=True, blank=True, )
    conditionalPatch = FHIR_primitive_BooleanField(null=True, blank=True, )
    class ConditionaldeleteChoices(models.TextChoices): NOT_SUPPORTED = 'not-supported', 'Not-supported'; SINGLE = 'single', 'Single'; MULTIPLE___HOW_CONDITIONAL_DELETE_IS_SUPPORTED = 'multiple - how conditional delete is supported', 'Multiple - how conditional delete is supported'; 
    conditionalDelete = FHIR_primitive_CodeField(choices=ConditionaldeleteChoices.choices, null=True, blank=True, )

class FHIR_CapabilityStatement_rest_resource_supportedProfile(models.Model):
    CapabilityStatement_rest_resource = models.ForeignKey(FHIR_CapabilityStatement_rest_resource, related_name='CapabilityStatement_rest_resource_supportedProfile', null=False, on_delete=models.CASCADE)
    
    supportedProfile = FHIR_primitive_CanonicalField(null=True, blank=True, )
    
class FHIR_CapabilityStatement_rest_resource_interaction(models.Model):
    CapabilityStatement_rest_resource = models.ForeignKey(FHIR_CapabilityStatement_rest_resource, related_name='CapabilityStatement_rest_resource_interaction', null=False, on_delete=models.CASCADE)
    class CodeChoices(models.TextChoices): READ = 'read', 'Read'; VREAD = 'vread', 'Vread'; UPDATE = 'update', 'Update'; UPDATE_CONDITIONAL = 'update-conditional', 'Update-conditional'; PATCH = 'patch', 'Patch'; PATCH_CONDITIONAL = 'patch-conditional', 'Patch-conditional'; DELETE = 'delete', 'Delete'; DELETE_CONDITIONAL_SINGLE = 'delete-conditional-single', 'Delete-conditional-single'; DELETE_CONDITIONAL_MULTIPLE = 'delete-conditional-multiple', 'Delete-conditional-multiple'; DELETE_HISTORY = 'delete-history', 'Delete-history'; DELETE_HISTORY_VERSION = 'delete-history-version', 'Delete-history-version'; HISTORY_INSTANCE = 'history-instance', 'History-instance'; HISTORY_TYPE = 'history-type', 'History-type'; CREATE = 'create', 'Create'; CREATE_CONDITIONAL = 'create-conditional', 'Create-conditional'; SEARCH_TYPE = 'search-type', 'Search-type'; 
    code = FHIR_primitive_CodeField(choices=CodeChoices.choices, null=True, blank=True, )
    documentation = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_CapabilityStatement_rest_resource_referencePolicy(models.Model):
    CapabilityStatement_rest_resource = models.ForeignKey(FHIR_CapabilityStatement_rest_resource, related_name='CapabilityStatement_rest_resource_referencePolicy', null=False, on_delete=models.CASCADE)
    
    class ReferencepolicyChoices(models.TextChoices): LITERAL = 'literal', 'Literal'; LOGICAL = 'logical', 'Logical'; RESOLVES = 'resolves', 'Resolves'; ENFORCED = 'enforced', 'Enforced'; LOCAL = 'local', 'Local'; 
    referencePolicy = FHIR_primitive_CodeField(choices=ReferencepolicyChoices.choices, null=True, blank=True, )
    
class FHIR_CapabilityStatement_rest_resource_searchInclude(models.Model):
    CapabilityStatement_rest_resource = models.ForeignKey(FHIR_CapabilityStatement_rest_resource, related_name='CapabilityStatement_rest_resource_searchInclude', null=False, on_delete=models.CASCADE)
    
    searchInclude = FHIR_primitive_StringField(null=True, blank=True, )
    
class FHIR_CapabilityStatement_rest_resource_searchRevInclude(models.Model):
    CapabilityStatement_rest_resource = models.ForeignKey(FHIR_CapabilityStatement_rest_resource, related_name='CapabilityStatement_rest_resource_searchRevInclude', null=False, on_delete=models.CASCADE)
    
    searchRevInclude = FHIR_primitive_StringField(null=True, blank=True, )
    
class FHIR_CapabilityStatement_rest_resource_searchParam(models.Model):
    CapabilityStatement_rest_resource = models.ForeignKey(FHIR_CapabilityStatement_rest_resource, related_name='CapabilityStatement_rest_resource_searchParam', null=False, on_delete=models.CASCADE)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    definition = FHIR_primitive_CanonicalField(null=True, blank=True, )
    class TypeChoices(models.TextChoices): NUMBER = 'number', 'Number'; DATE = 'date', 'Date'; STRING = 'string', 'String'; TOKEN = 'token', 'Token'; REFERENCE = 'reference', 'Reference'; COMPOSITE = 'composite', 'Composite'; QUANTITY = 'quantity', 'Quantity'; URI = 'uri', 'Uri'; SPECIAL = 'special', 'Special'; RESOURCE = 'resource', 'Resource'; 
    type = FHIR_primitive_CodeField(choices=TypeChoices.choices, null=True, blank=True, )
    documentation = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_CapabilityStatement_rest_resource_operation(models.Model):
    CapabilityStatement_rest_resource = models.ForeignKey(FHIR_CapabilityStatement_rest_resource, related_name='CapabilityStatement_rest_resource_operation', null=False, on_delete=models.CASCADE)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    definition = FHIR_primitive_CanonicalField(null=True, blank=True, )
    documentation = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_CapabilityStatement_rest_interaction(models.Model):
    CapabilityStatement_rest = models.ForeignKey(FHIR_CapabilityStatement_rest, related_name='CapabilityStatement_rest_interaction', null=False, on_delete=models.CASCADE)
    class CodeChoices(models.TextChoices): TRANSACTION = 'transaction', 'Transaction'; BATCH = 'batch', 'Batch'; SEARCH_SYSTEM = 'search-system', 'Search-system'; HISTORY_SYSTEM = 'history-system', 'History-system'; 
    code = FHIR_primitive_CodeField(choices=CodeChoices.choices, null=True, blank=True, )
    documentation = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_CapabilityStatement_rest_compartment(models.Model):
    CapabilityStatement_rest = models.ForeignKey(FHIR_CapabilityStatement_rest, related_name='CapabilityStatement_rest_compartment', null=False, on_delete=models.CASCADE)
    
    compartment = FHIR_primitive_CanonicalField(null=True, blank=True, )
    
class FHIR_CapabilityStatement_messaging(models.Model):
    CapabilityStatement = models.ForeignKey(FHIR_CapabilityStatement, related_name='CapabilityStatement_messaging', null=False, on_delete=models.CASCADE)
    reliableCache = FHIR_primitive_UnsignedIntField(null=True, blank=True, )
    documentation = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_CapabilityStatement_messaging_endpoint(models.Model):
    CapabilityStatement_messaging = models.ForeignKey(FHIR_CapabilityStatement_messaging, related_name='CapabilityStatement_messaging_endpoint', null=False, on_delete=models.CASCADE)
    protocol = models.OneToOneField("FHIR_GP_Coding", related_name='CapabilityStatement_messaging_endpoint_protocol', null=True, blank=True, on_delete=models.SET_NULL)
    address = FHIR_primitive_URLField(null=True, blank=True, )

class FHIR_CapabilityStatement_messaging_supportedMessage(models.Model):
    CapabilityStatement_messaging = models.ForeignKey(FHIR_CapabilityStatement_messaging, related_name='CapabilityStatement_messaging_supportedMessage', null=False, on_delete=models.CASCADE)
    class ModeChoices(models.TextChoices): SENDER = 'sender', 'Sender'; RECEIVER = 'receiver', 'Receiver'; 
    mode = FHIR_primitive_CodeField(choices=ModeChoices.choices, null=True, blank=True, )
    definition = FHIR_primitive_CanonicalField(null=True, blank=True, )

class FHIR_CapabilityStatement_document(models.Model):
    CapabilityStatement = models.ForeignKey(FHIR_CapabilityStatement, related_name='CapabilityStatement_document', null=False, on_delete=models.CASCADE)
    class ModeChoices(models.TextChoices): PRODUCER = 'producer', 'Producer'; CONSUMER = 'consumer', 'Consumer'; 
    mode = FHIR_primitive_CodeField(choices=ModeChoices.choices, null=True, blank=True, )
    documentation = FHIR_primitive_MarkdownField(null=True, blank=True, )
    profile = FHIR_primitive_CanonicalField(null=True, blank=True, )
