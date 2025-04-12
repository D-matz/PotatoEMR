from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Appointment(models.Model):
    #Identifier ForeignKey to this, related_name=appointment_identifiers
    class StatusChoices(models.TextChoices): PROPOSED = 'proposed', 'Proposed'; PENDING = 'pending', 'Pending'; BOOKED = 'booked', 'Booked'; ARRIVED = 'arrived', 'Arrived'; FULFILLED = 'fulfilled', 'Fulfilled'; CANCELLED = 'cancelled', 'Cancelled'; NOSHOW = 'noshow', 'No Show'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered in Error'; CHECKED_IN = 'checked-in', 'Checked In'; WAITLIST = 'waitlist', 'Waitlist'
    status = FHIR_primitive_CodeField(max_length=16, choices=StatusChoices.choices, null=True)

    BINDING_RULE_CANCELLATIONREASON = "https://www.hl7.org/fhir/valueset-appointment-cancellation-reason.html"
    cancellationReason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={'codings__binding_rule': BINDING_RULE_CANCELLATIONREASON}, related_name="appointment_cancellationReason")
    cancellationReason_cctext = FHIR_primitive_StringField(max_length=255, null=True, blank=True)

    #Class ForeignKey to this, related_name = appointment_classes
    #ServiceCategory ForeignKey to this, related_name = appointment_ServiceCategorys
    #ServiceType foreignKey to this
    #Specialty ForeignKey to this, related_name = appointment_specialty

    BINDING_RULE_IDK = "??"
    appointmentType_cc = models.ManyToManyField(FHIR_GP_Coding, related_name="appointment_appointmentType", limit_choices_to={'codings__binding_rule': BINDING_RULE_IDK })
    appointmentType_cctext = FHIR_primitive_StringField(max_length=255, null=True, blank=True)

    #reason ForeignKey to this, related_name = appointment_reason

    BINDING_RULE_PRIORITY = 'https://www.hl7.org/fhir/valueset-appointment-priority.html'
    priority_cc = models.ManyToManyField(FHIR_GP_Coding, related_name="appointment_priority",
                                            limit_choices_to={'codings__binding_rule': BINDING_RULE_PRIORITY})
    priority_cctext = FHIR_primitive_StringField(max_length=255, null=True, blank=True)

    description = FHIR_primitive_StringField(max_length=1024, null=True, blank=True)

    replaces = models.ManyToManyField("self", blank=True, symmetrical=False)
    #virtualService ForeignKey to this, related_name = appointment_virtualService
    #supportingInformation IDK not implemented TODO (should be key to any resource, but maybe generic bad idea)

    previousAppointment = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name="previous_appointment")
    originatingAppointment = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name="originating_appointment")

    start = FHIR_primitive_InstantField(max_length=64, null=True, blank=True)
    end = FHIR_primitive_InstantField(max_length=64, null=True, blank=True)
    minutesDuration = FHIR_primitive_PositiveIntField(null=True, blank=True)

    #requestedPeriod ForeignKey to this, related_name = appointment_requestedPeriod
    #slot ForeignKey to this, related_name = appointment_slot
    #account ForeignKey to this, related_name = appointment_account

    created = FHIR_primitive_DateTimeField(null=True, blank=True)
    cancellationDate = FHIR_primitive_DateTimeField(null=True, blank=True)

    #note ForeignKey to this, related_name = appointment_note
    #patientInstruction ForeignKey to this, related_name = appointmnet_patientInstruction
    #basedOn foreignKey to this, related_name = appointment_basdOn

    subject_patient = models.ForeignKey('FHIR_Patient', related_name="subject_group", null=True, on_delete=models.SET_NULL)
    subject_group = models.ForeignKey('FHIR_Patient', related_name="subject_patient", null=True, on_delete=models.SET_NULL)

    #participant foreign key to this

    recurrenceId = FHIR_primitive_PositiveIntField(null=True, blank=True)
    occurrenceChanged = FHIR_primitive_BooleanField(null=True, blank=True)

    #recurrenceTemplate foreign key to this


class FHIR_Appointment_Identifier(FHIR_GP_Identifier):
    appointment = models.ForeignKey(FHIR_Appointment, related_name="appointment_identifiers", on_delete=models.CASCADE)

class FHIR_Appointment_Class(models.Model):
    appointment = models.ForeignKey(FHIR_Appointment, related_name="appointment_classes", on_delete=models.CASCADE)
    BINDING_RULE_CLASS = "??"
    class_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={'codings__binding_rule': BINDING_RULE_CLASS })
    class_cctext = FHIR_primitive_StringField(max_length=255, null=True, blank=True)


class FHIR_Appointment_ServiceCategory(models.Model):
    appointment = models.ForeignKey(FHIR_Appointment, related_name="appointment_ServiceCategorys", on_delete=models.CASCADE)
    BINDING_RULE_CLASS = "??"
    serviceCategory_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={'codings__binding_rule': BINDING_RULE_CLASS })
    serviceCategory_cctext = FHIR_primitive_StringField(max_length=255, null=True, blank=True)

class FHIR_Appointment_ServiceType(models.Model):
    appointment = models.ForeignKey(FHIR_Appointment, related_name="appointment_ServiceTypes", on_delete=models.CASCADE)
    BINDING_RULE_CLASS = "??"
    serviceType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={'codings__binding_rule': BINDING_RULE_CLASS })
    serviceType_cctext = FHIR_primitive_StringField(max_length=255, null=True, blank=True)
    serviceType_ref = models.ForeignKey('FHIR_HealthcareService', related_name="appointments_serviceType_healthcareService", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Appointment_Specialty(models.Model):
    appointment = models.ForeignKey(FHIR_Appointment, related_name="appointment_specialty", on_delete=models.CASCADE)
    BINDING_RULE_CLASS = "??"
    specialty_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={'codings__binding_rule': BINDING_RULE_CLASS })
    specialty_cctext = FHIR_primitive_StringField(max_length=255, null=True, blank=True)

class FHIR_Appointment_Reason(models.Model):
    appointment = models.ForeignKey(FHIR_Appointment, related_name="appointment_reason", on_delete=models.CASCADE)
    BINDING_RULE_REASON = "??"
    reason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={'codings__binding_rule': BINDING_RULE_REASON })
    reason_cctext = FHIR_primitive_StringField(max_length=255, null=True, blank=True)
    reason_condition = models.ForeignKey('FHIR_Condition', related_name="reason_conditions", null=True, on_delete=models.SET_NULL)
    reason_diagnosticReport = models.ForeignKey('FHIR_DiagnosticReport', related_name="reason_diagnostic_reports", null=True, on_delete=models.SET_NULL)
    reason_procedure = models.ForeignKey('FHIR_Procedure', related_name="reason_procedures", null=True, on_delete=models.SET_NULL)
    reason_observation = models.ForeignKey('FHIR_Observation', related_name="reason_observations", null=True, on_delete=models.SET_NULL)
    reason_immunizationReccommendation = models.ForeignKey('FHIR_ImmunizationRecommendation', related_name="reason_immunization_recommendations", null=True, on_delete=models.SET_NULL)

class FHIR_Appointment_VirtualService(models.Model):
    appointment = models.ForeignKey(FHIR_Appointment, related_name="appointment_virtualService", on_delete=models.CASCADE)
    BINDING_RULE_VIRTUALSERVICE = "??"
    virtualService_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={'codings__binding_rule': BINDING_RULE_VIRTUALSERVICE })
    virtualService_cctext = FHIR_primitive_StringField(max_length=255, null=True, blank=True)

class FHIR_Appointment_Slot(models.Model):
    appointment = models.ForeignKey(FHIR_Appointment, related_name="appointment_slot", on_delete=models.CASCADE)
    BINDING_RULE_SLOT = "??"
    slot_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={'codings__binding_rule': BINDING_RULE_SLOT})
    slot_cctext = FHIR_primitive_StringField(max_length=255, null=True, blank=True)

class FHIR_Appointment_Account(models.Model):
    appointment = models.ForeignKey(FHIR_Appointment, related_name="appointment_account", on_delete=models.CASCADE)
    BINDING_RULE_ACCOUNT = "??"
    account_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={'codings__binding_rule': BINDING_RULE_ACCOUNT})
    account_cctext = FHIR_primitive_StringField(max_length=255, null=True, blank=True)

class FHIR_Appointment_Note(FHIR_GP_Annotation):
    appointment = models.ForeignKey(FHIR_Appointment, on_delete=models.CASCADE, related_name='notes')

class FHIR_Appointment_PatientInstruction(models.Model):
    appointment = models.ForeignKey(FHIR_Appointment, related_name="appointment_patientInstruction", on_delete=models.CASCADE)
    BINDING_RULE_PATIENT_INSTRUCTION = "??"
    instruction_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={'codings__binding_rule': BINDING_RULE_PATIENT_INSTRUCTION })
    instruction_cctext = FHIR_primitive_StringField(max_length=255, null=True, blank=True)
    instruction_documentReference = models.ForeignKey('FHIR_DocumentReference', related_name="instruction_document_references", null=True, on_delete=models.SET_NULL)
    instruction_binary = models.ForeignKey('FHIR_Binary', related_name="instruction_binaries", null=True, on_delete=models.SET_NULL)
    instruction_communication = models.ForeignKey('FHIR_Communication', related_name="instruction_communications", null=True, on_delete=models.SET_NULL)

class FHIR_Appointment_BasedOn(models.Model):
    appointment = models.ForeignKey(FHIR_Appointment, related_name="appointment_basedOn", on_delete=models.CASCADE)
    BINDING_RULE_BASED_ON = "??"
    basedOn_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={'codings__binding_rule': BINDING_RULE_BASED_ON })
    basedOn_cctext = FHIR_primitive_StringField(max_length=255, null=True, blank=True)
    basedOn_carePlan = models.ForeignKey('FHIR_CarePlan', related_name="based_on_care_plans", null=True, on_delete=models.SET_NULL)
    basedOn_deviceRequest = models.ForeignKey('FHIR_DeviceRequest', related_name="based_on_device_requests", null=True, on_delete=models.SET_NULL)
    basedOn_medicationRequest = models.ForeignKey('FHIR_MedicationRequest', related_name="based_on_medication_requests", null=True, on_delete=models.SET_NULL)
    basedOn_serviceRequest = models.ForeignKey('FHIR_ServiceRequest', related_name="based_on_service_requests", null=True, on_delete=models.SET_NULL)
    basedOn_requestOrchestration = models.ForeignKey('FHIR_RequestOrchestration', related_name="based_on_request_orchestrations", null=True, on_delete=models.SET_NULL)
    basedOn_nutritionOrder = models.ForeignKey('FHIR_NutritionOrder', related_name="based_on_nutrition_orders", null=True, on_delete=models.SET_NULL)
    basedOn_visionPrescription = models.ForeignKey('FHIR_VisionPrescription', related_name="based_on_vision_prescriptions", null=True, on_delete=models.SET_NULL)
    basedOn_immunizationRecommendation = models.ForeignKey('FHIR_ImmunizationRecommendation', related_name="based_on_immunization_recommendations", null=True, on_delete=models.SET_NULL)

class FHIR_Appointment_Participant(models.Model):
    appointment = models.ForeignKey(FHIR_Appointment, related_name="appointment_participant", on_delete=models.CASCADE)
    #type foreignKey to this
    period = models.OneToOneField(FHIR_GP_Period, on_delete=models.CASCADE, null=True, blank=True)
    actor_patient = models.ForeignKey("FHIR_Patient", null=True, blank=True, on_delete=models.SET_NULL)
    actor_group = models.ForeignKey("FHIR_Group", null=True, blank=True, on_delete=models.SET_NULL)
    actor_practitioner = models.ForeignKey("FHIR_Practitioner", null=True, blank=True, on_delete=models.SET_NULL)
    actor_practitioner_role = models.ForeignKey("FHIR_PractitionerRole", null=True, blank=True, on_delete=models.SET_NULL)
    actor_care_team = models.ForeignKey("FHIR_CareTeam", null=True, blank=True, on_delete=models.SET_NULL)
    actor_related_person = models.ForeignKey("FHIR_RelatedPerson", null=True, blank=True, on_delete=models.SET_NULL)
    actor_device = models.ForeignKey("FHIR_Device", null=True, blank=True, on_delete=models.SET_NULL)
    actor_healthcare_service = models.ForeignKey("FHIR_HealthcareService", null=True, blank=True, on_delete=models.SET_NULL)
    actor_location = models.ForeignKey("FHIR_Location", null=True, blank=True, on_delete=models.SET_NULL)
    required = FHIR_primitive_BooleanField(null=True, blank=True)
    status = FHIR_primitive_CodeField()

class FHIR_Appointment_Participant_Type(models.Model):
    appointment_participant = models.ForeignKey(FHIR_Appointment_Participant, related_name="appointment_participant_type", on_delete=models.CASCADE)
    BINDING_RULE_TYPE = "??"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={'codings__binding_rule': BINDING_RULE_TYPE })
    type_cctext = FHIR_primitive_StringField(max_length=255, null=True, blank=True)

class FHIR_Appointment_RecurrenceTemplate(models.Model):
    appointment = models.ForeignKey(FHIR_Appointment, related_name="appointment_recurrence_templates", on_delete=models.CASCADE)
    BINDING_RULE_TIMEZONE = "IANA Timezones"
    timezone_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={'codings__binding_rule': BINDING_RULE_TIMEZONE}, related_name="recurrence_template_timezone", blank=True)
    timezone_cctext = FHIR_primitive_StringField(max_length=255, null=True, blank=True)
    BINDING_RULE_RECURRENCE_TYPE = "Appointment Recurrence Type"
    recurrenceType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={'codings__binding_rule': BINDING_RULE_RECURRENCE_TYPE}, related_name="recurrence_template_recurrence_type")
    recurrenceType_cctext = FHIR_primitive_StringField(max_length=255, null=True, blank=True)
    lastOccurrenceDate = FHIR_primitive_DateField(null=True, blank=True)
    occurrenceCount = FHIR_primitive_PositiveIntField(null=True, blank=True)
    # occurrenceDate foreign key to this
    # Weekly template fields
    monday = FHIR_primitive_BooleanField(null=True, blank=True)
    tuesday = FHIR_primitive_BooleanField(null=True, blank=True)
    wednesday = FHIR_primitive_BooleanField(null=True, blank=True)
    thursday = FHIR_primitive_BooleanField(null=True, blank=True)
    friday = FHIR_primitive_BooleanField(null=True, blank=True)
    saturday = FHIR_primitive_BooleanField(null=True, blank=True)
    sunday = FHIR_primitive_BooleanField(null=True, blank=True)
    weekInterval = FHIR_primitive_PositiveIntField(null=True, blank=True)
    # Monthly template fields
    dayOfMonth = FHIR_primitive_PositiveIntField(null=True, blank=True)
    BINDING_RULE_WEEK_OF_MONTH = "Week Of Month"
    nthWeekOfMonth = models.ForeignKey(FHIR_GP_Coding, limit_choices_to={'codings__binding_rule': BINDING_RULE_WEEK_OF_MONTH},
                                         related_name="nth_week_of_month", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_RULE_DAYS_OF_WEEK = "Days Of Week"
    dayOfWeek = models.ForeignKey(FHIR_GP_Coding, limit_choices_to={'codings__binding_rule': BINDING_RULE_DAYS_OF_WEEK},
                                    related_name="day_of_week", null=True, blank=True, on_delete=models.SET_NULL)
    monthInterval = FHIR_primitive_PositiveIntField(null=True, blank=True)
    # Yearly template fields
    yearInterval = FHIR_primitive_PositiveIntField(null=True, blank=True)

class FHIR_Appointment_RecurrenceTemplate_OccurrenceDate(models.Model):
    Appointment_RecurrenceTemplate = models.ForeignKey(FHIR_Appointment_RecurrenceTemplate, related_name="appointment_recurrence_template_occurrenceDate", on_delete=models.CASCADE)
    occurrenceDate = FHIR_primitive_DateField(null=True, blank=True)

class FHIR_Appointment_RecurrenceTemplate_ExcludingDate(models.Model):
    Appointment_RecurrenceTemplate = models.ForeignKey(FHIR_Appointment_RecurrenceTemplate, related_name="appointment_recurrence_template_excludingDate", on_delete=models.CASCADE)
    excludingDate = FHIR_primitive_DateField(null=True, blank=True)

class FHIR_Appointment_RecurrenceTemplate_ExcludingRecurrenceId(models.Model):
    Appointment_RecurrenceTemplate = models.ForeignKey(FHIR_Appointment_RecurrenceTemplate, related_name="appointment_recurrence_template_excludingRecurrenceId", on_delete=models.CASCADE)
    excludingRecurrenceId = FHIR_primitive_PositiveIntField(null=True, blank=True)
