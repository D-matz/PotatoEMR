#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_SupplyDelivery(models.Model):
    basedOn = models.ManyToManyField("FHIR_SupplyRequest", related_name="SupplyDelivery_basedOn", blank=True)
    partOf_SupplyDelivery = models.ManyToManyField("FHIR_SupplyDelivery", related_name="SupplyDelivery_partOf", blank=True)
    partOf_Contract = models.ManyToManyField("FHIR_Contract", related_name="SupplyDelivery_partOf", blank=True)
    class StatusChoices(models.TextChoices): IN_PROGRESS = 'in-progress', 'In-progress'; COMPLETED = 'completed', 'Completed'; ABANDONED = 'abandoned', 'Abandoned'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    patient = models.ForeignKey("FHIR_Patient", related_name="SupplyDelivery_patient", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='SupplyDelivery_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_stage = "TODO"
    stage_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_stage}, related_name='SupplyDelivery_stage', blank=True)
    stage_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    occurrence_dateTime = FHIR_primitive_DateTimeField(null=True, blank=True, )
    occurrence_Period = models.OneToOneField("FHIR_GP_Period", related_name='SupplyDelivery_occurrence_Period', null=True, blank=True, on_delete=models.SET_NULL)
    occurrence_Timing = models.OneToOneField("FHIR_GP_Timing", related_name='SupplyDelivery_occurrence_Timing', null=True, blank=True, on_delete=models.SET_NULL)
    supplier_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="SupplyDelivery_supplier", null=True, blank=True, on_delete=models.SET_NULL)
    supplier_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="SupplyDelivery_supplier", null=True, blank=True, on_delete=models.SET_NULL)
    supplier_Organization = models.ForeignKey("FHIR_Organization", related_name="SupplyDelivery_supplier", null=True, blank=True, on_delete=models.SET_NULL)
    destination_Location = models.ForeignKey("FHIR_Location", related_name="SupplyDelivery_destination", null=True, blank=True, on_delete=models.SET_NULL)
    destination_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="SupplyDelivery_destination", null=True, blank=True, on_delete=models.SET_NULL)
    destination_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="SupplyDelivery_destination", null=True, blank=True, on_delete=models.SET_NULL)
    destination_Organization = models.ForeignKey("FHIR_Organization", related_name="SupplyDelivery_destination", null=True, blank=True, on_delete=models.SET_NULL)
    receiver_Practitioner = models.ManyToManyField("FHIR_Practitioner", related_name="SupplyDelivery_receiver", blank=True)
    receiver_PractitionerRole = models.ManyToManyField("FHIR_PractitionerRole", related_name="SupplyDelivery_receiver", blank=True)
    receiver_Organization = models.ManyToManyField("FHIR_Organization", related_name="SupplyDelivery_receiver", blank=True)

class FHIR_SupplyDelivery_identifier(FHIR_GP_Identifier):
    SupplyDelivery = models.ForeignKey(FHIR_SupplyDelivery, related_name='SupplyDelivery_identifier', null=False, on_delete=models.CASCADE)

class FHIR_SupplyDelivery_suppliedItem(models.Model):
    SupplyDelivery = models.ForeignKey(FHIR_SupplyDelivery, related_name='SupplyDelivery_suppliedItem', null=False, on_delete=models.CASCADE)
    quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='SupplyDelivery_suppliedItem_quantity', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_condition = "TODO"
    condition_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_condition}, related_name='SupplyDelivery_suppliedItem_condition', blank=True)
    condition_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_item_CodeableConcept = "TODO"
    item_CodeableConcept_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_item_CodeableConcept}, related_name='SupplyDelivery_suppliedItem_item_CodeableConcept', blank=True)
    item_CodeableConcept_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    item_Reference_Medication = models.ForeignKey("FHIR_Medication", related_name="SupplyDelivery_suppliedItem_item_Reference", null=True, blank=True, on_delete=models.SET_NULL)
    item_Reference_Substance = models.ForeignKey("FHIR_Substance", related_name="SupplyDelivery_suppliedItem_item_Reference", null=True, blank=True, on_delete=models.SET_NULL)
    item_Reference_Device = models.ForeignKey("FHIR_Device", related_name="SupplyDelivery_suppliedItem_item_Reference", null=True, blank=True, on_delete=models.SET_NULL)
    item_Reference_BiologicallyDerivedProduct = models.ForeignKey("FHIR_BiologicallyDerivedProduct", related_name="SupplyDelivery_suppliedItem_item_Reference", null=True, blank=True, on_delete=models.SET_NULL)
    item_Reference_NutritionProduct = models.ForeignKey("FHIR_NutritionProduct", related_name="SupplyDelivery_suppliedItem_item_Reference", null=True, blank=True, on_delete=models.SET_NULL)
    item_Reference_InventoryItem = models.ForeignKey("FHIR_InventoryItem", related_name="SupplyDelivery_suppliedItem_item_Reference", null=True, blank=True, on_delete=models.SET_NULL)
