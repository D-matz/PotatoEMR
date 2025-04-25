
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_PaymentNotice(models.Model):
    class StatusChoices(models.TextChoices): ACTIVE = 'active', 'Active'; CANCELLED = 'cancelled', 'Cancelled'; DRAFT = 'draft', 'Draft'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    created = FHIR_primitive_DateTimeField(null=True, blank=True, )
    reporter_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="PaymentNotice_reporter", null=True, blank=True, on_delete=models.SET_NULL)
    reporter_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="PaymentNotice_reporter", null=True, blank=True, on_delete=models.SET_NULL)
    reporter_Organization = models.ForeignKey("FHIR_Organization", related_name="PaymentNotice_reporter", null=True, blank=True, on_delete=models.SET_NULL)
    payment = models.ForeignKey("FHIR_PaymentReconciliation", related_name="PaymentNotice_payment", null=True, blank=True, on_delete=models.SET_NULL)
    paymentDate = FHIR_primitive_DateField(null=True, blank=True, )
    payee_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="PaymentNotice_payee", null=True, blank=True, on_delete=models.SET_NULL)
    payee_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="PaymentNotice_payee", null=True, blank=True, on_delete=models.SET_NULL)
    payee_Organization = models.ForeignKey("FHIR_Organization", related_name="PaymentNotice_payee", null=True, blank=True, on_delete=models.SET_NULL)
    recipient = models.ForeignKey("FHIR_Organization", related_name="PaymentNotice_recipient", null=True, blank=True, on_delete=models.SET_NULL)
    amount = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='PaymentNotice_amount', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_paymentStatus = 'TODO'
    paymentStatus_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_paymentStatus}, related_name='PaymentNotice_paymentStatus', blank=True)
    paymentStatus_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_PaymentNotice_identifier(FHIR_GP_Identifier):
    PaymentNotice = models.ForeignKey(FHIR_PaymentNotice, related_name='PaymentNotice_identifier', null=False, on_delete=models.CASCADE)
