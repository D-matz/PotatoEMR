
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_MessageHeader(models.Model):
    event = models.OneToOneField("FHIR_GP_Coding", related_name='MessageHeader_event', null=True, blank=True, on_delete=models.SET_NULL)
    event = FHIR_primitive_URIField(null=True, blank=True, )
    event = FHIR_primitive_CanonicalField(null=True, blank=True, )
    BINDING_reason = 'TODO'
    reason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_reason}, related_name='MessageHeader_reason', blank=True)
    reason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    definition = FHIR_primitive_CanonicalField(null=True, blank=True, )

class FHIR_MessageHeader_destination(models.Model):
    MessageHeader = models.ForeignKey(FHIR_MessageHeader, related_name='MessageHeader_destination', null=False, on_delete=models.CASCADE)
    endpoint = FHIR_primitive_URLField(null=True, blank=True, )
    endpoint = models.ForeignKey("FHIR_Endpoint", related_name="MessageHeader_destination_endpoint", null=True, blank=True, on_delete=models.SET_NULL)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    receiver_Device = models.ForeignKey("FHIR_Device", related_name="MessageHeader_destination_receiver", null=True, blank=True, on_delete=models.SET_NULL)
    receiver_Organization = models.ForeignKey("FHIR_Organization", related_name="MessageHeader_destination_receiver", null=True, blank=True, on_delete=models.SET_NULL)
    receiver_Patient = models.ForeignKey("FHIR_Patient", related_name="MessageHeader_destination_receiver", null=True, blank=True, on_delete=models.SET_NULL)
    receiver_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="MessageHeader_destination_receiver", null=True, blank=True, on_delete=models.SET_NULL)
    receiver_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="MessageHeader_destination_receiver", null=True, blank=True, on_delete=models.SET_NULL)
    receiver_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="MessageHeader_destination_receiver", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_MessageHeader_source(models.Model):
    MessageHeader = models.ForeignKey(FHIR_MessageHeader, related_name='MessageHeader_source', null=False, on_delete=models.CASCADE)
    endpoint = FHIR_primitive_URLField(null=True, blank=True, )
    endpoint = models.ForeignKey("FHIR_Endpoint", related_name="MessageHeader_source_endpoint", null=True, blank=True, on_delete=models.SET_NULL)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    software = FHIR_primitive_StringField(null=True, blank=True, )
    version = FHIR_primitive_StringField(null=True, blank=True, )
    contact = models.OneToOneField("FHIR_GP_ContactPoint", related_name='MessageHeader_source_contact', null=True, blank=True, on_delete=models.SET_NULL)
    sender_Device = models.ForeignKey("FHIR_Device", related_name="MessageHeader_source_sender", null=True, blank=True, on_delete=models.SET_NULL)
    sender_Organization = models.ForeignKey("FHIR_Organization", related_name="MessageHeader_source_sender", null=True, blank=True, on_delete=models.SET_NULL)
    sender_Patient = models.ForeignKey("FHIR_Patient", related_name="MessageHeader_source_sender", null=True, blank=True, on_delete=models.SET_NULL)
    sender_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="MessageHeader_source_sender", null=True, blank=True, on_delete=models.SET_NULL)
    sender_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="MessageHeader_source_sender", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_MessageHeader_response(models.Model):
    MessageHeader = models.ForeignKey(FHIR_MessageHeader, related_name='MessageHeader_response', null=False, on_delete=models.CASCADE)
    identifier = models.OneToOneField("FHIR_GP_Identifier", related_name='MessageHeader_response_identifier', null=True, blank=True, on_delete=models.SET_NULL)
    class CodeChoices(models.TextChoices): OK = 'ok', 'Ok'; TRANSIENT_ERROR = 'transient-error', 'Transient-error'; FATAL_ERROR = 'fatal-error', 'Fatal-error'; 
    code = FHIR_primitive_CodeField(choices=CodeChoices.choices, null=True, blank=True, )
    details = models.ForeignKey("FHIR_OperationOutcome", related_name="MessageHeader_response_details", null=True, blank=True, on_delete=models.SET_NULL)
