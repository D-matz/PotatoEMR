
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_CoverageEligibilityResponse(models.Model):
    class StatusChoices(models.TextChoices): ACTIVE = 'active', 'Active'; CANCELLED = 'cancelled', 'Cancelled'; DRAFT = 'draft', 'Draft'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    patient = models.ForeignKey("FHIR_Patient", related_name="CoverageEligibilityResponse_patient", null=True, blank=True, on_delete=models.SET_NULL)
    serviced = FHIR_primitive_DateField(null=True, blank=True, )
    serviced = models.OneToOneField("FHIR_GP_Period", related_name='CoverageEligibilityResponse_serviced', null=True, blank=True, on_delete=models.SET_NULL)
    created = FHIR_primitive_DateTimeField(null=True, blank=True, )
    requestor_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="CoverageEligibilityResponse_requestor", null=True, blank=True, on_delete=models.SET_NULL)
    requestor_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="CoverageEligibilityResponse_requestor", null=True, blank=True, on_delete=models.SET_NULL)
    requestor_Organization = models.ForeignKey("FHIR_Organization", related_name="CoverageEligibilityResponse_requestor", null=True, blank=True, on_delete=models.SET_NULL)
    request = models.ForeignKey("FHIR_CoverageEligibilityRequest", related_name="CoverageEligibilityResponse_request", null=True, blank=True, on_delete=models.SET_NULL)
    class OutcomeChoices(models.TextChoices): QUEUED = 'queued', 'Queued'; COMPLETE = 'complete', 'Complete'; ERROR = 'error', 'Error'; PARTIAL = 'partial', 'Partial'; 
    outcome = FHIR_primitive_CodeField(choices=OutcomeChoices.choices, null=True, blank=True, )
    disposition = FHIR_primitive_StringField(null=True, blank=True, )
    insurer = models.ForeignKey("FHIR_Organization", related_name="CoverageEligibilityResponse_insurer", null=True, blank=True, on_delete=models.SET_NULL)
    preAuthRef = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_form = 'TODO'
    form_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_form}, related_name='CoverageEligibilityResponse_form', blank=True)
    form_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_CoverageEligibilityResponse_identifier(FHIR_GP_Identifier):
    CoverageEligibilityResponse = models.ForeignKey(FHIR_CoverageEligibilityResponse, related_name='CoverageEligibilityResponse_identifier', null=False, on_delete=models.CASCADE)

class FHIR_CoverageEligibilityResponse_purpose(models.Model):
    CoverageEligibilityResponse = models.ForeignKey(FHIR_CoverageEligibilityResponse, related_name='CoverageEligibilityResponse_purpose', null=False, on_delete=models.CASCADE)
    
    class PurposeChoices(models.TextChoices): AUTH_REQUIREMENTS = 'auth-requirements', 'Auth-requirements'; BENEFITS = 'benefits', 'Benefits'; DISCOVERY = 'discovery', 'Discovery'; VALIDATION = 'validation', 'Validation'; 
    purpose = FHIR_primitive_CodeField(choices=PurposeChoices.choices, null=True, blank=True, )
    
class FHIR_CoverageEligibilityResponse_event(models.Model):
    CoverageEligibilityResponse = models.ForeignKey(FHIR_CoverageEligibilityResponse, related_name='CoverageEligibilityResponse_event', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='CoverageEligibilityResponse_event_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    when = FHIR_primitive_DateTimeField(null=True, blank=True, )
    when = models.OneToOneField("FHIR_GP_Period", related_name='CoverageEligibilityResponse_event_when', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_CoverageEligibilityResponse_insurance(models.Model):
    CoverageEligibilityResponse = models.ForeignKey(FHIR_CoverageEligibilityResponse, related_name='CoverageEligibilityResponse_insurance', null=False, on_delete=models.CASCADE)
    coverage = models.ForeignKey("FHIR_Coverage", related_name="CoverageEligibilityResponse_insurance_coverage", null=True, blank=True, on_delete=models.SET_NULL)
    inforce = FHIR_primitive_BooleanField(null=True, blank=True, )
    benefitPeriod = models.OneToOneField("FHIR_GP_Period", related_name='CoverageEligibilityResponse_insurance_benefitPeriod', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_CoverageEligibilityResponse_insurance_item(models.Model):
    CoverageEligibilityResponse_insurance = models.ForeignKey(FHIR_CoverageEligibilityResponse_insurance, related_name='CoverageEligibilityResponse_insurance_item', null=False, on_delete=models.CASCADE)
    BINDING_category = 'TODO'
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='CoverageEligibilityResponse_insurance_item_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_productOrService = 'TODO'
    productOrService_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_productOrService}, related_name='CoverageEligibilityResponse_insurance_item_productOrService', blank=True)
    productOrService_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    provider_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="CoverageEligibilityResponse_insurance_item_provider", null=True, blank=True, on_delete=models.SET_NULL)
    provider_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="CoverageEligibilityResponse_insurance_item_provider", null=True, blank=True, on_delete=models.SET_NULL)
    excluded = FHIR_primitive_BooleanField(null=True, blank=True, )
    name = FHIR_primitive_StringField(null=True, blank=True, )
    description = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_network = 'TODO'
    network_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_network}, related_name='CoverageEligibilityResponse_insurance_item_network', blank=True)
    network_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_unit = 'TODO'
    unit_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_unit}, related_name='CoverageEligibilityResponse_insurance_item_unit', blank=True)
    unit_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_term = 'TODO'
    term_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_term}, related_name='CoverageEligibilityResponse_insurance_item_term', blank=True)
    term_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    authorizationRequired = FHIR_primitive_BooleanField(null=True, blank=True, )
    authorizationUrl = FHIR_primitive_URIField(null=True, blank=True, )

class FHIR_CoverageEligibilityResponse_insurance_item_modifier(models.Model):
    CoverageEligibilityResponse_insurance_item = models.ForeignKey(FHIR_CoverageEligibilityResponse_insurance_item, related_name='CoverageEligibilityResponse_insurance_item_modifier', null=False, on_delete=models.CASCADE)
    BINDING_modifier = 'TODO'
    modifier_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_modifier}, related_name='CoverageEligibilityResponse_insurance_item_modifier', blank=True)
    modifier_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_CoverageEligibilityResponse_insurance_item_benefit(models.Model):
    CoverageEligibilityResponse_insurance_item = models.ForeignKey(FHIR_CoverageEligibilityResponse_insurance_item, related_name='CoverageEligibilityResponse_insurance_item_benefit', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='CoverageEligibilityResponse_insurance_item_benefit_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    allowed = FHIR_primitive_UnsignedIntField(null=True, blank=True, )
    allowed = FHIR_primitive_StringField(null=True, blank=True, )
    allowed = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='CoverageEligibilityResponse_insurance_item_benefit_allowed', null=True, blank=True, on_delete=models.SET_NULL)
    used = FHIR_primitive_UnsignedIntField(null=True, blank=True, )
    used = FHIR_primitive_StringField(null=True, blank=True, )
    used = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='CoverageEligibilityResponse_insurance_item_benefit_used', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_CoverageEligibilityResponse_insurance_item_authorizationSupporting(models.Model):
    CoverageEligibilityResponse_insurance_item = models.ForeignKey(FHIR_CoverageEligibilityResponse_insurance_item, related_name='CoverageEligibilityResponse_insurance_item_authorizationSupporting', null=False, on_delete=models.CASCADE)
    BINDING_authorizationSupporting = 'TODO'
    authorizationSupporting_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_authorizationSupporting}, related_name='CoverageEligibilityResponse_insurance_item_authorizationSupporting', blank=True)
    authorizationSupporting_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_CoverageEligibilityResponse_error(models.Model):
    CoverageEligibilityResponse = models.ForeignKey(FHIR_CoverageEligibilityResponse, related_name='CoverageEligibilityResponse_error', null=False, on_delete=models.CASCADE)
    BINDING_code = 'TODO'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='CoverageEligibilityResponse_error_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_CoverageEligibilityResponse_error_expression(models.Model):
    CoverageEligibilityResponse_error = models.ForeignKey(FHIR_CoverageEligibilityResponse_error, related_name='CoverageEligibilityResponse_error_expression', null=False, on_delete=models.CASCADE)
    
    expression = FHIR_primitive_StringField(null=True, blank=True, )
    