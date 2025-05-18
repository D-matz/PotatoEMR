#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_CoverageEligibilityRequest(models.Model):
    class StatusChoices(models.TextChoices): ACTIVE = 'active', 'Active'; CANCELLED = 'cancelled', 'Cancelled'; DRAFT = 'draft', 'Draft'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    BINDING_priority = "TODO"
    priority_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_priority}, related_name='CoverageEligibilityRequest_priority', blank=True)
    priority_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    patient = models.ForeignKey("FHIR_Patient", related_name="CoverageEligibilityRequest_patient", null=True, blank=True, on_delete=models.SET_NULL)
    serviced_date = FHIR_primitive_DateField(null=True, blank=True, )
    serviced_Period = models.OneToOneField("FHIR_GP_Period", related_name='CoverageEligibilityRequest_serviced_Period', null=True, blank=True, on_delete=models.SET_NULL)
    created = FHIR_primitive_DateTimeField(null=True, blank=True, )
    enterer_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="CoverageEligibilityRequest_enterer", null=True, blank=True, on_delete=models.SET_NULL)
    enterer_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="CoverageEligibilityRequest_enterer", null=True, blank=True, on_delete=models.SET_NULL)
    provider_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="CoverageEligibilityRequest_provider", null=True, blank=True, on_delete=models.SET_NULL)
    provider_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="CoverageEligibilityRequest_provider", null=True, blank=True, on_delete=models.SET_NULL)
    provider_Organization = models.ForeignKey("FHIR_Organization", related_name="CoverageEligibilityRequest_provider", null=True, blank=True, on_delete=models.SET_NULL)
    insurer = models.ForeignKey("FHIR_Organization", related_name="CoverageEligibilityRequest_insurer", null=True, blank=True, on_delete=models.SET_NULL)
    facility = models.ForeignKey("FHIR_Location", related_name="CoverageEligibilityRequest_facility", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_CoverageEligibilityRequest_identifier(FHIR_GP_Identifier):
    CoverageEligibilityRequest = models.ForeignKey(FHIR_CoverageEligibilityRequest, related_name='CoverageEligibilityRequest_identifier', null=False, on_delete=models.CASCADE)

class FHIR_CoverageEligibilityRequest_purpose(models.Model):
    CoverageEligibilityRequest = models.ForeignKey(FHIR_CoverageEligibilityRequest, related_name='CoverageEligibilityRequest_purpose', null=False, on_delete=models.CASCADE)
    
    class PurposeChoices(models.TextChoices): AUTH_REQUIREMENTS = 'auth-requirements', 'Auth-requirements'; BENEFITS = 'benefits', 'Benefits'; DISCOVERY = 'discovery', 'Discovery'; VALIDATION = 'validation', 'Validation'; 
    purpose = FHIR_primitive_CodeField(choices=PurposeChoices.choices, null=True, blank=True, )
    
class FHIR_CoverageEligibilityRequest_event(models.Model):
    CoverageEligibilityRequest = models.ForeignKey(FHIR_CoverageEligibilityRequest, related_name='CoverageEligibilityRequest_event', null=False, on_delete=models.CASCADE)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='CoverageEligibilityRequest_event_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    when_dateTime = FHIR_primitive_DateTimeField(null=True, blank=True, )
    when_Period = models.OneToOneField("FHIR_GP_Period", related_name='CoverageEligibilityRequest_event_when_Period', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_CoverageEligibilityRequest_supportingInfo(models.Model):
    CoverageEligibilityRequest = models.ForeignKey(FHIR_CoverageEligibilityRequest, related_name='CoverageEligibilityRequest_supportingInfo', null=False, on_delete=models.CASCADE)
    sequence = FHIR_primitive_PositiveIntField(null=True, blank=True, )
                            #skipping Reference(Any) for field information as CoverageEligibilityRequest information not in referenceAny_targets
    appliesToAll = FHIR_primitive_BooleanField(null=True, blank=True, )

class FHIR_CoverageEligibilityRequest_insurance(models.Model):
    CoverageEligibilityRequest = models.ForeignKey(FHIR_CoverageEligibilityRequest, related_name='CoverageEligibilityRequest_insurance', null=False, on_delete=models.CASCADE)
    focal = FHIR_primitive_BooleanField(null=True, blank=True, )
    coverage = models.ForeignKey("FHIR_Coverage", related_name="CoverageEligibilityRequest_insurance_coverage", null=True, blank=True, on_delete=models.SET_NULL)
    businessArrangement = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_CoverageEligibilityRequest_item(models.Model):
    CoverageEligibilityRequest = models.ForeignKey(FHIR_CoverageEligibilityRequest, related_name='CoverageEligibilityRequest_item', null=False, on_delete=models.CASCADE)
    BINDING_category = "TODO"
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='CoverageEligibilityRequest_item_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_productOrService = "TODO"
    productOrService_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_productOrService}, related_name='CoverageEligibilityRequest_item_productOrService', blank=True)
    productOrService_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    provider_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="CoverageEligibilityRequest_item_provider", null=True, blank=True, on_delete=models.SET_NULL)
    provider_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="CoverageEligibilityRequest_item_provider", null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='CoverageEligibilityRequest_item_quantity', null=True, blank=True, on_delete=models.SET_NULL)
    unitPrice = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='CoverageEligibilityRequest_item_unitPrice', null=True, blank=True, on_delete=models.SET_NULL)
    facility_Location = models.ForeignKey("FHIR_Location", related_name="CoverageEligibilityRequest_item_facility", null=True, blank=True, on_delete=models.SET_NULL)
    facility_Organization = models.ForeignKey("FHIR_Organization", related_name="CoverageEligibilityRequest_item_facility", null=True, blank=True, on_delete=models.SET_NULL)
                            #skipping Reference(Any) for field detail as CoverageEligibilityRequest detail not in referenceAny_targets

class FHIR_CoverageEligibilityRequest_item_supportingInfoSequence(models.Model):
    CoverageEligibilityRequest_item = models.ForeignKey(FHIR_CoverageEligibilityRequest_item, related_name='CoverageEligibilityRequest_item_supportingInfoSequence', null=False, on_delete=models.CASCADE)
    
    supportingInfoSequence = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    
class FHIR_CoverageEligibilityRequest_item_modifier(models.Model):
    CoverageEligibilityRequest_item = models.ForeignKey(FHIR_CoverageEligibilityRequest_item, related_name='CoverageEligibilityRequest_item_modifier', null=False, on_delete=models.CASCADE)
    BINDING_modifier = "TODO"
    modifier_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_modifier}, related_name='CoverageEligibilityRequest_item_modifier', blank=True)
    modifier_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_CoverageEligibilityRequest_item_diagnosis(models.Model):
    CoverageEligibilityRequest_item = models.ForeignKey(FHIR_CoverageEligibilityRequest_item, related_name='CoverageEligibilityRequest_item_diagnosis', null=False, on_delete=models.CASCADE)
    BINDING_diagnosis_CodeableConcept = "TODO"
    diagnosis_CodeableConcept_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_diagnosis_CodeableConcept}, related_name='CoverageEligibilityRequest_item_diagnosis_diagnosis_CodeableConcept', blank=True)
    diagnosis_CodeableConcept_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    diagnosis_Reference = models.ForeignKey("FHIR_Condition", related_name="CoverageEligibilityRequest_item_diagnosis_diagnosis_Reference", null=True, blank=True, on_delete=models.SET_NULL)
