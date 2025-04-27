#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_NutritionProduct(models.Model):
    BINDING_code = 'TODO'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='NutritionProduct_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    class StatusChoices(models.TextChoices): ACTIVE = 'active', 'Active'; INACTIVE = 'inactive', 'Inactive'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    manufacturer_Organization = models.ManyToManyField("FHIR_Organization", related_name="NutritionProduct_manufacturer", blank=True)
    manufacturer_RelatedPerson = models.ManyToManyField("FHIR_RelatedPerson", related_name="NutritionProduct_manufacturer", blank=True)
    ingredientSummary = FHIR_primitive_MarkdownField(null=True, blank=True, )
    energy = models.OneToOneField("FHIR_GP_Quantity", related_name='NutritionProduct_energy', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_NutritionProduct_category(models.Model):
    NutritionProduct = models.ForeignKey(FHIR_NutritionProduct, related_name='NutritionProduct_category', null=False, on_delete=models.CASCADE)
    BINDING_category = 'TODO'
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='NutritionProduct_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_NutritionProduct_nutrient(models.Model):
    NutritionProduct = models.ForeignKey(FHIR_NutritionProduct, related_name='NutritionProduct_nutrient', null=False, on_delete=models.CASCADE)
    BINDING_item = 'TODO'
    item_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_item}, related_name='NutritionProduct_nutrient_item', blank=True)
    item_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    item_SubstanceDefinition_ref = models.ForeignKey("FHIR_SubstanceDefinition", related_name="NutritionProduct_nutrient_item_SubstanceDefinition", null=True, blank=True, on_delete=models.SET_NULL)
    amount = models.OneToOneField("FHIR_GP_Ratio", related_name='NutritionProduct_nutrient_amount', null=True, blank=True, on_delete=models.SET_NULL)
    amount = models.OneToOneField("FHIR_GP_Quantity", related_name='NutritionProduct_nutrient_amount', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_NutritionProduct_ingredient(models.Model):
    NutritionProduct = models.ForeignKey(FHIR_NutritionProduct, related_name='NutritionProduct_ingredient', null=False, on_delete=models.CASCADE)
    BINDING_item = 'TODO'
    item_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_item}, related_name='NutritionProduct_ingredient_item', blank=True)
    item_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    item_NutritionProduct_ref = models.ForeignKey("FHIR_NutritionProduct", related_name="NutritionProduct_ingredient_item_NutritionProduct", null=True, blank=True, on_delete=models.SET_NULL)
    amount = models.OneToOneField("FHIR_GP_Ratio", related_name='NutritionProduct_ingredient_amount', null=True, blank=True, on_delete=models.SET_NULL)
    amount = models.OneToOneField("FHIR_GP_Quantity", related_name='NutritionProduct_ingredient_amount', null=True, blank=True, on_delete=models.SET_NULL)
    allergen = FHIR_primitive_BooleanField(null=True, blank=True, )

class FHIR_NutritionProduct_characteristic(models.Model):
    NutritionProduct = models.ForeignKey(FHIR_NutritionProduct, related_name='NutritionProduct_characteristic', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='NutritionProduct_characteristic_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_value = 'TODO'
    value_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_value}, related_name='NutritionProduct_characteristic_value', blank=True)
    value_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value = FHIR_primitive_StringField(null=True, blank=True, )
    value = models.OneToOneField("FHIR_GP_Quantity", related_name='NutritionProduct_characteristic_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = FHIR_primitive_Base64BinaryField(null=True, blank=True, )
    value = models.OneToOneField("FHIR_GP_Attachment", related_name='NutritionProduct_characteristic_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = FHIR_primitive_BooleanField(null=True, blank=True, )

class FHIR_NutritionProduct_instance(models.Model):
    NutritionProduct = models.ForeignKey(FHIR_NutritionProduct, related_name='NutritionProduct_instance', null=False, on_delete=models.CASCADE)
    quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='NutritionProduct_instance_quantity', null=True, blank=True, on_delete=models.SET_NULL)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    lotNumber = FHIR_primitive_StringField(null=True, blank=True, )
    expiry = FHIR_primitive_DateTimeField(null=True, blank=True, )
    useBy = FHIR_primitive_DateTimeField(null=True, blank=True, )
    biologicalSourceEvent = models.OneToOneField("FHIR_GP_Identifier", related_name='NutritionProduct_instance_biologicalSourceEvent', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_NutritionProduct_instance_identifier(FHIR_GP_Identifier):
    NutritionProduct_instance = models.ForeignKey(FHIR_NutritionProduct_instance, related_name='NutritionProduct_instance_identifier', null=False, on_delete=models.CASCADE)

class FHIR_NutritionProduct_note(FHIR_GP_Annotation):
    NutritionProduct = models.ForeignKey(FHIR_NutritionProduct, related_name='NutritionProduct_note', null=False, on_delete=models.CASCADE)
