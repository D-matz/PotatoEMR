
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_ManufacturedItemDefinition(models.Model):
    class StatusChoices(models.TextChoices): DRAFT = 'draft', 'Draft'; ACTIVE = 'active', 'Active'; RETIRED = 'retired', 'Retired'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    name = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_manufacturedDoseForm = 'TODO'
    manufacturedDoseForm_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_manufacturedDoseForm}, related_name='ManufacturedItemDefinition_manufacturedDoseForm', blank=True)
    manufacturedDoseForm_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_unitOfPresentation = 'TODO'
    unitOfPresentation_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_unitOfPresentation}, related_name='ManufacturedItemDefinition_unitOfPresentation', blank=True)
    unitOfPresentation_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    manufacturer = models.ManyToManyField("FHIR_Organization", related_name="ManufacturedItemDefinition_manufacturer", blank=True)

class FHIR_ManufacturedItemDefinition_identifier(FHIR_GP_Identifier):
    ManufacturedItemDefinition = models.ForeignKey(FHIR_ManufacturedItemDefinition, related_name='ManufacturedItemDefinition_identifier', null=False, on_delete=models.CASCADE)

class FHIR_ManufacturedItemDefinition_ingredient(models.Model):
    ManufacturedItemDefinition = models.ForeignKey(FHIR_ManufacturedItemDefinition, related_name='ManufacturedItemDefinition_ingredient', null=False, on_delete=models.CASCADE)
    BINDING_ingredient = 'TODO'
    ingredient_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_ingredient}, related_name='ManufacturedItemDefinition_ingredient', blank=True)
    ingredient_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ManufacturedItemDefinition_property(models.Model):
    ManufacturedItemDefinition = models.ForeignKey(FHIR_ManufacturedItemDefinition, related_name='ManufacturedItemDefinition_property', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='ManufacturedItemDefinition_property_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_value = 'TODO'
    value_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_value}, related_name='ManufacturedItemDefinition_property_value', blank=True)
    value_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value = models.OneToOneField("FHIR_GP_Quantity", related_name='ManufacturedItemDefinition_property_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = FHIR_primitive_DateField(null=True, blank=True, )
    value = FHIR_primitive_BooleanField(null=True, blank=True, )
    value = FHIR_primitive_MarkdownField(null=True, blank=True, )
    value = models.OneToOneField("FHIR_GP_Attachment", related_name='ManufacturedItemDefinition_property_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.ForeignKey("FHIR_Binary", related_name="ManufacturedItemDefinition_property_value", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ManufacturedItemDefinition_component(models.Model):
    ManufacturedItemDefinition = models.ForeignKey(FHIR_ManufacturedItemDefinition, related_name='ManufacturedItemDefinition_component', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='ManufacturedItemDefinition_component_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_ManufacturedItemDefinition_component_function(models.Model):
    ManufacturedItemDefinition_component = models.ForeignKey(FHIR_ManufacturedItemDefinition_component, related_name='ManufacturedItemDefinition_component_function', null=False, on_delete=models.CASCADE)
    BINDING_function = 'TODO'
    function_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_function}, related_name='ManufacturedItemDefinition_component_function', blank=True)
    function_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ManufacturedItemDefinition_component_amount(FHIR_GP_Quantity):
    ManufacturedItemDefinition_component = models.ForeignKey(FHIR_ManufacturedItemDefinition_component, related_name='ManufacturedItemDefinition_component_amount', null=False, on_delete=models.CASCADE)

class FHIR_ManufacturedItemDefinition_component_constituent(models.Model):
    ManufacturedItemDefinition_component = models.ForeignKey(FHIR_ManufacturedItemDefinition_component, related_name='ManufacturedItemDefinition_component_constituent', null=False, on_delete=models.CASCADE)

class FHIR_ManufacturedItemDefinition_component_constituent_amount(FHIR_GP_Quantity):
    ManufacturedItemDefinition_component_constituent = models.ForeignKey(FHIR_ManufacturedItemDefinition_component_constituent, related_name='ManufacturedItemDefinition_component_constituent_amount', null=False, on_delete=models.CASCADE)

class FHIR_ManufacturedItemDefinition_component_constituent_location(models.Model):
    ManufacturedItemDefinition_component_constituent = models.ForeignKey(FHIR_ManufacturedItemDefinition_component_constituent, related_name='ManufacturedItemDefinition_component_constituent_location', null=False, on_delete=models.CASCADE)
    BINDING_location = 'TODO'
    location_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_location}, related_name='ManufacturedItemDefinition_component_constituent_location', blank=True)
    location_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ManufacturedItemDefinition_component_constituent_function(models.Model):
    ManufacturedItemDefinition_component_constituent = models.ForeignKey(FHIR_ManufacturedItemDefinition_component_constituent, related_name='ManufacturedItemDefinition_component_constituent_function', null=False, on_delete=models.CASCADE)
    BINDING_function = 'TODO'
    function_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_function}, related_name='ManufacturedItemDefinition_component_constituent_function', blank=True)
    function_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ManufacturedItemDefinition_component_constituent_hasIngredient(models.Model):
    ManufacturedItemDefinition_component_constituent = models.ForeignKey(FHIR_ManufacturedItemDefinition_component_constituent, related_name='ManufacturedItemDefinition_component_constituent_hasIngredient', null=False, on_delete=models.CASCADE)
    BINDING_hasIngredient = 'TODO'
    hasIngredient_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_hasIngredient}, related_name='ManufacturedItemDefinition_component_constituent_hasIngredient', blank=True)
    hasIngredient_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    hasIngredient_Ingredient_ref = models.ForeignKey("FHIR_Ingredient", related_name="ManufacturedItemDefinition_component_constituent_hasIngredient", null=True, blank=True, on_delete=models.SET_NULL)
