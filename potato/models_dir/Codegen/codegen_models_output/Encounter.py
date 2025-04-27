#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Encounter(models.Model):
    class StatusChoices(models.TextChoices): PLANNED = 'planned', 'Planned'; IN_PROGRESS = 'in-progress', 'In-progress'; ON_HOLD = 'on-hold', 'On-hold'; DISCHARGED = 'discharged', 'Discharged'; COMPLETED = 'completed', 'Completed'; CANCELLED = 'cancelled', 'Cancelled'; DISCONTINUED = 'discontinued', 'Discontinued'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    BINDING_priority = "TODO"
    priority_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_priority}, related_name='Encounter_priority', blank=True)
    priority_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    subject_Patient = models.ForeignKey("FHIR_Patient", related_name="Encounter_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Group = models.ForeignKey("FHIR_Group", related_name="Encounter_subject", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_subjectStatus = "TODO"
    subjectStatus_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_subjectStatus}, related_name='Encounter_subjectStatus', blank=True)
    subjectStatus_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    episodeOfCare = models.ManyToManyField("FHIR_EpisodeOfCare", related_name="Encounter_episodeOfCare", blank=True)
    basedOn_CarePlan = models.ManyToManyField("FHIR_CarePlan", related_name="Encounter_basedOn", blank=True)
    basedOn_DeviceRequest = models.ManyToManyField("FHIR_DeviceRequest", related_name="Encounter_basedOn", blank=True)
    basedOn_MedicationRequest = models.ManyToManyField("FHIR_MedicationRequest", related_name="Encounter_basedOn", blank=True)
    basedOn_ServiceRequest = models.ManyToManyField("FHIR_ServiceRequest", related_name="Encounter_basedOn", blank=True)
    basedOn_RequestOrchestration = models.ManyToManyField("FHIR_RequestOrchestration", related_name="Encounter_basedOn", blank=True)
    basedOn_NutritionOrder = models.ManyToManyField("FHIR_NutritionOrder", related_name="Encounter_basedOn", blank=True)
    basedOn_VisionPrescription = models.ManyToManyField("FHIR_VisionPrescription", related_name="Encounter_basedOn", blank=True)
    basedOn_ImmunizationRecommendation = models.ManyToManyField("FHIR_ImmunizationRecommendation", related_name="Encounter_basedOn", blank=True)
    careTeam = models.ManyToManyField("FHIR_CareTeam", related_name="Encounter_careTeam", blank=True)
    partOf = models.ForeignKey("FHIR_Encounter", related_name="Encounter_partOf", null=True, blank=True, on_delete=models.SET_NULL)
    serviceProvider = models.ForeignKey("FHIR_Organization", related_name="Encounter_serviceProvider", null=True, blank=True, on_delete=models.SET_NULL)
    appointment = models.ManyToManyField("FHIR_Appointment", related_name="Encounter_appointment", blank=True)
    actualPeriod = models.OneToOneField("FHIR_GP_Period", related_name='Encounter_actualPeriod', null=True, blank=True, on_delete=models.SET_NULL)
    plannedStartDate = FHIR_primitive_DateTimeField(null=True, blank=True, )
    plannedEndDate = FHIR_primitive_DateTimeField(null=True, blank=True, )
    length = models.OneToOneField("FHIR_GP_Quantity_Duration", related_name='Encounter_length', null=True, blank=True, on_delete=models.SET_NULL)
    account = models.ManyToManyField("FHIR_Account", related_name="Encounter_account", blank=True)

class FHIR_Encounter_identifier(FHIR_GP_Identifier):
    Encounter = models.ForeignKey(FHIR_Encounter, related_name='Encounter_identifier', null=False, on_delete=models.CASCADE)

class FHIR_Encounter_class(models.Model):
    Encounter = models.ForeignKey(FHIR_Encounter, related_name='Encounter_class', null=False, on_delete=models.CASCADE)
    BINDING_class = "TODO"
    class_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_class}, related_name='Encounter_class', blank=True)
    class_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Encounter_type(models.Model):
    Encounter = models.ForeignKey(FHIR_Encounter, related_name='Encounter_type', null=False, on_delete=models.CASCADE)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Encounter_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Encounter_serviceType(models.Model):
    Encounter = models.ForeignKey(FHIR_Encounter, related_name='Encounter_serviceType', null=False, on_delete=models.CASCADE)
    BINDING_serviceType = "TODO"
    serviceType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_serviceType}, related_name='Encounter_serviceType', blank=True)
    serviceType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    serviceType_HealthcareService_ref = models.ForeignKey("FHIR_HealthcareService", related_name="Encounter_serviceType_HealthcareService", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Encounter_participant(models.Model):
    Encounter = models.ForeignKey(FHIR_Encounter, related_name='Encounter_participant', null=False, on_delete=models.CASCADE)
    period = models.OneToOneField("FHIR_GP_Period", related_name='Encounter_participant_period', null=True, blank=True, on_delete=models.SET_NULL)
    actor_Patient = models.ForeignKey("FHIR_Patient", related_name="Encounter_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Group = models.ForeignKey("FHIR_Group", related_name="Encounter_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="Encounter_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="Encounter_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="Encounter_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Device = models.ForeignKey("FHIR_Device", related_name="Encounter_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_HealthcareService = models.ForeignKey("FHIR_HealthcareService", related_name="Encounter_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Encounter_participant_type(models.Model):
    Encounter_participant = models.ForeignKey(FHIR_Encounter_participant, related_name='Encounter_participant_type', null=False, on_delete=models.CASCADE)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Encounter_participant_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Encounter_virtualService(FHIR_meta_VirtualServiceDetail):
    Encounter = models.ForeignKey(FHIR_Encounter, related_name='Encounter_virtualService', null=False, on_delete=models.CASCADE)

class FHIR_Encounter_reason(models.Model):
    Encounter = models.ForeignKey(FHIR_Encounter, related_name='Encounter_reason', null=False, on_delete=models.CASCADE)

class FHIR_Encounter_reason_use(models.Model):
    Encounter_reason = models.ForeignKey(FHIR_Encounter_reason, related_name='Encounter_reason_use', null=False, on_delete=models.CASCADE)
    BINDING_use = "TODO"
    use_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_use}, related_name='Encounter_reason_use', blank=True)
    use_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Encounter_reason_value(models.Model):
    Encounter_reason = models.ForeignKey(FHIR_Encounter_reason, related_name='Encounter_reason_value', null=False, on_delete=models.CASCADE)
    BINDING_value = "TODO"
    value_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_value}, related_name='Encounter_reason_value', blank=True)
    value_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value_Condition_ref = models.ForeignKey("FHIR_Condition", related_name="Encounter_reason_value_Condition", null=True, blank=True, on_delete=models.SET_NULL)
    value_DiagnosticReport_ref = models.ForeignKey("FHIR_DiagnosticReport", related_name="Encounter_reason_value_DiagnosticReport", null=True, blank=True, on_delete=models.SET_NULL)
    value_Observation_ref = models.ForeignKey("FHIR_Observation", related_name="Encounter_reason_value_Observation", null=True, blank=True, on_delete=models.SET_NULL)
    value_ImmunizationRecommendation_ref = models.ForeignKey("FHIR_ImmunizationRecommendation", related_name="Encounter_reason_value_ImmunizationRecommendation", null=True, blank=True, on_delete=models.SET_NULL)
    value_Procedure_ref = models.ForeignKey("FHIR_Procedure", related_name="Encounter_reason_value_Procedure", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Encounter_diagnosis(models.Model):
    Encounter = models.ForeignKey(FHIR_Encounter, related_name='Encounter_diagnosis', null=False, on_delete=models.CASCADE)

class FHIR_Encounter_diagnosis_condition(models.Model):
    Encounter_diagnosis = models.ForeignKey(FHIR_Encounter_diagnosis, related_name='Encounter_diagnosis_condition', null=False, on_delete=models.CASCADE)
    BINDING_condition = "TODO"
    condition_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_condition}, related_name='Encounter_diagnosis_condition', blank=True)
    condition_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    condition_Condition_ref = models.ForeignKey("FHIR_Condition", related_name="Encounter_diagnosis_condition_Condition", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Encounter_diagnosis_use(models.Model):
    Encounter_diagnosis = models.ForeignKey(FHIR_Encounter_diagnosis, related_name='Encounter_diagnosis_use', null=False, on_delete=models.CASCADE)
    BINDING_use = "TODO"
    use_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_use}, related_name='Encounter_diagnosis_use', blank=True)
    use_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Encounter_dietPreference(models.Model):
    Encounter = models.ForeignKey(FHIR_Encounter, related_name='Encounter_dietPreference', null=False, on_delete=models.CASCADE)
    BINDING_dietPreference = "TODO"
    dietPreference_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_dietPreference}, related_name='Encounter_dietPreference', blank=True)
    dietPreference_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Encounter_specialArrangement(models.Model):
    Encounter = models.ForeignKey(FHIR_Encounter, related_name='Encounter_specialArrangement', null=False, on_delete=models.CASCADE)
    BINDING_specialArrangement = "TODO"
    specialArrangement_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_specialArrangement}, related_name='Encounter_specialArrangement', blank=True)
    specialArrangement_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Encounter_specialCourtesy(models.Model):
    Encounter = models.ForeignKey(FHIR_Encounter, related_name='Encounter_specialCourtesy', null=False, on_delete=models.CASCADE)
    BINDING_specialCourtesy = "TODO"
    specialCourtesy_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_specialCourtesy}, related_name='Encounter_specialCourtesy', blank=True)
    specialCourtesy_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Encounter_admission(models.Model):
    Encounter = models.ForeignKey(FHIR_Encounter, related_name='Encounter_admission', null=False, on_delete=models.CASCADE)
    preAdmissionIdentifier = models.OneToOneField("FHIR_GP_Identifier", related_name='Encounter_admission_preAdmissionIdentifier', null=True, blank=True, on_delete=models.SET_NULL)
    origin_Location = models.ForeignKey("FHIR_Location", related_name="Encounter_admission_origin", null=True, blank=True, on_delete=models.SET_NULL)
    origin_Organization = models.ForeignKey("FHIR_Organization", related_name="Encounter_admission_origin", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_admitSource = "TODO"
    admitSource_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_admitSource}, related_name='Encounter_admission_admitSource', blank=True)
    admitSource_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_reAdmission = "TODO"
    reAdmission_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_reAdmission}, related_name='Encounter_admission_reAdmission', blank=True)
    reAdmission_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    destination_Location = models.ForeignKey("FHIR_Location", related_name="Encounter_admission_destination", null=True, blank=True, on_delete=models.SET_NULL)
    destination_Organization = models.ForeignKey("FHIR_Organization", related_name="Encounter_admission_destination", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_dischargeDisposition = "TODO"
    dischargeDisposition_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_dischargeDisposition}, related_name='Encounter_admission_dischargeDisposition', blank=True)
    dischargeDisposition_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_Encounter_location(models.Model):
    Encounter = models.ForeignKey(FHIR_Encounter, related_name='Encounter_location', null=False, on_delete=models.CASCADE)
    location = models.ForeignKey("FHIR_Location", related_name="Encounter_location_location", null=True, blank=True, on_delete=models.SET_NULL)
    class StatusChoices(models.TextChoices): PLANNED = 'planned', 'Planned'; ACTIVE = 'active', 'Active'; RESERVED = 'reserved', 'Reserved'; COMPLETED = 'completed', 'Completed'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    BINDING_form = "TODO"
    form_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_form}, related_name='Encounter_location_form', blank=True)
    form_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    period = models.OneToOneField("FHIR_GP_Period", related_name='Encounter_location_period', null=True, blank=True, on_delete=models.SET_NULL)
