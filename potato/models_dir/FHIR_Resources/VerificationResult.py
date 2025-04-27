#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_VerificationResult(models.Model):
    BINDING_need = 'TODO'
    need_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_need}, related_name='VerificationResult_need', blank=True)
    need_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    class StatusChoices(models.TextChoices): ATTESTED = 'attested', 'Attested'; VALIDATED = 'validated', 'Validated'; IN_PROCESS = 'in-process', 'In-process'; REQ_REVALID = 'req-revalid', 'Req-revalid'; VAL_FAIL = 'val-fail', 'Val-fail'; REVAL_FAIL = 'reval-fail', 'Reval-fail'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    statusDate = FHIR_primitive_DateTimeField(null=True, blank=True, )
    BINDING_validationType = 'TODO'
    validationType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_validationType}, related_name='VerificationResult_validationType', blank=True)
    validationType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    frequency = models.OneToOneField("FHIR_GP_Timing", related_name='VerificationResult_frequency', null=True, blank=True, on_delete=models.SET_NULL)
    lastPerformed = FHIR_primitive_DateTimeField(null=True, blank=True, )
    nextScheduled = FHIR_primitive_DateField(null=True, blank=True, )
    BINDING_failureAction = 'TODO'
    failureAction_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_failureAction}, related_name='VerificationResult_failureAction', blank=True)
    failureAction_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_VerificationResult_targetLocation(models.Model):
    VerificationResult = models.ForeignKey(FHIR_VerificationResult, related_name='VerificationResult_targetLocation', null=False, on_delete=models.CASCADE)
    
    targetLocation = FHIR_primitive_StringField(null=True, blank=True, )
    
class FHIR_VerificationResult_validationProcess(models.Model):
    VerificationResult = models.ForeignKey(FHIR_VerificationResult, related_name='VerificationResult_validationProcess', null=False, on_delete=models.CASCADE)
    BINDING_validationProcess = 'TODO'
    validationProcess_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_validationProcess}, related_name='VerificationResult_validationProcess', blank=True)
    validationProcess_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_VerificationResult_primarySource(models.Model):
    VerificationResult = models.ForeignKey(FHIR_VerificationResult, related_name='VerificationResult_primarySource', null=False, on_delete=models.CASCADE)
    who_Organization = models.ForeignKey("FHIR_Organization", related_name="VerificationResult_primarySource_who", null=True, blank=True, on_delete=models.SET_NULL)
    who_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="VerificationResult_primarySource_who", null=True, blank=True, on_delete=models.SET_NULL)
    who_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="VerificationResult_primarySource_who", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_validationStatus = 'TODO'
    validationStatus_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_validationStatus}, related_name='VerificationResult_primarySource_validationStatus', blank=True)
    validationStatus_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    validationDate = FHIR_primitive_DateTimeField(null=True, blank=True, )
    BINDING_canPushUpdates = 'TODO'
    canPushUpdates_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_canPushUpdates}, related_name='VerificationResult_primarySource_canPushUpdates', blank=True)
    canPushUpdates_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_VerificationResult_primarySource_type(models.Model):
    VerificationResult_primarySource = models.ForeignKey(FHIR_VerificationResult_primarySource, related_name='VerificationResult_primarySource_type', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='VerificationResult_primarySource_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_VerificationResult_primarySource_communicationMethod(models.Model):
    VerificationResult_primarySource = models.ForeignKey(FHIR_VerificationResult_primarySource, related_name='VerificationResult_primarySource_communicationMethod', null=False, on_delete=models.CASCADE)
    BINDING_communicationMethod = 'TODO'
    communicationMethod_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_communicationMethod}, related_name='VerificationResult_primarySource_communicationMethod', blank=True)
    communicationMethod_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_VerificationResult_primarySource_pushTypeAvailable(models.Model):
    VerificationResult_primarySource = models.ForeignKey(FHIR_VerificationResult_primarySource, related_name='VerificationResult_primarySource_pushTypeAvailable', null=False, on_delete=models.CASCADE)
    BINDING_pushTypeAvailable = 'TODO'
    pushTypeAvailable_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_pushTypeAvailable}, related_name='VerificationResult_primarySource_pushTypeAvailable', blank=True)
    pushTypeAvailable_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_VerificationResult_attestation(models.Model):
    VerificationResult = models.ForeignKey(FHIR_VerificationResult, related_name='VerificationResult_attestation', null=False, on_delete=models.CASCADE)
    who_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="VerificationResult_attestation_who", null=True, blank=True, on_delete=models.SET_NULL)
    who_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="VerificationResult_attestation_who", null=True, blank=True, on_delete=models.SET_NULL)
    who_Organization = models.ForeignKey("FHIR_Organization", related_name="VerificationResult_attestation_who", null=True, blank=True, on_delete=models.SET_NULL)
    onBehalfOf_Organization = models.ForeignKey("FHIR_Organization", related_name="VerificationResult_attestation_onBehalfOf", null=True, blank=True, on_delete=models.SET_NULL)
    onBehalfOf_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="VerificationResult_attestation_onBehalfOf", null=True, blank=True, on_delete=models.SET_NULL)
    onBehalfOf_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="VerificationResult_attestation_onBehalfOf", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_communicationMethod = 'TODO'
    communicationMethod_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_communicationMethod}, related_name='VerificationResult_attestation_communicationMethod', blank=True)
    communicationMethod_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    date = FHIR_primitive_DateField(null=True, blank=True, )
    sourceIdentityCertificate = FHIR_primitive_StringField(null=True, blank=True, )
    proxyIdentityCertificate = FHIR_primitive_StringField(null=True, blank=True, )
    proxySignature = models.OneToOneField("FHIR_GP_Signature", related_name='VerificationResult_attestation_proxySignature', null=True, blank=True, on_delete=models.SET_NULL)
    sourceSignature = models.OneToOneField("FHIR_GP_Signature", related_name='VerificationResult_attestation_sourceSignature', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_VerificationResult_validator(models.Model):
    VerificationResult = models.ForeignKey(FHIR_VerificationResult, related_name='VerificationResult_validator', null=False, on_delete=models.CASCADE)
    organization = models.ForeignKey("FHIR_Organization", related_name="VerificationResult_validator_organization", null=True, blank=True, on_delete=models.SET_NULL)
    identityCertificate = FHIR_primitive_StringField(null=True, blank=True, )
    attestationSignature = models.OneToOneField("FHIR_GP_Signature", related_name='VerificationResult_validator_attestationSignature', null=True, blank=True, on_delete=models.SET_NULL)
