from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *

#an encounter must have at least 1 location and at least 1 status
#it probably should have patient and practitioner participants, but doesn't have to
class FHIR_Encounter(models.Model):
    #identifier foreign key to this
    class StatusChoices(models.TextChoices): PLANNED = 'planned', 'Planned'; IN_PROGRESS = 'in-progress', 'In Progress'; ON_HOLD = 'on-hold', 'On Hold'; DISCHARGED = 'discharged', 'Discharged'; COMPLETED = 'completed', 'Completed'; CANCELLED = 'cancelled', 'Cancelled'; DISCONTINUED = 'discontinued', 'Discontinued'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered in Error'; UNKNOWN = 'unknown', 'Unknown'
    status = FHIR_primitive_CodeField(max_length=16, choices=StatusChoices.choices, null=False)

    #class foreign key to this

    BINDING_RULE_PRIORITY = 'todo'
    priority_cc = models.ManyToManyField(FHIR_GP_Coding, related_name='encounter_priority', limit_choices_to={'codings__binding_rule': BINDING_RULE_PRIORITY})
    priority_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

    #type foreign key to this

    #serviceType foreign key to this

    subject_patient = models.ForeignKey('FHIR_Patient', related_name="encounter_subject_patient", null=True, on_delete=models.SET_NULL)
    subject_group = models.ForeignKey('FHIR_Patient', related_name="encounter_subject_group", null=True, on_delete=models.SET_NULL)

    BINDING_RULE_SUBJECTSTATUS = 'todo'
    subjectStatus_cc = models.ManyToManyField(FHIR_GP_Coding, related_name='encounter_subjectStatus', limit_choices_to={'codings__binding_rule': BINDING_RULE_SUBJECTSTATUS})
    subjectStatus_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

    episodeOfCare_ref = models.ManyToManyField('FHIR_EpisodeOfCare', related_name='encounter_episodeOfCare', blank=True)

    basedOn_carePlan_ref = models.ManyToManyField('FHIR_CarePlan', related_name='encounter_basedOn_carePlan', blank=True)
    basedOn_deviceRequest_ref = models.ManyToManyField('FHIR_DeviceRequest', related_name='encounter_basedOn_deviceRequest', blank=True)
    basedOn_medicationRequest_ref = models.ManyToManyField('FHIR_MedicationRequest', related_name='encounter_basedOn_medicationRequest', blank=True)
    basedOn_serviceRequest_ref = models.ManyToManyField('FHIR_ServiceRequest', related_name='encounter_basedOn_serviceRequest', blank=True)
    basedOn_careTeam_ref = models.ManyToManyField('FHIR_CareTeam', related_name='encounter_basedOn_careTeam', blank=True)

    careTeam = models.ManyToManyField('FHIR_CareTeam', related_name='encounter_careTeam', blank=True)
    partOf_ref = models.ForeignKey('FHIR_Encounter', related_name='encounter_partOf', null=True, on_delete=models.SET_NULL, blank=True)
    serviceProvider_ref = models.ForeignKey('FHIR_Organization', related_name='encounter_serviceProvider', null=True, on_delete=models.SET_NULL, blank=True)

    #participant foreign key to this

    appointment = models.ManyToManyField('FHIR_Appointment', related_name='encounter_appointment', blank=True)
    
    #virtualServiceDetail foreign key to this

    actualPeriod = FHIR_GP_Period()
    plannedStartDate = FHIR_primitive_DateTimeField(null=True, blank=True)
    plannedEndDate = FHIR_primitive_DateTimeField(null=True, blank=True)
    length = FHIR_GP_Quantity_Duration()

    #reason foreign key to this

    #diagnosis foreign key to this

    account = models.ManyToManyField('FHIR_Account', related_name='encounter_account', blank=True)

    #dietPreference foreign key to this
    #specialArrangement foreign key to this
    #specialCourtesy foreign key to this

    #admission backbone element
    admission_preAdmissionIdentifier = models.OneToOneField('FHIR_GP_Identifier', related_name='encounter_admission_preAdmissionIdentifier', null=True, blank=True, on_delete=models.SET_NULL)
    admission_origin_location = models.ForeignKey('FHIR_Location', related_name='encounter_admission_origin_location', null=True, blank=True, on_delete=models.SET_NULL)
    admission_origin_organization = models.ForeignKey('FHIR_Organization', related_name='encounter_admission_origin_organization', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_RULE_ADMIT_SOURCE = 'todo'
    admission_admitSource_cc = models.ManyToManyField(FHIR_GP_Coding, related_name='encounter_admission_admitSource', limit_choices_to={'codings__binding_rule': BINDING_RULE_ADMIT_SOURCE })
    admission_admitSource_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_RULE_READMISSION = 'todo'
    admission_readmission_cc = models.ManyToManyField(FHIR_GP_Coding, related_name='encounter_admission_readmission', limit_choices_to={'codings__binding_rule': BINDING_RULE_READMISSION })
    admission_readmission_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    admission_destination_location = models.ForeignKey('FHIR_Location', related_name='encounter_admission_destination_location', null=True, blank=True, on_delete=models.SET_NULL)
    admission_destination_organization = models.ForeignKey('FHIR_Organization', related_name='encounter_admission_destination_organization', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_RULE_DISCHARGE_DISPOSITION = 'todo'
    admission_dischargeDisposition_cc = models.ManyToManyField(FHIR_GP_Coding, related_name='encounter_admission_dischargeDisposition', limit_choices_to={'codings__binding_rule': BINDING_RULE_DISCHARGE_DISPOSITION })
    admission_dischargeDisposition_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

    #location backbone element
    location_ref = models.ForeignKey('FHIR_Location', related_name='encounter_location', null=False, on_delete=models.CASCADE)
    class LocationStatus(models.TextChoices): PLANNED = 'planned', 'Planned'; ACTIVE = 'active', 'Active'; RESERVED = 'reserved', 'Reserved'; COMPLETED = 'completed', 'Completed'
    location_status = FHIR_primitive_CodeField(max_length=16, choices=LocationStatus.choices, null=True, blank=True)
    BINDING_RULE_LOCATION_FORM = 'todo'
    location_form_cc = models.ManyToManyField(FHIR_GP_Coding, related_name='encounter_location_form', limit_choices_to={'codings__binding_rule': BINDING_RULE_LOCATION_FORM })
    location_form_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    location_period = FHIR_GP_Period()

class FHIR_Encounter_Identifier(FHIR_GP_Identifier):
    encounter = models.ForeignKey(FHIR_Encounter, on_delete=models.CASCADE, related_name='identifiers')

class FHIR_Encounter_Class(models.Model):
    encounter = models.ForeignKey(FHIR_Encounter, on_delete=models.CASCADE, related_name='classes')
    BINDING_RULE_CLASS = 'todo'
    class_cc = models.ManyToManyField(FHIR_GP_Coding, related_name='encounter_class', limit_choices_to={'codings__binding_rule': BINDING_RULE_CLASS})
    class_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_Encounter_Type(models.Model):
    encounter = models.ForeignKey(FHIR_Encounter, on_delete=models.CASCADE, related_name='types')
    BINDING_RULE_TYPE = 'todo'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, related_name='encounter_type', limit_choices_to={'codings__binding_rule': BINDING_RULE_TYPE})

class FHIR_Encounter_ServiceType(models.Model):
    encounter = models.ForeignKey(FHIR_Encounter, on_delete=models.CASCADE, related_name='service_types')
    BINDING_RULE_SERVICETYPE = 'todo'
    serviceType_cc = models.ManyToManyField(FHIR_GP_Coding, related_name='encounter_service_type', limit_choices_to={'codings__binding_rule': BINDING_RULE_SERVICETYPE})
    serviceType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    serviceType_reference = models.ForeignKey('FHIR_ServiceRequest', on_delete=models.CASCADE, related_name='encounter_service_type', null=True, blank=True)

class FHIR_Encounter_Participant(models.Model):
    encounter = models.ForeignKey(FHIR_Encounter, on_delete=models.CASCADE, related_name='participants')
    period = FHIR_GP_Period()
    actor_patient = models.ForeignKey('FHIR_Patient', related_name="encounter_participant_actor_patient", null=True, on_delete=models.SET_NULL, blank=True)
    actor_group = models.ForeignKey('FHIR_Group', related_name="encounter_participant_actor_group", null=True, on_delete=models.SET_NULL, blank=True)
    actor_relatedPerson = models.ForeignKey('FHIR_RelatedPerson', related_name="encounter_participant_actor_relatedPerson", null=True, on_delete=models.SET_NULL, blank=True)
    actor_practitioner = models.ForeignKey('FHIR_Practitioner', related_name="encounter_participant_actor_practitioner", null=True, on_delete=models.SET_NULL, blank=True)
    actor_practitionerRole = models.ForeignKey('FHIR_PractitionerRole', related_name="encounter_participant_actor_practitionerRole", null=True, on_delete=models.SET_NULL, blank=True)
    actor_device = models.ForeignKey('FHIR_Device', related_name="encounter_participant_actor_device", null=True, on_delete=models.SET_NULL, blank=True)
    actor_healthcareService = models.ForeignKey('FHIR_HealthcareService', related_name="encounter_participant_actor_healthcareService", null=True, on_delete=models.SET_NULL, blank=True)

class FHIR_Encounter_Participant_Type(models.Model):
    encounter_participant = models.ForeignKey(FHIR_Encounter_Participant, on_delete=models.CASCADE, related_name='participant_types')
    BINDING_RULE_PARTICIPANT_TYPE = 'todo'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, related_name='encounter_participant', limit_choices_to={'codings__binding_rule': BINDING_RULE_PARTICIPANT_TYPE})
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_Encounter_VirtualServiceDetail(FHIR_meta_VirtualServiceDetail):
    encounter = models.ForeignKey(FHIR_Encounter, on_delete=models.CASCADE, related_name='virtualServiceDetails')

class FHIR_Encounter_Reason(models.Model):
    encounter = models.ForeignKey(FHIR_Encounter, on_delete=models.CASCADE, related_name='reasons')

class FHIR_Encounter_Reason_Use(models.Model):
    encounter_reason = models.ForeignKey(FHIR_Encounter_Reason, on_delete=models.CASCADE, related_name='reason_uses')
    BINDING_RULE_REASON_USE = 'todo'
    use_cc = models.ManyToManyField(FHIR_GP_Coding, related_name='encounter_reason_use', limit_choices_to={'codings__binding_rule': BINDING_RULE_REASON_USE})
    use_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_Encounter_Reason_Value(models.Model):
    encounter_reason = models.ForeignKey(FHIR_Encounter_Reason, on_delete=models.CASCADE, related_name='reason_values')

    BINDING_RULE_REASON_VALUE_CONDITION = 'todo'
    value_condition_cc = models.ManyToManyField(FHIR_GP_Coding, related_name='encounter_reason_value_condition', limit_choices_to={'codings__binding_rule': BINDING_RULE_REASON_VALUE_CONDITION })
    value_condition_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value_condition_ref = models.ForeignKey('FHIR_Condition', on_delete=models.CASCADE, related_name='encounter_reason', null=True, blank=True)

    BINDING_RULE_REASON_VALUE_DIAGNOSTICREPORT = 'todo'
    value_diagnosticReport_cc = models.ManyToManyField(FHIR_GP_Coding, related_name='encounter_reason_value_diagnosticreport', limit_choices_to={'codings__binding_rule': BINDING_RULE_REASON_VALUE_DIAGNOSTICREPORT })
    value_diagnosticReport_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value_diagnosticReport_ref = models.ForeignKey('FHIR_DiagnosticReport', on_delete=models.CASCADE, related_name='encounter_reason', null=True, blank=True)

    BINDING_RULE_REASON_VALUE_OBSERVATION = 'todo'
    value_observation_cc = models.ManyToManyField(FHIR_GP_Coding, related_name='encounter_reason_value_observation', limit_choices_to={'codings__binding_rule': BINDING_RULE_REASON_VALUE_OBSERVATION })
    value_observation_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value_observation_ref = models.ForeignKey('FHIR_Observation', on_delete=models.CASCADE, related_name='encounter_reason', null=True, blank=True)

    BINDING_RULE_REASON_VALUE_IMMUNIZATIONRECOMMENDATION = 'todo'
    value_immunizationRecommendation_cc = models.ManyToManyField(FHIR_GP_Coding, related_name='encounter_reason_value_immunization', limit_choices_to={'codings__binding_rule': BINDING_RULE_REASON_VALUE_IMMUNIZATIONRECOMMENDATION })
    value_immunizationRecommendation_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value_immunizationRecommendation_ref = models.ForeignKey('FHIR_ImmunizationRecommendation', on_delete=models.CASCADE, related_name='encounter_reason', null=True, blank=True)

    BINDING_RULE_REASON_VALUE_PROCEDURE = 'todo'
    value_procedure_cc = models.ManyToManyField(FHIR_GP_Coding, related_name='encounter_reason_value_procedure', limit_choices_to={'codings__binding_rule': BINDING_RULE_REASON_VALUE_PROCEDURE })
    value_procedure_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value_procedure_ref = models.ForeignKey('FHIR_Procedure', on_delete=models.CASCADE, related_name='encounter_reason', null=True, blank=True)

class FHIR_Encounter_Diagnosis(models.Model):
    encounter = models.ForeignKey(FHIR_Encounter, on_delete=models.CASCADE, related_name='diagnoses')

class FHIR_Encounter_Diagnosis_Condition(models.Model):
    encounter_diagnosis = models.ForeignKey(FHIR_Encounter_Diagnosis, on_delete=models.CASCADE, related_name='condition')
    BINDING_RULE_DIAGNOSIS_CONDITION = 'todo'
    condition_cc = models.ManyToManyField(FHIR_GP_Coding, related_name='encounter_diagnosis_condition', limit_choices_to={'codings__binding_rule': BINDING_RULE_DIAGNOSIS_CONDITION })
    condition_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    condition_ref = models.ForeignKey('FHIR_Condition', on_delete=models.CASCADE, related_name='encounter_diagnosis', null=True, blank=True)

class FHIR_Encounter_Diagnosis_Use(models.Model):
    encounter_diagnosis = models.ForeignKey(FHIR_Encounter_Diagnosis, on_delete=models.CASCADE, related_name='use')
    BINDING_RULE_DIAGNOSIS_USE = 'todo'
    use_cc = models.ManyToManyField(FHIR_GP_Coding, related_name='encounter_diagnosis_use', limit_choices_to={'codings__binding_rule': BINDING_RULE_DIAGNOSIS_USE })
    use_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_Encounter_DietPreference(models.Model):
    encounter = models.ForeignKey(FHIR_Encounter, on_delete=models.CASCADE, related_name='dietPreferences')
    BINDING_RULE_DIET_PREFERENCE = 'todo'
    dietPreference_cc = models.ManyToManyField(FHIR_GP_Coding, related_name='encounter_dietPreference', limit_choices_to={'codings__binding_rule': BINDING_RULE_DIET_PREFERENCE })
    dietPreference_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_Encounter_SpecialArrangement(models.Model):
    encounter = models.ForeignKey(FHIR_Encounter, on_delete=models.CASCADE, related_name='specialArrangements')
    BINDING_RULE_SPECIAL_ARRANGEMENT = 'todo'
    specialArrangement_cc = models.ManyToManyField(FHIR_GP_Coding, related_name='encounter_specialArrangement', limit_choices_to={'codings__binding_rule': BINDING_RULE_SPECIAL_ARRANGEMENT })
    specialArrangement_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_Encounter_SpecialCourtesy(models.Model):
    encounter = models.ForeignKey(FHIR_Encounter, on_delete=models.CASCADE, related_name='specialCourtesies')
    BINDING_RULE_SPECIAL_COURTESY = 'todo'
    specialCourtesy_cc = models.ManyToManyField(FHIR_GP_Coding, related_name='encounter_specialCourtesy', limit_choices_to={'codings__binding_rule': BINDING_RULE_SPECIAL_COURTESY })
    specialCourtesy_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

