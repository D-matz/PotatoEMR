#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Appointment(models.Model):
    class StatusChoices(models.TextChoices): PROPOSED = 'proposed', 'Proposed'; PENDING = 'pending', 'Pending'; BOOKED = 'booked', 'Booked'; ARRIVED = 'arrived', 'Arrived'; FULFILLED = 'fulfilled', 'Fulfilled'; CANCELLED = 'cancelled', 'Cancelled'; NOSHOW = 'noshow', 'Noshow'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; CHECKED_IN = 'checked-in', 'Checked-in'; WAITLIST = 'waitlist', 'Waitlist'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    BINDING_cancellationReason = 'TODO'
    cancellationReason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_cancellationReason}, related_name='Appointment_cancellationReason', blank=True)
    cancellationReason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_appointmentType = 'TODO'
    appointmentType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_appointmentType}, related_name='Appointment_appointmentType', blank=True)
    appointmentType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_priority = 'TODO'
    priority_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_priority}, related_name='Appointment_priority', blank=True)
    priority_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    description = FHIR_primitive_StringField(null=True, blank=True, )
    replaces = models.ManyToManyField("FHIR_Appointment", related_name="Appointment_replaces", blank=True)
    previousAppointment = models.ForeignKey("FHIR_Appointment", related_name="Appointment_previousAppointment", null=True, blank=True, on_delete=models.SET_NULL)
    originatingAppointment = models.ForeignKey("FHIR_Appointment", related_name="Appointment_originatingAppointment", null=True, blank=True, on_delete=models.SET_NULL)
    start = FHIR_primitive_InstantField(null=True, blank=True, )
    end = FHIR_primitive_InstantField(null=True, blank=True, )
    minutesDuration = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    slot = models.ManyToManyField("FHIR_Slot", related_name="Appointment_slot", blank=True)
    account = models.ManyToManyField("FHIR_Account", related_name="Appointment_account", blank=True)
    created = FHIR_primitive_DateTimeField(null=True, blank=True, )
    cancellationDate = FHIR_primitive_DateTimeField(null=True, blank=True, )
    basedOn_CarePlan = models.ManyToManyField("FHIR_CarePlan", related_name="Appointment_basedOn", blank=True)
    basedOn_DeviceRequest = models.ManyToManyField("FHIR_DeviceRequest", related_name="Appointment_basedOn", blank=True)
    basedOn_MedicationRequest = models.ManyToManyField("FHIR_MedicationRequest", related_name="Appointment_basedOn", blank=True)
    basedOn_ServiceRequest = models.ManyToManyField("FHIR_ServiceRequest", related_name="Appointment_basedOn", blank=True)
    basedOn_RequestOrchestration = models.ManyToManyField("FHIR_RequestOrchestration", related_name="Appointment_basedOn", blank=True)
    basedOn_NutritionOrder = models.ManyToManyField("FHIR_NutritionOrder", related_name="Appointment_basedOn", blank=True)
    basedOn_VisionPrescription = models.ManyToManyField("FHIR_VisionPrescription", related_name="Appointment_basedOn", blank=True)
    basedOn_ImmunizationRecommendation = models.ManyToManyField("FHIR_ImmunizationRecommendation", related_name="Appointment_basedOn", blank=True)
    subject_Patient = models.ForeignKey("FHIR_Patient", related_name="Appointment_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Group = models.ForeignKey("FHIR_Group", related_name="Appointment_subject", null=True, blank=True, on_delete=models.SET_NULL)
    recurrenceId = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    occurrenceChanged = FHIR_primitive_BooleanField(null=True, blank=True, )

class FHIR_Appointment_identifier(FHIR_GP_Identifier):
    Appointment = models.ForeignKey(FHIR_Appointment, related_name='Appointment_identifier', null=False, on_delete=models.CASCADE)

class FHIR_Appointment_class(models.Model):
    Appointment = models.ForeignKey(FHIR_Appointment, related_name='Appointment_class', null=False, on_delete=models.CASCADE)
    BINDING_class = 'TODO'
    class_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_class}, related_name='Appointment_class', blank=True)
    class_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Appointment_serviceCategory(models.Model):
    Appointment = models.ForeignKey(FHIR_Appointment, related_name='Appointment_serviceCategory', null=False, on_delete=models.CASCADE)
    BINDING_serviceCategory = 'TODO'
    serviceCategory_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_serviceCategory}, related_name='Appointment_serviceCategory', blank=True)
    serviceCategory_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Appointment_serviceType(models.Model):
    Appointment = models.ForeignKey(FHIR_Appointment, related_name='Appointment_serviceType', null=False, on_delete=models.CASCADE)
    BINDING_serviceType = 'TODO'
    serviceType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_serviceType}, related_name='Appointment_serviceType', blank=True)
    serviceType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    serviceType_HealthcareService_ref = models.ForeignKey("FHIR_HealthcareService", related_name="Appointment_serviceType_HealthcareService", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Appointment_specialty(models.Model):
    Appointment = models.ForeignKey(FHIR_Appointment, related_name='Appointment_specialty', null=False, on_delete=models.CASCADE)
    BINDING_specialty = 'TODO'
    specialty_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_specialty}, related_name='Appointment_specialty', blank=True)
    specialty_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Appointment_reason(models.Model):
    Appointment = models.ForeignKey(FHIR_Appointment, related_name='Appointment_reason', null=False, on_delete=models.CASCADE)
    BINDING_reason = 'TODO'
    reason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_reason}, related_name='Appointment_reason', blank=True)
    reason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    reason_Condition_ref = models.ForeignKey("FHIR_Condition", related_name="Appointment_reason_Condition", null=True, blank=True, on_delete=models.SET_NULL)
    reason_DiagnosticReport_ref = models.ForeignKey("FHIR_DiagnosticReport", related_name="Appointment_reason_DiagnosticReport", null=True, blank=True, on_delete=models.SET_NULL)
    reason_Procedure_ref = models.ForeignKey("FHIR_Procedure", related_name="Appointment_reason_Procedure", null=True, blank=True, on_delete=models.SET_NULL)
    reason_Observation_ref = models.ForeignKey("FHIR_Observation", related_name="Appointment_reason_Observation", null=True, blank=True, on_delete=models.SET_NULL)
    reason_ImmunizationRecommendation_ref = models.ForeignKey("FHIR_ImmunizationRecommendation", related_name="Appointment_reason_ImmunizationRecommendation", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Appointment_virtualService(FHIR_meta_VirtualServiceDetail):
    Appointment = models.ForeignKey(FHIR_Appointment, related_name='Appointment_virtualService', null=False, on_delete=models.CASCADE)

class FHIR_Appointment_requestedPeriod(FHIR_GP_Period):
    Appointment = models.ForeignKey(FHIR_Appointment, related_name='Appointment_requestedPeriod', null=False, on_delete=models.CASCADE)

class FHIR_Appointment_note(FHIR_GP_Annotation):
    Appointment = models.ForeignKey(FHIR_Appointment, related_name='Appointment_note', null=False, on_delete=models.CASCADE)

class FHIR_Appointment_patientInstruction(models.Model):
    Appointment = models.ForeignKey(FHIR_Appointment, related_name='Appointment_patientInstruction', null=False, on_delete=models.CASCADE)
    BINDING_patientInstruction = 'TODO'
    patientInstruction_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_patientInstruction}, related_name='Appointment_patientInstruction', blank=True)
    patientInstruction_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    patientInstruction_DocumentReference_ref = models.ForeignKey("FHIR_DocumentReference", related_name="Appointment_patientInstruction_DocumentReference", null=True, blank=True, on_delete=models.SET_NULL)
    patientInstruction_Binary_ref = models.ForeignKey("FHIR_Binary", related_name="Appointment_patientInstruction_Binary", null=True, blank=True, on_delete=models.SET_NULL)
    patientInstruction_Communication_ref = models.ForeignKey("FHIR_Communication", related_name="Appointment_patientInstruction_Communication", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Appointment_participant(models.Model):
    Appointment = models.ForeignKey(FHIR_Appointment, related_name='Appointment_participant', null=False, on_delete=models.CASCADE)
    period = models.OneToOneField("FHIR_GP_Period", related_name='Appointment_participant_period', null=True, blank=True, on_delete=models.SET_NULL)
    actor_Patient = models.ForeignKey("FHIR_Patient", related_name="Appointment_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Group = models.ForeignKey("FHIR_Group", related_name="Appointment_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="Appointment_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="Appointment_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_CareTeam = models.ForeignKey("FHIR_CareTeam", related_name="Appointment_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="Appointment_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Device = models.ForeignKey("FHIR_Device", related_name="Appointment_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_HealthcareService = models.ForeignKey("FHIR_HealthcareService", related_name="Appointment_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Location = models.ForeignKey("FHIR_Location", related_name="Appointment_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)
    required = FHIR_primitive_BooleanField(null=True, blank=True, )
    class StatusChoices(models.TextChoices): ACCEPTED = 'accepted', 'Accepted'; DECLINED = 'declined', 'Declined'; TENTATIVE = 'tentative', 'Tentative'; NEEDS_ACTION = 'needs-action', 'Needs-action'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )

class FHIR_Appointment_participant_type(models.Model):
    Appointment_participant = models.ForeignKey(FHIR_Appointment_participant, related_name='Appointment_participant_type', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Appointment_participant_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Appointment_recurrenceTemplate(models.Model):
    Appointment = models.ForeignKey(FHIR_Appointment, related_name='Appointment_recurrenceTemplate', null=False, on_delete=models.CASCADE)
    BINDING_timezone = 'TODO'
    timezone_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_timezone}, related_name='Appointment_recurrenceTemplate_timezone', blank=True)
    timezone_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_recurrenceType = 'TODO'
    recurrenceType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_recurrenceType}, related_name='Appointment_recurrenceTemplate_recurrenceType', blank=True)
    recurrenceType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    lastOccurrenceDate = FHIR_primitive_DateField(null=True, blank=True, )
    occurrenceCount = FHIR_primitive_PositiveIntField(null=True, blank=True, )

class FHIR_Appointment_recurrenceTemplate_occurrenceDate(models.Model):
    Appointment_recurrenceTemplate = models.ForeignKey(FHIR_Appointment_recurrenceTemplate, related_name='Appointment_recurrenceTemplate_occurrenceDate', null=False, on_delete=models.CASCADE)
    
    occurrenceDate = FHIR_primitive_DateField(null=True, blank=True, )
    
class FHIR_Appointment_recurrenceTemplate_weeklyTemplate(models.Model):
    Appointment_recurrenceTemplate = models.ForeignKey(FHIR_Appointment_recurrenceTemplate, related_name='Appointment_recurrenceTemplate_weeklyTemplate', null=False, on_delete=models.CASCADE)
    monday = FHIR_primitive_BooleanField(null=True, blank=True, )
    tuesday = FHIR_primitive_BooleanField(null=True, blank=True, )
    wednesday = FHIR_primitive_BooleanField(null=True, blank=True, )
    thursday = FHIR_primitive_BooleanField(null=True, blank=True, )
    friday = FHIR_primitive_BooleanField(null=True, blank=True, )
    saturday = FHIR_primitive_BooleanField(null=True, blank=True, )
    sunday = FHIR_primitive_BooleanField(null=True, blank=True, )
    weekInterval = FHIR_primitive_PositiveIntField(null=True, blank=True, )

class FHIR_Appointment_recurrenceTemplate_monthlyTemplate(models.Model):
    Appointment_recurrenceTemplate = models.ForeignKey(FHIR_Appointment_recurrenceTemplate, related_name='Appointment_recurrenceTemplate_monthlyTemplate', null=False, on_delete=models.CASCADE)
    dayOfMonth = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    nthWeekOfMonth = models.OneToOneField("FHIR_GP_Coding", related_name='Appointment_recurrenceTemplate_monthlyTemplate_nthWeekOfMonth', null=True, blank=True, on_delete=models.SET_NULL)
    dayOfWeek = models.OneToOneField("FHIR_GP_Coding", related_name='Appointment_recurrenceTemplate_monthlyTemplate_dayOfWeek', null=True, blank=True, on_delete=models.SET_NULL)
    monthInterval = FHIR_primitive_PositiveIntField(null=True, blank=True, )

class FHIR_Appointment_recurrenceTemplate_yearlyTemplate(models.Model):
    Appointment_recurrenceTemplate = models.ForeignKey(FHIR_Appointment_recurrenceTemplate, related_name='Appointment_recurrenceTemplate_yearlyTemplate', null=False, on_delete=models.CASCADE)
    yearInterval = FHIR_primitive_PositiveIntField(null=True, blank=True, )

class FHIR_Appointment_recurrenceTemplate_excludingDate(models.Model):
    Appointment_recurrenceTemplate = models.ForeignKey(FHIR_Appointment_recurrenceTemplate, related_name='Appointment_recurrenceTemplate_excludingDate', null=False, on_delete=models.CASCADE)
    
    excludingDate = FHIR_primitive_DateField(null=True, blank=True, )
    
class FHIR_Appointment_recurrenceTemplate_excludingRecurrenceId(models.Model):
    Appointment_recurrenceTemplate = models.ForeignKey(FHIR_Appointment_recurrenceTemplate, related_name='Appointment_recurrenceTemplate_excludingRecurrenceId', null=False, on_delete=models.CASCADE)
    
    excludingRecurrenceId = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    