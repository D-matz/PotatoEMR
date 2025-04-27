#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_ClaimResponse(models.Model):
    class StatusChoices(models.TextChoices): ACTIVE = 'active', 'Active'; CANCELLED = 'cancelled', 'Cancelled'; DRAFT = 'draft', 'Draft'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='ClaimResponse_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_subType = "TODO"
    subType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_subType}, related_name='ClaimResponse_subType', blank=True)
    subType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    class UseChoices(models.TextChoices): CLAIM = 'claim', 'Claim'; PREAUTHORIZATION = 'preauthorization', 'Preauthorization'; PREDETERMINATION = 'predetermination', 'Predetermination'; 
    use = FHIR_primitive_CodeField(choices=UseChoices.choices, null=True, blank=True, )
    patient = models.ForeignKey("FHIR_Patient", related_name="ClaimResponse_patient", null=True, blank=True, on_delete=models.SET_NULL)
    created = FHIR_primitive_DateTimeField(null=True, blank=True, )
    insurer = models.ForeignKey("FHIR_Organization", related_name="ClaimResponse_insurer", null=True, blank=True, on_delete=models.SET_NULL)
    requestor_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="ClaimResponse_requestor", null=True, blank=True, on_delete=models.SET_NULL)
    requestor_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="ClaimResponse_requestor", null=True, blank=True, on_delete=models.SET_NULL)
    requestor_Organization = models.ForeignKey("FHIR_Organization", related_name="ClaimResponse_requestor", null=True, blank=True, on_delete=models.SET_NULL)
    request = models.ForeignKey("FHIR_Claim", related_name="ClaimResponse_request", null=True, blank=True, on_delete=models.SET_NULL)
    class OutcomeChoices(models.TextChoices): QUEUED = 'queued', 'Queued'; COMPLETE = 'complete', 'Complete'; ERROR = 'error', 'Error'; PARTIAL = 'partial', 'Partial'; 
    outcome = FHIR_primitive_CodeField(choices=OutcomeChoices.choices, null=True, blank=True, )
    BINDING_decision = "TODO"
    decision_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_decision}, related_name='ClaimResponse_decision', blank=True)
    decision_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    disposition = FHIR_primitive_StringField(null=True, blank=True, )
    preAuthRef = FHIR_primitive_StringField(null=True, blank=True, )
    preAuthPeriod = models.OneToOneField("FHIR_GP_Period", related_name='ClaimResponse_preAuthPeriod', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_payeeType = "TODO"
    payeeType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_payeeType}, related_name='ClaimResponse_payeeType', blank=True)
    payeeType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    encounter = models.ManyToManyField("FHIR_Encounter", related_name="ClaimResponse_encounter", blank=True)
    BINDING_diagnosisRelatedGroup = "TODO"
    diagnosisRelatedGroup_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_diagnosisRelatedGroup}, related_name='ClaimResponse_diagnosisRelatedGroup', blank=True)
    diagnosisRelatedGroup_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_fundsReserve = "TODO"
    fundsReserve_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_fundsReserve}, related_name='ClaimResponse_fundsReserve', blank=True)
    fundsReserve_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_formCode = "TODO"
    formCode_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_formCode}, related_name='ClaimResponse_formCode', blank=True)
    formCode_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    form = models.OneToOneField("FHIR_GP_Attachment", related_name='ClaimResponse_form', null=True, blank=True, on_delete=models.SET_NULL)
    communicationRequest = models.ManyToManyField("FHIR_CommunicationRequest", related_name="ClaimResponse_communicationRequest", blank=True)

class FHIR_ClaimResponse_identifier(FHIR_GP_Identifier):
    ClaimResponse = models.ForeignKey(FHIR_ClaimResponse, related_name='ClaimResponse_identifier', null=False, on_delete=models.CASCADE)

class FHIR_ClaimResponse_traceNumber(FHIR_GP_Identifier):
    ClaimResponse = models.ForeignKey(FHIR_ClaimResponse, related_name='ClaimResponse_traceNumber', null=False, on_delete=models.CASCADE)

class FHIR_ClaimResponse_event(models.Model):
    ClaimResponse = models.ForeignKey(FHIR_ClaimResponse, related_name='ClaimResponse_event', null=False, on_delete=models.CASCADE)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='ClaimResponse_event_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    when = FHIR_primitive_DateTimeField(null=True, blank=True, )
    when = models.OneToOneField("FHIR_GP_Period", related_name='ClaimResponse_event_when', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ClaimResponse_item(models.Model):
    ClaimResponse = models.ForeignKey(FHIR_ClaimResponse, related_name='ClaimResponse_item', null=False, on_delete=models.CASCADE)
    itemSequence = FHIR_primitive_PositiveIntField(null=True, blank=True, )

class FHIR_ClaimResponse_item_traceNumber(FHIR_GP_Identifier):
    ClaimResponse_item = models.ForeignKey(FHIR_ClaimResponse_item, related_name='ClaimResponse_item_traceNumber', null=False, on_delete=models.CASCADE)

class FHIR_ClaimResponse_item_noteNumber(models.Model):
    ClaimResponse_item = models.ForeignKey(FHIR_ClaimResponse_item, related_name='ClaimResponse_item_noteNumber', null=False, on_delete=models.CASCADE)
    
    noteNumber = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    
class FHIR_ClaimResponse_item_reviewOutcome(models.Model):
    ClaimResponse_item = models.ForeignKey(FHIR_ClaimResponse_item, related_name='ClaimResponse_item_reviewOutcome', null=False, on_delete=models.CASCADE)
    BINDING_decision = "TODO"
    decision_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_decision}, related_name='ClaimResponse_item_reviewOutcome_decision', blank=True)
    decision_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    preAuthRef = FHIR_primitive_StringField(null=True, blank=True, )
    preAuthPeriod = models.OneToOneField("FHIR_GP_Period", related_name='ClaimResponse_item_reviewOutcome_preAuthPeriod', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ClaimResponse_item_reviewOutcome_reason(models.Model):
    ClaimResponse_item_reviewOutcome = models.ForeignKey(FHIR_ClaimResponse_item_reviewOutcome, related_name='ClaimResponse_item_reviewOutcome_reason', null=False, on_delete=models.CASCADE)
    BINDING_reason = "TODO"
    reason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_reason}, related_name='ClaimResponse_item_reviewOutcome_reason', blank=True)
    reason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ClaimResponse_item_adjudication(models.Model):
    ClaimResponse_item = models.ForeignKey(FHIR_ClaimResponse_item, related_name='ClaimResponse_item_adjudication', null=False, on_delete=models.CASCADE)
    BINDING_category = "TODO"
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='ClaimResponse_item_adjudication_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_reason = "TODO"
    reason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_reason}, related_name='ClaimResponse_item_adjudication_reason', blank=True)
    reason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    amount = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='ClaimResponse_item_adjudication_amount', null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='ClaimResponse_item_adjudication_quantity', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ClaimResponse_item_detail(models.Model):
    ClaimResponse_item = models.ForeignKey(FHIR_ClaimResponse_item, related_name='ClaimResponse_item_detail', null=False, on_delete=models.CASCADE)
    detailSequence = FHIR_primitive_PositiveIntField(null=True, blank=True, )

class FHIR_ClaimResponse_item_detail_traceNumber(FHIR_GP_Identifier):
    ClaimResponse_item_detail = models.ForeignKey(FHIR_ClaimResponse_item_detail, related_name='ClaimResponse_item_detail_traceNumber', null=False, on_delete=models.CASCADE)

class FHIR_ClaimResponse_item_detail_noteNumber(models.Model):
    ClaimResponse_item_detail = models.ForeignKey(FHIR_ClaimResponse_item_detail, related_name='ClaimResponse_item_detail_noteNumber', null=False, on_delete=models.CASCADE)
    
    noteNumber = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    
class FHIR_ClaimResponse_item_detail_subDetail(models.Model):
    ClaimResponse_item_detail = models.ForeignKey(FHIR_ClaimResponse_item_detail, related_name='ClaimResponse_item_detail_subDetail', null=False, on_delete=models.CASCADE)
    subDetailSequence = FHIR_primitive_PositiveIntField(null=True, blank=True, )

class FHIR_ClaimResponse_item_detail_subDetail_traceNumber(FHIR_GP_Identifier):
    ClaimResponse_item_detail_subDetail = models.ForeignKey(FHIR_ClaimResponse_item_detail_subDetail, related_name='ClaimResponse_item_detail_subDetail_traceNumber', null=False, on_delete=models.CASCADE)

class FHIR_ClaimResponse_item_detail_subDetail_noteNumber(models.Model):
    ClaimResponse_item_detail_subDetail = models.ForeignKey(FHIR_ClaimResponse_item_detail_subDetail, related_name='ClaimResponse_item_detail_subDetail_noteNumber', null=False, on_delete=models.CASCADE)
    
    noteNumber = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    
class FHIR_ClaimResponse_addItem(models.Model):
    ClaimResponse = models.ForeignKey(FHIR_ClaimResponse, related_name='ClaimResponse_addItem', null=False, on_delete=models.CASCADE)
    provider_Practitioner = models.ManyToManyField("FHIR_Practitioner", related_name="ClaimResponse_addItem_provider", blank=True)
    provider_PractitionerRole = models.ManyToManyField("FHIR_PractitionerRole", related_name="ClaimResponse_addItem_provider", blank=True)
    provider_Organization = models.ManyToManyField("FHIR_Organization", related_name="ClaimResponse_addItem_provider", blank=True)
    BINDING_revenue = "TODO"
    revenue_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_revenue}, related_name='ClaimResponse_addItem_revenue', blank=True)
    revenue_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_productOrService = "TODO"
    productOrService_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_productOrService}, related_name='ClaimResponse_addItem_productOrService', blank=True)
    productOrService_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_productOrServiceEnd = "TODO"
    productOrServiceEnd_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_productOrServiceEnd}, related_name='ClaimResponse_addItem_productOrServiceEnd', blank=True)
    productOrServiceEnd_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    request_DeviceRequest = models.ManyToManyField("FHIR_DeviceRequest", related_name="ClaimResponse_addItem_request", blank=True)
    request_MedicationRequest = models.ManyToManyField("FHIR_MedicationRequest", related_name="ClaimResponse_addItem_request", blank=True)
    request_NutritionOrder = models.ManyToManyField("FHIR_NutritionOrder", related_name="ClaimResponse_addItem_request", blank=True)
    request_ServiceRequest = models.ManyToManyField("FHIR_ServiceRequest", related_name="ClaimResponse_addItem_request", blank=True)
    request_SupplyRequest = models.ManyToManyField("FHIR_SupplyRequest", related_name="ClaimResponse_addItem_request", blank=True)
    request_VisionPrescription = models.ManyToManyField("FHIR_VisionPrescription", related_name="ClaimResponse_addItem_request", blank=True)
    serviced = FHIR_primitive_DateField(null=True, blank=True, )
    serviced = models.OneToOneField("FHIR_GP_Period", related_name='ClaimResponse_addItem_serviced', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_location = "TODO"
    location_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_location}, related_name='ClaimResponse_addItem_location', blank=True)
    location_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    location = models.OneToOneField("FHIR_GP_Address", related_name='ClaimResponse_addItem_location', null=True, blank=True, on_delete=models.SET_NULL)
    location = models.ForeignKey("FHIR_Location", related_name="ClaimResponse_addItem_location", null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='ClaimResponse_addItem_quantity', null=True, blank=True, on_delete=models.SET_NULL)
    unitPrice = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='ClaimResponse_addItem_unitPrice', null=True, blank=True, on_delete=models.SET_NULL)
    factor = FHIR_primitive_DecimalField(null=True, blank=True, )
    tax = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='ClaimResponse_addItem_tax', null=True, blank=True, on_delete=models.SET_NULL)
    net = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='ClaimResponse_addItem_net', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ClaimResponse_addItem_itemSequence(models.Model):
    ClaimResponse_addItem = models.ForeignKey(FHIR_ClaimResponse_addItem, related_name='ClaimResponse_addItem_itemSequence', null=False, on_delete=models.CASCADE)
    
    itemSequence = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    
class FHIR_ClaimResponse_addItem_detailSequence(models.Model):
    ClaimResponse_addItem = models.ForeignKey(FHIR_ClaimResponse_addItem, related_name='ClaimResponse_addItem_detailSequence', null=False, on_delete=models.CASCADE)
    
    detailSequence = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    
class FHIR_ClaimResponse_addItem_subdetailSequence(models.Model):
    ClaimResponse_addItem = models.ForeignKey(FHIR_ClaimResponse_addItem, related_name='ClaimResponse_addItem_subdetailSequence', null=False, on_delete=models.CASCADE)
    
    subdetailSequence = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    
class FHIR_ClaimResponse_addItem_traceNumber(FHIR_GP_Identifier):
    ClaimResponse_addItem = models.ForeignKey(FHIR_ClaimResponse_addItem, related_name='ClaimResponse_addItem_traceNumber', null=False, on_delete=models.CASCADE)

class FHIR_ClaimResponse_addItem_modifier(models.Model):
    ClaimResponse_addItem = models.ForeignKey(FHIR_ClaimResponse_addItem, related_name='ClaimResponse_addItem_modifier', null=False, on_delete=models.CASCADE)
    BINDING_modifier = "TODO"
    modifier_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_modifier}, related_name='ClaimResponse_addItem_modifier', blank=True)
    modifier_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ClaimResponse_addItem_programCode(models.Model):
    ClaimResponse_addItem = models.ForeignKey(FHIR_ClaimResponse_addItem, related_name='ClaimResponse_addItem_programCode', null=False, on_delete=models.CASCADE)
    BINDING_programCode = "TODO"
    programCode_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_programCode}, related_name='ClaimResponse_addItem_programCode', blank=True)
    programCode_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ClaimResponse_addItem_bodySite(models.Model):
    ClaimResponse_addItem = models.ForeignKey(FHIR_ClaimResponse_addItem, related_name='ClaimResponse_addItem_bodySite', null=False, on_delete=models.CASCADE)

class FHIR_ClaimResponse_addItem_bodySite_site(models.Model):
    ClaimResponse_addItem_bodySite = models.ForeignKey(FHIR_ClaimResponse_addItem_bodySite, related_name='ClaimResponse_addItem_bodySite_site', null=False, on_delete=models.CASCADE)
    BINDING_site = "TODO"
    site_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_site}, related_name='ClaimResponse_addItem_bodySite_site', blank=True)
    site_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    site_BodyStructure_ref = models.ForeignKey("FHIR_BodyStructure", related_name="ClaimResponse_addItem_bodySite_site_BodyStructure", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ClaimResponse_addItem_bodySite_subSite(models.Model):
    ClaimResponse_addItem_bodySite = models.ForeignKey(FHIR_ClaimResponse_addItem_bodySite, related_name='ClaimResponse_addItem_bodySite_subSite', null=False, on_delete=models.CASCADE)
    BINDING_subSite = "TODO"
    subSite_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_subSite}, related_name='ClaimResponse_addItem_bodySite_subSite', blank=True)
    subSite_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ClaimResponse_addItem_noteNumber(models.Model):
    ClaimResponse_addItem = models.ForeignKey(FHIR_ClaimResponse_addItem, related_name='ClaimResponse_addItem_noteNumber', null=False, on_delete=models.CASCADE)
    
    noteNumber = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    
class FHIR_ClaimResponse_addItem_detail(models.Model):
    ClaimResponse_addItem = models.ForeignKey(FHIR_ClaimResponse_addItem, related_name='ClaimResponse_addItem_detail', null=False, on_delete=models.CASCADE)
    BINDING_revenue = "TODO"
    revenue_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_revenue}, related_name='ClaimResponse_addItem_detail_revenue', blank=True)
    revenue_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_productOrService = "TODO"
    productOrService_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_productOrService}, related_name='ClaimResponse_addItem_detail_productOrService', blank=True)
    productOrService_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_productOrServiceEnd = "TODO"
    productOrServiceEnd_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_productOrServiceEnd}, related_name='ClaimResponse_addItem_detail_productOrServiceEnd', blank=True)
    productOrServiceEnd_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='ClaimResponse_addItem_detail_quantity', null=True, blank=True, on_delete=models.SET_NULL)
    unitPrice = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='ClaimResponse_addItem_detail_unitPrice', null=True, blank=True, on_delete=models.SET_NULL)
    factor = FHIR_primitive_DecimalField(null=True, blank=True, )
    tax = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='ClaimResponse_addItem_detail_tax', null=True, blank=True, on_delete=models.SET_NULL)
    net = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='ClaimResponse_addItem_detail_net', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ClaimResponse_addItem_detail_traceNumber(FHIR_GP_Identifier):
    ClaimResponse_addItem_detail = models.ForeignKey(FHIR_ClaimResponse_addItem_detail, related_name='ClaimResponse_addItem_detail_traceNumber', null=False, on_delete=models.CASCADE)

class FHIR_ClaimResponse_addItem_detail_modifier(models.Model):
    ClaimResponse_addItem_detail = models.ForeignKey(FHIR_ClaimResponse_addItem_detail, related_name='ClaimResponse_addItem_detail_modifier', null=False, on_delete=models.CASCADE)
    BINDING_modifier = "TODO"
    modifier_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_modifier}, related_name='ClaimResponse_addItem_detail_modifier', blank=True)
    modifier_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ClaimResponse_addItem_detail_noteNumber(models.Model):
    ClaimResponse_addItem_detail = models.ForeignKey(FHIR_ClaimResponse_addItem_detail, related_name='ClaimResponse_addItem_detail_noteNumber', null=False, on_delete=models.CASCADE)
    
    noteNumber = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    
class FHIR_ClaimResponse_addItem_detail_subDetail(models.Model):
    ClaimResponse_addItem_detail = models.ForeignKey(FHIR_ClaimResponse_addItem_detail, related_name='ClaimResponse_addItem_detail_subDetail', null=False, on_delete=models.CASCADE)
    BINDING_revenue = "TODO"
    revenue_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_revenue}, related_name='ClaimResponse_addItem_detail_subDetail_revenue', blank=True)
    revenue_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_productOrService = "TODO"
    productOrService_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_productOrService}, related_name='ClaimResponse_addItem_detail_subDetail_productOrService', blank=True)
    productOrService_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_productOrServiceEnd = "TODO"
    productOrServiceEnd_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_productOrServiceEnd}, related_name='ClaimResponse_addItem_detail_subDetail_productOrServiceEnd', blank=True)
    productOrServiceEnd_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='ClaimResponse_addItem_detail_subDetail_quantity', null=True, blank=True, on_delete=models.SET_NULL)
    unitPrice = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='ClaimResponse_addItem_detail_subDetail_unitPrice', null=True, blank=True, on_delete=models.SET_NULL)
    factor = FHIR_primitive_DecimalField(null=True, blank=True, )
    tax = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='ClaimResponse_addItem_detail_subDetail_tax', null=True, blank=True, on_delete=models.SET_NULL)
    net = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='ClaimResponse_addItem_detail_subDetail_net', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ClaimResponse_addItem_detail_subDetail_traceNumber(FHIR_GP_Identifier):
    ClaimResponse_addItem_detail_subDetail = models.ForeignKey(FHIR_ClaimResponse_addItem_detail_subDetail, related_name='ClaimResponse_addItem_detail_subDetail_traceNumber', null=False, on_delete=models.CASCADE)

class FHIR_ClaimResponse_addItem_detail_subDetail_modifier(models.Model):
    ClaimResponse_addItem_detail_subDetail = models.ForeignKey(FHIR_ClaimResponse_addItem_detail_subDetail, related_name='ClaimResponse_addItem_detail_subDetail_modifier', null=False, on_delete=models.CASCADE)
    BINDING_modifier = "TODO"
    modifier_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_modifier}, related_name='ClaimResponse_addItem_detail_subDetail_modifier', blank=True)
    modifier_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ClaimResponse_addItem_detail_subDetail_noteNumber(models.Model):
    ClaimResponse_addItem_detail_subDetail = models.ForeignKey(FHIR_ClaimResponse_addItem_detail_subDetail, related_name='ClaimResponse_addItem_detail_subDetail_noteNumber', null=False, on_delete=models.CASCADE)
    
    noteNumber = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    
class FHIR_ClaimResponse_total(models.Model):
    ClaimResponse = models.ForeignKey(FHIR_ClaimResponse, related_name='ClaimResponse_total', null=False, on_delete=models.CASCADE)
    BINDING_category = "TODO"
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='ClaimResponse_total_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    amount = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='ClaimResponse_total_amount', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ClaimResponse_payment(models.Model):
    ClaimResponse = models.ForeignKey(FHIR_ClaimResponse, related_name='ClaimResponse_payment', null=False, on_delete=models.CASCADE)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='ClaimResponse_payment_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    adjustment = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='ClaimResponse_payment_adjustment', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_adjustmentReason = "TODO"
    adjustmentReason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_adjustmentReason}, related_name='ClaimResponse_payment_adjustmentReason', blank=True)
    adjustmentReason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    date = FHIR_primitive_DateField(null=True, blank=True, )
    amount = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='ClaimResponse_payment_amount', null=True, blank=True, on_delete=models.SET_NULL)
    identifier = models.OneToOneField("FHIR_GP_Identifier", related_name='ClaimResponse_payment_identifier', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ClaimResponse_processNote(models.Model):
    ClaimResponse = models.ForeignKey(FHIR_ClaimResponse, related_name='ClaimResponse_processNote', null=False, on_delete=models.CASCADE)
    number = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='ClaimResponse_processNote_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    text = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_language = "TODO"
    language_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_language}, related_name='ClaimResponse_processNote_language', blank=True)
    language_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_ClaimResponse_insurance(models.Model):
    ClaimResponse = models.ForeignKey(FHIR_ClaimResponse, related_name='ClaimResponse_insurance', null=False, on_delete=models.CASCADE)
    sequence = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    focal = FHIR_primitive_BooleanField(null=True, blank=True, )
    coverage = models.ForeignKey("FHIR_Coverage", related_name="ClaimResponse_insurance_coverage", null=True, blank=True, on_delete=models.SET_NULL)
    businessArrangement = FHIR_primitive_StringField(null=True, blank=True, )
    claimResponse = models.ForeignKey("FHIR_ClaimResponse", related_name="ClaimResponse_insurance_claimResponse", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ClaimResponse_error(models.Model):
    ClaimResponse = models.ForeignKey(FHIR_ClaimResponse, related_name='ClaimResponse_error', null=False, on_delete=models.CASCADE)
    itemSequence = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    detailSequence = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    subDetailSequence = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    BINDING_code = "TODO"
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='ClaimResponse_error_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_ClaimResponse_error_expression(models.Model):
    ClaimResponse_error = models.ForeignKey(FHIR_ClaimResponse_error, related_name='ClaimResponse_error_expression', null=False, on_delete=models.CASCADE)
    
    expression = FHIR_primitive_StringField(null=True, blank=True, )
    