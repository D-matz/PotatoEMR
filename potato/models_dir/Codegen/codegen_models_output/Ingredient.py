#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Ingredient(models.Model):
    identifier = models.OneToOneField("FHIR_GP_Identifier", related_name='Ingredient_identifier', null=True, blank=True, on_delete=models.SET_NULL)
    class StatusChoices(models.TextChoices): DRAFT = 'draft', 'Draft'; ACTIVE = 'active', 'Active'; RETIRED = 'retired', 'Retired'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    for_MedicinalProductDefinition = models.ManyToManyField("FHIR_MedicinalProductDefinition", related_name="Ingredient_for", blank=True)
    for_AdministrableProductDefinition = models.ManyToManyField("FHIR_AdministrableProductDefinition", related_name="Ingredient_for", blank=True)
    for_ManufacturedItemDefinition = models.ManyToManyField("FHIR_ManufacturedItemDefinition", related_name="Ingredient_for", blank=True)
    BINDING_role = "TODO"
    role_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_role}, related_name='Ingredient_role', blank=True)
    role_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_group = "TODO"
    group_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_group}, related_name='Ingredient_group', blank=True)
    group_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    allergenicIndicator = FHIR_primitive_BooleanField(null=True, blank=True, )
    comment = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_Ingredient_function(models.Model):
    Ingredient = models.ForeignKey(FHIR_Ingredient, related_name='Ingredient_function', null=False, on_delete=models.CASCADE)
    BINDING_function = "TODO"
    function_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_function}, related_name='Ingredient_function', blank=True)
    function_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Ingredient_manufacturer(models.Model):
    Ingredient = models.ForeignKey(FHIR_Ingredient, related_name='Ingredient_manufacturer', null=False, on_delete=models.CASCADE)
    class RoleChoices(models.TextChoices): ALLOWED = 'allowed', 'Allowed'; POSSIBLE = 'possible', 'Possible'; ACTUAL = 'actual', 'Actual'; 
    role = FHIR_primitive_CodeField(choices=RoleChoices.choices, null=True, blank=True, )
    manufacturer = models.ForeignKey("FHIR_Organization", related_name="Ingredient_manufacturer_manufacturer", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Ingredient_substance(models.Model):
    Ingredient = models.ForeignKey(FHIR_Ingredient, related_name='Ingredient_substance', null=False, on_delete=models.CASCADE)
    BINDING_code = "TODO"
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='Ingredient_substance_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    code_SubstanceDefinition_ref = models.ForeignKey("FHIR_SubstanceDefinition", related_name="Ingredient_substance_code_SubstanceDefinition", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Ingredient_substance_strength(models.Model):
    Ingredient_substance = models.ForeignKey(FHIR_Ingredient_substance, related_name='Ingredient_substance_strength', null=False, on_delete=models.CASCADE)
    presentation = models.OneToOneField("FHIR_GP_Ratio", related_name='Ingredient_substance_strength_presentation', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_presentation = "TODO"
    presentation_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_presentation}, related_name='Ingredient_substance_strength_presentation', blank=True)
    presentation_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    presentation = models.OneToOneField("FHIR_GP_Quantity", related_name='Ingredient_substance_strength_presentation', null=True, blank=True, on_delete=models.SET_NULL)
    textPresentation = FHIR_primitive_StringField(null=True, blank=True, )
    concentration = models.OneToOneField("FHIR_GP_Ratio", related_name='Ingredient_substance_strength_concentration', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_concentration = "TODO"
    concentration_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_concentration}, related_name='Ingredient_substance_strength_concentration', blank=True)
    concentration_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    concentration = models.OneToOneField("FHIR_GP_Quantity", related_name='Ingredient_substance_strength_concentration', null=True, blank=True, on_delete=models.SET_NULL)
    textConcentration = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_basis = "TODO"
    basis_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_basis}, related_name='Ingredient_substance_strength_basis', blank=True)
    basis_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    measurementPoint = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_Ingredient_substance_strength_country(models.Model):
    Ingredient_substance_strength = models.ForeignKey(FHIR_Ingredient_substance_strength, related_name='Ingredient_substance_strength_country', null=False, on_delete=models.CASCADE)
    BINDING_country = "TODO"
    country_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_country}, related_name='Ingredient_substance_strength_country', blank=True)
    country_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Ingredient_substance_strength_referenceStrength(models.Model):
    Ingredient_substance_strength = models.ForeignKey(FHIR_Ingredient_substance_strength, related_name='Ingredient_substance_strength_referenceStrength', null=False, on_delete=models.CASCADE)
    BINDING_substance = "TODO"
    substance_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_substance}, related_name='Ingredient_substance_strength_referenceStrength_substance', blank=True)
    substance_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    substance_SubstanceDefinition_ref = models.ForeignKey("FHIR_SubstanceDefinition", related_name="Ingredient_substance_strength_referenceStrength_substance_SubstanceDefinition", null=True, blank=True, on_delete=models.SET_NULL)
    strength = models.OneToOneField("FHIR_GP_Ratio", related_name='Ingredient_substance_strength_referenceStrength_strength', null=True, blank=True, on_delete=models.SET_NULL)
    strength = models.OneToOneField("FHIR_GP_Quantity", related_name='Ingredient_substance_strength_referenceStrength_strength', null=True, blank=True, on_delete=models.SET_NULL)
    measurementPoint = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_Ingredient_substance_strength_referenceStrength_country(models.Model):
    Ingredient_substance_strength_referenceStrength = models.ForeignKey(FHIR_Ingredient_substance_strength_referenceStrength, related_name='Ingredient_substance_strength_referenceStrength_country', null=False, on_delete=models.CASCADE)
    BINDING_country = "TODO"
    country_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_country}, related_name='Ingredient_substance_strength_referenceStrength_country', blank=True)
    country_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    