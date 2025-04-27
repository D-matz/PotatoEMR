#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_InventoryReport(models.Model):
    class StatusChoices(models.TextChoices): DRAFT = 'draft', 'Draft'; REQUESTED = 'requested', 'Requested'; ACTIVE = 'active', 'Active'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    class CounttypeChoices(models.TextChoices): SNAPSHOT = 'snapshot', 'Snapshot'; DIFFERENCE = 'difference', 'Difference'; 
    countType = FHIR_primitive_CodeField(choices=CounttypeChoices.choices, null=True, blank=True, )
    BINDING_operationType = 'TODO'
    operationType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_operationType}, related_name='InventoryReport_operationType', blank=True)
    operationType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_operationTypeReason = 'TODO'
    operationTypeReason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_operationTypeReason}, related_name='InventoryReport_operationTypeReason', blank=True)
    operationTypeReason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    reportedDateTime = FHIR_primitive_DateTimeField(null=True, blank=True, )
    reporter_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="InventoryReport_reporter", null=True, blank=True, on_delete=models.SET_NULL)
    reporter_Patient = models.ForeignKey("FHIR_Patient", related_name="InventoryReport_reporter", null=True, blank=True, on_delete=models.SET_NULL)
    reporter_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="InventoryReport_reporter", null=True, blank=True, on_delete=models.SET_NULL)
    reporter_Device = models.ForeignKey("FHIR_Device", related_name="InventoryReport_reporter", null=True, blank=True, on_delete=models.SET_NULL)
    reportingPeriod = models.OneToOneField("FHIR_GP_Period", related_name='InventoryReport_reportingPeriod', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_InventoryReport_identifier(FHIR_GP_Identifier):
    InventoryReport = models.ForeignKey(FHIR_InventoryReport, related_name='InventoryReport_identifier', null=False, on_delete=models.CASCADE)

class FHIR_InventoryReport_inventoryListing(models.Model):
    InventoryReport = models.ForeignKey(FHIR_InventoryReport, related_name='InventoryReport_inventoryListing', null=False, on_delete=models.CASCADE)
    location = models.ForeignKey("FHIR_Location", related_name="InventoryReport_inventoryListing_location", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_itemStatus = 'TODO'
    itemStatus_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_itemStatus}, related_name='InventoryReport_inventoryListing_itemStatus', blank=True)
    itemStatus_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    countingDateTime = FHIR_primitive_DateTimeField(null=True, blank=True, )

class FHIR_InventoryReport_inventoryListing_item(models.Model):
    InventoryReport_inventoryListing = models.ForeignKey(FHIR_InventoryReport_inventoryListing, related_name='InventoryReport_inventoryListing_item', null=False, on_delete=models.CASCADE)
    BINDING_category = 'TODO'
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='InventoryReport_inventoryListing_item_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='InventoryReport_inventoryListing_item_quantity', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_item = 'TODO'
    item_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_item}, related_name='InventoryReport_inventoryListing_item_item', blank=True)
    item_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    item_Medication_ref = models.ForeignKey("FHIR_Medication", related_name="InventoryReport_inventoryListing_item_item_Medication", null=True, blank=True, on_delete=models.SET_NULL)
    item_Device_ref = models.ForeignKey("FHIR_Device", related_name="InventoryReport_inventoryListing_item_item_Device", null=True, blank=True, on_delete=models.SET_NULL)
    item_NutritionProduct_ref = models.ForeignKey("FHIR_NutritionProduct", related_name="InventoryReport_inventoryListing_item_item_NutritionProduct", null=True, blank=True, on_delete=models.SET_NULL)
    item_InventoryItem_ref = models.ForeignKey("FHIR_InventoryItem", related_name="InventoryReport_inventoryListing_item_item_InventoryItem", null=True, blank=True, on_delete=models.SET_NULL)
    item_BiologicallyDerivedProduct_ref = models.ForeignKey("FHIR_BiologicallyDerivedProduct", related_name="InventoryReport_inventoryListing_item_item_BiologicallyDerivedProduct", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_InventoryReport_note(FHIR_GP_Annotation):
    InventoryReport = models.ForeignKey(FHIR_InventoryReport, related_name='InventoryReport_note', null=False, on_delete=models.CASCADE)
