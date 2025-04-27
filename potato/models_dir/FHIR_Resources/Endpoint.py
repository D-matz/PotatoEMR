#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Endpoint(models.Model):
    class StatusChoices(models.TextChoices): ACTIVE = 'active', 'Active'; LIMITED = 'limited', 'Limited'; SUSPENDED = 'suspended', 'Suspended'; ERROR = 'error', 'Error'; OFF = 'off', 'Off'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    name = FHIR_primitive_StringField(null=True, blank=True, )
    description = FHIR_primitive_StringField(null=True, blank=True, )
    managingOrganization = models.ForeignKey("FHIR_Organization", related_name="Endpoint_managingOrganization", null=True, blank=True, on_delete=models.SET_NULL)
    period = models.OneToOneField("FHIR_GP_Period", related_name='Endpoint_period', null=True, blank=True, on_delete=models.SET_NULL)
    address = FHIR_primitive_URLField(null=True, blank=True, )

class FHIR_Endpoint_identifier(FHIR_GP_Identifier):
    Endpoint = models.ForeignKey(FHIR_Endpoint, related_name='Endpoint_identifier', null=False, on_delete=models.CASCADE)

class FHIR_Endpoint_connectionType(models.Model):
    Endpoint = models.ForeignKey(FHIR_Endpoint, related_name='Endpoint_connectionType', null=False, on_delete=models.CASCADE)
    BINDING_connectionType = 'TODO'
    connectionType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_connectionType}, related_name='Endpoint_connectionType', blank=True)
    connectionType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Endpoint_environmentType(models.Model):
    Endpoint = models.ForeignKey(FHIR_Endpoint, related_name='Endpoint_environmentType', null=False, on_delete=models.CASCADE)
    BINDING_environmentType = 'TODO'
    environmentType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_environmentType}, related_name='Endpoint_environmentType', blank=True)
    environmentType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Endpoint_contact(FHIR_GP_ContactPoint):
    Endpoint = models.ForeignKey(FHIR_Endpoint, related_name='Endpoint_contact', null=False, on_delete=models.CASCADE)

class FHIR_Endpoint_payload(models.Model):
    Endpoint = models.ForeignKey(FHIR_Endpoint, related_name='Endpoint_payload', null=False, on_delete=models.CASCADE)

class FHIR_Endpoint_payload_type(models.Model):
    Endpoint_payload = models.ForeignKey(FHIR_Endpoint_payload, related_name='Endpoint_payload_type', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Endpoint_payload_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Endpoint_payload_mimeType(models.Model):
    Endpoint_payload = models.ForeignKey(FHIR_Endpoint_payload, related_name='Endpoint_payload_mimeType', null=False, on_delete=models.CASCADE)
    
    class MimetypeChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    mimeType = FHIR_primitive_CodeField(choices=MimetypeChoices.choices, null=True, blank=True, )
    
class FHIR_Endpoint_payload_profileCanonical(models.Model):
    Endpoint_payload = models.ForeignKey(FHIR_Endpoint_payload, related_name='Endpoint_payload_profileCanonical', null=False, on_delete=models.CASCADE)
    
    profileCanonical = FHIR_primitive_CanonicalField(null=True, blank=True, )
    
class FHIR_Endpoint_payload_profileUri(models.Model):
    Endpoint_payload = models.ForeignKey(FHIR_Endpoint_payload, related_name='Endpoint_payload_profileUri', null=False, on_delete=models.CASCADE)
    
    profileUri = FHIR_primitive_URIField(null=True, blank=True, )
    
class FHIR_Endpoint_header(models.Model):
    Endpoint = models.ForeignKey(FHIR_Endpoint, related_name='Endpoint_header', null=False, on_delete=models.CASCADE)
    
    header = FHIR_primitive_StringField(null=True, blank=True, )
    