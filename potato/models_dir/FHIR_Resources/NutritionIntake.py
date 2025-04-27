#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_NutritionIntake(models.Model):
    basedOn_NutritionOrder = models.ManyToManyField("FHIR_NutritionOrder", related_name="NutritionIntake_basedOn", blank=True)
    basedOn_CarePlan = models.ManyToManyField("FHIR_CarePlan", related_name="NutritionIntake_basedOn", blank=True)
    basedOn_ServiceRequest = models.ManyToManyField("FHIR_ServiceRequest", related_name="NutritionIntake_basedOn", blank=True)
    partOf_NutritionIntake = models.ManyToManyField("FHIR_NutritionIntake", related_name="NutritionIntake_partOf", blank=True)
    partOf_Procedure = models.ManyToManyField("FHIR_Procedure", related_name="NutritionIntake_partOf", blank=True)
    partOf_Observation = models.ManyToManyField("FHIR_Observation", related_name="NutritionIntake_partOf", blank=True)
    class StatusChoices(models.TextChoices): PREPARATION = 'preparation', 'Preparation'; IN_PROGRESS = 'in-progress', 'In-progress'; NOT_DONE = 'not-done', 'Not-done'; ON_HOLD = 'on-hold', 'On-hold'; STOPPED = 'stopped', 'Stopped'; COMPLETED = 'completed', 'Completed'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    BINDING_code = 'TODO'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='NutritionIntake_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    subject_Patient = models.ForeignKey("FHIR_Patient", related_name="NutritionIntake_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Group = models.ForeignKey("FHIR_Group", related_name="NutritionIntake_subject", null=True, blank=True, on_delete=models.SET_NULL)
    encounter = models.ForeignKey("FHIR_Encounter", related_name="NutritionIntake_encounter", null=True, blank=True, on_delete=models.SET_NULL)
    occurrence = FHIR_primitive_DateTimeField(null=True, blank=True, )
    occurrence = models.OneToOneField("FHIR_GP_Period", related_name='NutritionIntake_occurrence', null=True, blank=True, on_delete=models.SET_NULL)
    recorded = FHIR_primitive_DateTimeField(null=True, blank=True, )
    reported = FHIR_primitive_BooleanField(null=True, blank=True, )
    reported_Patient = models.ForeignKey("FHIR_Patient", related_name="NutritionIntake_reported", null=True, blank=True, on_delete=models.SET_NULL)
    reported_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="NutritionIntake_reported", null=True, blank=True, on_delete=models.SET_NULL)
    reported_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="NutritionIntake_reported", null=True, blank=True, on_delete=models.SET_NULL)
    reported_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="NutritionIntake_reported", null=True, blank=True, on_delete=models.SET_NULL)
    reported_Organization = models.ForeignKey("FHIR_Organization", related_name="NutritionIntake_reported", null=True, blank=True, on_delete=models.SET_NULL)
    reported_Group = models.ForeignKey("FHIR_Group", related_name="NutritionIntake_reported", null=True, blank=True, on_delete=models.SET_NULL)
    location = models.ForeignKey("FHIR_Location", related_name="NutritionIntake_location", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_NutritionIntake_identifier(FHIR_GP_Identifier):
    NutritionIntake = models.ForeignKey(FHIR_NutritionIntake, related_name='NutritionIntake_identifier', null=False, on_delete=models.CASCADE)

class FHIR_NutritionIntake_statusReason(models.Model):
    NutritionIntake = models.ForeignKey(FHIR_NutritionIntake, related_name='NutritionIntake_statusReason', null=False, on_delete=models.CASCADE)
    BINDING_statusReason = 'TODO'
    statusReason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_statusReason}, related_name='NutritionIntake_statusReason', blank=True)
    statusReason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_NutritionIntake_nutritionItem(models.Model):
    NutritionIntake = models.ForeignKey(FHIR_NutritionIntake, related_name='NutritionIntake_nutritionItem', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='NutritionIntake_nutritionItem_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_nutritionProduct = 'TODO'
    nutritionProduct_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_nutritionProduct}, related_name='NutritionIntake_nutritionItem_nutritionProduct', blank=True)
    nutritionProduct_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    nutritionProduct_NutritionProduct_ref = models.ForeignKey("FHIR_NutritionProduct", related_name="NutritionIntake_nutritionItem_nutritionProduct_NutritionProduct", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_NutritionIntake_nutritionItem_consumedItem(models.Model):
    NutritionIntake_nutritionItem = models.ForeignKey(FHIR_NutritionIntake_nutritionItem, related_name='NutritionIntake_nutritionItem_consumedItem', null=False, on_delete=models.CASCADE)
    schedule = models.OneToOneField("FHIR_GP_Timing", related_name='NutritionIntake_nutritionItem_consumedItem_schedule', null=True, blank=True, on_delete=models.SET_NULL)
    amount = models.OneToOneField("FHIR_GP_Quantity", related_name='NutritionIntake_nutritionItem_consumedItem_amount', null=True, blank=True, on_delete=models.SET_NULL)
    rate = models.OneToOneField("FHIR_GP_Quantity", related_name='NutritionIntake_nutritionItem_consumedItem_rate', null=True, blank=True, on_delete=models.SET_NULL)
    rate = models.OneToOneField("FHIR_GP_Ratio", related_name='NutritionIntake_nutritionItem_consumedItem_rate', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_NutritionIntake_nutritionItem_consumedItem_totalIntake(models.Model):
    NutritionIntake_nutritionItem_consumedItem = models.ForeignKey(FHIR_NutritionIntake_nutritionItem_consumedItem, related_name='NutritionIntake_nutritionItem_consumedItem_totalIntake', null=False, on_delete=models.CASCADE)
    BINDING_nutrient = 'TODO'
    nutrient_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_nutrient}, related_name='NutritionIntake_nutritionItem_consumedItem_totalIntake_nutrient', blank=True)
    nutrient_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    nutrient_Substance_ref = models.ForeignKey("FHIR_Substance", related_name="NutritionIntake_nutritionItem_consumedItem_totalIntake_nutrient_Substance", null=True, blank=True, on_delete=models.SET_NULL)
    amount = models.OneToOneField("FHIR_GP_Quantity", related_name='NutritionIntake_nutritionItem_consumedItem_totalIntake_amount', null=True, blank=True, on_delete=models.SET_NULL)
    energy = models.OneToOneField("FHIR_GP_Quantity", related_name='NutritionIntake_nutritionItem_consumedItem_totalIntake_energy', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_NutritionIntake_nutritionItem_notConsumedItem(models.Model):
    NutritionIntake_nutritionItem = models.ForeignKey(FHIR_NutritionIntake_nutritionItem, related_name='NutritionIntake_nutritionItem_notConsumedItem', null=False, on_delete=models.CASCADE)
    BINDING_reason = 'TODO'
    reason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_reason}, related_name='NutritionIntake_nutritionItem_notConsumedItem_reason', blank=True)
    reason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    schedule = models.OneToOneField("FHIR_GP_Timing", related_name='NutritionIntake_nutritionItem_notConsumedItem_schedule', null=True, blank=True, on_delete=models.SET_NULL)
    amount = models.OneToOneField("FHIR_GP_Quantity", related_name='NutritionIntake_nutritionItem_notConsumedItem_amount', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_NutritionIntake_performer(models.Model):
    NutritionIntake = models.ForeignKey(FHIR_NutritionIntake, related_name='NutritionIntake_performer', null=False, on_delete=models.CASCADE)
    BINDING_function = 'TODO'
    function_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_function}, related_name='NutritionIntake_performer_function', blank=True)
    function_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    actor_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="NutritionIntake_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="NutritionIntake_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Organization = models.ForeignKey("FHIR_Organization", related_name="NutritionIntake_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_CareTeam = models.ForeignKey("FHIR_CareTeam", related_name="NutritionIntake_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Patient = models.ForeignKey("FHIR_Patient", related_name="NutritionIntake_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Device = models.ForeignKey("FHIR_Device", related_name="NutritionIntake_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="NutritionIntake_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Group = models.ForeignKey("FHIR_Group", related_name="NutritionIntake_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_NutritionIntake_reason(models.Model):
    NutritionIntake = models.ForeignKey(FHIR_NutritionIntake, related_name='NutritionIntake_reason', null=False, on_delete=models.CASCADE)
    BINDING_reason = 'TODO'
    reason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_reason}, related_name='NutritionIntake_reason', blank=True)
    reason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    reason_Condition_ref = models.ForeignKey("FHIR_Condition", related_name="NutritionIntake_reason_Condition", null=True, blank=True, on_delete=models.SET_NULL)
    reason_Observation_ref = models.ForeignKey("FHIR_Observation", related_name="NutritionIntake_reason_Observation", null=True, blank=True, on_delete=models.SET_NULL)
    reason_DiagnosticReport_ref = models.ForeignKey("FHIR_DiagnosticReport", related_name="NutritionIntake_reason_DiagnosticReport", null=True, blank=True, on_delete=models.SET_NULL)
    reason_DocumentReference_ref = models.ForeignKey("FHIR_DocumentReference", related_name="NutritionIntake_reason_DocumentReference", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_NutritionIntake_note(FHIR_GP_Annotation):
    NutritionIntake = models.ForeignKey(FHIR_NutritionIntake, related_name='NutritionIntake_note', null=False, on_delete=models.CASCADE)
