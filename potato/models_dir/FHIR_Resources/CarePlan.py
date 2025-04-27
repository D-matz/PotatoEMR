#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_CarePlan(models.Model):
    basedOn_CarePlan = models.ManyToManyField("FHIR_CarePlan", related_name="CarePlan_basedOn", blank=True)
    basedOn_ServiceRequest = models.ManyToManyField("FHIR_ServiceRequest", related_name="CarePlan_basedOn", blank=True)
    basedOn_RequestOrchestration = models.ManyToManyField("FHIR_RequestOrchestration", related_name="CarePlan_basedOn", blank=True)
    basedOn_NutritionOrder = models.ManyToManyField("FHIR_NutritionOrder", related_name="CarePlan_basedOn", blank=True)
    replaces = models.ManyToManyField("FHIR_CarePlan", related_name="CarePlan_replaces", blank=True)
    partOf = models.ManyToManyField("FHIR_CarePlan", related_name="CarePlan_partOf", blank=True)
    class StatusChoices(models.TextChoices): DRAFT = 'draft', 'Draft'; ACTIVE = 'active', 'Active'; ON_HOLD = 'on-hold', 'On-hold'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; ENDED = 'ended', 'Ended'; COMPLETED = 'completed', 'Completed'; REVOKED = 'revoked', 'Revoked'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    class IntentChoices(models.TextChoices): PROPOSAL = 'proposal', 'Proposal'; PLAN = 'plan', 'Plan'; ORDER = 'order', 'Order'; OPTION = 'option', 'Option'; DIRECTIVE = 'directive', 'Directive'; 
    intent = FHIR_primitive_CodeField(choices=IntentChoices.choices, null=True, blank=True, )
    title = FHIR_primitive_StringField(null=True, blank=True, )
    description = FHIR_primitive_StringField(null=True, blank=True, )
    subject_Patient = models.ForeignKey("FHIR_Patient", related_name="CarePlan_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Group = models.ForeignKey("FHIR_Group", related_name="CarePlan_subject", null=True, blank=True, on_delete=models.SET_NULL)
    encounter = models.ForeignKey("FHIR_Encounter", related_name="CarePlan_encounter", null=True, blank=True, on_delete=models.SET_NULL)
    period = models.OneToOneField("FHIR_GP_Period", related_name='CarePlan_period', null=True, blank=True, on_delete=models.SET_NULL)
    created = FHIR_primitive_DateTimeField(null=True, blank=True, )
    custodian_Patient = models.ForeignKey("FHIR_Patient", related_name="CarePlan_custodian", null=True, blank=True, on_delete=models.SET_NULL)
    custodian_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="CarePlan_custodian", null=True, blank=True, on_delete=models.SET_NULL)
    custodian_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="CarePlan_custodian", null=True, blank=True, on_delete=models.SET_NULL)
    custodian_Device = models.ForeignKey("FHIR_Device", related_name="CarePlan_custodian", null=True, blank=True, on_delete=models.SET_NULL)
    custodian_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="CarePlan_custodian", null=True, blank=True, on_delete=models.SET_NULL)
    custodian_Organization = models.ForeignKey("FHIR_Organization", related_name="CarePlan_custodian", null=True, blank=True, on_delete=models.SET_NULL)
    custodian_CareTeam = models.ForeignKey("FHIR_CareTeam", related_name="CarePlan_custodian", null=True, blank=True, on_delete=models.SET_NULL)
    contributor_Patient = models.ManyToManyField("FHIR_Patient", related_name="CarePlan_contributor", blank=True)
    contributor_Practitioner = models.ManyToManyField("FHIR_Practitioner", related_name="CarePlan_contributor", blank=True)
    contributor_PractitionerRole = models.ManyToManyField("FHIR_PractitionerRole", related_name="CarePlan_contributor", blank=True)
    contributor_Device = models.ManyToManyField("FHIR_Device", related_name="CarePlan_contributor", blank=True)
    contributor_RelatedPerson = models.ManyToManyField("FHIR_RelatedPerson", related_name="CarePlan_contributor", blank=True)
    contributor_Organization = models.ManyToManyField("FHIR_Organization", related_name="CarePlan_contributor", blank=True)
    contributor_CareTeam = models.ManyToManyField("FHIR_CareTeam", related_name="CarePlan_contributor", blank=True)
    careTeam = models.ManyToManyField("FHIR_CareTeam", related_name="CarePlan_careTeam", blank=True)
    goal = models.ManyToManyField("FHIR_Goal", related_name="CarePlan_goal", blank=True)

class FHIR_CarePlan_identifier(FHIR_GP_Identifier):
    CarePlan = models.ForeignKey(FHIR_CarePlan, related_name='CarePlan_identifier', null=False, on_delete=models.CASCADE)

class FHIR_CarePlan_category(models.Model):
    CarePlan = models.ForeignKey(FHIR_CarePlan, related_name='CarePlan_category', null=False, on_delete=models.CASCADE)
    BINDING_category = 'TODO'
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='CarePlan_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_CarePlan_addresses(models.Model):
    CarePlan = models.ForeignKey(FHIR_CarePlan, related_name='CarePlan_addresses', null=False, on_delete=models.CASCADE)
    BINDING_addresses = 'TODO'
    addresses_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_addresses}, related_name='CarePlan_addresses', blank=True)
    addresses_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    addresses_Condition_ref = models.ForeignKey("FHIR_Condition", related_name="CarePlan_addresses_Condition", null=True, blank=True, on_delete=models.SET_NULL)
    addresses_Procedure_ref = models.ForeignKey("FHIR_Procedure", related_name="CarePlan_addresses_Procedure", null=True, blank=True, on_delete=models.SET_NULL)
    addresses_MedicationAdministration_ref = models.ForeignKey("FHIR_MedicationAdministration", related_name="CarePlan_addresses_MedicationAdministration", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_CarePlan_activity(models.Model):
    CarePlan = models.ForeignKey(FHIR_CarePlan, related_name='CarePlan_activity', null=False, on_delete=models.CASCADE)
    plannedActivityReference_Appointment = models.ForeignKey("FHIR_Appointment", related_name="CarePlan_activity_plannedActivityReference", null=True, blank=True, on_delete=models.SET_NULL)
    plannedActivityReference_CommunicationRequest = models.ForeignKey("FHIR_CommunicationRequest", related_name="CarePlan_activity_plannedActivityReference", null=True, blank=True, on_delete=models.SET_NULL)
    plannedActivityReference_DeviceRequest = models.ForeignKey("FHIR_DeviceRequest", related_name="CarePlan_activity_plannedActivityReference", null=True, blank=True, on_delete=models.SET_NULL)
    plannedActivityReference_MedicationRequest = models.ForeignKey("FHIR_MedicationRequest", related_name="CarePlan_activity_plannedActivityReference", null=True, blank=True, on_delete=models.SET_NULL)
    plannedActivityReference_NutritionOrder = models.ForeignKey("FHIR_NutritionOrder", related_name="CarePlan_activity_plannedActivityReference", null=True, blank=True, on_delete=models.SET_NULL)
    plannedActivityReference_Task = models.ForeignKey("FHIR_Task", related_name="CarePlan_activity_plannedActivityReference", null=True, blank=True, on_delete=models.SET_NULL)
    plannedActivityReference_ServiceRequest = models.ForeignKey("FHIR_ServiceRequest", related_name="CarePlan_activity_plannedActivityReference", null=True, blank=True, on_delete=models.SET_NULL)
    plannedActivityReference_VisionPrescription = models.ForeignKey("FHIR_VisionPrescription", related_name="CarePlan_activity_plannedActivityReference", null=True, blank=True, on_delete=models.SET_NULL)
    plannedActivityReference_RequestOrchestration = models.ForeignKey("FHIR_RequestOrchestration", related_name="CarePlan_activity_plannedActivityReference", null=True, blank=True, on_delete=models.SET_NULL)
    plannedActivityReference_ImmunizationRecommendation = models.ForeignKey("FHIR_ImmunizationRecommendation", related_name="CarePlan_activity_plannedActivityReference", null=True, blank=True, on_delete=models.SET_NULL)
    plannedActivityReference_SupplyRequest = models.ForeignKey("FHIR_SupplyRequest", related_name="CarePlan_activity_plannedActivityReference", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_CarePlan_activity_performedActivity(models.Model):
    CarePlan_activity = models.ForeignKey(FHIR_CarePlan_activity, related_name='CarePlan_activity_performedActivity', null=False, on_delete=models.CASCADE)
    BINDING_performedActivity = 'TODO'
    performedActivity_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_performedActivity}, related_name='CarePlan_activity_performedActivity', blank=True)
    performedActivity_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_CarePlan_activity_progress(FHIR_GP_Annotation):
    CarePlan_activity = models.ForeignKey(FHIR_CarePlan_activity, related_name='CarePlan_activity_progress', null=False, on_delete=models.CASCADE)

class FHIR_CarePlan_note(FHIR_GP_Annotation):
    CarePlan = models.ForeignKey(FHIR_CarePlan, related_name='CarePlan_note', null=False, on_delete=models.CASCADE)
