from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *

class FHIR_Appointment(models.Model):
    #Identifier ForeignKey to this, related_name=appointment_identifiers
    class StatusChoices(models.TextChoices): PROPOSED = 'proposed', 'Proposed'; PENDING = 'pending', 'Pending'; BOOKED = 'booked', 'Booked'; ARRIVED = 'arrived', 'Arrived'; FULFILLED = 'fulfilled', 'Fulfilled'; CANCELLED = 'cancelled', 'Cancelled'; NOSHOW = 'noshow', 'No Show'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered in Error'; CHECKED_IN = 'checked-in', 'Checked In'; WAITLIST = 'waitlist', 'Waitlist'
    status = FHIR_primitive_CodeField(max_length=16, choices=StatusChoices.choices, null=True)

    cancellationReason_cc = models.ManyToManyField(FHIR_GP_Coding, related_name="appointment_cancellationReason",
                                            limit_choices_to={'binding__binding_rule': '????'})
    cancellationReason_cctext = FHIR_primitive_StringField(max_length=255, null=True, blank=True)

    #Class ForeignKey to this, related_name = appointment_classes
    #ServiceCategory ForeignKey to this, related_name = appointment_ServiceCategorys

#   serviceType codeablereference??

    #Specialty ForeignKey to this, related_name = appointment_specialty
