
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_InventoryItem(models.Model):
    class StatusChoices(models.TextChoices): ACTIVE = 'active', 'Active'; INACTIVE = 'inactive', 'Inactive'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    BINDING_baseUnit = 'TODO'
    baseUnit_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_baseUnit}, related_name='InventoryItem_baseUnit', blank=True)
    baseUnit_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    netContent = models.OneToOneField("FHIR_GP_Quantity", related_name='InventoryItem_netContent', null=True, blank=True, on_delete=models.SET_NULL)
    productReference_Medication = models.ForeignKey("FHIR_Medication", related_name="InventoryItem_productReference", null=True, blank=True, on_delete=models.SET_NULL)
    productReference_Device = models.ForeignKey("FHIR_Device", related_name="InventoryItem_productReference", null=True, blank=True, on_delete=models.SET_NULL)
    productReference_NutritionProduct = models.ForeignKey("FHIR_NutritionProduct", related_name="InventoryItem_productReference", null=True, blank=True, on_delete=models.SET_NULL)
    productReference_BiologicallyDerivedProduct = models.ForeignKey("FHIR_BiologicallyDerivedProduct", related_name="InventoryItem_productReference", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_InventoryItem_identifier(FHIR_GP_Identifier):
    InventoryItem = models.ForeignKey(FHIR_InventoryItem, related_name='InventoryItem_identifier', null=False, on_delete=models.CASCADE)

class FHIR_InventoryItem_category(models.Model):
    InventoryItem = models.ForeignKey(FHIR_InventoryItem, related_name='InventoryItem_category', null=False, on_delete=models.CASCADE)
    BINDING_category = 'TODO'
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='InventoryItem_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_InventoryItem_code(models.Model):
    InventoryItem = models.ForeignKey(FHIR_InventoryItem, related_name='InventoryItem_code', null=False, on_delete=models.CASCADE)
    BINDING_code = 'TODO'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='InventoryItem_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_InventoryItem_name(models.Model):
    InventoryItem = models.ForeignKey(FHIR_InventoryItem, related_name='InventoryItem_name', null=False, on_delete=models.CASCADE)
    nameType = models.OneToOneField("FHIR_GP_Coding", related_name='InventoryItem_name_nameType', null=True, blank=True, on_delete=models.SET_NULL)
    class LanguageChoices(models.TextChoices): THE_LANGUAGE_USED_TO_EXPRESS_THE_ITEM_NAME = 'The language used to express the item name', 'The language used to express the item name'; 
    language = FHIR_primitive_CodeField(choices=LanguageChoices.choices, null=True, blank=True, )
    name = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_InventoryItem_responsibleOrganization(models.Model):
    InventoryItem = models.ForeignKey(FHIR_InventoryItem, related_name='InventoryItem_responsibleOrganization', null=False, on_delete=models.CASCADE)
    BINDING_role = 'TODO'
    role_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_role}, related_name='InventoryItem_responsibleOrganization_role', blank=True)
    role_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    organization = models.ForeignKey("FHIR_Organization", related_name="InventoryItem_responsibleOrganization_organization", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_InventoryItem_description(models.Model):
    InventoryItem = models.ForeignKey(FHIR_InventoryItem, related_name='InventoryItem_description', null=False, on_delete=models.CASCADE)
    class LanguageChoices(models.TextChoices): THE_LANGUAGE_THAT_IS_USED_IN_THE_ITEM_DESCRIPTION = 'The language that is used in the item description', 'The language that is used in the item description'; 
    language = FHIR_primitive_CodeField(choices=LanguageChoices.choices, null=True, blank=True, )
    description = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_InventoryItem_inventoryStatus(models.Model):
    InventoryItem = models.ForeignKey(FHIR_InventoryItem, related_name='InventoryItem_inventoryStatus', null=False, on_delete=models.CASCADE)
    BINDING_inventoryStatus = 'TODO'
    inventoryStatus_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_inventoryStatus}, related_name='InventoryItem_inventoryStatus', blank=True)
    inventoryStatus_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_InventoryItem_association(models.Model):
    InventoryItem = models.ForeignKey(FHIR_InventoryItem, related_name='InventoryItem_association', null=False, on_delete=models.CASCADE)
    BINDING_associationType = 'TODO'
    associationType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_associationType}, related_name='InventoryItem_association_associationType', blank=True)
    associationType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    relatedItem_InventoryItem = models.ForeignKey("FHIR_InventoryItem", related_name="InventoryItem_association_relatedItem", null=True, blank=True, on_delete=models.SET_NULL)
    relatedItem_Medication = models.ForeignKey("FHIR_Medication", related_name="InventoryItem_association_relatedItem", null=True, blank=True, on_delete=models.SET_NULL)
    relatedItem_MedicationKnowledge = models.ForeignKey("FHIR_MedicationKnowledge", related_name="InventoryItem_association_relatedItem", null=True, blank=True, on_delete=models.SET_NULL)
    relatedItem_Device = models.ForeignKey("FHIR_Device", related_name="InventoryItem_association_relatedItem", null=True, blank=True, on_delete=models.SET_NULL)
    relatedItem_DeviceDefinition = models.ForeignKey("FHIR_DeviceDefinition", related_name="InventoryItem_association_relatedItem", null=True, blank=True, on_delete=models.SET_NULL)
    relatedItem_NutritionProduct = models.ForeignKey("FHIR_NutritionProduct", related_name="InventoryItem_association_relatedItem", null=True, blank=True, on_delete=models.SET_NULL)
    relatedItem_BiologicallyDerivedProduct = models.ForeignKey("FHIR_BiologicallyDerivedProduct", related_name="InventoryItem_association_relatedItem", null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.OneToOneField("FHIR_GP_Ratio", related_name='InventoryItem_association_quantity', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_InventoryItem_characteristic(models.Model):
    InventoryItem = models.ForeignKey(FHIR_InventoryItem, related_name='InventoryItem_characteristic', null=False, on_delete=models.CASCADE)
    BINDING_characteristicType = 'TODO'
    characteristicType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_characteristicType}, related_name='InventoryItem_characteristic_characteristicType', blank=True)
    characteristicType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value = FHIR_primitive_StringField(null=True, blank=True, )
    value = FHIR_primitive_DecimalField(null=True, blank=True, )
    value = FHIR_primitive_BooleanField(null=True, blank=True, )
    value = FHIR_primitive_URLField(null=True, blank=True, )
    value = FHIR_primitive_DateTimeField(null=True, blank=True, )
    value = models.OneToOneField("FHIR_GP_Quantity", related_name='InventoryItem_characteristic_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_Range", related_name='InventoryItem_characteristic_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_Ratio", related_name='InventoryItem_characteristic_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_Annotation", related_name='InventoryItem_characteristic_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_Address", related_name='InventoryItem_characteristic_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_Quantity_Duration", related_name='InventoryItem_characteristic_value', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_value = 'TODO'
    value_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_value}, related_name='InventoryItem_characteristic_value', blank=True)
    value_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_InventoryItem_instance(models.Model):
    InventoryItem = models.ForeignKey(FHIR_InventoryItem, related_name='InventoryItem_instance', null=False, on_delete=models.CASCADE)
    lotNumber = FHIR_primitive_StringField(null=True, blank=True, )
    expiry = FHIR_primitive_DateTimeField(null=True, blank=True, )
    subject_Patient = models.ForeignKey("FHIR_Patient", related_name="InventoryItem_instance_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Organization = models.ForeignKey("FHIR_Organization", related_name="InventoryItem_instance_subject", null=True, blank=True, on_delete=models.SET_NULL)
    location = models.ForeignKey("FHIR_Location", related_name="InventoryItem_instance_location", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_InventoryItem_instance_identifier(FHIR_GP_Identifier):
    InventoryItem_instance = models.ForeignKey(FHIR_InventoryItem_instance, related_name='InventoryItem_instance_identifier', null=False, on_delete=models.CASCADE)
