#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_PaymentReconciliation(models.Model):
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='PaymentReconciliation_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    class StatusChoices(models.TextChoices): ACTIVE = 'active', 'Active'; CANCELLED = 'cancelled', 'Cancelled'; DRAFT = 'draft', 'Draft'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    BINDING_kind = "TODO"
    kind_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_kind}, related_name='PaymentReconciliation_kind', blank=True)
    kind_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    period = models.OneToOneField("FHIR_GP_Period", related_name='PaymentReconciliation_period', null=True, blank=True, on_delete=models.SET_NULL)
    created = FHIR_primitive_DateTimeField(null=True, blank=True, )
    enterer_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="PaymentReconciliation_enterer", null=True, blank=True, on_delete=models.SET_NULL)
    enterer_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="PaymentReconciliation_enterer", null=True, blank=True, on_delete=models.SET_NULL)
    enterer_Organization = models.ForeignKey("FHIR_Organization", related_name="PaymentReconciliation_enterer", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_issuerType = "TODO"
    issuerType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_issuerType}, related_name='PaymentReconciliation_issuerType', blank=True)
    issuerType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    paymentIssuer_Organization = models.ForeignKey("FHIR_Organization", related_name="PaymentReconciliation_paymentIssuer", null=True, blank=True, on_delete=models.SET_NULL)
    paymentIssuer_Patient = models.ForeignKey("FHIR_Patient", related_name="PaymentReconciliation_paymentIssuer", null=True, blank=True, on_delete=models.SET_NULL)
    paymentIssuer_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="PaymentReconciliation_paymentIssuer", null=True, blank=True, on_delete=models.SET_NULL)
    request = models.ForeignKey("FHIR_Task", related_name="PaymentReconciliation_request", null=True, blank=True, on_delete=models.SET_NULL)
    requestor_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="PaymentReconciliation_requestor", null=True, blank=True, on_delete=models.SET_NULL)
    requestor_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="PaymentReconciliation_requestor", null=True, blank=True, on_delete=models.SET_NULL)
    requestor_Organization = models.ForeignKey("FHIR_Organization", related_name="PaymentReconciliation_requestor", null=True, blank=True, on_delete=models.SET_NULL)
    class OutcomeChoices(models.TextChoices): QUEUED = 'queued', 'Queued'; COMPLETE = 'complete', 'Complete'; ERROR = 'error', 'Error'; PARTIAL = 'partial', 'Partial'; 
    outcome = FHIR_primitive_CodeField(choices=OutcomeChoices.choices, null=True, blank=True, )
    disposition = FHIR_primitive_StringField(null=True, blank=True, )
    date = FHIR_primitive_DateField(null=True, blank=True, )
    location = models.ForeignKey("FHIR_Location", related_name="PaymentReconciliation_location", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_method = "TODO"
    method_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_method}, related_name='PaymentReconciliation_method', blank=True)
    method_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    cardBrand = FHIR_primitive_StringField(null=True, blank=True, )
    accountNumber = FHIR_primitive_StringField(null=True, blank=True, )
    expirationDate = FHIR_primitive_DateField(null=True, blank=True, )
    processor = FHIR_primitive_StringField(null=True, blank=True, )
    referenceNumber = FHIR_primitive_StringField(null=True, blank=True, )
    authorization = FHIR_primitive_StringField(null=True, blank=True, )
    tenderedAmount = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='PaymentReconciliation_tenderedAmount', null=True, blank=True, on_delete=models.SET_NULL)
    returnedAmount = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='PaymentReconciliation_returnedAmount', null=True, blank=True, on_delete=models.SET_NULL)
    amount = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='PaymentReconciliation_amount', null=True, blank=True, on_delete=models.SET_NULL)
    paymentIdentifier = models.OneToOneField("FHIR_GP_Identifier", related_name='PaymentReconciliation_paymentIdentifier', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_formCode = "TODO"
    formCode_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_formCode}, related_name='PaymentReconciliation_formCode', blank=True)
    formCode_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_PaymentReconciliation_identifier(FHIR_GP_Identifier):
    PaymentReconciliation = models.ForeignKey(FHIR_PaymentReconciliation, related_name='PaymentReconciliation_identifier', null=False, on_delete=models.CASCADE)

class FHIR_PaymentReconciliation_allocation(models.Model):
    PaymentReconciliation = models.ForeignKey(FHIR_PaymentReconciliation, related_name='PaymentReconciliation_allocation', null=False, on_delete=models.CASCADE)
    identifier = models.OneToOneField("FHIR_GP_Identifier", related_name='PaymentReconciliation_allocation_identifier', null=True, blank=True, on_delete=models.SET_NULL)
    predecessor = models.OneToOneField("FHIR_GP_Identifier", related_name='PaymentReconciliation_allocation_predecessor', null=True, blank=True, on_delete=models.SET_NULL)
    target_Claim = models.ForeignKey("FHIR_Claim", related_name="PaymentReconciliation_allocation_target", null=True, blank=True, on_delete=models.SET_NULL)
    target_Account = models.ForeignKey("FHIR_Account", related_name="PaymentReconciliation_allocation_target", null=True, blank=True, on_delete=models.SET_NULL)
    target_Invoice = models.ForeignKey("FHIR_Invoice", related_name="PaymentReconciliation_allocation_target", null=True, blank=True, on_delete=models.SET_NULL)
    target_ChargeItem = models.ForeignKey("FHIR_ChargeItem", related_name="PaymentReconciliation_allocation_target", null=True, blank=True, on_delete=models.SET_NULL)
    target_Encounter = models.ForeignKey("FHIR_Encounter", related_name="PaymentReconciliation_allocation_target", null=True, blank=True, on_delete=models.SET_NULL)
    target_Contract = models.ForeignKey("FHIR_Contract", related_name="PaymentReconciliation_allocation_target", null=True, blank=True, on_delete=models.SET_NULL)
    targetItem_string = FHIR_primitive_StringField(null=True, blank=True, )
    targetItem_Identifier = models.OneToOneField("FHIR_GP_Identifier", related_name='PaymentReconciliation_allocation_targetItem_Identifier', null=True, blank=True, on_delete=models.SET_NULL)
    targetItem_positiveInt = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    encounter = models.ForeignKey("FHIR_Encounter", related_name="PaymentReconciliation_allocation_encounter", null=True, blank=True, on_delete=models.SET_NULL)
    account = models.ForeignKey("FHIR_Account", related_name="PaymentReconciliation_allocation_account", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='PaymentReconciliation_allocation_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    submitter_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="PaymentReconciliation_allocation_submitter", null=True, blank=True, on_delete=models.SET_NULL)
    submitter_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="PaymentReconciliation_allocation_submitter", null=True, blank=True, on_delete=models.SET_NULL)
    submitter_Organization = models.ForeignKey("FHIR_Organization", related_name="PaymentReconciliation_allocation_submitter", null=True, blank=True, on_delete=models.SET_NULL)
    response = models.ForeignKey("FHIR_ClaimResponse", related_name="PaymentReconciliation_allocation_response", null=True, blank=True, on_delete=models.SET_NULL)
    date = FHIR_primitive_DateField(null=True, blank=True, )
    responsible = models.ForeignKey("FHIR_PractitionerRole", related_name="PaymentReconciliation_allocation_responsible", null=True, blank=True, on_delete=models.SET_NULL)
    payee_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="PaymentReconciliation_allocation_payee", null=True, blank=True, on_delete=models.SET_NULL)
    payee_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="PaymentReconciliation_allocation_payee", null=True, blank=True, on_delete=models.SET_NULL)
    payee_Organization = models.ForeignKey("FHIR_Organization", related_name="PaymentReconciliation_allocation_payee", null=True, blank=True, on_delete=models.SET_NULL)
    amount = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='PaymentReconciliation_allocation_amount', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_PaymentReconciliation_processNote(models.Model):
    PaymentReconciliation = models.ForeignKey(FHIR_PaymentReconciliation, related_name='PaymentReconciliation_processNote', null=False, on_delete=models.CASCADE)
    class TypeChoices(models.TextChoices): DISPLAY = 'display', 'Display'; PRINT = 'print', 'Print'; PRINTOPER = 'printoper', 'Printoper'; 
    type = FHIR_primitive_CodeField(choices=TypeChoices.choices, null=True, blank=True, )
    text = FHIR_primitive_StringField(null=True, blank=True, )
