
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Coverage(models.Model):
    class StatusChoices(models.TextChoices): ACTIVE = 'active', 'Active'; CANCELLED = 'cancelled', 'Cancelled'; DRAFT = 'draft', 'Draft'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    class KindChoices(models.TextChoices): INSURANCE = 'insurance', 'Insurance'; SELF_PAY = 'self-pay', 'Self-pay'; OTHER = 'other', 'Other'; 
    kind = FHIR_primitive_CodeField(choices=KindChoices.choices, null=True, blank=True, )
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Coverage_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    policyHolder_Patient = models.ForeignKey("FHIR_Patient", related_name="Coverage_policyHolder", null=True, blank=True, on_delete=models.SET_NULL)
    policyHolder_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="Coverage_policyHolder", null=True, blank=True, on_delete=models.SET_NULL)
    policyHolder_Organization = models.ForeignKey("FHIR_Organization", related_name="Coverage_policyHolder", null=True, blank=True, on_delete=models.SET_NULL)
    subscriber_Patient = models.ForeignKey("FHIR_Patient", related_name="Coverage_subscriber", null=True, blank=True, on_delete=models.SET_NULL)
    subscriber_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="Coverage_subscriber", null=True, blank=True, on_delete=models.SET_NULL)
    beneficiary = models.ForeignKey("FHIR_Patient", related_name="Coverage_beneficiary", null=True, blank=True, on_delete=models.SET_NULL)
    dependent = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_relationship = 'TODO'
    relationship_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_relationship}, related_name='Coverage_relationship', blank=True)
    relationship_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    period = models.OneToOneField("FHIR_GP_Period", related_name='Coverage_period', null=True, blank=True, on_delete=models.SET_NULL)
    insurer = models.ForeignKey("FHIR_Organization", related_name="Coverage_insurer", null=True, blank=True, on_delete=models.SET_NULL)
    order = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    network = FHIR_primitive_StringField(null=True, blank=True, )
    subrogation = FHIR_primitive_BooleanField(null=True, blank=True, )
    contract = models.ManyToManyField("FHIR_Contract", related_name="Coverage_contract", blank=True)
    insurancePlan = models.ForeignKey("FHIR_InsurancePlan", related_name="Coverage_insurancePlan", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Coverage_identifier(FHIR_GP_Identifier):
    Coverage = models.ForeignKey(FHIR_Coverage, related_name='Coverage_identifier', null=False, on_delete=models.CASCADE)

class FHIR_Coverage_paymentBy(models.Model):
    Coverage = models.ForeignKey(FHIR_Coverage, related_name='Coverage_paymentBy', null=False, on_delete=models.CASCADE)
    party_Patient = models.ForeignKey("FHIR_Patient", related_name="Coverage_paymentBy_party", null=True, blank=True, on_delete=models.SET_NULL)
    party_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="Coverage_paymentBy_party", null=True, blank=True, on_delete=models.SET_NULL)
    party_Organization = models.ForeignKey("FHIR_Organization", related_name="Coverage_paymentBy_party", null=True, blank=True, on_delete=models.SET_NULL)
    responsibility = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_Coverage_subscriberId(FHIR_GP_Identifier):
    Coverage = models.ForeignKey(FHIR_Coverage, related_name='Coverage_subscriberId', null=False, on_delete=models.CASCADE)

class FHIR_Coverage_class(models.Model):
    Coverage = models.ForeignKey(FHIR_Coverage, related_name='Coverage_class', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Coverage_class_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value = models.OneToOneField("FHIR_GP_Identifier", related_name='Coverage_class_value', null=True, blank=True, on_delete=models.SET_NULL)
    name = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_Coverage_costToBeneficiary(models.Model):
    Coverage = models.ForeignKey(FHIR_Coverage, related_name='Coverage_costToBeneficiary', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Coverage_costToBeneficiary_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_category = 'TODO'
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='Coverage_costToBeneficiary_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_network = 'TODO'
    network_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_network}, related_name='Coverage_costToBeneficiary_network', blank=True)
    network_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_unit = 'TODO'
    unit_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_unit}, related_name='Coverage_costToBeneficiary_unit', blank=True)
    unit_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_term = 'TODO'
    term_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_term}, related_name='Coverage_costToBeneficiary_term', blank=True)
    term_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value = models.OneToOneField("FHIR_GP_Quantity", related_name='Coverage_costToBeneficiary_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='Coverage_costToBeneficiary_value', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Coverage_costToBeneficiary_exception(models.Model):
    Coverage_costToBeneficiary = models.ForeignKey(FHIR_Coverage_costToBeneficiary, related_name='Coverage_costToBeneficiary_exception', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Coverage_costToBeneficiary_exception_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    period = models.OneToOneField("FHIR_GP_Period", related_name='Coverage_costToBeneficiary_exception_period', null=True, blank=True, on_delete=models.SET_NULL)
