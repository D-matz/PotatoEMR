
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_AppointmentResponse(models.Model):
    appointment = models.ForeignKey("FHIR_Appointment", related_name="AppointmentResponse_appointment", null=True, blank=True, on_delete=models.SET_NULL)
    proposedNewTime = FHIR_primitive_BooleanField(null=True, blank=True, )
    start = FHIR_primitive_InstantField(null=True, blank=True, )
    end = FHIR_primitive_InstantField(null=True, blank=True, )
    actor_Patient = models.ForeignKey("FHIR_Patient", related_name="AppointmentResponse_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Group = models.ForeignKey("FHIR_Group", related_name="AppointmentResponse_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="AppointmentResponse_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="AppointmentResponse_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="AppointmentResponse_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Device = models.ForeignKey("FHIR_Device", related_name="AppointmentResponse_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_HealthcareService = models.ForeignKey("FHIR_HealthcareService", related_name="AppointmentResponse_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Location = models.ForeignKey("FHIR_Location", related_name="AppointmentResponse_actor", null=True, blank=True, on_delete=models.SET_NULL)
    class ParticipantstatusChoices(models.TextChoices): ACCEPTED = 'accepted', 'Accepted'; DECLINED = 'declined', 'Declined'; TENTATIVE = 'tentative', 'Tentative'; NEEDS_ACTION = 'needs-action', 'Needs-action'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; 
    participantStatus = FHIR_primitive_CodeField(choices=ParticipantstatusChoices.choices, null=True, blank=True, )
    comment = FHIR_primitive_MarkdownField(null=True, blank=True, )
    recurring = FHIR_primitive_BooleanField(null=True, blank=True, )
    occurrenceDate = FHIR_primitive_DateField(null=True, blank=True, )
    recurrenceId = FHIR_primitive_PositiveIntField(null=True, blank=True, )

class FHIR_AppointmentResponse_identifier(FHIR_GP_Identifier):
    AppointmentResponse = models.ForeignKey(FHIR_AppointmentResponse, related_name='AppointmentResponse_identifier', null=False, on_delete=models.CASCADE)

class FHIR_AppointmentResponse_participantType(models.Model):
    AppointmentResponse = models.ForeignKey(FHIR_AppointmentResponse, related_name='AppointmentResponse_participantType', null=False, on_delete=models.CASCADE)
    BINDING_participantType = 'TODO'
    participantType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_participantType}, related_name='AppointmentResponse_participantType', blank=True)
    participantType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    