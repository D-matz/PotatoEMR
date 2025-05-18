#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_SupplyRequest(models.Model):
    class StatusChoices(models.TextChoices): DRAFT = 'draft', 'Draft'; ACTIVE = 'active', 'Active'; SUSPENDED_PLUS = 'suspended +', 'Suspended +'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    class IntentChoices(models.TextChoices): PROPOSAL = 'proposal', 'Proposal'; PLAN = 'plan', 'Plan'; DIRECTIVE = 'directive', 'Directive'; ORDER = 'order', 'Order'; ORIGINAL_ORDER = 'original-order', 'Original-order'; REFLEX_ORDER = 'reflex-order', 'Reflex-order'; FILLER_ORDER = 'filler-order', 'Filler-order'; INSTANCE_ORDER = 'instance-order', 'Instance-order'; OPTION = 'option', 'Option'; 
    intent = FHIR_primitive_CodeField(choices=IntentChoices.choices, null=True, blank=True, )
                            #skipping Reference(Any) for field basedOn as SupplyRequest basedOn not in referenceAny_targets
    BINDING_category = "TODO"
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='SupplyRequest_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    class PriorityChoices(models.TextChoices): ROUTINE = 'routine', 'Routine'; URGENT = 'urgent', 'Urgent'; ASAP = 'asap', 'Asap'; STAT = 'stat', 'Stat'; 
    priority = FHIR_primitive_CodeField(choices=PriorityChoices.choices, null=True, blank=True, )
    deliverFor = models.ForeignKey("FHIR_Patient", related_name="SupplyRequest_deliverFor", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_item = "TODO"
    item_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_item}, related_name='SupplyRequest_item', blank=True)
    item_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    item_Medication_ref = models.ForeignKey("FHIR_Medication", related_name="SupplyRequest_item_Medication", null=True, blank=True, on_delete=models.SET_NULL)
    item_Substance_ref = models.ForeignKey("FHIR_Substance", related_name="SupplyRequest_item_Substance", null=True, blank=True, on_delete=models.SET_NULL)
    item_Device_ref = models.ForeignKey("FHIR_Device", related_name="SupplyRequest_item_Device", null=True, blank=True, on_delete=models.SET_NULL)
    item_DeviceDefinition_ref = models.ForeignKey("FHIR_DeviceDefinition", related_name="SupplyRequest_item_DeviceDefinition", null=True, blank=True, on_delete=models.SET_NULL)
    item_BiologicallyDerivedProduct_ref = models.ForeignKey("FHIR_BiologicallyDerivedProduct", related_name="SupplyRequest_item_BiologicallyDerivedProduct", null=True, blank=True, on_delete=models.SET_NULL)
    item_NutritionProduct_ref = models.ForeignKey("FHIR_NutritionProduct", related_name="SupplyRequest_item_NutritionProduct", null=True, blank=True, on_delete=models.SET_NULL)
    item_InventoryItem_ref = models.ForeignKey("FHIR_InventoryItem", related_name="SupplyRequest_item_InventoryItem", null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='SupplyRequest_quantity', null=True, blank=True, on_delete=models.SET_NULL)
    occurrence_dateTime = FHIR_primitive_DateTimeField(null=True, blank=True, )
    occurrence_Period = models.OneToOneField("FHIR_GP_Period", related_name='SupplyRequest_occurrence_Period', null=True, blank=True, on_delete=models.SET_NULL)
    occurrence_Timing = models.OneToOneField("FHIR_GP_Timing", related_name='SupplyRequest_occurrence_Timing', null=True, blank=True, on_delete=models.SET_NULL)
    authoredOn = FHIR_primitive_DateTimeField(null=True, blank=True, )
    requester_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="SupplyRequest_requester", null=True, blank=True, on_delete=models.SET_NULL)
    requester_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="SupplyRequest_requester", null=True, blank=True, on_delete=models.SET_NULL)
    requester_Organization = models.ForeignKey("FHIR_Organization", related_name="SupplyRequest_requester", null=True, blank=True, on_delete=models.SET_NULL)
    requester_Patient = models.ForeignKey("FHIR_Patient", related_name="SupplyRequest_requester", null=True, blank=True, on_delete=models.SET_NULL)
    requester_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="SupplyRequest_requester", null=True, blank=True, on_delete=models.SET_NULL)
    requester_Device = models.ForeignKey("FHIR_Device", related_name="SupplyRequest_requester", null=True, blank=True, on_delete=models.SET_NULL)
    requester_CareTeam = models.ForeignKey("FHIR_CareTeam", related_name="SupplyRequest_requester", null=True, blank=True, on_delete=models.SET_NULL)
    supplier_Organization = models.ManyToManyField("FHIR_Organization", related_name="SupplyRequest_supplier", blank=True)
    supplier_HealthcareService = models.ManyToManyField("FHIR_HealthcareService", related_name="SupplyRequest_supplier", blank=True)
    deliverFrom_Organization = models.ForeignKey("FHIR_Organization", related_name="SupplyRequest_deliverFrom", null=True, blank=True, on_delete=models.SET_NULL)
    deliverFrom_Location = models.ForeignKey("FHIR_Location", related_name="SupplyRequest_deliverFrom", null=True, blank=True, on_delete=models.SET_NULL)
    deliverTo_Organization = models.ForeignKey("FHIR_Organization", related_name="SupplyRequest_deliverTo", null=True, blank=True, on_delete=models.SET_NULL)
    deliverTo_Location = models.ForeignKey("FHIR_Location", related_name="SupplyRequest_deliverTo", null=True, blank=True, on_delete=models.SET_NULL)
    deliverTo_Patient = models.ForeignKey("FHIR_Patient", related_name="SupplyRequest_deliverTo", null=True, blank=True, on_delete=models.SET_NULL)
    deliverTo_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="SupplyRequest_deliverTo", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_SupplyRequest_identifier(FHIR_GP_Identifier):
    SupplyRequest = models.ForeignKey(FHIR_SupplyRequest, related_name='SupplyRequest_identifier', null=False, on_delete=models.CASCADE)

class FHIR_SupplyRequest_parameter(models.Model):
    SupplyRequest = models.ForeignKey(FHIR_SupplyRequest, related_name='SupplyRequest_parameter', null=False, on_delete=models.CASCADE)
    BINDING_code = "TODO"
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='SupplyRequest_parameter_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_value_CodeableConcept = "TODO"
    value_CodeableConcept_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_value_CodeableConcept}, related_name='SupplyRequest_parameter_value_CodeableConcept', blank=True)
    value_CodeableConcept_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value_Quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='SupplyRequest_parameter_value_Quantity', null=True, blank=True, on_delete=models.SET_NULL)
    value_Range = models.OneToOneField("FHIR_GP_Range", related_name='SupplyRequest_parameter_value_Range', null=True, blank=True, on_delete=models.SET_NULL)
    value_boolean = FHIR_primitive_BooleanField(null=True, blank=True, )

class FHIR_SupplyRequest_reason(models.Model):
    SupplyRequest = models.ForeignKey(FHIR_SupplyRequest, related_name='SupplyRequest_reason', null=False, on_delete=models.CASCADE)
    BINDING_reason = "TODO"
    reason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_reason}, related_name='SupplyRequest_reason', blank=True)
    reason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    reason_Condition_ref = models.ForeignKey("FHIR_Condition", related_name="SupplyRequest_reason_Condition", null=True, blank=True, on_delete=models.SET_NULL)
    reason_Observation_ref = models.ForeignKey("FHIR_Observation", related_name="SupplyRequest_reason_Observation", null=True, blank=True, on_delete=models.SET_NULL)
    reason_DiagnosticReport_ref = models.ForeignKey("FHIR_DiagnosticReport", related_name="SupplyRequest_reason_DiagnosticReport", null=True, blank=True, on_delete=models.SET_NULL)
    reason_DocumentReference_ref = models.ForeignKey("FHIR_DocumentReference", related_name="SupplyRequest_reason_DocumentReference", null=True, blank=True, on_delete=models.SET_NULL)
