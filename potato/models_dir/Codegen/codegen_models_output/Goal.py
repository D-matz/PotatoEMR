#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Goal(models.Model):
    class LifecyclestatusChoices(models.TextChoices): PROPOSED = 'proposed', 'Proposed'; PLANNED = 'planned', 'Planned'; ACCEPTED = 'accepted', 'Accepted'; ACTIVE = 'active', 'Active'; ON_HOLD = 'on-hold', 'On-hold'; COMPLETED = 'completed', 'Completed'; CANCELLED = 'cancelled', 'Cancelled'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; REJECTED = 'rejected', 'Rejected'; 
    lifecycleStatus = FHIR_primitive_CodeField(choices=LifecyclestatusChoices.choices, null=True, blank=True, )
    BINDING_achievementStatus = "TODO"
    achievementStatus_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_achievementStatus}, related_name='Goal_achievementStatus', blank=True)
    achievementStatus_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    continuous = FHIR_primitive_BooleanField(null=True, blank=True, )
    BINDING_priority = "TODO"
    priority_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_priority}, related_name='Goal_priority', blank=True)
    priority_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_description = "TODO"
    description_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_description}, related_name='Goal_description', blank=True)
    description_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    subject_Patient = models.ForeignKey("FHIR_Patient", related_name="Goal_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Group = models.ForeignKey("FHIR_Group", related_name="Goal_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Organization = models.ForeignKey("FHIR_Organization", related_name="Goal_subject", null=True, blank=True, on_delete=models.SET_NULL)
    start_date = FHIR_primitive_DateField(null=True, blank=True, )
    BINDING_start_CodeableConcept = "TODO"
    start_CodeableConcept_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_start_CodeableConcept}, related_name='Goal_start_CodeableConcept', blank=True)
    start_CodeableConcept_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    statusDate = FHIR_primitive_DateField(null=True, blank=True, )
    source_Patient = models.ForeignKey("FHIR_Patient", related_name="Goal_source", null=True, blank=True, on_delete=models.SET_NULL)
    source_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="Goal_source", null=True, blank=True, on_delete=models.SET_NULL)
    source_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="Goal_source", null=True, blank=True, on_delete=models.SET_NULL)
    source_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="Goal_source", null=True, blank=True, on_delete=models.SET_NULL)
    source_CareTeam = models.ForeignKey("FHIR_CareTeam", related_name="Goal_source", null=True, blank=True, on_delete=models.SET_NULL)
    source_Group = models.ForeignKey("FHIR_Group", related_name="Goal_source", null=True, blank=True, on_delete=models.SET_NULL)
    addresses_Condition = models.ManyToManyField("FHIR_Condition", related_name="Goal_addresses", blank=True)
    addresses_Observation = models.ManyToManyField("FHIR_Observation", related_name="Goal_addresses", blank=True)
    addresses_MedicationStatement = models.ManyToManyField("FHIR_MedicationStatement", related_name="Goal_addresses", blank=True)
    addresses_MedicationRequest = models.ManyToManyField("FHIR_MedicationRequest", related_name="Goal_addresses", blank=True)
    addresses_NutritionOrder = models.ManyToManyField("FHIR_NutritionOrder", related_name="Goal_addresses", blank=True)
    addresses_ServiceRequest = models.ManyToManyField("FHIR_ServiceRequest", related_name="Goal_addresses", blank=True)
    addresses_RiskAssessment = models.ManyToManyField("FHIR_RiskAssessment", related_name="Goal_addresses", blank=True)
    addresses_Procedure = models.ManyToManyField("FHIR_Procedure", related_name="Goal_addresses", blank=True)
    addresses_NutritionIntake = models.ManyToManyField("FHIR_NutritionIntake", related_name="Goal_addresses", blank=True)

class FHIR_Goal_identifier(FHIR_GP_Identifier):
    Goal = models.ForeignKey(FHIR_Goal, related_name='Goal_identifier', null=False, on_delete=models.CASCADE)

class FHIR_Goal_category(models.Model):
    Goal = models.ForeignKey(FHIR_Goal, related_name='Goal_category', null=False, on_delete=models.CASCADE)
    BINDING_category = "TODO"
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='Goal_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Goal_acceptance(models.Model):
    Goal = models.ForeignKey(FHIR_Goal, related_name='Goal_acceptance', null=False, on_delete=models.CASCADE)
    participant_Patient = models.ForeignKey("FHIR_Patient", related_name="Goal_acceptance_participant", null=True, blank=True, on_delete=models.SET_NULL)
    participant_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="Goal_acceptance_participant", null=True, blank=True, on_delete=models.SET_NULL)
    participant_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="Goal_acceptance_participant", null=True, blank=True, on_delete=models.SET_NULL)
    participant_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="Goal_acceptance_participant", null=True, blank=True, on_delete=models.SET_NULL)
    participant_CareTeam = models.ForeignKey("FHIR_CareTeam", related_name="Goal_acceptance_participant", null=True, blank=True, on_delete=models.SET_NULL)
    participant_Organization = models.ForeignKey("FHIR_Organization", related_name="Goal_acceptance_participant", null=True, blank=True, on_delete=models.SET_NULL)
    class StatusChoices(models.TextChoices): AGREE = 'agree', 'Agree'; DISAGREE = 'disagree', 'Disagree'; PENDING = 'pending', 'Pending'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    BINDING_priority = "TODO"
    priority_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_priority}, related_name='Goal_acceptance_priority', blank=True)
    priority_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_Goal_target(models.Model):
    Goal = models.ForeignKey(FHIR_Goal, related_name='Goal_target', null=False, on_delete=models.CASCADE)
    BINDING_measure = "TODO"
    measure_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_measure}, related_name='Goal_target_measure', blank=True)
    measure_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    detail_Quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='Goal_target_detail_Quantity', null=True, blank=True, on_delete=models.SET_NULL)
    detail_Range = models.OneToOneField("FHIR_GP_Range", related_name='Goal_target_detail_Range', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_detail_CodeableConcept = "TODO"
    detail_CodeableConcept_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_detail_CodeableConcept}, related_name='Goal_target_detail_CodeableConcept', blank=True)
    detail_CodeableConcept_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    detail_string = FHIR_primitive_StringField(null=True, blank=True, )
    detail_boolean = FHIR_primitive_BooleanField(null=True, blank=True, )
    detail_Ratio = models.OneToOneField("FHIR_GP_Ratio", related_name='Goal_target_detail_Ratio', null=True, blank=True, on_delete=models.SET_NULL)
    due_date = FHIR_primitive_DateField(null=True, blank=True, )
    due_Duration = models.OneToOneField("FHIR_GP_Quantity_Duration", related_name='Goal_target_due_Duration', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Goal_statusReason(models.Model):
    Goal = models.ForeignKey(FHIR_Goal, related_name='Goal_statusReason', null=False, on_delete=models.CASCADE)
    BINDING_statusReason = "TODO"
    statusReason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_statusReason}, related_name='Goal_statusReason', blank=True)
    statusReason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Goal_note(FHIR_GP_Annotation):
    Goal = models.ForeignKey(FHIR_Goal, related_name='Goal_note', null=False, on_delete=models.CASCADE)
