#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_PackagedProductDefinition(models.Model):
    name = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='PackagedProductDefinition_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    packageFor = models.ManyToManyField("FHIR_MedicinalProductDefinition", related_name="PackagedProductDefinition_packageFor", blank=True)
    BINDING_status = "TODO"
    status_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_status}, related_name='PackagedProductDefinition_status', blank=True)
    status_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    statusDate = FHIR_primitive_DateTimeField(null=True, blank=True, )
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    copackagedIndicator = FHIR_primitive_BooleanField(null=True, blank=True, )
    manufacturer = models.ManyToManyField("FHIR_Organization", related_name="PackagedProductDefinition_manufacturer", blank=True)
    attachedDocument = models.ManyToManyField("FHIR_DocumentReference", related_name="PackagedProductDefinition_attachedDocument", blank=True)

class FHIR_PackagedProductDefinition_identifier(FHIR_GP_Identifier):
    PackagedProductDefinition = models.ForeignKey(FHIR_PackagedProductDefinition, related_name='PackagedProductDefinition_identifier', null=False, on_delete=models.CASCADE)

class FHIR_PackagedProductDefinition_containedItemQuantity(FHIR_GP_Quantity):
    PackagedProductDefinition = models.ForeignKey(FHIR_PackagedProductDefinition, related_name='PackagedProductDefinition_containedItemQuantity', null=False, on_delete=models.CASCADE)

class FHIR_PackagedProductDefinition_legalStatusOfSupply(models.Model):
    PackagedProductDefinition = models.ForeignKey(FHIR_PackagedProductDefinition, related_name='PackagedProductDefinition_legalStatusOfSupply', null=False, on_delete=models.CASCADE)
    BINDING_code = "TODO"
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='PackagedProductDefinition_legalStatusOfSupply_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_jurisdiction = "TODO"
    jurisdiction_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_jurisdiction}, related_name='PackagedProductDefinition_legalStatusOfSupply_jurisdiction', blank=True)
    jurisdiction_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_PackagedProductDefinition_packaging(models.Model):
    PackagedProductDefinition = models.ForeignKey(FHIR_PackagedProductDefinition, related_name='PackagedProductDefinition_packaging', null=False, on_delete=models.CASCADE)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='PackagedProductDefinition_packaging_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    componentPart = FHIR_primitive_BooleanField(null=True, blank=True, )
    manufacturer = models.ManyToManyField("FHIR_Organization", related_name="PackagedProductDefinition_packaging_manufacturer", blank=True)

class FHIR_PackagedProductDefinition_packaging_identifier(FHIR_GP_Identifier):
    PackagedProductDefinition_packaging = models.ForeignKey(FHIR_PackagedProductDefinition_packaging, related_name='PackagedProductDefinition_packaging_identifier', null=False, on_delete=models.CASCADE)

class FHIR_PackagedProductDefinition_packaging_material(models.Model):
    PackagedProductDefinition_packaging = models.ForeignKey(FHIR_PackagedProductDefinition_packaging, related_name='PackagedProductDefinition_packaging_material', null=False, on_delete=models.CASCADE)
    BINDING_material = "TODO"
    material_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_material}, related_name='PackagedProductDefinition_packaging_material', blank=True)
    material_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_PackagedProductDefinition_packaging_alternateMaterial(models.Model):
    PackagedProductDefinition_packaging = models.ForeignKey(FHIR_PackagedProductDefinition_packaging, related_name='PackagedProductDefinition_packaging_alternateMaterial', null=False, on_delete=models.CASCADE)
    BINDING_alternateMaterial = "TODO"
    alternateMaterial_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_alternateMaterial}, related_name='PackagedProductDefinition_packaging_alternateMaterial', blank=True)
    alternateMaterial_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_PackagedProductDefinition_packaging_property(models.Model):
    PackagedProductDefinition_packaging = models.ForeignKey(FHIR_PackagedProductDefinition_packaging, related_name='PackagedProductDefinition_packaging_property', null=False, on_delete=models.CASCADE)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='PackagedProductDefinition_packaging_property_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_value = "TODO"
    value_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_value}, related_name='PackagedProductDefinition_packaging_property_value', blank=True)
    value_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value = models.OneToOneField("FHIR_GP_Quantity", related_name='PackagedProductDefinition_packaging_property_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = FHIR_primitive_DateField(null=True, blank=True, )
    value = FHIR_primitive_BooleanField(null=True, blank=True, )
    value = models.OneToOneField("FHIR_GP_Attachment", related_name='PackagedProductDefinition_packaging_property_value', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_PackagedProductDefinition_packaging_containedItem(models.Model):
    PackagedProductDefinition_packaging = models.ForeignKey(FHIR_PackagedProductDefinition_packaging, related_name='PackagedProductDefinition_packaging_containedItem', null=False, on_delete=models.CASCADE)
    BINDING_item = "TODO"
    item_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_item}, related_name='PackagedProductDefinition_packaging_containedItem_item', blank=True)
    item_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    item_ManufacturedItemDefinition_ref = models.ForeignKey("FHIR_ManufacturedItemDefinition", related_name="PackagedProductDefinition_packaging_containedItem_item_ManufacturedItemDefinition", null=True, blank=True, on_delete=models.SET_NULL)
    item_DeviceDefinition_ref = models.ForeignKey("FHIR_DeviceDefinition", related_name="PackagedProductDefinition_packaging_containedItem_item_DeviceDefinition", null=True, blank=True, on_delete=models.SET_NULL)
    item_PackagedProductDefinition_ref = models.ForeignKey("FHIR_PackagedProductDefinition", related_name="PackagedProductDefinition_packaging_containedItem_item_PackagedProductDefinition", null=True, blank=True, on_delete=models.SET_NULL)
    item_BiologicallyDerivedProduct_ref = models.ForeignKey("FHIR_BiologicallyDerivedProduct", related_name="PackagedProductDefinition_packaging_containedItem_item_BiologicallyDerivedProduct", null=True, blank=True, on_delete=models.SET_NULL)
    item_NutritionProduct_ref = models.ForeignKey("FHIR_NutritionProduct", related_name="PackagedProductDefinition_packaging_containedItem_item_NutritionProduct", null=True, blank=True, on_delete=models.SET_NULL)
    amount = models.OneToOneField("FHIR_GP_Quantity", related_name='PackagedProductDefinition_packaging_containedItem_amount', null=True, blank=True, on_delete=models.SET_NULL)
