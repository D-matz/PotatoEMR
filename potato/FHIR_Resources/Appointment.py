# from django.db import models
# from ..FHIR_DataTypes.FHIR_generalpurpose import *
# from ..FHIR_DataTypes.FHIR_primitive import *

# class FHIR_Appointment(models.Model):
#     #Identifier ForeignKey to this, related_name=appointment_identifiers
#     class StatusChoices(models.TextChoices): PROPOSED = 'proposed', 'Proposed'; PENDING = 'pending', 'Pending'; BOOKED = 'booked', 'Booked'; ARRIVED = 'arrived', 'Arrived'; FULFILLED = 'fulfilled', 'Fulfilled'; CANCELLED = 'cancelled', 'Cancelled'; NOSHOW = 'noshow', 'No Show'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered in Error'; CHECKED_IN = 'checked-in', 'Checked In'; WAITLIST = 'waitlist', 'Waitlist'
#     status = FHIR_primitive_CodeField(max_length=16, choices=StatusChoices.choices, null=True)

#     cancellationReason_cc = models.ManyToManyField(FHIR_GP_Coding, related_name="appointment_cancellationReason",
#                                             limit_choices_to={'binding__binding_rule': 'https://www.hl7.org/fhir/valueset-appointment-cancellation-reason.html'})
#     cancellationReason_cctext = FHIR_primitive_StringField(max_length=255, null=True, blank=True)

#     #Class ForeignKey to this, related_name = appointment_classes
#     #ServiceCategory ForeignKey to this, related_name = appointment_ServiceCategorys
#     #Specialty ForeignKey to this, related_name = appointment_specialty

#     appointmentType_cc = models.ManyToManyField(FHIR_GP_Coding, related_name="appointment_appointmentType",
#                                             limit_choices_to={'binding__binding_rule': 'https://www.hl7.org/fhir/valueset-appointment-type.html'})
#     appointmentType_cctext = FHIR_primitive_StringField(max_length=255, null=True, blank=True)

#     #reason ForeignKey to this, related_name = appointment_reason

#     priority_cc = models.ManyToManyField(FHIR_GP_Coding, related_name="appointment_priority",
#                                             limit_choices_to={'binding__binding_rule': 'https://www.hl7.org/fhir/valueset-appointment-priority.html'})
#     priority_cctext = FHIR_primitive_StringField(max_length=255, null=True, blank=True)

#     description = FHIR_primitive_StringField(max_length=1024, null=True, blank=True)

#     #replaces ForeignKey to this, related_name = appointment_replaces
#     #virtualService ForeignKey to this, related_name = appointment_virtualService
#     #supportingInformation ForeignKey to this, related_name = appointment_supportingInformation
    
#     previousAppointment = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name="previous_appointment")
#     originatingAppointment = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name="originating_appointment")

#     start = FHIR_primitive_InstantField(max_length=64, null=True, blank=True)
#     end = FHIR_primitive_InstantField(max_length=64, null=True, blank=True)
#     minutesDuration = FHIR_primitive_PositiveIntField(null=True, blank=True)

#     #requestedPeriod ForeignKey to this, related_name = appointment_requestedPeriod
#     #slot ForeignKey to this, related_name = appointment_slot
#     #account ForeignKey to this, related_name = appointment_account

#     created = FHIR_primitive_DateTimeField(null=True, blank=True)
#     cancellationDate = FHIR_primitive_DateTimeField(null=True, blank=True)

#     #note ForeignKey to this, related_name = appointment_note
#     #patientInstruction ForeignKey to this, related_name = appointmnet_patientInstruction
#     #basedOn foreignKey to this, related_name = appointment_basdOn

#     subject_patient = models.ForeignKey('FHIR_GP_Patient', null=True, on_delete=models.SET_NULL)
#     subject_group = models.ForeignKey('FHIR_GP_Patient', null=True, on_delete=models.SET_NULL)

#     #participant foreign key to this

#     recurrenceId = FHIR_primitive_PositiveIntField(null=True, blank=True)
#     occurrenceChanged = FHIR_primitive_BooleanField(null=True, blank=True)

#     #recurrenceTemplate foreign key to this


# class FHIR_Appointment_Identifier(FHIR_GP_Identifier):
#     appointment = models.ForeignKey(FHIR_Appointment, related_name="appointment_identifiers", on_delete=models.CASCADE)

# class FHIR_Appointment_Class(models.Model):
#     appointment = models.ForeignKey(FHIR_Appointment, related_name="appointment_classes", on_delete=models.CASCADE)


# class FHIR_Appointment_Participant(models.Model):
#     class StatusChoices(models.TextChoices): 
#         ACCEPTED = 'accepted', 'Accepted'
#         DECLINED = 'declined', 'Declined'
#         TENTATIVE = 'tentative', 'Tentative'
#         NEEDS_ACTION = 'needs-action', 'Needs Action'
    
#     appointment = models.ForeignKey(FHIR_Appointment, on_delete=models.CASCADE, related_name="participants")
#     status = FHIR_primitive_CodeField(max_length=16, choices=StatusChoices.choices)
#     required = FHIR_primitive_BooleanField(null=True, blank=True)
#     period = models.OneToOneField(FHIR_GP_Period, null=True, blank=True, on_delete=models.CASCADE)
    
#     # Type is a CodeableConcept
#     type_cc = models.ManyToManyField(FHIR_GP_Coding, related_name="participant_type", blank=True,
#                                     limit_choices_to={'binding__binding_rule': 'https://www.hl7.org/fhir/valueset-participant-type.html'})
#     type_cctext = FHIR_primitive_StringField(max_length=255, null=True, blank=True)
    
#     # Actor references
#     actor_patient_foreignKey = models.ForeignKey('FHIR_Patient', null=True, blank=True, on_delete=models.SET_NULL, related_name="appointments_as_participant")
#     actor_group_foreignKey = models.ForeignKey('FHIR_Group', null=True, blank=True, on_delete=models.SET_NULL, related_name="appointments_as_participant")
#     actor_practitioner_foreignKey = models.ForeignKey('FHIR_Practitioner', null=True, blank=True, on_delete=models.SET_NULL, related_name="appointments_as_participant")
#     actor_practitionerRole_foreignKey = models.ForeignKey('FHIR_PractitionerRole', null=True, blank=True, on_delete=models.SET_NULL, related_name="appointments_as_participant")
#     actor_careTeam_foreignKey = models.ForeignKey('FHIR_CareTeam', null=True, blank=True, on_delete=models.SET_NULL, related_name="appointments_as_participant")
#     actor_relatedPerson_foreignKey = models.ForeignKey('FHIR_RelatedPerson', null=True, blank=True, on_delete=models.SET_NULL, related_name="appointments_as_participant")
#     actor_device_foreignKey = models.ForeignKey('FHIR_Device', null=True, blank=True, on_delete=models.SET_NULL, related_name="appointments_as_participant")
#     actor_healthcareService_foreignKey = models.ForeignKey('FHIR_HealthcareService', null=True, blank=True, on_delete=models.SET_NULL, related_name="appointments_as_participant")
#     actor_location_foreignKey = models.ForeignKey('FHIR_Location', null=True, blank=True, on_delete=models.SET_NULL, related_name="appointments_as_participant")
    
