#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Consent(models.Model):
    class StatusChoices(models.TextChoices): DRAFT = 'draft', 'Draft'; ACTIVE = 'active', 'Active'; INACTIVE = 'inactive', 'Inactive'; NOT_DONE = 'not-done', 'Not-done'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    subject_Patient = models.ForeignKey("FHIR_Patient", related_name="Consent_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="Consent_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_ResearchSubject = models.ForeignKey("FHIR_ResearchSubject", related_name="Consent_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Group = models.ForeignKey("FHIR_Group", related_name="Consent_subject", null=True, blank=True, on_delete=models.SET_NULL)
    date = FHIR_primitive_DateField(null=True, blank=True, )
    period = models.OneToOneField("FHIR_GP_Period", related_name='Consent_period', null=True, blank=True, on_delete=models.SET_NULL)
    grantor_CareTeam = models.ManyToManyField("FHIR_CareTeam", related_name="Consent_grantor", blank=True)
    grantor_Group = models.ManyToManyField("FHIR_Group", related_name="Consent_grantor", blank=True)
    grantor_HealthcareService = models.ManyToManyField("FHIR_HealthcareService", related_name="Consent_grantor", blank=True)
    grantor_Organization = models.ManyToManyField("FHIR_Organization", related_name="Consent_grantor", blank=True)
    grantor_Patient = models.ManyToManyField("FHIR_Patient", related_name="Consent_grantor", blank=True)
    grantor_Practitioner = models.ManyToManyField("FHIR_Practitioner", related_name="Consent_grantor", blank=True)
    grantor_RelatedPerson = models.ManyToManyField("FHIR_RelatedPerson", related_name="Consent_grantor", blank=True)
    grantor_PractitionerRole = models.ManyToManyField("FHIR_PractitionerRole", related_name="Consent_grantor", blank=True)
    grantee_CareTeam = models.ManyToManyField("FHIR_CareTeam", related_name="Consent_grantee", blank=True)
    grantee_Group = models.ManyToManyField("FHIR_Group", related_name="Consent_grantee", blank=True)
    grantee_HealthcareService = models.ManyToManyField("FHIR_HealthcareService", related_name="Consent_grantee", blank=True)
    grantee_Organization = models.ManyToManyField("FHIR_Organization", related_name="Consent_grantee", blank=True)
    grantee_Patient = models.ManyToManyField("FHIR_Patient", related_name="Consent_grantee", blank=True)
    grantee_Practitioner = models.ManyToManyField("FHIR_Practitioner", related_name="Consent_grantee", blank=True)
    grantee_RelatedPerson = models.ManyToManyField("FHIR_RelatedPerson", related_name="Consent_grantee", blank=True)
    grantee_PractitionerRole = models.ManyToManyField("FHIR_PractitionerRole", related_name="Consent_grantee", blank=True)
    manager_HealthcareService = models.ManyToManyField("FHIR_HealthcareService", related_name="Consent_manager", blank=True)
    manager_Organization = models.ManyToManyField("FHIR_Organization", related_name="Consent_manager", blank=True)
    manager_Patient = models.ManyToManyField("FHIR_Patient", related_name="Consent_manager", blank=True)
    manager_Practitioner = models.ManyToManyField("FHIR_Practitioner", related_name="Consent_manager", blank=True)
    controller_HealthcareService = models.ManyToManyField("FHIR_HealthcareService", related_name="Consent_controller", blank=True)
    controller_Organization = models.ManyToManyField("FHIR_Organization", related_name="Consent_controller", blank=True)
    controller_Patient = models.ManyToManyField("FHIR_Patient", related_name="Consent_controller", blank=True)
    controller_Practitioner = models.ManyToManyField("FHIR_Practitioner", related_name="Consent_controller", blank=True)
    sourceReference_Consent = models.ManyToManyField("FHIR_Consent", related_name="Consent_sourceReference", blank=True)
    sourceReference_DocumentReference = models.ManyToManyField("FHIR_DocumentReference", related_name="Consent_sourceReference", blank=True)
    sourceReference_Contract = models.ManyToManyField("FHIR_Contract", related_name="Consent_sourceReference", blank=True)
    sourceReference_QuestionnaireResponse = models.ManyToManyField("FHIR_QuestionnaireResponse", related_name="Consent_sourceReference", blank=True)
    policyText = models.ManyToManyField("FHIR_DocumentReference", related_name="Consent_policyText", blank=True)
    class DecisionChoices(models.TextChoices): DENY = 'deny', 'Deny'; PERMIT = 'permit', 'Permit'; 
    decision = FHIR_primitive_CodeField(choices=DecisionChoices.choices, null=True, blank=True, )
    provisionReference = models.ManyToManyField("FHIR_Permission", related_name="Consent_provisionReference", blank=True)

class FHIR_Consent_identifier(FHIR_GP_Identifier):
    Consent = models.ForeignKey(FHIR_Consent, related_name='Consent_identifier', null=False, on_delete=models.CASCADE)

class FHIR_Consent_category(models.Model):
    Consent = models.ForeignKey(FHIR_Consent, related_name='Consent_category', null=False, on_delete=models.CASCADE)
    BINDING_category = "TODO"
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='Consent_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Consent_sourceAttachment(FHIR_GP_Attachment):
    Consent = models.ForeignKey(FHIR_Consent, related_name='Consent_sourceAttachment', null=False, on_delete=models.CASCADE)

class FHIR_Consent_regulatoryBasis(models.Model):
    Consent = models.ForeignKey(FHIR_Consent, related_name='Consent_regulatoryBasis', null=False, on_delete=models.CASCADE)
    BINDING_regulatoryBasis = "TODO"
    regulatoryBasis_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_regulatoryBasis}, related_name='Consent_regulatoryBasis', blank=True)
    regulatoryBasis_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Consent_policyBasis(models.Model):
    Consent = models.ForeignKey(FHIR_Consent, related_name='Consent_policyBasis', null=False, on_delete=models.CASCADE)
    uri = FHIR_primitive_URIField(null=True, blank=True, )

class FHIR_Consent_verification(models.Model):
    Consent = models.ForeignKey(FHIR_Consent, related_name='Consent_verification', null=False, on_delete=models.CASCADE)
    verified = FHIR_primitive_BooleanField(null=True, blank=True, )
    BINDING_verificationType = "TODO"
    verificationType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_verificationType}, related_name='Consent_verification_verificationType', blank=True)
    verificationType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    verifiedBy_Organization = models.ForeignKey("FHIR_Organization", related_name="Consent_verification_verifiedBy", null=True, blank=True, on_delete=models.SET_NULL)
    verifiedBy_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="Consent_verification_verifiedBy", null=True, blank=True, on_delete=models.SET_NULL)
    verifiedBy_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="Consent_verification_verifiedBy", null=True, blank=True, on_delete=models.SET_NULL)
    verifiedWith_Patient = models.ForeignKey("FHIR_Patient", related_name="Consent_verification_verifiedWith", null=True, blank=True, on_delete=models.SET_NULL)
    verifiedWith_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="Consent_verification_verifiedWith", null=True, blank=True, on_delete=models.SET_NULL)
    verifiedWith_Group = models.ForeignKey("FHIR_Group", related_name="Consent_verification_verifiedWith", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Consent_verification_verificationDate(models.Model):
    Consent_verification = models.ForeignKey(FHIR_Consent_verification, related_name='Consent_verification_verificationDate', null=False, on_delete=models.CASCADE)
    
    verificationDate = FHIR_primitive_DateTimeField(null=True, blank=True, )
    
class FHIR_Consent_provision(models.Model):
    Consent = models.ForeignKey(FHIR_Consent, related_name='Consent_provision', null=False, on_delete=models.CASCADE)
    period = models.OneToOneField("FHIR_GP_Period", related_name='Consent_provision_period', null=True, blank=True, on_delete=models.SET_NULL)
    dataPeriod = models.OneToOneField("FHIR_GP_Period", related_name='Consent_provision_dataPeriod', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Consent_provision_actor(models.Model):
    Consent_provision = models.ForeignKey(FHIR_Consent_provision, related_name='Consent_provision_actor', null=False, on_delete=models.CASCADE)
    BINDING_role = "TODO"
    role_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_role}, related_name='Consent_provision_actor_role', blank=True)
    role_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    reference_Device = models.ForeignKey("FHIR_Device", related_name="Consent_provision_actor_reference", null=True, blank=True, on_delete=models.SET_NULL)
    reference_Group = models.ForeignKey("FHIR_Group", related_name="Consent_provision_actor_reference", null=True, blank=True, on_delete=models.SET_NULL)
    reference_CareTeam = models.ForeignKey("FHIR_CareTeam", related_name="Consent_provision_actor_reference", null=True, blank=True, on_delete=models.SET_NULL)
    reference_Organization = models.ForeignKey("FHIR_Organization", related_name="Consent_provision_actor_reference", null=True, blank=True, on_delete=models.SET_NULL)
    reference_Patient = models.ForeignKey("FHIR_Patient", related_name="Consent_provision_actor_reference", null=True, blank=True, on_delete=models.SET_NULL)
    reference_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="Consent_provision_actor_reference", null=True, blank=True, on_delete=models.SET_NULL)
    reference_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="Consent_provision_actor_reference", null=True, blank=True, on_delete=models.SET_NULL)
    reference_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="Consent_provision_actor_reference", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Consent_provision_action(models.Model):
    Consent_provision = models.ForeignKey(FHIR_Consent_provision, related_name='Consent_provision_action', null=False, on_delete=models.CASCADE)
    BINDING_action = "TODO"
    action_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_action}, related_name='Consent_provision_action', blank=True)
    action_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Consent_provision_securityLabel(FHIR_GP_Coding):
    Consent_provision = models.ForeignKey(FHIR_Consent_provision, related_name='Consent_provision_securityLabel', null=False, on_delete=models.CASCADE)

class FHIR_Consent_provision_purpose(FHIR_GP_Coding):
    Consent_provision = models.ForeignKey(FHIR_Consent_provision, related_name='Consent_provision_purpose', null=False, on_delete=models.CASCADE)

class FHIR_Consent_provision_documentType(FHIR_GP_Coding):
    Consent_provision = models.ForeignKey(FHIR_Consent_provision, related_name='Consent_provision_documentType', null=False, on_delete=models.CASCADE)

class FHIR_Consent_provision_resourceType(FHIR_GP_Coding):
    Consent_provision = models.ForeignKey(FHIR_Consent_provision, related_name='Consent_provision_resourceType', null=False, on_delete=models.CASCADE)

class FHIR_Consent_provision_code(models.Model):
    Consent_provision = models.ForeignKey(FHIR_Consent_provision, related_name='Consent_provision_code', null=False, on_delete=models.CASCADE)
    BINDING_code = "TODO"
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='Consent_provision_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Consent_provision_data(models.Model):
    Consent_provision = models.ForeignKey(FHIR_Consent_provision, related_name='Consent_provision_data', null=False, on_delete=models.CASCADE)
    class MeaningChoices(models.TextChoices): INSTANCE = 'instance', 'Instance'; RELATED = 'related', 'Related'; DEPENDENTS = 'dependents', 'Dependents'; AUTHOREDBY = 'authoredby', 'Authoredby'; 
    meaning = FHIR_primitive_CodeField(choices=MeaningChoices.choices, null=True, blank=True, )
