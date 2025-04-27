#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Invoice(models.Model):
    class StatusChoices(models.TextChoices): DRAFT = 'draft', 'Draft'; ISSUED = 'issued', 'Issued'; BALANCED = 'balanced', 'Balanced'; CANCELLED = 'cancelled', 'Cancelled'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    cancelledReason = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Invoice_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    subject_Patient = models.ForeignKey("FHIR_Patient", related_name="Invoice_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Group = models.ForeignKey("FHIR_Group", related_name="Invoice_subject", null=True, blank=True, on_delete=models.SET_NULL)
    recipient_Organization = models.ForeignKey("FHIR_Organization", related_name="Invoice_recipient", null=True, blank=True, on_delete=models.SET_NULL)
    recipient_Patient = models.ForeignKey("FHIR_Patient", related_name="Invoice_recipient", null=True, blank=True, on_delete=models.SET_NULL)
    recipient_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="Invoice_recipient", null=True, blank=True, on_delete=models.SET_NULL)
    date = FHIR_primitive_DateTimeField(null=True, blank=True, )
    creation = FHIR_primitive_DateTimeField(null=True, blank=True, )
    period = FHIR_primitive_DateField(null=True, blank=True, )
    period = models.OneToOneField("FHIR_GP_Period", related_name='Invoice_period', null=True, blank=True, on_delete=models.SET_NULL)
    issuer = models.ForeignKey("FHIR_Organization", related_name="Invoice_issuer", null=True, blank=True, on_delete=models.SET_NULL)
    account = models.ForeignKey("FHIR_Account", related_name="Invoice_account", null=True, blank=True, on_delete=models.SET_NULL)
    totalNet = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='Invoice_totalNet', null=True, blank=True, on_delete=models.SET_NULL)
    totalGross = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='Invoice_totalGross', null=True, blank=True, on_delete=models.SET_NULL)
    paymentTerms = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_Invoice_identifier(FHIR_GP_Identifier):
    Invoice = models.ForeignKey(FHIR_Invoice, related_name='Invoice_identifier', null=False, on_delete=models.CASCADE)

class FHIR_Invoice_participant(models.Model):
    Invoice = models.ForeignKey(FHIR_Invoice, related_name='Invoice_participant', null=False, on_delete=models.CASCADE)
    BINDING_role = "TODO"
    role_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_role}, related_name='Invoice_participant_role', blank=True)
    role_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    actor_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="Invoice_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Organization = models.ForeignKey("FHIR_Organization", related_name="Invoice_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Patient = models.ForeignKey("FHIR_Patient", related_name="Invoice_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="Invoice_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Device = models.ForeignKey("FHIR_Device", related_name="Invoice_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="Invoice_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Invoice_lineItem(models.Model):
    Invoice = models.ForeignKey(FHIR_Invoice, related_name='Invoice_lineItem', null=False, on_delete=models.CASCADE)
    sequence = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    serviced = FHIR_primitive_DateField(null=True, blank=True, )
    serviced = models.OneToOneField("FHIR_GP_Period", related_name='Invoice_lineItem_serviced', null=True, blank=True, on_delete=models.SET_NULL)
    chargeItem = models.ForeignKey("FHIR_ChargeItem", related_name="Invoice_lineItem_chargeItem", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_chargeItem = "TODO"
    chargeItem_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_chargeItem}, related_name='Invoice_lineItem_chargeItem', blank=True)
    chargeItem_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_Invoice_note(FHIR_GP_Annotation):
    Invoice = models.ForeignKey(FHIR_Invoice, related_name='Invoice_note', null=False, on_delete=models.CASCADE)
