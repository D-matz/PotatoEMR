#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_ExplanationOfBenefit(models.Model):
    class StatusChoices(models.TextChoices): ACTIVE = 'active', 'Active'; CANCELLED = 'cancelled', 'Cancelled'; DRAFT = 'draft', 'Draft'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='ExplanationOfBenefit_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_subType = "TODO"
    subType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_subType}, related_name='ExplanationOfBenefit_subType', blank=True)
    subType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    class UseChoices(models.TextChoices): CLAIM = 'claim', 'Claim'; PREAUTHORIZATION = 'preauthorization', 'Preauthorization'; PREDETERMINATION = 'predetermination', 'Predetermination'; 
    use = FHIR_primitive_CodeField(choices=UseChoices.choices, null=True, blank=True, )
    patient = models.ForeignKey("FHIR_Patient", related_name="ExplanationOfBenefit_patient", null=True, blank=True, on_delete=models.SET_NULL)
    billablePeriod = models.OneToOneField("FHIR_GP_Period", related_name='ExplanationOfBenefit_billablePeriod', null=True, blank=True, on_delete=models.SET_NULL)
    created = FHIR_primitive_DateTimeField(null=True, blank=True, )
    enterer_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="ExplanationOfBenefit_enterer", null=True, blank=True, on_delete=models.SET_NULL)
    enterer_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="ExplanationOfBenefit_enterer", null=True, blank=True, on_delete=models.SET_NULL)
    enterer_Patient = models.ForeignKey("FHIR_Patient", related_name="ExplanationOfBenefit_enterer", null=True, blank=True, on_delete=models.SET_NULL)
    enterer_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="ExplanationOfBenefit_enterer", null=True, blank=True, on_delete=models.SET_NULL)
    insurer = models.ForeignKey("FHIR_Organization", related_name="ExplanationOfBenefit_insurer", null=True, blank=True, on_delete=models.SET_NULL)
    provider_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="ExplanationOfBenefit_provider", null=True, blank=True, on_delete=models.SET_NULL)
    provider_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="ExplanationOfBenefit_provider", null=True, blank=True, on_delete=models.SET_NULL)
    provider_Organization = models.ForeignKey("FHIR_Organization", related_name="ExplanationOfBenefit_provider", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_priority = "TODO"
    priority_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_priority}, related_name='ExplanationOfBenefit_priority', blank=True)
    priority_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_fundsReserveRequested = "TODO"
    fundsReserveRequested_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_fundsReserveRequested}, related_name='ExplanationOfBenefit_fundsReserveRequested', blank=True)
    fundsReserveRequested_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_fundsReserve = "TODO"
    fundsReserve_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_fundsReserve}, related_name='ExplanationOfBenefit_fundsReserve', blank=True)
    fundsReserve_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    prescription_MedicationRequest = models.ForeignKey("FHIR_MedicationRequest", related_name="ExplanationOfBenefit_prescription", null=True, blank=True, on_delete=models.SET_NULL)
    prescription_VisionPrescription = models.ForeignKey("FHIR_VisionPrescription", related_name="ExplanationOfBenefit_prescription", null=True, blank=True, on_delete=models.SET_NULL)
    originalPrescription = models.ForeignKey("FHIR_MedicationRequest", related_name="ExplanationOfBenefit_originalPrescription", null=True, blank=True, on_delete=models.SET_NULL)
    referral = models.ForeignKey("FHIR_ServiceRequest", related_name="ExplanationOfBenefit_referral", null=True, blank=True, on_delete=models.SET_NULL)
    encounter = models.ManyToManyField("FHIR_Encounter", related_name="ExplanationOfBenefit_encounter", blank=True)
    facility_Location = models.ForeignKey("FHIR_Location", related_name="ExplanationOfBenefit_facility", null=True, blank=True, on_delete=models.SET_NULL)
    facility_Organization = models.ForeignKey("FHIR_Organization", related_name="ExplanationOfBenefit_facility", null=True, blank=True, on_delete=models.SET_NULL)
    claim = models.ForeignKey("FHIR_Claim", related_name="ExplanationOfBenefit_claim", null=True, blank=True, on_delete=models.SET_NULL)
    claimResponse = models.ForeignKey("FHIR_ClaimResponse", related_name="ExplanationOfBenefit_claimResponse", null=True, blank=True, on_delete=models.SET_NULL)
    class OutcomeChoices(models.TextChoices): QUEUED = 'queued', 'Queued'; COMPLETE = 'complete', 'Complete'; ERROR = 'error', 'Error'; PARTIAL = 'partial', 'Partial'; 
    outcome = FHIR_primitive_CodeField(choices=OutcomeChoices.choices, null=True, blank=True, )
    BINDING_decision = "TODO"
    decision_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_decision}, related_name='ExplanationOfBenefit_decision', blank=True)
    decision_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    disposition = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_diagnosisRelatedGroup = "TODO"
    diagnosisRelatedGroup_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_diagnosisRelatedGroup}, related_name='ExplanationOfBenefit_diagnosisRelatedGroup', blank=True)
    diagnosisRelatedGroup_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    precedence = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    patientPaid = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='ExplanationOfBenefit_patientPaid', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_formCode = "TODO"
    formCode_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_formCode}, related_name='ExplanationOfBenefit_formCode', blank=True)
    formCode_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    form = models.OneToOneField("FHIR_GP_Attachment", related_name='ExplanationOfBenefit_form', null=True, blank=True, on_delete=models.SET_NULL)
    benefitPeriod = models.OneToOneField("FHIR_GP_Period", related_name='ExplanationOfBenefit_benefitPeriod', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ExplanationOfBenefit_identifier(FHIR_GP_Identifier):
    ExplanationOfBenefit = models.ForeignKey(FHIR_ExplanationOfBenefit, related_name='ExplanationOfBenefit_identifier', null=False, on_delete=models.CASCADE)

class FHIR_ExplanationOfBenefit_traceNumber(FHIR_GP_Identifier):
    ExplanationOfBenefit = models.ForeignKey(FHIR_ExplanationOfBenefit, related_name='ExplanationOfBenefit_traceNumber', null=False, on_delete=models.CASCADE)

class FHIR_ExplanationOfBenefit_related(models.Model):
    ExplanationOfBenefit = models.ForeignKey(FHIR_ExplanationOfBenefit, related_name='ExplanationOfBenefit_related', null=False, on_delete=models.CASCADE)
    claim = models.ForeignKey("FHIR_Claim", related_name="ExplanationOfBenefit_related_claim", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_relationship = "TODO"
    relationship_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_relationship}, related_name='ExplanationOfBenefit_related_relationship', blank=True)
    relationship_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    reference = models.OneToOneField("FHIR_GP_Identifier", related_name='ExplanationOfBenefit_related_reference', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ExplanationOfBenefit_event(models.Model):
    ExplanationOfBenefit = models.ForeignKey(FHIR_ExplanationOfBenefit, related_name='ExplanationOfBenefit_event', null=False, on_delete=models.CASCADE)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='ExplanationOfBenefit_event_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    when = FHIR_primitive_DateTimeField(null=True, blank=True, )
    when = models.OneToOneField("FHIR_GP_Period", related_name='ExplanationOfBenefit_event_when', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ExplanationOfBenefit_payee(models.Model):
    ExplanationOfBenefit = models.ForeignKey(FHIR_ExplanationOfBenefit, related_name='ExplanationOfBenefit_payee', null=False, on_delete=models.CASCADE)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='ExplanationOfBenefit_payee_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    party_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="ExplanationOfBenefit_payee_party", null=True, blank=True, on_delete=models.SET_NULL)
    party_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="ExplanationOfBenefit_payee_party", null=True, blank=True, on_delete=models.SET_NULL)
    party_Organization = models.ForeignKey("FHIR_Organization", related_name="ExplanationOfBenefit_payee_party", null=True, blank=True, on_delete=models.SET_NULL)
    party_Patient = models.ForeignKey("FHIR_Patient", related_name="ExplanationOfBenefit_payee_party", null=True, blank=True, on_delete=models.SET_NULL)
    party_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="ExplanationOfBenefit_payee_party", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ExplanationOfBenefit_preAuthRef(models.Model):
    ExplanationOfBenefit = models.ForeignKey(FHIR_ExplanationOfBenefit, related_name='ExplanationOfBenefit_preAuthRef', null=False, on_delete=models.CASCADE)
    
    preAuthRef = FHIR_primitive_StringField(null=True, blank=True, )
    
class FHIR_ExplanationOfBenefit_preAuthRefPeriod(FHIR_GP_Period):
    ExplanationOfBenefit = models.ForeignKey(FHIR_ExplanationOfBenefit, related_name='ExplanationOfBenefit_preAuthRefPeriod', null=False, on_delete=models.CASCADE)

class FHIR_ExplanationOfBenefit_careTeam(models.Model):
    ExplanationOfBenefit = models.ForeignKey(FHIR_ExplanationOfBenefit, related_name='ExplanationOfBenefit_careTeam', null=False, on_delete=models.CASCADE)
    sequence = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    provider_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="ExplanationOfBenefit_careTeam_provider", null=True, blank=True, on_delete=models.SET_NULL)
    provider_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="ExplanationOfBenefit_careTeam_provider", null=True, blank=True, on_delete=models.SET_NULL)
    provider_Organization = models.ForeignKey("FHIR_Organization", related_name="ExplanationOfBenefit_careTeam_provider", null=True, blank=True, on_delete=models.SET_NULL)
    responsible = FHIR_primitive_BooleanField(null=True, blank=True, )
    BINDING_role = "TODO"
    role_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_role}, related_name='ExplanationOfBenefit_careTeam_role', blank=True)
    role_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_specialty = "TODO"
    specialty_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_specialty}, related_name='ExplanationOfBenefit_careTeam_specialty', blank=True)
    specialty_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_ExplanationOfBenefit_supportingInfo(models.Model):
    ExplanationOfBenefit = models.ForeignKey(FHIR_ExplanationOfBenefit, related_name='ExplanationOfBenefit_supportingInfo', null=False, on_delete=models.CASCADE)
    sequence = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    BINDING_category = "TODO"
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='ExplanationOfBenefit_supportingInfo_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_code = "TODO"
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='ExplanationOfBenefit_supportingInfo_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    timing = FHIR_primitive_DateField(null=True, blank=True, )
    timing = models.OneToOneField("FHIR_GP_Period", related_name='ExplanationOfBenefit_supportingInfo_timing', null=True, blank=True, on_delete=models.SET_NULL)
    value = FHIR_primitive_BooleanField(null=True, blank=True, )
    value = FHIR_primitive_StringField(null=True, blank=True, )
    value = models.OneToOneField("FHIR_GP_Quantity", related_name='ExplanationOfBenefit_supportingInfo_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_Attachment", related_name='ExplanationOfBenefit_supportingInfo_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_Identifier", related_name='ExplanationOfBenefit_supportingInfo_value', null=True, blank=True, on_delete=models.SET_NULL)
    reason = models.OneToOneField("FHIR_GP_Coding", related_name='ExplanationOfBenefit_supportingInfo_reason', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ExplanationOfBenefit_diagnosis(models.Model):
    ExplanationOfBenefit = models.ForeignKey(FHIR_ExplanationOfBenefit, related_name='ExplanationOfBenefit_diagnosis', null=False, on_delete=models.CASCADE)
    sequence = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    BINDING_diagnosis = "TODO"
    diagnosis_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_diagnosis}, related_name='ExplanationOfBenefit_diagnosis_diagnosis', blank=True)
    diagnosis_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    diagnosis = models.ForeignKey("FHIR_Condition", related_name="ExplanationOfBenefit_diagnosis_diagnosis", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_onAdmission = "TODO"
    onAdmission_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_onAdmission}, related_name='ExplanationOfBenefit_diagnosis_onAdmission', blank=True)
    onAdmission_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_ExplanationOfBenefit_diagnosis_type(models.Model):
    ExplanationOfBenefit_diagnosis = models.ForeignKey(FHIR_ExplanationOfBenefit_diagnosis, related_name='ExplanationOfBenefit_diagnosis_type', null=False, on_delete=models.CASCADE)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='ExplanationOfBenefit_diagnosis_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ExplanationOfBenefit_procedure(models.Model):
    ExplanationOfBenefit = models.ForeignKey(FHIR_ExplanationOfBenefit, related_name='ExplanationOfBenefit_procedure', null=False, on_delete=models.CASCADE)
    sequence = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    date = FHIR_primitive_DateTimeField(null=True, blank=True, )
    BINDING_procedure = "TODO"
    procedure_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_procedure}, related_name='ExplanationOfBenefit_procedure_procedure', blank=True)
    procedure_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    procedure = models.ForeignKey("FHIR_Procedure", related_name="ExplanationOfBenefit_procedure_procedure", null=True, blank=True, on_delete=models.SET_NULL)
    udi = models.ManyToManyField("FHIR_Device", related_name="ExplanationOfBenefit_procedure_udi", blank=True)

class FHIR_ExplanationOfBenefit_procedure_type(models.Model):
    ExplanationOfBenefit_procedure = models.ForeignKey(FHIR_ExplanationOfBenefit_procedure, related_name='ExplanationOfBenefit_procedure_type', null=False, on_delete=models.CASCADE)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='ExplanationOfBenefit_procedure_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ExplanationOfBenefit_insurance(models.Model):
    ExplanationOfBenefit = models.ForeignKey(FHIR_ExplanationOfBenefit, related_name='ExplanationOfBenefit_insurance', null=False, on_delete=models.CASCADE)
    focal = FHIR_primitive_BooleanField(null=True, blank=True, )
    coverage = models.ForeignKey("FHIR_Coverage", related_name="ExplanationOfBenefit_insurance_coverage", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ExplanationOfBenefit_insurance_preAuthRef(models.Model):
    ExplanationOfBenefit_insurance = models.ForeignKey(FHIR_ExplanationOfBenefit_insurance, related_name='ExplanationOfBenefit_insurance_preAuthRef', null=False, on_delete=models.CASCADE)
    
    preAuthRef = FHIR_primitive_StringField(null=True, blank=True, )
    
class FHIR_ExplanationOfBenefit_accident(models.Model):
    ExplanationOfBenefit = models.ForeignKey(FHIR_ExplanationOfBenefit, related_name='ExplanationOfBenefit_accident', null=False, on_delete=models.CASCADE)
    date = FHIR_primitive_DateField(null=True, blank=True, )
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='ExplanationOfBenefit_accident_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    location = models.OneToOneField("FHIR_GP_Address", related_name='ExplanationOfBenefit_accident_location', null=True, blank=True, on_delete=models.SET_NULL)
    location = models.ForeignKey("FHIR_Location", related_name="ExplanationOfBenefit_accident_location", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ExplanationOfBenefit_item(models.Model):
    ExplanationOfBenefit = models.ForeignKey(FHIR_ExplanationOfBenefit, related_name='ExplanationOfBenefit_item', null=False, on_delete=models.CASCADE)
    sequence = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    BINDING_revenue = "TODO"
    revenue_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_revenue}, related_name='ExplanationOfBenefit_item_revenue', blank=True)
    revenue_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_category = "TODO"
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='ExplanationOfBenefit_item_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_productOrService = "TODO"
    productOrService_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_productOrService}, related_name='ExplanationOfBenefit_item_productOrService', blank=True)
    productOrService_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_productOrServiceEnd = "TODO"
    productOrServiceEnd_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_productOrServiceEnd}, related_name='ExplanationOfBenefit_item_productOrServiceEnd', blank=True)
    productOrServiceEnd_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    request_DeviceRequest = models.ManyToManyField("FHIR_DeviceRequest", related_name="ExplanationOfBenefit_item_request", blank=True)
    request_MedicationRequest = models.ManyToManyField("FHIR_MedicationRequest", related_name="ExplanationOfBenefit_item_request", blank=True)
    request_NutritionOrder = models.ManyToManyField("FHIR_NutritionOrder", related_name="ExplanationOfBenefit_item_request", blank=True)
    request_ServiceRequest = models.ManyToManyField("FHIR_ServiceRequest", related_name="ExplanationOfBenefit_item_request", blank=True)
    request_SupplyRequest = models.ManyToManyField("FHIR_SupplyRequest", related_name="ExplanationOfBenefit_item_request", blank=True)
    request_VisionPrescription = models.ManyToManyField("FHIR_VisionPrescription", related_name="ExplanationOfBenefit_item_request", blank=True)
    serviced = FHIR_primitive_DateField(null=True, blank=True, )
    serviced = models.OneToOneField("FHIR_GP_Period", related_name='ExplanationOfBenefit_item_serviced', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_location = "TODO"
    location_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_location}, related_name='ExplanationOfBenefit_item_location', blank=True)
    location_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    location = models.OneToOneField("FHIR_GP_Address", related_name='ExplanationOfBenefit_item_location', null=True, blank=True, on_delete=models.SET_NULL)
    location = models.ForeignKey("FHIR_Location", related_name="ExplanationOfBenefit_item_location", null=True, blank=True, on_delete=models.SET_NULL)
    patientPaid = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='ExplanationOfBenefit_item_patientPaid', null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='ExplanationOfBenefit_item_quantity', null=True, blank=True, on_delete=models.SET_NULL)
    unitPrice = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='ExplanationOfBenefit_item_unitPrice', null=True, blank=True, on_delete=models.SET_NULL)
    factor = FHIR_primitive_DecimalField(null=True, blank=True, )
    tax = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='ExplanationOfBenefit_item_tax', null=True, blank=True, on_delete=models.SET_NULL)
    net = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='ExplanationOfBenefit_item_net', null=True, blank=True, on_delete=models.SET_NULL)
    udi = models.ManyToManyField("FHIR_Device", related_name="ExplanationOfBenefit_item_udi", blank=True)
    encounter = models.ManyToManyField("FHIR_Encounter", related_name="ExplanationOfBenefit_item_encounter", blank=True)

class FHIR_ExplanationOfBenefit_item_careTeamSequence(models.Model):
    ExplanationOfBenefit_item = models.ForeignKey(FHIR_ExplanationOfBenefit_item, related_name='ExplanationOfBenefit_item_careTeamSequence', null=False, on_delete=models.CASCADE)
    
    careTeamSequence = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    
class FHIR_ExplanationOfBenefit_item_diagnosisSequence(models.Model):
    ExplanationOfBenefit_item = models.ForeignKey(FHIR_ExplanationOfBenefit_item, related_name='ExplanationOfBenefit_item_diagnosisSequence', null=False, on_delete=models.CASCADE)
    
    diagnosisSequence = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    
class FHIR_ExplanationOfBenefit_item_procedureSequence(models.Model):
    ExplanationOfBenefit_item = models.ForeignKey(FHIR_ExplanationOfBenefit_item, related_name='ExplanationOfBenefit_item_procedureSequence', null=False, on_delete=models.CASCADE)
    
    procedureSequence = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    
class FHIR_ExplanationOfBenefit_item_informationSequence(models.Model):
    ExplanationOfBenefit_item = models.ForeignKey(FHIR_ExplanationOfBenefit_item, related_name='ExplanationOfBenefit_item_informationSequence', null=False, on_delete=models.CASCADE)
    
    informationSequence = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    
class FHIR_ExplanationOfBenefit_item_traceNumber(FHIR_GP_Identifier):
    ExplanationOfBenefit_item = models.ForeignKey(FHIR_ExplanationOfBenefit_item, related_name='ExplanationOfBenefit_item_traceNumber', null=False, on_delete=models.CASCADE)

class FHIR_ExplanationOfBenefit_item_modifier(models.Model):
    ExplanationOfBenefit_item = models.ForeignKey(FHIR_ExplanationOfBenefit_item, related_name='ExplanationOfBenefit_item_modifier', null=False, on_delete=models.CASCADE)
    BINDING_modifier = "TODO"
    modifier_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_modifier}, related_name='ExplanationOfBenefit_item_modifier', blank=True)
    modifier_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ExplanationOfBenefit_item_programCode(models.Model):
    ExplanationOfBenefit_item = models.ForeignKey(FHIR_ExplanationOfBenefit_item, related_name='ExplanationOfBenefit_item_programCode', null=False, on_delete=models.CASCADE)
    BINDING_programCode = "TODO"
    programCode_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_programCode}, related_name='ExplanationOfBenefit_item_programCode', blank=True)
    programCode_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ExplanationOfBenefit_item_bodySite(models.Model):
    ExplanationOfBenefit_item = models.ForeignKey(FHIR_ExplanationOfBenefit_item, related_name='ExplanationOfBenefit_item_bodySite', null=False, on_delete=models.CASCADE)

class FHIR_ExplanationOfBenefit_item_bodySite_site(models.Model):
    ExplanationOfBenefit_item_bodySite = models.ForeignKey(FHIR_ExplanationOfBenefit_item_bodySite, related_name='ExplanationOfBenefit_item_bodySite_site', null=False, on_delete=models.CASCADE)
    BINDING_site = "TODO"
    site_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_site}, related_name='ExplanationOfBenefit_item_bodySite_site', blank=True)
    site_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    site_BodyStructure_ref = models.ForeignKey("FHIR_BodyStructure", related_name="ExplanationOfBenefit_item_bodySite_site_BodyStructure", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ExplanationOfBenefit_item_bodySite_subSite(models.Model):
    ExplanationOfBenefit_item_bodySite = models.ForeignKey(FHIR_ExplanationOfBenefit_item_bodySite, related_name='ExplanationOfBenefit_item_bodySite_subSite', null=False, on_delete=models.CASCADE)
    BINDING_subSite = "TODO"
    subSite_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_subSite}, related_name='ExplanationOfBenefit_item_bodySite_subSite', blank=True)
    subSite_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ExplanationOfBenefit_item_noteNumber(models.Model):
    ExplanationOfBenefit_item = models.ForeignKey(FHIR_ExplanationOfBenefit_item, related_name='ExplanationOfBenefit_item_noteNumber', null=False, on_delete=models.CASCADE)
    
    noteNumber = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    
class FHIR_ExplanationOfBenefit_item_reviewOutcome(models.Model):
    ExplanationOfBenefit_item = models.ForeignKey(FHIR_ExplanationOfBenefit_item, related_name='ExplanationOfBenefit_item_reviewOutcome', null=False, on_delete=models.CASCADE)
    BINDING_decision = "TODO"
    decision_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_decision}, related_name='ExplanationOfBenefit_item_reviewOutcome_decision', blank=True)
    decision_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    preAuthRef = FHIR_primitive_StringField(null=True, blank=True, )
    preAuthPeriod = models.OneToOneField("FHIR_GP_Period", related_name='ExplanationOfBenefit_item_reviewOutcome_preAuthPeriod', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ExplanationOfBenefit_item_reviewOutcome_reason(models.Model):
    ExplanationOfBenefit_item_reviewOutcome = models.ForeignKey(FHIR_ExplanationOfBenefit_item_reviewOutcome, related_name='ExplanationOfBenefit_item_reviewOutcome_reason', null=False, on_delete=models.CASCADE)
    BINDING_reason = "TODO"
    reason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_reason}, related_name='ExplanationOfBenefit_item_reviewOutcome_reason', blank=True)
    reason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ExplanationOfBenefit_item_adjudication(models.Model):
    ExplanationOfBenefit_item = models.ForeignKey(FHIR_ExplanationOfBenefit_item, related_name='ExplanationOfBenefit_item_adjudication', null=False, on_delete=models.CASCADE)
    BINDING_category = "TODO"
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='ExplanationOfBenefit_item_adjudication_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_reason = "TODO"
    reason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_reason}, related_name='ExplanationOfBenefit_item_adjudication_reason', blank=True)
    reason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    amount = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='ExplanationOfBenefit_item_adjudication_amount', null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='ExplanationOfBenefit_item_adjudication_quantity', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ExplanationOfBenefit_item_detail(models.Model):
    ExplanationOfBenefit_item = models.ForeignKey(FHIR_ExplanationOfBenefit_item, related_name='ExplanationOfBenefit_item_detail', null=False, on_delete=models.CASCADE)
    sequence = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    BINDING_revenue = "TODO"
    revenue_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_revenue}, related_name='ExplanationOfBenefit_item_detail_revenue', blank=True)
    revenue_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_category = "TODO"
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='ExplanationOfBenefit_item_detail_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_productOrService = "TODO"
    productOrService_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_productOrService}, related_name='ExplanationOfBenefit_item_detail_productOrService', blank=True)
    productOrService_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_productOrServiceEnd = "TODO"
    productOrServiceEnd_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_productOrServiceEnd}, related_name='ExplanationOfBenefit_item_detail_productOrServiceEnd', blank=True)
    productOrServiceEnd_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    patientPaid = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='ExplanationOfBenefit_item_detail_patientPaid', null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='ExplanationOfBenefit_item_detail_quantity', null=True, blank=True, on_delete=models.SET_NULL)
    unitPrice = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='ExplanationOfBenefit_item_detail_unitPrice', null=True, blank=True, on_delete=models.SET_NULL)
    factor = FHIR_primitive_DecimalField(null=True, blank=True, )
    tax = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='ExplanationOfBenefit_item_detail_tax', null=True, blank=True, on_delete=models.SET_NULL)
    net = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='ExplanationOfBenefit_item_detail_net', null=True, blank=True, on_delete=models.SET_NULL)
    udi = models.ManyToManyField("FHIR_Device", related_name="ExplanationOfBenefit_item_detail_udi", blank=True)

class FHIR_ExplanationOfBenefit_item_detail_traceNumber(FHIR_GP_Identifier):
    ExplanationOfBenefit_item_detail = models.ForeignKey(FHIR_ExplanationOfBenefit_item_detail, related_name='ExplanationOfBenefit_item_detail_traceNumber', null=False, on_delete=models.CASCADE)

class FHIR_ExplanationOfBenefit_item_detail_modifier(models.Model):
    ExplanationOfBenefit_item_detail = models.ForeignKey(FHIR_ExplanationOfBenefit_item_detail, related_name='ExplanationOfBenefit_item_detail_modifier', null=False, on_delete=models.CASCADE)
    BINDING_modifier = "TODO"
    modifier_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_modifier}, related_name='ExplanationOfBenefit_item_detail_modifier', blank=True)
    modifier_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ExplanationOfBenefit_item_detail_programCode(models.Model):
    ExplanationOfBenefit_item_detail = models.ForeignKey(FHIR_ExplanationOfBenefit_item_detail, related_name='ExplanationOfBenefit_item_detail_programCode', null=False, on_delete=models.CASCADE)
    BINDING_programCode = "TODO"
    programCode_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_programCode}, related_name='ExplanationOfBenefit_item_detail_programCode', blank=True)
    programCode_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ExplanationOfBenefit_item_detail_noteNumber(models.Model):
    ExplanationOfBenefit_item_detail = models.ForeignKey(FHIR_ExplanationOfBenefit_item_detail, related_name='ExplanationOfBenefit_item_detail_noteNumber', null=False, on_delete=models.CASCADE)
    
    noteNumber = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    
class FHIR_ExplanationOfBenefit_item_detail_subDetail(models.Model):
    ExplanationOfBenefit_item_detail = models.ForeignKey(FHIR_ExplanationOfBenefit_item_detail, related_name='ExplanationOfBenefit_item_detail_subDetail', null=False, on_delete=models.CASCADE)
    sequence = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    BINDING_revenue = "TODO"
    revenue_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_revenue}, related_name='ExplanationOfBenefit_item_detail_subDetail_revenue', blank=True)
    revenue_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_category = "TODO"
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='ExplanationOfBenefit_item_detail_subDetail_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_productOrService = "TODO"
    productOrService_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_productOrService}, related_name='ExplanationOfBenefit_item_detail_subDetail_productOrService', blank=True)
    productOrService_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_productOrServiceEnd = "TODO"
    productOrServiceEnd_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_productOrServiceEnd}, related_name='ExplanationOfBenefit_item_detail_subDetail_productOrServiceEnd', blank=True)
    productOrServiceEnd_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    patientPaid = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='ExplanationOfBenefit_item_detail_subDetail_patientPaid', null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='ExplanationOfBenefit_item_detail_subDetail_quantity', null=True, blank=True, on_delete=models.SET_NULL)
    unitPrice = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='ExplanationOfBenefit_item_detail_subDetail_unitPrice', null=True, blank=True, on_delete=models.SET_NULL)
    factor = FHIR_primitive_DecimalField(null=True, blank=True, )
    tax = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='ExplanationOfBenefit_item_detail_subDetail_tax', null=True, blank=True, on_delete=models.SET_NULL)
    net = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='ExplanationOfBenefit_item_detail_subDetail_net', null=True, blank=True, on_delete=models.SET_NULL)
    udi = models.ManyToManyField("FHIR_Device", related_name="ExplanationOfBenefit_item_detail_subDetail_udi", blank=True)

class FHIR_ExplanationOfBenefit_item_detail_subDetail_traceNumber(FHIR_GP_Identifier):
    ExplanationOfBenefit_item_detail_subDetail = models.ForeignKey(FHIR_ExplanationOfBenefit_item_detail_subDetail, related_name='ExplanationOfBenefit_item_detail_subDetail_traceNumber', null=False, on_delete=models.CASCADE)

class FHIR_ExplanationOfBenefit_item_detail_subDetail_modifier(models.Model):
    ExplanationOfBenefit_item_detail_subDetail = models.ForeignKey(FHIR_ExplanationOfBenefit_item_detail_subDetail, related_name='ExplanationOfBenefit_item_detail_subDetail_modifier', null=False, on_delete=models.CASCADE)
    BINDING_modifier = "TODO"
    modifier_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_modifier}, related_name='ExplanationOfBenefit_item_detail_subDetail_modifier', blank=True)
    modifier_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ExplanationOfBenefit_item_detail_subDetail_programCode(models.Model):
    ExplanationOfBenefit_item_detail_subDetail = models.ForeignKey(FHIR_ExplanationOfBenefit_item_detail_subDetail, related_name='ExplanationOfBenefit_item_detail_subDetail_programCode', null=False, on_delete=models.CASCADE)
    BINDING_programCode = "TODO"
    programCode_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_programCode}, related_name='ExplanationOfBenefit_item_detail_subDetail_programCode', blank=True)
    programCode_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ExplanationOfBenefit_item_detail_subDetail_noteNumber(models.Model):
    ExplanationOfBenefit_item_detail_subDetail = models.ForeignKey(FHIR_ExplanationOfBenefit_item_detail_subDetail, related_name='ExplanationOfBenefit_item_detail_subDetail_noteNumber', null=False, on_delete=models.CASCADE)
    
    noteNumber = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    
class FHIR_ExplanationOfBenefit_addItem(models.Model):
    ExplanationOfBenefit = models.ForeignKey(FHIR_ExplanationOfBenefit, related_name='ExplanationOfBenefit_addItem', null=False, on_delete=models.CASCADE)
    provider_Practitioner = models.ManyToManyField("FHIR_Practitioner", related_name="ExplanationOfBenefit_addItem_provider", blank=True)
    provider_PractitionerRole = models.ManyToManyField("FHIR_PractitionerRole", related_name="ExplanationOfBenefit_addItem_provider", blank=True)
    provider_Organization = models.ManyToManyField("FHIR_Organization", related_name="ExplanationOfBenefit_addItem_provider", blank=True)
    BINDING_revenue = "TODO"
    revenue_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_revenue}, related_name='ExplanationOfBenefit_addItem_revenue', blank=True)
    revenue_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_productOrService = "TODO"
    productOrService_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_productOrService}, related_name='ExplanationOfBenefit_addItem_productOrService', blank=True)
    productOrService_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_productOrServiceEnd = "TODO"
    productOrServiceEnd_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_productOrServiceEnd}, related_name='ExplanationOfBenefit_addItem_productOrServiceEnd', blank=True)
    productOrServiceEnd_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    request_DeviceRequest = models.ManyToManyField("FHIR_DeviceRequest", related_name="ExplanationOfBenefit_addItem_request", blank=True)
    request_MedicationRequest = models.ManyToManyField("FHIR_MedicationRequest", related_name="ExplanationOfBenefit_addItem_request", blank=True)
    request_NutritionOrder = models.ManyToManyField("FHIR_NutritionOrder", related_name="ExplanationOfBenefit_addItem_request", blank=True)
    request_ServiceRequest = models.ManyToManyField("FHIR_ServiceRequest", related_name="ExplanationOfBenefit_addItem_request", blank=True)
    request_SupplyRequest = models.ManyToManyField("FHIR_SupplyRequest", related_name="ExplanationOfBenefit_addItem_request", blank=True)
    request_VisionPrescription = models.ManyToManyField("FHIR_VisionPrescription", related_name="ExplanationOfBenefit_addItem_request", blank=True)
    serviced = FHIR_primitive_DateField(null=True, blank=True, )
    serviced = models.OneToOneField("FHIR_GP_Period", related_name='ExplanationOfBenefit_addItem_serviced', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_location = "TODO"
    location_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_location}, related_name='ExplanationOfBenefit_addItem_location', blank=True)
    location_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    location = models.OneToOneField("FHIR_GP_Address", related_name='ExplanationOfBenefit_addItem_location', null=True, blank=True, on_delete=models.SET_NULL)
    location = models.ForeignKey("FHIR_Location", related_name="ExplanationOfBenefit_addItem_location", null=True, blank=True, on_delete=models.SET_NULL)
    patientPaid = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='ExplanationOfBenefit_addItem_patientPaid', null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='ExplanationOfBenefit_addItem_quantity', null=True, blank=True, on_delete=models.SET_NULL)
    unitPrice = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='ExplanationOfBenefit_addItem_unitPrice', null=True, blank=True, on_delete=models.SET_NULL)
    factor = FHIR_primitive_DecimalField(null=True, blank=True, )
    tax = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='ExplanationOfBenefit_addItem_tax', null=True, blank=True, on_delete=models.SET_NULL)
    net = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='ExplanationOfBenefit_addItem_net', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ExplanationOfBenefit_addItem_itemSequence(models.Model):
    ExplanationOfBenefit_addItem = models.ForeignKey(FHIR_ExplanationOfBenefit_addItem, related_name='ExplanationOfBenefit_addItem_itemSequence', null=False, on_delete=models.CASCADE)
    
    itemSequence = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    
class FHIR_ExplanationOfBenefit_addItem_detailSequence(models.Model):
    ExplanationOfBenefit_addItem = models.ForeignKey(FHIR_ExplanationOfBenefit_addItem, related_name='ExplanationOfBenefit_addItem_detailSequence', null=False, on_delete=models.CASCADE)
    
    detailSequence = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    
class FHIR_ExplanationOfBenefit_addItem_subDetailSequence(models.Model):
    ExplanationOfBenefit_addItem = models.ForeignKey(FHIR_ExplanationOfBenefit_addItem, related_name='ExplanationOfBenefit_addItem_subDetailSequence', null=False, on_delete=models.CASCADE)
    
    subDetailSequence = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    
class FHIR_ExplanationOfBenefit_addItem_traceNumber(FHIR_GP_Identifier):
    ExplanationOfBenefit_addItem = models.ForeignKey(FHIR_ExplanationOfBenefit_addItem, related_name='ExplanationOfBenefit_addItem_traceNumber', null=False, on_delete=models.CASCADE)

class FHIR_ExplanationOfBenefit_addItem_modifier(models.Model):
    ExplanationOfBenefit_addItem = models.ForeignKey(FHIR_ExplanationOfBenefit_addItem, related_name='ExplanationOfBenefit_addItem_modifier', null=False, on_delete=models.CASCADE)
    BINDING_modifier = "TODO"
    modifier_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_modifier}, related_name='ExplanationOfBenefit_addItem_modifier', blank=True)
    modifier_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ExplanationOfBenefit_addItem_programCode(models.Model):
    ExplanationOfBenefit_addItem = models.ForeignKey(FHIR_ExplanationOfBenefit_addItem, related_name='ExplanationOfBenefit_addItem_programCode', null=False, on_delete=models.CASCADE)
    BINDING_programCode = "TODO"
    programCode_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_programCode}, related_name='ExplanationOfBenefit_addItem_programCode', blank=True)
    programCode_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ExplanationOfBenefit_addItem_bodySite(models.Model):
    ExplanationOfBenefit_addItem = models.ForeignKey(FHIR_ExplanationOfBenefit_addItem, related_name='ExplanationOfBenefit_addItem_bodySite', null=False, on_delete=models.CASCADE)

class FHIR_ExplanationOfBenefit_addItem_bodySite_site(models.Model):
    ExplanationOfBenefit_addItem_bodySite = models.ForeignKey(FHIR_ExplanationOfBenefit_addItem_bodySite, related_name='ExplanationOfBenefit_addItem_bodySite_site', null=False, on_delete=models.CASCADE)
    BINDING_site = "TODO"
    site_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_site}, related_name='ExplanationOfBenefit_addItem_bodySite_site', blank=True)
    site_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    site_BodyStructure_ref = models.ForeignKey("FHIR_BodyStructure", related_name="ExplanationOfBenefit_addItem_bodySite_site_BodyStructure", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ExplanationOfBenefit_addItem_bodySite_subSite(models.Model):
    ExplanationOfBenefit_addItem_bodySite = models.ForeignKey(FHIR_ExplanationOfBenefit_addItem_bodySite, related_name='ExplanationOfBenefit_addItem_bodySite_subSite', null=False, on_delete=models.CASCADE)
    BINDING_subSite = "TODO"
    subSite_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_subSite}, related_name='ExplanationOfBenefit_addItem_bodySite_subSite', blank=True)
    subSite_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ExplanationOfBenefit_addItem_noteNumber(models.Model):
    ExplanationOfBenefit_addItem = models.ForeignKey(FHIR_ExplanationOfBenefit_addItem, related_name='ExplanationOfBenefit_addItem_noteNumber', null=False, on_delete=models.CASCADE)
    
    noteNumber = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    
class FHIR_ExplanationOfBenefit_addItem_detail(models.Model):
    ExplanationOfBenefit_addItem = models.ForeignKey(FHIR_ExplanationOfBenefit_addItem, related_name='ExplanationOfBenefit_addItem_detail', null=False, on_delete=models.CASCADE)
    BINDING_revenue = "TODO"
    revenue_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_revenue}, related_name='ExplanationOfBenefit_addItem_detail_revenue', blank=True)
    revenue_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_productOrService = "TODO"
    productOrService_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_productOrService}, related_name='ExplanationOfBenefit_addItem_detail_productOrService', blank=True)
    productOrService_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_productOrServiceEnd = "TODO"
    productOrServiceEnd_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_productOrServiceEnd}, related_name='ExplanationOfBenefit_addItem_detail_productOrServiceEnd', blank=True)
    productOrServiceEnd_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    patientPaid = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='ExplanationOfBenefit_addItem_detail_patientPaid', null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='ExplanationOfBenefit_addItem_detail_quantity', null=True, blank=True, on_delete=models.SET_NULL)
    unitPrice = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='ExplanationOfBenefit_addItem_detail_unitPrice', null=True, blank=True, on_delete=models.SET_NULL)
    factor = FHIR_primitive_DecimalField(null=True, blank=True, )
    tax = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='ExplanationOfBenefit_addItem_detail_tax', null=True, blank=True, on_delete=models.SET_NULL)
    net = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='ExplanationOfBenefit_addItem_detail_net', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ExplanationOfBenefit_addItem_detail_traceNumber(FHIR_GP_Identifier):
    ExplanationOfBenefit_addItem_detail = models.ForeignKey(FHIR_ExplanationOfBenefit_addItem_detail, related_name='ExplanationOfBenefit_addItem_detail_traceNumber', null=False, on_delete=models.CASCADE)

class FHIR_ExplanationOfBenefit_addItem_detail_modifier(models.Model):
    ExplanationOfBenefit_addItem_detail = models.ForeignKey(FHIR_ExplanationOfBenefit_addItem_detail, related_name='ExplanationOfBenefit_addItem_detail_modifier', null=False, on_delete=models.CASCADE)
    BINDING_modifier = "TODO"
    modifier_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_modifier}, related_name='ExplanationOfBenefit_addItem_detail_modifier', blank=True)
    modifier_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ExplanationOfBenefit_addItem_detail_noteNumber(models.Model):
    ExplanationOfBenefit_addItem_detail = models.ForeignKey(FHIR_ExplanationOfBenefit_addItem_detail, related_name='ExplanationOfBenefit_addItem_detail_noteNumber', null=False, on_delete=models.CASCADE)
    
    noteNumber = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    
class FHIR_ExplanationOfBenefit_addItem_detail_subDetail(models.Model):
    ExplanationOfBenefit_addItem_detail = models.ForeignKey(FHIR_ExplanationOfBenefit_addItem_detail, related_name='ExplanationOfBenefit_addItem_detail_subDetail', null=False, on_delete=models.CASCADE)
    BINDING_revenue = "TODO"
    revenue_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_revenue}, related_name='ExplanationOfBenefit_addItem_detail_subDetail_revenue', blank=True)
    revenue_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_productOrService = "TODO"
    productOrService_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_productOrService}, related_name='ExplanationOfBenefit_addItem_detail_subDetail_productOrService', blank=True)
    productOrService_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_productOrServiceEnd = "TODO"
    productOrServiceEnd_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_productOrServiceEnd}, related_name='ExplanationOfBenefit_addItem_detail_subDetail_productOrServiceEnd', blank=True)
    productOrServiceEnd_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    patientPaid = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='ExplanationOfBenefit_addItem_detail_subDetail_patientPaid', null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='ExplanationOfBenefit_addItem_detail_subDetail_quantity', null=True, blank=True, on_delete=models.SET_NULL)
    unitPrice = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='ExplanationOfBenefit_addItem_detail_subDetail_unitPrice', null=True, blank=True, on_delete=models.SET_NULL)
    factor = FHIR_primitive_DecimalField(null=True, blank=True, )
    tax = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='ExplanationOfBenefit_addItem_detail_subDetail_tax', null=True, blank=True, on_delete=models.SET_NULL)
    net = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='ExplanationOfBenefit_addItem_detail_subDetail_net', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ExplanationOfBenefit_addItem_detail_subDetail_traceNumber(FHIR_GP_Identifier):
    ExplanationOfBenefit_addItem_detail_subDetail = models.ForeignKey(FHIR_ExplanationOfBenefit_addItem_detail_subDetail, related_name='ExplanationOfBenefit_addItem_detail_subDetail_traceNumber', null=False, on_delete=models.CASCADE)

class FHIR_ExplanationOfBenefit_addItem_detail_subDetail_modifier(models.Model):
    ExplanationOfBenefit_addItem_detail_subDetail = models.ForeignKey(FHIR_ExplanationOfBenefit_addItem_detail_subDetail, related_name='ExplanationOfBenefit_addItem_detail_subDetail_modifier', null=False, on_delete=models.CASCADE)
    BINDING_modifier = "TODO"
    modifier_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_modifier}, related_name='ExplanationOfBenefit_addItem_detail_subDetail_modifier', blank=True)
    modifier_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ExplanationOfBenefit_addItem_detail_subDetail_noteNumber(models.Model):
    ExplanationOfBenefit_addItem_detail_subDetail = models.ForeignKey(FHIR_ExplanationOfBenefit_addItem_detail_subDetail, related_name='ExplanationOfBenefit_addItem_detail_subDetail_noteNumber', null=False, on_delete=models.CASCADE)
    
    noteNumber = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    
class FHIR_ExplanationOfBenefit_total(models.Model):
    ExplanationOfBenefit = models.ForeignKey(FHIR_ExplanationOfBenefit, related_name='ExplanationOfBenefit_total', null=False, on_delete=models.CASCADE)
    BINDING_category = "TODO"
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='ExplanationOfBenefit_total_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    amount = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='ExplanationOfBenefit_total_amount', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ExplanationOfBenefit_payment(models.Model):
    ExplanationOfBenefit = models.ForeignKey(FHIR_ExplanationOfBenefit, related_name='ExplanationOfBenefit_payment', null=False, on_delete=models.CASCADE)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='ExplanationOfBenefit_payment_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    adjustment = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='ExplanationOfBenefit_payment_adjustment', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_adjustmentReason = "TODO"
    adjustmentReason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_adjustmentReason}, related_name='ExplanationOfBenefit_payment_adjustmentReason', blank=True)
    adjustmentReason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    date = FHIR_primitive_DateField(null=True, blank=True, )
    amount = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='ExplanationOfBenefit_payment_amount', null=True, blank=True, on_delete=models.SET_NULL)
    identifier = models.OneToOneField("FHIR_GP_Identifier", related_name='ExplanationOfBenefit_payment_identifier', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ExplanationOfBenefit_processNote(models.Model):
    ExplanationOfBenefit = models.ForeignKey(FHIR_ExplanationOfBenefit, related_name='ExplanationOfBenefit_processNote', null=False, on_delete=models.CASCADE)
    number = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='ExplanationOfBenefit_processNote_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    text = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_language = "TODO"
    language_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_language}, related_name='ExplanationOfBenefit_processNote_language', blank=True)
    language_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_ExplanationOfBenefit_benefitBalance(models.Model):
    ExplanationOfBenefit = models.ForeignKey(FHIR_ExplanationOfBenefit, related_name='ExplanationOfBenefit_benefitBalance', null=False, on_delete=models.CASCADE)
    BINDING_category = "TODO"
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='ExplanationOfBenefit_benefitBalance_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    excluded = FHIR_primitive_BooleanField(null=True, blank=True, )
    name = FHIR_primitive_StringField(null=True, blank=True, )
    description = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_network = "TODO"
    network_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_network}, related_name='ExplanationOfBenefit_benefitBalance_network', blank=True)
    network_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_unit = "TODO"
    unit_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_unit}, related_name='ExplanationOfBenefit_benefitBalance_unit', blank=True)
    unit_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_term = "TODO"
    term_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_term}, related_name='ExplanationOfBenefit_benefitBalance_term', blank=True)
    term_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_ExplanationOfBenefit_benefitBalance_financial(models.Model):
    ExplanationOfBenefit_benefitBalance = models.ForeignKey(FHIR_ExplanationOfBenefit_benefitBalance, related_name='ExplanationOfBenefit_benefitBalance_financial', null=False, on_delete=models.CASCADE)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='ExplanationOfBenefit_benefitBalance_financial_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    allowed = FHIR_primitive_UnsignedIntField(null=True, blank=True, )
    allowed = FHIR_primitive_StringField(null=True, blank=True, )
    allowed = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='ExplanationOfBenefit_benefitBalance_financial_allowed', null=True, blank=True, on_delete=models.SET_NULL)
    used = FHIR_primitive_UnsignedIntField(null=True, blank=True, )
    used = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='ExplanationOfBenefit_benefitBalance_financial_used', null=True, blank=True, on_delete=models.SET_NULL)
