#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_NutritionOrder(models.Model):
    basedOn_CarePlan = models.ManyToManyField("FHIR_CarePlan", related_name="NutritionOrder_basedOn", blank=True)
    basedOn_NutritionOrder = models.ManyToManyField("FHIR_NutritionOrder", related_name="NutritionOrder_basedOn", blank=True)
    basedOn_ServiceRequest = models.ManyToManyField("FHIR_ServiceRequest", related_name="NutritionOrder_basedOn", blank=True)
    basedOn_RequestOrchestration = models.ManyToManyField("FHIR_RequestOrchestration", related_name="NutritionOrder_basedOn", blank=True)
    groupIdentifier = models.OneToOneField("FHIR_GP_Identifier", related_name='NutritionOrder_groupIdentifier', null=True, blank=True, on_delete=models.SET_NULL)
    class StatusChoices(models.TextChoices): DRAFT = 'draft', 'Draft'; ACTIVE = 'active', 'Active'; ON_HOLD = 'on-hold', 'On-hold'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; ENDED = 'ended', 'Ended'; COMPLETED = 'completed', 'Completed'; REVOKED = 'revoked', 'Revoked'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    class IntentChoices(models.TextChoices): PROPOSAL = 'proposal', 'Proposal'; PLAN = 'plan', 'Plan'; DIRECTIVE = 'directive', 'Directive'; ORDER = 'order', 'Order'; ORIGINAL_ORDER = 'original-order', 'Original-order'; REFLEX_ORDER = 'reflex-order', 'Reflex-order'; FILLER_ORDER = 'filler-order', 'Filler-order'; INSTANCE_ORDER = 'instance-order', 'Instance-order'; OPTION = 'option', 'Option'; 
    intent = FHIR_primitive_CodeField(choices=IntentChoices.choices, null=True, blank=True, )
    class PriorityChoices(models.TextChoices): ROUTINE = 'routine', 'Routine'; URGENT = 'urgent', 'Urgent'; ASAP = 'asap', 'Asap'; STAT = 'stat', 'Stat'; 
    priority = FHIR_primitive_CodeField(choices=PriorityChoices.choices, null=True, blank=True, )
    subject_Patient = models.ForeignKey("FHIR_Patient", related_name="NutritionOrder_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Group = models.ForeignKey("FHIR_Group", related_name="NutritionOrder_subject", null=True, blank=True, on_delete=models.SET_NULL)
    encounter = models.ForeignKey("FHIR_Encounter", related_name="NutritionOrder_encounter", null=True, blank=True, on_delete=models.SET_NULL)
                            #skipping Reference(Any) for field supportingInformation as NutritionOrder supportingInformation not in referenceAny_targets
    dateTime = FHIR_primitive_DateTimeField(null=True, blank=True, )
    requester_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="NutritionOrder_requester", null=True, blank=True, on_delete=models.SET_NULL)
    requester_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="NutritionOrder_requester", null=True, blank=True, on_delete=models.SET_NULL)
    allergyIntolerance = models.ManyToManyField("FHIR_AllergyIntolerance", related_name="NutritionOrder_allergyIntolerance", blank=True)
    outsideFoodAllowed = FHIR_primitive_BooleanField(null=True, blank=True, )

class FHIR_NutritionOrder_identifier(FHIR_GP_Identifier):
    NutritionOrder = models.ForeignKey(FHIR_NutritionOrder, related_name='NutritionOrder_identifier', null=False, on_delete=models.CASCADE)

class FHIR_NutritionOrder_instantiatesCanonical(models.Model):
    NutritionOrder = models.ForeignKey(FHIR_NutritionOrder, related_name='NutritionOrder_instantiatesCanonical', null=False, on_delete=models.CASCADE)
    
    instantiatesCanonical = FHIR_primitive_CanonicalField(null=True, blank=True, )
    
class FHIR_NutritionOrder_performer(models.Model):
    NutritionOrder = models.ForeignKey(FHIR_NutritionOrder, related_name='NutritionOrder_performer', null=False, on_delete=models.CASCADE)
    BINDING_performer = "TODO"
    performer_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_performer}, related_name='NutritionOrder_performer', blank=True)
    performer_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    performer_CareTeam_ref = models.ForeignKey("FHIR_CareTeam", related_name="NutritionOrder_performer_CareTeam", null=True, blank=True, on_delete=models.SET_NULL)
    performer_Practitioner_ref = models.ForeignKey("FHIR_Practitioner", related_name="NutritionOrder_performer_Practitioner", null=True, blank=True, on_delete=models.SET_NULL)
    performer_PractitionerRole_ref = models.ForeignKey("FHIR_PractitionerRole", related_name="NutritionOrder_performer_PractitionerRole", null=True, blank=True, on_delete=models.SET_NULL)
    performer_RelatedPerson_ref = models.ForeignKey("FHIR_RelatedPerson", related_name="NutritionOrder_performer_RelatedPerson", null=True, blank=True, on_delete=models.SET_NULL)
    performer_Patient_ref = models.ForeignKey("FHIR_Patient", related_name="NutritionOrder_performer_Patient", null=True, blank=True, on_delete=models.SET_NULL)
    performer_Organization_ref = models.ForeignKey("FHIR_Organization", related_name="NutritionOrder_performer_Organization", null=True, blank=True, on_delete=models.SET_NULL)
    performer_Group_ref = models.ForeignKey("FHIR_Group", related_name="NutritionOrder_performer_Group", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_NutritionOrder_foodPreferenceModifier(models.Model):
    NutritionOrder = models.ForeignKey(FHIR_NutritionOrder, related_name='NutritionOrder_foodPreferenceModifier', null=False, on_delete=models.CASCADE)
    BINDING_foodPreferenceModifier = "TODO"
    foodPreferenceModifier_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_foodPreferenceModifier}, related_name='NutritionOrder_foodPreferenceModifier', blank=True)
    foodPreferenceModifier_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_NutritionOrder_excludeFoodModifier(models.Model):
    NutritionOrder = models.ForeignKey(FHIR_NutritionOrder, related_name='NutritionOrder_excludeFoodModifier', null=False, on_delete=models.CASCADE)
    BINDING_excludeFoodModifier = "TODO"
    excludeFoodModifier_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_excludeFoodModifier}, related_name='NutritionOrder_excludeFoodModifier', blank=True)
    excludeFoodModifier_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_NutritionOrder_oralDiet(models.Model):
    NutritionOrder = models.ForeignKey(FHIR_NutritionOrder, related_name='NutritionOrder_oralDiet', null=False, on_delete=models.CASCADE)
    instruction = FHIR_primitive_StringField(null=True, blank=True, )
    caloricDensity = models.OneToOneField("FHIR_GP_Quantity", related_name='NutritionOrder_oralDiet_caloricDensity', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_NutritionOrder_oralDiet_type(models.Model):
    NutritionOrder_oralDiet = models.ForeignKey(FHIR_NutritionOrder_oralDiet, related_name='NutritionOrder_oralDiet_type', null=False, on_delete=models.CASCADE)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='NutritionOrder_oralDiet_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_NutritionOrder_oralDiet_schedule(models.Model):
    NutritionOrder_oralDiet = models.ForeignKey(FHIR_NutritionOrder_oralDiet, related_name='NutritionOrder_oralDiet_schedule', null=False, on_delete=models.CASCADE)
    asNeeded = FHIR_primitive_BooleanField(null=True, blank=True, )
    BINDING_asNeededFor = "TODO"
    asNeededFor_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_asNeededFor}, related_name='NutritionOrder_oralDiet_schedule_asNeededFor', blank=True)
    asNeededFor_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_NutritionOrder_oralDiet_schedule_timing(FHIR_GP_Timing):
    NutritionOrder_oralDiet_schedule = models.ForeignKey(FHIR_NutritionOrder_oralDiet_schedule, related_name='NutritionOrder_oralDiet_schedule_timing', null=False, on_delete=models.CASCADE)

class FHIR_NutritionOrder_oralDiet_nutrient(models.Model):
    NutritionOrder_oralDiet = models.ForeignKey(FHIR_NutritionOrder_oralDiet, related_name='NutritionOrder_oralDiet_nutrient', null=False, on_delete=models.CASCADE)
    BINDING_modifier = "TODO"
    modifier_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_modifier}, related_name='NutritionOrder_oralDiet_nutrient_modifier', blank=True)
    modifier_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    amount = models.OneToOneField("FHIR_GP_Quantity", related_name='NutritionOrder_oralDiet_nutrient_amount', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_NutritionOrder_oralDiet_texture(models.Model):
    NutritionOrder_oralDiet = models.ForeignKey(FHIR_NutritionOrder_oralDiet, related_name='NutritionOrder_oralDiet_texture', null=False, on_delete=models.CASCADE)
    BINDING_modifier = "TODO"
    modifier_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_modifier}, related_name='NutritionOrder_oralDiet_texture_modifier', blank=True)
    modifier_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='NutritionOrder_oralDiet_texture_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_NutritionOrder_supplement(models.Model):
    NutritionOrder = models.ForeignKey(FHIR_NutritionOrder, related_name='NutritionOrder_supplement', null=False, on_delete=models.CASCADE)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='NutritionOrder_supplement_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    type_NutritionProduct_ref = models.ForeignKey("FHIR_NutritionProduct", related_name="NutritionOrder_supplement_type_NutritionProduct", null=True, blank=True, on_delete=models.SET_NULL)
    productName = FHIR_primitive_StringField(null=True, blank=True, )
    quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='NutritionOrder_supplement_quantity', null=True, blank=True, on_delete=models.SET_NULL)
    instruction = FHIR_primitive_StringField(null=True, blank=True, )
    caloricDensity = models.OneToOneField("FHIR_GP_Quantity", related_name='NutritionOrder_supplement_caloricDensity', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_NutritionOrder_supplement_schedule(models.Model):
    NutritionOrder_supplement = models.ForeignKey(FHIR_NutritionOrder_supplement, related_name='NutritionOrder_supplement_schedule', null=False, on_delete=models.CASCADE)
    asNeeded = FHIR_primitive_BooleanField(null=True, blank=True, )
    BINDING_asNeededFor = "TODO"
    asNeededFor_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_asNeededFor}, related_name='NutritionOrder_supplement_schedule_asNeededFor', blank=True)
    asNeededFor_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_NutritionOrder_supplement_schedule_timing(FHIR_GP_Timing):
    NutritionOrder_supplement_schedule = models.ForeignKey(FHIR_NutritionOrder_supplement_schedule, related_name='NutritionOrder_supplement_schedule_timing', null=False, on_delete=models.CASCADE)

class FHIR_NutritionOrder_enteralFormula(models.Model):
    NutritionOrder = models.ForeignKey(FHIR_NutritionOrder, related_name='NutritionOrder_enteralFormula', null=False, on_delete=models.CASCADE)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='NutritionOrder_enteralFormula_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    type_NutritionProduct_ref = models.ForeignKey("FHIR_NutritionProduct", related_name="NutritionOrder_enteralFormula_type_NutritionProduct", null=True, blank=True, on_delete=models.SET_NULL)
    productName = FHIR_primitive_StringField(null=True, blank=True, )
    caloricDensity = models.OneToOneField("FHIR_GP_Quantity", related_name='NutritionOrder_enteralFormula_caloricDensity', null=True, blank=True, on_delete=models.SET_NULL)
    maxVolumeToAdminister = models.OneToOneField("FHIR_GP_Quantity", related_name='NutritionOrder_enteralFormula_maxVolumeToAdminister', null=True, blank=True, on_delete=models.SET_NULL)
    administrationInstruction = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_NutritionOrder_enteralFormula_deliveryDevice(models.Model):
    NutritionOrder_enteralFormula = models.ForeignKey(FHIR_NutritionOrder_enteralFormula, related_name='NutritionOrder_enteralFormula_deliveryDevice', null=False, on_delete=models.CASCADE)
    BINDING_deliveryDevice = "TODO"
    deliveryDevice_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_deliveryDevice}, related_name='NutritionOrder_enteralFormula_deliveryDevice', blank=True)
    deliveryDevice_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    deliveryDevice_DeviceDefinition_ref = models.ForeignKey("FHIR_DeviceDefinition", related_name="NutritionOrder_enteralFormula_deliveryDevice_DeviceDefinition", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_NutritionOrder_enteralFormula_routeOfAdministration(models.Model):
    NutritionOrder_enteralFormula = models.ForeignKey(FHIR_NutritionOrder_enteralFormula, related_name='NutritionOrder_enteralFormula_routeOfAdministration', null=False, on_delete=models.CASCADE)
    BINDING_routeOfAdministration = "TODO"
    routeOfAdministration_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_routeOfAdministration}, related_name='NutritionOrder_enteralFormula_routeOfAdministration', blank=True)
    routeOfAdministration_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_NutritionOrder_enteralFormula_administration(models.Model):
    NutritionOrder_enteralFormula = models.ForeignKey(FHIR_NutritionOrder_enteralFormula, related_name='NutritionOrder_enteralFormula_administration', null=False, on_delete=models.CASCADE)
    quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='NutritionOrder_enteralFormula_administration_quantity', null=True, blank=True, on_delete=models.SET_NULL)
    rate_Quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='NutritionOrder_enteralFormula_administration_rate_Quantity', null=True, blank=True, on_delete=models.SET_NULL)
    rate_Ratio = models.OneToOneField("FHIR_GP_Ratio", related_name='NutritionOrder_enteralFormula_administration_rate_Ratio', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_NutritionOrder_enteralFormula_administration_schedule(models.Model):
    NutritionOrder_enteralFormula_administration = models.ForeignKey(FHIR_NutritionOrder_enteralFormula_administration, related_name='NutritionOrder_enteralFormula_administration_schedule', null=False, on_delete=models.CASCADE)
    asNeeded = FHIR_primitive_BooleanField(null=True, blank=True, )
    BINDING_asNeededFor = "TODO"
    asNeededFor_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_asNeededFor}, related_name='NutritionOrder_enteralFormula_administration_schedule_asNeededFor', blank=True)
    asNeededFor_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_NutritionOrder_enteralFormula_administration_schedule_timing(FHIR_GP_Timing):
    NutritionOrder_enteralFormula_administration_schedule = models.ForeignKey(FHIR_NutritionOrder_enteralFormula_administration_schedule, related_name='NutritionOrder_enteralFormula_administration_schedule_timing', null=False, on_delete=models.CASCADE)

class FHIR_NutritionOrder_additive(models.Model):
    NutritionOrder = models.ForeignKey(FHIR_NutritionOrder, related_name='NutritionOrder_additive', null=False, on_delete=models.CASCADE)
    BINDING_modularType = "TODO"
    modularType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_modularType}, related_name='NutritionOrder_additive_modularType', blank=True)
    modularType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    modularType_NutritionProduct_ref = models.ForeignKey("FHIR_NutritionProduct", related_name="NutritionOrder_additive_modularType_NutritionProduct", null=True, blank=True, on_delete=models.SET_NULL)
    productName = FHIR_primitive_StringField(null=True, blank=True, )
    quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='NutritionOrder_additive_quantity', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_NutritionOrder_additive_routeOfAdministration(models.Model):
    NutritionOrder_additive = models.ForeignKey(FHIR_NutritionOrder_additive, related_name='NutritionOrder_additive_routeOfAdministration', null=False, on_delete=models.CASCADE)
    BINDING_routeOfAdministration = "TODO"
    routeOfAdministration_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_routeOfAdministration}, related_name='NutritionOrder_additive_routeOfAdministration', blank=True)
    routeOfAdministration_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_NutritionOrder_note(FHIR_GP_Annotation):
    NutritionOrder = models.ForeignKey(FHIR_NutritionOrder, related_name='NutritionOrder_note', null=False, on_delete=models.CASCADE)
