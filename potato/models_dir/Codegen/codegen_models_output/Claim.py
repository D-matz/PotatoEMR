#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Claim(models.Model):
    class StatusChoices(models.TextChoices): ACTIVE = 'active', 'Active'; CANCELLED = 'cancelled', 'Cancelled'; DRAFT = 'draft', 'Draft'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Claim_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_subType = "TODO"
    subType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_subType}, related_name='Claim_subType', blank=True)
    subType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    class UseChoices(models.TextChoices): CLAIM = 'claim', 'Claim'; PREAUTHORIZATION = 'preauthorization', 'Preauthorization'; PREDETERMINATION = 'predetermination', 'Predetermination'; 
    use = FHIR_primitive_CodeField(choices=UseChoices.choices, null=True, blank=True, )
    patient = models.ForeignKey("FHIR_Patient", related_name="Claim_patient", null=True, blank=True, on_delete=models.SET_NULL)
    billablePeriod = models.OneToOneField("FHIR_GP_Period", related_name='Claim_billablePeriod', null=True, blank=True, on_delete=models.SET_NULL)
    created = FHIR_primitive_DateTimeField(null=True, blank=True, )
    enterer_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="Claim_enterer", null=True, blank=True, on_delete=models.SET_NULL)
    enterer_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="Claim_enterer", null=True, blank=True, on_delete=models.SET_NULL)
    enterer_Patient = models.ForeignKey("FHIR_Patient", related_name="Claim_enterer", null=True, blank=True, on_delete=models.SET_NULL)
    enterer_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="Claim_enterer", null=True, blank=True, on_delete=models.SET_NULL)
    insurer = models.ForeignKey("FHIR_Organization", related_name="Claim_insurer", null=True, blank=True, on_delete=models.SET_NULL)
    provider_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="Claim_provider", null=True, blank=True, on_delete=models.SET_NULL)
    provider_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="Claim_provider", null=True, blank=True, on_delete=models.SET_NULL)
    provider_Organization = models.ForeignKey("FHIR_Organization", related_name="Claim_provider", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_priority = "TODO"
    priority_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_priority}, related_name='Claim_priority', blank=True)
    priority_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_fundsReserve = "TODO"
    fundsReserve_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_fundsReserve}, related_name='Claim_fundsReserve', blank=True)
    fundsReserve_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    prescription_DeviceRequest = models.ForeignKey("FHIR_DeviceRequest", related_name="Claim_prescription", null=True, blank=True, on_delete=models.SET_NULL)
    prescription_MedicationRequest = models.ForeignKey("FHIR_MedicationRequest", related_name="Claim_prescription", null=True, blank=True, on_delete=models.SET_NULL)
    prescription_VisionPrescription = models.ForeignKey("FHIR_VisionPrescription", related_name="Claim_prescription", null=True, blank=True, on_delete=models.SET_NULL)
    originalPrescription_DeviceRequest = models.ForeignKey("FHIR_DeviceRequest", related_name="Claim_originalPrescription", null=True, blank=True, on_delete=models.SET_NULL)
    originalPrescription_MedicationRequest = models.ForeignKey("FHIR_MedicationRequest", related_name="Claim_originalPrescription", null=True, blank=True, on_delete=models.SET_NULL)
    originalPrescription_VisionPrescription = models.ForeignKey("FHIR_VisionPrescription", related_name="Claim_originalPrescription", null=True, blank=True, on_delete=models.SET_NULL)
    referral = models.ForeignKey("FHIR_ServiceRequest", related_name="Claim_referral", null=True, blank=True, on_delete=models.SET_NULL)
    encounter = models.ManyToManyField("FHIR_Encounter", related_name="Claim_encounter", blank=True)
    facility_Location = models.ForeignKey("FHIR_Location", related_name="Claim_facility", null=True, blank=True, on_delete=models.SET_NULL)
    facility_Organization = models.ForeignKey("FHIR_Organization", related_name="Claim_facility", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_diagnosisRelatedGroup = "TODO"
    diagnosisRelatedGroup_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_diagnosisRelatedGroup}, related_name='Claim_diagnosisRelatedGroup', blank=True)
    diagnosisRelatedGroup_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    patientPaid = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='Claim_patientPaid', null=True, blank=True, on_delete=models.SET_NULL)
    total = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='Claim_total', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Claim_identifier(FHIR_GP_Identifier):
    Claim = models.ForeignKey(FHIR_Claim, related_name='Claim_identifier', null=False, on_delete=models.CASCADE)

class FHIR_Claim_traceNumber(FHIR_GP_Identifier):
    Claim = models.ForeignKey(FHIR_Claim, related_name='Claim_traceNumber', null=False, on_delete=models.CASCADE)

class FHIR_Claim_related(models.Model):
    Claim = models.ForeignKey(FHIR_Claim, related_name='Claim_related', null=False, on_delete=models.CASCADE)
    claim = models.ForeignKey("FHIR_Claim", related_name="Claim_related_claim", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_relationship = "TODO"
    relationship_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_relationship}, related_name='Claim_related_relationship', blank=True)
    relationship_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    reference = models.OneToOneField("FHIR_GP_Identifier", related_name='Claim_related_reference', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Claim_payee(models.Model):
    Claim = models.ForeignKey(FHIR_Claim, related_name='Claim_payee', null=False, on_delete=models.CASCADE)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Claim_payee_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    party_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="Claim_payee_party", null=True, blank=True, on_delete=models.SET_NULL)
    party_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="Claim_payee_party", null=True, blank=True, on_delete=models.SET_NULL)
    party_Organization = models.ForeignKey("FHIR_Organization", related_name="Claim_payee_party", null=True, blank=True, on_delete=models.SET_NULL)
    party_Patient = models.ForeignKey("FHIR_Patient", related_name="Claim_payee_party", null=True, blank=True, on_delete=models.SET_NULL)
    party_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="Claim_payee_party", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Claim_event(models.Model):
    Claim = models.ForeignKey(FHIR_Claim, related_name='Claim_event', null=False, on_delete=models.CASCADE)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Claim_event_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    when_dateTime = FHIR_primitive_DateTimeField(null=True, blank=True, )
    when_Period = models.OneToOneField("FHIR_GP_Period", related_name='Claim_event_when_Period', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Claim_careTeam(models.Model):
    Claim = models.ForeignKey(FHIR_Claim, related_name='Claim_careTeam', null=False, on_delete=models.CASCADE)
    sequence = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    provider_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="Claim_careTeam_provider", null=True, blank=True, on_delete=models.SET_NULL)
    provider_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="Claim_careTeam_provider", null=True, blank=True, on_delete=models.SET_NULL)
    provider_Organization = models.ForeignKey("FHIR_Organization", related_name="Claim_careTeam_provider", null=True, blank=True, on_delete=models.SET_NULL)
    responsible = FHIR_primitive_BooleanField(null=True, blank=True, )
    BINDING_role = "TODO"
    role_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_role}, related_name='Claim_careTeam_role', blank=True)
    role_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_specialty = "TODO"
    specialty_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_specialty}, related_name='Claim_careTeam_specialty', blank=True)
    specialty_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_Claim_supportingInfo(models.Model):
    Claim = models.ForeignKey(FHIR_Claim, related_name='Claim_supportingInfo', null=False, on_delete=models.CASCADE)
    sequence = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    BINDING_category = "TODO"
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='Claim_supportingInfo_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_code = "TODO"
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='Claim_supportingInfo_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    timing_date = FHIR_primitive_DateField(null=True, blank=True, )
    timing_Period = models.OneToOneField("FHIR_GP_Period", related_name='Claim_supportingInfo_timing_Period', null=True, blank=True, on_delete=models.SET_NULL)
    value_boolean = FHIR_primitive_BooleanField(null=True, blank=True, )
    value_string = FHIR_primitive_StringField(null=True, blank=True, )
    value_Quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='Claim_supportingInfo_value_Quantity', null=True, blank=True, on_delete=models.SET_NULL)
    value_Attachment = models.OneToOneField("FHIR_GP_Attachment", related_name='Claim_supportingInfo_value_Attachment', null=True, blank=True, on_delete=models.SET_NULL)
                            #skipping Reference(Any) for field value_Reference as Claim value_Reference not in referenceAny_targets
    value_Identifier = models.OneToOneField("FHIR_GP_Identifier", related_name='Claim_supportingInfo_value_Identifier', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_reason = "TODO"
    reason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_reason}, related_name='Claim_supportingInfo_reason', blank=True)
    reason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_Claim_diagnosis(models.Model):
    Claim = models.ForeignKey(FHIR_Claim, related_name='Claim_diagnosis', null=False, on_delete=models.CASCADE)
    sequence = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    BINDING_diagnosis_CodeableConcept = "TODO"
    diagnosis_CodeableConcept_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_diagnosis_CodeableConcept}, related_name='Claim_diagnosis_diagnosis_CodeableConcept', blank=True)
    diagnosis_CodeableConcept_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    diagnosis_Reference = models.ForeignKey("FHIR_Condition", related_name="Claim_diagnosis_diagnosis_Reference", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_onAdmission = "TODO"
    onAdmission_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_onAdmission}, related_name='Claim_diagnosis_onAdmission', blank=True)
    onAdmission_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_Claim_diagnosis_type(models.Model):
    Claim_diagnosis = models.ForeignKey(FHIR_Claim_diagnosis, related_name='Claim_diagnosis_type', null=False, on_delete=models.CASCADE)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Claim_diagnosis_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Claim_procedure(models.Model):
    Claim = models.ForeignKey(FHIR_Claim, related_name='Claim_procedure', null=False, on_delete=models.CASCADE)
    sequence = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    date = FHIR_primitive_DateTimeField(null=True, blank=True, )
    BINDING_procedure_CodeableConcept = "TODO"
    procedure_CodeableConcept_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_procedure_CodeableConcept}, related_name='Claim_procedure_procedure_CodeableConcept', blank=True)
    procedure_CodeableConcept_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    procedure_Reference = models.ForeignKey("FHIR_Procedure", related_name="Claim_procedure_procedure_Reference", null=True, blank=True, on_delete=models.SET_NULL)
    udi = models.ManyToManyField("FHIR_Device", related_name="Claim_procedure_udi", blank=True)

class FHIR_Claim_procedure_type(models.Model):
    Claim_procedure = models.ForeignKey(FHIR_Claim_procedure, related_name='Claim_procedure_type', null=False, on_delete=models.CASCADE)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Claim_procedure_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Claim_insurance(models.Model):
    Claim = models.ForeignKey(FHIR_Claim, related_name='Claim_insurance', null=False, on_delete=models.CASCADE)
    sequence = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    focal = FHIR_primitive_BooleanField(null=True, blank=True, )
    identifier = models.OneToOneField("FHIR_GP_Identifier", related_name='Claim_insurance_identifier', null=True, blank=True, on_delete=models.SET_NULL)
    coverage = models.ForeignKey("FHIR_Coverage", related_name="Claim_insurance_coverage", null=True, blank=True, on_delete=models.SET_NULL)
    businessArrangement = FHIR_primitive_StringField(null=True, blank=True, )
    claimResponse = models.ForeignKey("FHIR_ClaimResponse", related_name="Claim_insurance_claimResponse", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Claim_insurance_preAuthRef(models.Model):
    Claim_insurance = models.ForeignKey(FHIR_Claim_insurance, related_name='Claim_insurance_preAuthRef', null=False, on_delete=models.CASCADE)
    
    preAuthRef = FHIR_primitive_StringField(null=True, blank=True, )
    
class FHIR_Claim_accident(models.Model):
    Claim = models.ForeignKey(FHIR_Claim, related_name='Claim_accident', null=False, on_delete=models.CASCADE)
    date = FHIR_primitive_DateField(null=True, blank=True, )
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Claim_accident_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    location_Address = models.OneToOneField("FHIR_GP_Address", related_name='Claim_accident_location_Address', null=True, blank=True, on_delete=models.SET_NULL)
    location_Reference = models.ForeignKey("FHIR_Location", related_name="Claim_accident_location_Reference", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Claim_item(models.Model):
    Claim = models.ForeignKey(FHIR_Claim, related_name='Claim_item', null=False, on_delete=models.CASCADE)
    sequence = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    BINDING_revenue = "TODO"
    revenue_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_revenue}, related_name='Claim_item_revenue', blank=True)
    revenue_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_category = "TODO"
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='Claim_item_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_productOrService = "TODO"
    productOrService_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_productOrService}, related_name='Claim_item_productOrService', blank=True)
    productOrService_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_productOrServiceEnd = "TODO"
    productOrServiceEnd_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_productOrServiceEnd}, related_name='Claim_item_productOrServiceEnd', blank=True)
    productOrServiceEnd_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    request_DeviceRequest = models.ManyToManyField("FHIR_DeviceRequest", related_name="Claim_item_request", blank=True)
    request_MedicationRequest = models.ManyToManyField("FHIR_MedicationRequest", related_name="Claim_item_request", blank=True)
    request_NutritionOrder = models.ManyToManyField("FHIR_NutritionOrder", related_name="Claim_item_request", blank=True)
    request_ServiceRequest = models.ManyToManyField("FHIR_ServiceRequest", related_name="Claim_item_request", blank=True)
    request_SupplyRequest = models.ManyToManyField("FHIR_SupplyRequest", related_name="Claim_item_request", blank=True)
    request_VisionPrescription = models.ManyToManyField("FHIR_VisionPrescription", related_name="Claim_item_request", blank=True)
    serviced_date = FHIR_primitive_DateField(null=True, blank=True, )
    serviced_Period = models.OneToOneField("FHIR_GP_Period", related_name='Claim_item_serviced_Period', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_location_CodeableConcept = "TODO"
    location_CodeableConcept_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_location_CodeableConcept}, related_name='Claim_item_location_CodeableConcept', blank=True)
    location_CodeableConcept_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    location_Address = models.OneToOneField("FHIR_GP_Address", related_name='Claim_item_location_Address', null=True, blank=True, on_delete=models.SET_NULL)
    location_Reference = models.ForeignKey("FHIR_Location", related_name="Claim_item_location_Reference", null=True, blank=True, on_delete=models.SET_NULL)
    patientPaid = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='Claim_item_patientPaid', null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='Claim_item_quantity', null=True, blank=True, on_delete=models.SET_NULL)
    unitPrice = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='Claim_item_unitPrice', null=True, blank=True, on_delete=models.SET_NULL)
    factor = FHIR_primitive_DecimalField(null=True, blank=True, )
    tax = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='Claim_item_tax', null=True, blank=True, on_delete=models.SET_NULL)
    net = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='Claim_item_net', null=True, blank=True, on_delete=models.SET_NULL)
    udi = models.ManyToManyField("FHIR_Device", related_name="Claim_item_udi", blank=True)
    encounter = models.ManyToManyField("FHIR_Encounter", related_name="Claim_item_encounter", blank=True)

class FHIR_Claim_item_traceNumber(FHIR_GP_Identifier):
    Claim_item = models.ForeignKey(FHIR_Claim_item, related_name='Claim_item_traceNumber', null=False, on_delete=models.CASCADE)

class FHIR_Claim_item_careTeamSequence(models.Model):
    Claim_item = models.ForeignKey(FHIR_Claim_item, related_name='Claim_item_careTeamSequence', null=False, on_delete=models.CASCADE)
    
    careTeamSequence = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    
class FHIR_Claim_item_diagnosisSequence(models.Model):
    Claim_item = models.ForeignKey(FHIR_Claim_item, related_name='Claim_item_diagnosisSequence', null=False, on_delete=models.CASCADE)
    
    diagnosisSequence = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    
class FHIR_Claim_item_procedureSequence(models.Model):
    Claim_item = models.ForeignKey(FHIR_Claim_item, related_name='Claim_item_procedureSequence', null=False, on_delete=models.CASCADE)
    
    procedureSequence = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    
class FHIR_Claim_item_informationSequence(models.Model):
    Claim_item = models.ForeignKey(FHIR_Claim_item, related_name='Claim_item_informationSequence', null=False, on_delete=models.CASCADE)
    
    informationSequence = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    
class FHIR_Claim_item_modifier(models.Model):
    Claim_item = models.ForeignKey(FHIR_Claim_item, related_name='Claim_item_modifier', null=False, on_delete=models.CASCADE)
    BINDING_modifier = "TODO"
    modifier_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_modifier}, related_name='Claim_item_modifier', blank=True)
    modifier_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Claim_item_programCode(models.Model):
    Claim_item = models.ForeignKey(FHIR_Claim_item, related_name='Claim_item_programCode', null=False, on_delete=models.CASCADE)
    BINDING_programCode = "TODO"
    programCode_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_programCode}, related_name='Claim_item_programCode', blank=True)
    programCode_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Claim_item_bodySite(models.Model):
    Claim_item = models.ForeignKey(FHIR_Claim_item, related_name='Claim_item_bodySite', null=False, on_delete=models.CASCADE)

class FHIR_Claim_item_bodySite_site(models.Model):
    Claim_item_bodySite = models.ForeignKey(FHIR_Claim_item_bodySite, related_name='Claim_item_bodySite_site', null=False, on_delete=models.CASCADE)
    BINDING_site = "TODO"
    site_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_site}, related_name='Claim_item_bodySite_site', blank=True)
    site_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    site_BodyStructure_ref = models.ForeignKey("FHIR_BodyStructure", related_name="Claim_item_bodySite_site_BodyStructure", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Claim_item_bodySite_subSite(models.Model):
    Claim_item_bodySite = models.ForeignKey(FHIR_Claim_item_bodySite, related_name='Claim_item_bodySite_subSite', null=False, on_delete=models.CASCADE)
    BINDING_subSite = "TODO"
    subSite_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_subSite}, related_name='Claim_item_bodySite_subSite', blank=True)
    subSite_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Claim_item_detail(models.Model):
    Claim_item = models.ForeignKey(FHIR_Claim_item, related_name='Claim_item_detail', null=False, on_delete=models.CASCADE)
    sequence = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    BINDING_revenue = "TODO"
    revenue_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_revenue}, related_name='Claim_item_detail_revenue', blank=True)
    revenue_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_category = "TODO"
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='Claim_item_detail_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_productOrService = "TODO"
    productOrService_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_productOrService}, related_name='Claim_item_detail_productOrService', blank=True)
    productOrService_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_productOrServiceEnd = "TODO"
    productOrServiceEnd_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_productOrServiceEnd}, related_name='Claim_item_detail_productOrServiceEnd', blank=True)
    productOrServiceEnd_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    patientPaid = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='Claim_item_detail_patientPaid', null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='Claim_item_detail_quantity', null=True, blank=True, on_delete=models.SET_NULL)
    unitPrice = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='Claim_item_detail_unitPrice', null=True, blank=True, on_delete=models.SET_NULL)
    factor = FHIR_primitive_DecimalField(null=True, blank=True, )
    tax = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='Claim_item_detail_tax', null=True, blank=True, on_delete=models.SET_NULL)
    net = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='Claim_item_detail_net', null=True, blank=True, on_delete=models.SET_NULL)
    udi = models.ManyToManyField("FHIR_Device", related_name="Claim_item_detail_udi", blank=True)

class FHIR_Claim_item_detail_traceNumber(FHIR_GP_Identifier):
    Claim_item_detail = models.ForeignKey(FHIR_Claim_item_detail, related_name='Claim_item_detail_traceNumber', null=False, on_delete=models.CASCADE)

class FHIR_Claim_item_detail_modifier(models.Model):
    Claim_item_detail = models.ForeignKey(FHIR_Claim_item_detail, related_name='Claim_item_detail_modifier', null=False, on_delete=models.CASCADE)
    BINDING_modifier = "TODO"
    modifier_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_modifier}, related_name='Claim_item_detail_modifier', blank=True)
    modifier_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Claim_item_detail_programCode(models.Model):
    Claim_item_detail = models.ForeignKey(FHIR_Claim_item_detail, related_name='Claim_item_detail_programCode', null=False, on_delete=models.CASCADE)
    BINDING_programCode = "TODO"
    programCode_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_programCode}, related_name='Claim_item_detail_programCode', blank=True)
    programCode_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Claim_item_detail_subDetail(models.Model):
    Claim_item_detail = models.ForeignKey(FHIR_Claim_item_detail, related_name='Claim_item_detail_subDetail', null=False, on_delete=models.CASCADE)
    sequence = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    BINDING_revenue = "TODO"
    revenue_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_revenue}, related_name='Claim_item_detail_subDetail_revenue', blank=True)
    revenue_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_category = "TODO"
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='Claim_item_detail_subDetail_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_productOrService = "TODO"
    productOrService_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_productOrService}, related_name='Claim_item_detail_subDetail_productOrService', blank=True)
    productOrService_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_productOrServiceEnd = "TODO"
    productOrServiceEnd_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_productOrServiceEnd}, related_name='Claim_item_detail_subDetail_productOrServiceEnd', blank=True)
    productOrServiceEnd_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    patientPaid = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='Claim_item_detail_subDetail_patientPaid', null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='Claim_item_detail_subDetail_quantity', null=True, blank=True, on_delete=models.SET_NULL)
    unitPrice = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='Claim_item_detail_subDetail_unitPrice', null=True, blank=True, on_delete=models.SET_NULL)
    factor = FHIR_primitive_DecimalField(null=True, blank=True, )
    tax = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='Claim_item_detail_subDetail_tax', null=True, blank=True, on_delete=models.SET_NULL)
    net = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='Claim_item_detail_subDetail_net', null=True, blank=True, on_delete=models.SET_NULL)
    udi = models.ManyToManyField("FHIR_Device", related_name="Claim_item_detail_subDetail_udi", blank=True)

class FHIR_Claim_item_detail_subDetail_traceNumber(FHIR_GP_Identifier):
    Claim_item_detail_subDetail = models.ForeignKey(FHIR_Claim_item_detail_subDetail, related_name='Claim_item_detail_subDetail_traceNumber', null=False, on_delete=models.CASCADE)

class FHIR_Claim_item_detail_subDetail_modifier(models.Model):
    Claim_item_detail_subDetail = models.ForeignKey(FHIR_Claim_item_detail_subDetail, related_name='Claim_item_detail_subDetail_modifier', null=False, on_delete=models.CASCADE)
    BINDING_modifier = "TODO"
    modifier_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_modifier}, related_name='Claim_item_detail_subDetail_modifier', blank=True)
    modifier_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Claim_item_detail_subDetail_programCode(models.Model):
    Claim_item_detail_subDetail = models.ForeignKey(FHIR_Claim_item_detail_subDetail, related_name='Claim_item_detail_subDetail_programCode', null=False, on_delete=models.CASCADE)
    BINDING_programCode = "TODO"
    programCode_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_programCode}, related_name='Claim_item_detail_subDetail_programCode', blank=True)
    programCode_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    