
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_InsuranceProduct(models.Model):
    class StatusChoices(models.TextChoices): DRAFT = 'draft', 'Draft'; ACTIVE = 'active', 'Active'; RETIRED = 'retired', 'Retired'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    name = FHIR_primitive_StringField(null=True, blank=True, )
    period = models.OneToOneField("FHIR_GP_Period", related_name='InsuranceProduct_period', null=True, blank=True, on_delete=models.SET_NULL)
    ownedBy = models.ForeignKey("FHIR_Organization", related_name="InsuranceProduct_ownedBy", null=True, blank=True, on_delete=models.SET_NULL)
    administeredBy = models.ForeignKey("FHIR_Organization", related_name="InsuranceProduct_administeredBy", null=True, blank=True, on_delete=models.SET_NULL)
    coverageArea = models.ManyToManyField("FHIR_Location", related_name="InsuranceProduct_coverageArea", blank=True)
    endpoint = models.ManyToManyField("FHIR_Endpoint", related_name="InsuranceProduct_endpoint", blank=True)
    network = models.ManyToManyField("FHIR_Organization", related_name="InsuranceProduct_network", blank=True)

class FHIR_InsuranceProduct_identifier(FHIR_GP_Identifier):
    InsuranceProduct = models.ForeignKey(FHIR_InsuranceProduct, related_name='InsuranceProduct_identifier', null=False, on_delete=models.CASCADE)

class FHIR_InsuranceProduct_type(models.Model):
    InsuranceProduct = models.ForeignKey(FHIR_InsuranceProduct, related_name='InsuranceProduct_type', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='InsuranceProduct_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_InsuranceProduct_alias(models.Model):
    InsuranceProduct = models.ForeignKey(FHIR_InsuranceProduct, related_name='InsuranceProduct_alias', null=False, on_delete=models.CASCADE)
    
    alias = FHIR_primitive_StringField(null=True, blank=True, )
    
class FHIR_InsuranceProduct_contact(FHIR_meta_ExtendedContactDetail):
    InsuranceProduct = models.ForeignKey(FHIR_InsuranceProduct, related_name='InsuranceProduct_contact', null=False, on_delete=models.CASCADE)

class FHIR_InsuranceProduct_coverage(models.Model):
    InsuranceProduct = models.ForeignKey(FHIR_InsuranceProduct, related_name='InsuranceProduct_coverage', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='InsuranceProduct_coverage_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    network = models.ManyToManyField("FHIR_Organization", related_name="InsuranceProduct_coverage_network", blank=True)

class FHIR_InsuranceProduct_coverage_benefit(models.Model):
    InsuranceProduct_coverage = models.ForeignKey(FHIR_InsuranceProduct_coverage, related_name='InsuranceProduct_coverage_benefit', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='InsuranceProduct_coverage_benefit_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    requirement = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_InsuranceProduct_coverage_benefit_limit(models.Model):
    InsuranceProduct_coverage_benefit = models.ForeignKey(FHIR_InsuranceProduct_coverage_benefit, related_name='InsuranceProduct_coverage_benefit_limit', null=False, on_delete=models.CASCADE)
    value = models.OneToOneField("FHIR_GP_Quantity", related_name='InsuranceProduct_coverage_benefit_limit_value', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_code = 'TODO'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='InsuranceProduct_coverage_benefit_limit_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_InsuranceProduct_related(models.Model):
    InsuranceProduct = models.ForeignKey(FHIR_InsuranceProduct, related_name='InsuranceProduct_related', null=False, on_delete=models.CASCADE)
    product = models.ForeignKey("FHIR_InsuranceProduct", related_name="InsuranceProduct_related_product", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_relationship = 'TODO'
    relationship_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_relationship}, related_name='InsuranceProduct_related_relationship', blank=True)
    relationship_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    period = models.OneToOneField("FHIR_GP_Period", related_name='InsuranceProduct_related_period', null=True, blank=True, on_delete=models.SET_NULL)
