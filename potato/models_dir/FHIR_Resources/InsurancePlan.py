#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_InsurancePlan(models.Model):
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='InsurancePlan_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    product = models.ForeignKey("FHIR_InsuranceProduct", related_name="InsurancePlan_product", null=True, blank=True, on_delete=models.SET_NULL)
    coverageArea = models.ManyToManyField("FHIR_Location", related_name="InsurancePlan_coverageArea", blank=True)
    network = models.ManyToManyField("FHIR_Organization", related_name="InsurancePlan_network", blank=True)

class FHIR_InsurancePlan_identifier(FHIR_GP_Identifier):
    InsurancePlan = models.ForeignKey(FHIR_InsurancePlan, related_name='InsurancePlan_identifier', null=False, on_delete=models.CASCADE)

class FHIR_InsurancePlan_generalCost(models.Model):
    InsurancePlan = models.ForeignKey(FHIR_InsurancePlan, related_name='InsurancePlan_generalCost', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='InsurancePlan_generalCost_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    groupSize = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    cost = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='InsurancePlan_generalCost_cost', null=True, blank=True, on_delete=models.SET_NULL)
    comment = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_InsurancePlan_specificCost(models.Model):
    InsurancePlan = models.ForeignKey(FHIR_InsurancePlan, related_name='InsurancePlan_specificCost', null=False, on_delete=models.CASCADE)
    BINDING_category = 'TODO'
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='InsurancePlan_specificCost_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_InsurancePlan_specificCost_benefit(models.Model):
    InsurancePlan_specificCost = models.ForeignKey(FHIR_InsurancePlan_specificCost, related_name='InsurancePlan_specificCost_benefit', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='InsurancePlan_specificCost_benefit_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_InsurancePlan_specificCost_benefit_cost(models.Model):
    InsurancePlan_specificCost_benefit = models.ForeignKey(FHIR_InsurancePlan_specificCost_benefit, related_name='InsurancePlan_specificCost_benefit_cost', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='InsurancePlan_specificCost_benefit_cost_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_applicability = 'TODO'
    applicability_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_applicability}, related_name='InsurancePlan_specificCost_benefit_cost_applicability', blank=True)
    applicability_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value = models.OneToOneField("FHIR_GP_Quantity", related_name='InsurancePlan_specificCost_benefit_cost_value', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_InsurancePlan_specificCost_benefit_cost_qualifier(models.Model):
    InsurancePlan_specificCost_benefit_cost = models.ForeignKey(FHIR_InsurancePlan_specificCost_benefit_cost, related_name='InsurancePlan_specificCost_benefit_cost_qualifier', null=False, on_delete=models.CASCADE)
    BINDING_qualifier = 'TODO'
    qualifier_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_qualifier}, related_name='InsurancePlan_specificCost_benefit_cost_qualifier', blank=True)
    qualifier_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    