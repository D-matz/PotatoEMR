#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_TestScript(models.Model):
    url = FHIR_primitive_URIField(null=True, blank=True, )
    version = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm_string = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm_Coding = models.OneToOneField("FHIR_GP_Coding", related_name='TestScript_versionAlgorithm_Coding', null=True, blank=True, on_delete=models.SET_NULL)
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

class FHIR_TestScript_identifier(FHIR_GP_Identifier):
    TestScript = models.ForeignKey(FHIR_TestScript, related_name='TestScript_identifier', null=False, on_delete=models.CASCADE)

class FHIR_TestScript_jurisdiction(models.Model):
    TestScript = models.ForeignKey(FHIR_TestScript, related_name='TestScript_jurisdiction', null=False, on_delete=models.CASCADE)
    BINDING_jurisdiction = "TODO"
    jurisdiction_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_jurisdiction}, related_name='TestScript_jurisdiction', blank=True)
    jurisdiction_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_TestScript_testSystem(models.Model):
    TestScript = models.ForeignKey(FHIR_TestScript, related_name='TestScript_testSystem', null=False, on_delete=models.CASCADE)
    index = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    title = FHIR_primitive_StringField(null=True, blank=True, )
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    url = FHIR_primitive_URLField(null=True, blank=True, )

class FHIR_TestScript_testSystem_actor(models.Model):
    TestScript_testSystem = models.ForeignKey(FHIR_TestScript_testSystem, related_name='TestScript_testSystem_actor', null=False, on_delete=models.CASCADE)
    
    actor = FHIR_primitive_CanonicalField(null=True, blank=True, )
    
class FHIR_TestScript_metadata(models.Model):
    TestScript = models.ForeignKey(FHIR_TestScript, related_name='TestScript_metadata', null=False, on_delete=models.CASCADE)

class FHIR_TestScript_metadata_link(models.Model):
    TestScript_metadata = models.ForeignKey(FHIR_TestScript_metadata, related_name='TestScript_metadata_link', null=False, on_delete=models.CASCADE)
    url = FHIR_primitive_URIField(null=True, blank=True, )
    description = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_TestScript_metadata_capability(models.Model):
    TestScript_metadata = models.ForeignKey(FHIR_TestScript_metadata, related_name='TestScript_metadata_capability', null=False, on_delete=models.CASCADE)
    required = FHIR_primitive_BooleanField(null=True, blank=True, )
    validated = FHIR_primitive_BooleanField(null=True, blank=True, )
    description = FHIR_primitive_StringField(null=True, blank=True, )
    capabilities = FHIR_primitive_CanonicalField(null=True, blank=True, )

class FHIR_TestScript_metadata_capability_link(models.Model):
    TestScript_metadata_capability = models.ForeignKey(FHIR_TestScript_metadata_capability, related_name='TestScript_metadata_capability_link', null=False, on_delete=models.CASCADE)
    
    link = FHIR_primitive_URIField(null=True, blank=True, )
    
class FHIR_TestScript_scope(models.Model):
    TestScript = models.ForeignKey(FHIR_TestScript, related_name='TestScript_scope', null=False, on_delete=models.CASCADE)
    artifact = FHIR_primitive_CanonicalField(null=True, blank=True, )
    BINDING_conformance = "TODO"
    conformance_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_conformance}, related_name='TestScript_scope_conformance', blank=True)
    conformance_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_phase = "TODO"
    phase_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_phase}, related_name='TestScript_scope_phase', blank=True)
    phase_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_TestScript_fixture(models.Model):
    TestScript = models.ForeignKey(FHIR_TestScript, related_name='TestScript_fixture', null=False, on_delete=models.CASCADE)
    autocreate = FHIR_primitive_BooleanField(null=True, blank=True, )
    autodelete = FHIR_primitive_BooleanField(null=True, blank=True, )
                            #skipping Reference(Any) for field resource as TestScript resource not in referenceAny_targets

class FHIR_TestScript_profile(models.Model):
    TestScript = models.ForeignKey(FHIR_TestScript, related_name='TestScript_profile', null=False, on_delete=models.CASCADE)
    
    profile = FHIR_primitive_CanonicalField(null=True, blank=True, )
    
class FHIR_TestScript_variable(models.Model):
    TestScript = models.ForeignKey(FHIR_TestScript, related_name='TestScript_variable', null=False, on_delete=models.CASCADE)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    defaultValue = FHIR_primitive_StringField(null=True, blank=True, )
    description = FHIR_primitive_StringField(null=True, blank=True, )
    expression = FHIR_primitive_StringField(null=True, blank=True, )
    headerField = FHIR_primitive_StringField(null=True, blank=True, )
    hint = FHIR_primitive_StringField(null=True, blank=True, )
    path = FHIR_primitive_StringField(null=True, blank=True, )
    sourceId = FHIR_primitive_IdField(null=True, blank=True, )

class FHIR_TestScript_setup(models.Model):
    TestScript = models.ForeignKey(FHIR_TestScript, related_name='TestScript_setup', null=False, on_delete=models.CASCADE)

class FHIR_TestScript_setup_action(models.Model):
    TestScript_setup = models.ForeignKey(FHIR_TestScript_setup, related_name='TestScript_setup_action', null=False, on_delete=models.CASCADE)

class FHIR_TestScript_setup_action_common(models.Model):
    TestScript_setup_action = models.ForeignKey(FHIR_TestScript_setup_action, related_name='TestScript_setup_action_common', null=False, on_delete=models.CASCADE)
    testScript = FHIR_primitive_CanonicalField(null=True, blank=True, )
    keyRef = FHIR_primitive_IdField(null=True, blank=True, )

class FHIR_TestScript_setup_action_common_parameter(models.Model):
    TestScript_setup_action_common = models.ForeignKey(FHIR_TestScript_setup_action_common, related_name='TestScript_setup_action_common_parameter', null=False, on_delete=models.CASCADE)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    value = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_TestScript_setup_action_operation(models.Model):
    TestScript_setup_action = models.ForeignKey(FHIR_TestScript_setup_action, related_name='TestScript_setup_action_operation', null=False, on_delete=models.CASCADE)
    type = models.OneToOneField("FHIR_GP_Coding", related_name='TestScript_setup_action_operation_type', null=True, blank=True, on_delete=models.SET_NULL)
    resource = FHIR_primitive_URIField(null=True, blank=True, )
    label = FHIR_primitive_StringField(null=True, blank=True, )
    description = FHIR_primitive_StringField(null=True, blank=True, )
    class AcceptChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    accept = FHIR_primitive_CodeField(choices=AcceptChoices.choices, null=True, blank=True, )
    class ContenttypeChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    contentType = FHIR_primitive_CodeField(choices=ContenttypeChoices.choices, null=True, blank=True, )
    encodeRequestUrl = FHIR_primitive_BooleanField(null=True, blank=True, )
    class MethodChoices(models.TextChoices): DELETE = 'delete', 'Delete'; GET = 'get', 'Get'; OPTIONS = 'options', 'Options'; PATCH = 'patch', 'Patch'; POST = 'post', 'Post'; PUT = 'put', 'Put'; HEAD = 'head', 'Head'; 
    method = FHIR_primitive_CodeField(choices=MethodChoices.choices, null=True, blank=True, )
    params = FHIR_primitive_StringField(null=True, blank=True, )
    requestId = FHIR_primitive_IdField(null=True, blank=True, )
    responseId = FHIR_primitive_IdField(null=True, blank=True, )
    sourceId = FHIR_primitive_IdField(null=True, blank=True, )
    targetId = FHIR_primitive_IdField(null=True, blank=True, )
    url = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_TestScript_setup_action_operation_requestHeader(models.Model):
    TestScript_setup_action_operation = models.ForeignKey(FHIR_TestScript_setup_action_operation, related_name='TestScript_setup_action_operation_requestHeader', null=False, on_delete=models.CASCADE)
    field = FHIR_primitive_StringField(null=True, blank=True, )
    value = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_TestScript_setup_action_assert(models.Model):
    TestScript_setup_action = models.ForeignKey(FHIR_TestScript_setup_action, related_name='TestScript_setup_action_assert', null=False, on_delete=models.CASCADE)
    label = FHIR_primitive_StringField(null=True, blank=True, )
    description = FHIR_primitive_StringField(null=True, blank=True, )
    class DirectionChoices(models.TextChoices): RESPONSE = 'response', 'Response'; REQUEST = 'request', 'Request'; 
    direction = FHIR_primitive_CodeField(choices=DirectionChoices.choices, null=True, blank=True, )
    compareToSourceId = FHIR_primitive_StringField(null=True, blank=True, )
    compareToSourceExpression = FHIR_primitive_StringField(null=True, blank=True, )
    compareToSourcePath = FHIR_primitive_StringField(null=True, blank=True, )
    class ContenttypeChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    contentType = FHIR_primitive_CodeField(choices=ContenttypeChoices.choices, null=True, blank=True, )
    class DefaultmanualcompletionChoices(models.TextChoices): FAIL = 'fail', 'Fail'; PASS = 'pass', 'Pass'; SKIP = 'skip', 'Skip'; STOP = 'stop', 'Stop'; 
    defaultManualCompletion = FHIR_primitive_CodeField(choices=DefaultmanualcompletionChoices.choices, null=True, blank=True, )
    expression = FHIR_primitive_StringField(null=True, blank=True, )
    headerField = FHIR_primitive_StringField(null=True, blank=True, )
    minimumId = FHIR_primitive_StringField(null=True, blank=True, )
    navigationLinks = FHIR_primitive_BooleanField(null=True, blank=True, )
    class OperatorChoices(models.TextChoices): EQUALS = 'equals', 'Equals'; NOTEQUALS = 'notEquals', 'Notequals'; IN = 'in', 'In'; NOTIN = 'notIn', 'Notin'; GREATERTHAN = 'greaterThan', 'Greaterthan'; LESSTHAN = 'lessThan', 'Lessthan'; EMPTY = 'empty', 'Empty'; NOTEMPTY = 'notEmpty', 'Notempty'; CONTAINS = 'contains', 'Contains'; NOTCONTAINS = 'notContains', 'Notcontains'; EVAL = 'eval', 'Eval'; MANUALEVAL = 'manualEval', 'Manualeval'; 
    operator = FHIR_primitive_CodeField(choices=OperatorChoices.choices, null=True, blank=True, )
    path = FHIR_primitive_StringField(null=True, blank=True, )
    class RequestmethodChoices(models.TextChoices): DELETE = 'delete', 'Delete'; GET = 'get', 'Get'; OPTIONS = 'options', 'Options'; PATCH = 'patch', 'Patch'; POST = 'post', 'Post'; PUT = 'put', 'Put'; HEAD = 'head', 'Head'; 
    requestMethod = FHIR_primitive_CodeField(choices=RequestmethodChoices.choices, null=True, blank=True, )
    requestURL = FHIR_primitive_StringField(null=True, blank=True, )
    resource = FHIR_primitive_URIField(null=True, blank=True, )
    class ResponseChoices(models.TextChoices): CONTINUE = 'continue', 'Continue'; SWITCHINGPROTOCOLS = 'switchingProtocols', 'Switchingprotocols'; OKAY = 'okay', 'Okay'; CREATED = 'created', 'Created'; ACCEPTED = 'accepted', 'Accepted'; NONAUTHORITATIVEINFORMATION = 'nonAuthoritativeInformation', 'Nonauthoritativeinformation'; NOCONTENT = 'noContent', 'Nocontent'; RESETCONTENT = 'resetContent', 'Resetcontent'; PARTIALCONTENT = 'partialContent', 'Partialcontent'; MULTIPLECHOICES = 'multipleChoices', 'Multiplechoices'; MOVEDPERMANENTLY = 'movedPermanently', 'Movedpermanently'; FOUND = 'found', 'Found'; SEEOTHER = 'seeOther', 'Seeother'; NOTMODIFIED = 'notModified', 'Notmodified'; USEPROXY = 'useProxy', 'Useproxy'; TEMPORARYREDIRECT = 'temporaryRedirect', 'Temporaryredirect'; PERMANENTREDIRECT = 'permanentRedirect', 'Permanentredirect'; BADREQUEST = 'badRequest', 'Badrequest'; UNAUTHORIZED = 'unauthorized', 'Unauthorized'; PAYMENTREQUIRED = 'paymentRequired', 'Paymentrequired'; FORBIDDEN = 'forbidden', 'Forbidden'; NOTFOUND = 'notFound', 'Notfound'; METHODNOTALLOWED = 'methodNotAllowed', 'Methodnotallowed'; NOTACCEPTABLE = 'notAcceptable', 'Notacceptable'; PROXYAUTHENTICATIONREQUIRED = 'proxyAuthenticationRequired', 'Proxyauthenticationrequired'; REQUESTTIMEOUT = 'requestTimeout', 'Requesttimeout'; CONFLICT = 'conflict', 'Conflict'; GONE = 'gone', 'Gone'; LENGTHREQUIRED = 'lengthRequired', 'Lengthrequired'; PRECONDITIONFAILED = 'preconditionFailed', 'Preconditionfailed'; CONTENTTOOLARGE = 'contentTooLarge', 'Contenttoolarge'; URITOOLONG = 'uriTooLong', 'Uritoolong'; UNSUPPORTEDMEDIATYPE = 'unsupportedMediaType', 'Unsupportedmediatype'; RANGENOTSATISFIABLE = 'rangeNotSatisfiable', 'Rangenotsatisfiable'; EXPECTATIONFAILED = 'expectationFailed', 'Expectationfailed'; MISDIRECTEDREQUEST = 'misdirectedRequest', 'Misdirectedrequest'; UNPROCESSABLECONTENT = 'unprocessableContent', 'Unprocessablecontent'; UPGRADEREQUIRED = 'upgradeRequired', 'Upgraderequired'; INTERNALSERVERERROR = 'internalServerError', 'Internalservererror'; NOTIMPLEMENTED = 'notImplemented', 'Notimplemented'; BADGATEWAY = 'badGateway', 'Badgateway'; SERVICEUNAVAILABLE = 'serviceUnavailable', 'Serviceunavailable'; GATEWAYTIMEOUT = 'gatewayTimeout', 'Gatewaytimeout'; HTTPVERSIONNOTSUPPORTED = 'httpVersionNotSupported', 'Httpversionnotsupported'; 
    response = FHIR_primitive_CodeField(choices=ResponseChoices.choices, null=True, blank=True, )
    responseCode = FHIR_primitive_StringField(null=True, blank=True, )
    sourceId = FHIR_primitive_IdField(null=True, blank=True, )
    stopTestOnFail = FHIR_primitive_BooleanField(null=True, blank=True, )
    validateProfileId = FHIR_primitive_IdField(null=True, blank=True, )
    value = FHIR_primitive_StringField(null=True, blank=True, )
    warningOnly = FHIR_primitive_BooleanField(null=True, blank=True, )

class FHIR_TestScript_setup_action_assert_requirement(models.Model):
    TestScript_setup_action_assert = models.ForeignKey(FHIR_TestScript_setup_action_assert, related_name='TestScript_setup_action_assert_requirement', null=False, on_delete=models.CASCADE)
    reference = FHIR_primitive_CanonicalField(null=True, blank=True, )
    key = FHIR_primitive_IdField(null=True, blank=True, )

class FHIR_TestScript_test(models.Model):
    TestScript = models.ForeignKey(FHIR_TestScript, related_name='TestScript_test', null=False, on_delete=models.CASCADE)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    description = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_TestScript_test_action(models.Model):
    TestScript_test = models.ForeignKey(FHIR_TestScript_test, related_name='TestScript_test_action', null=False, on_delete=models.CASCADE)

class FHIR_TestScript_teardown(models.Model):
    TestScript = models.ForeignKey(FHIR_TestScript, related_name='TestScript_teardown', null=False, on_delete=models.CASCADE)

class FHIR_TestScript_teardown_action(models.Model):
    TestScript_teardown = models.ForeignKey(FHIR_TestScript_teardown, related_name='TestScript_teardown_action', null=False, on_delete=models.CASCADE)

class FHIR_TestScript_common(models.Model):
    TestScript = models.ForeignKey(FHIR_TestScript, related_name='TestScript_common', null=False, on_delete=models.CASCADE)
    key = FHIR_primitive_IdField(null=True, blank=True, )
    name = FHIR_primitive_StringField(null=True, blank=True, )
    description = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_TestScript_common_parameter(models.Model):
    TestScript_common = models.ForeignKey(FHIR_TestScript_common, related_name='TestScript_common_parameter', null=False, on_delete=models.CASCADE)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    description = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_TestScript_common_action(models.Model):
    TestScript_common = models.ForeignKey(FHIR_TestScript_common, related_name='TestScript_common_action', null=False, on_delete=models.CASCADE)
