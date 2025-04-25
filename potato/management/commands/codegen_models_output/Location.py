
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Location(models.Model):
    class StatusChoices(models.TextChoices): ACTIVE = 'active', 'Active'; SUSPENDED = 'suspended', 'Suspended'; INACTIVE = 'inactive', 'Inactive'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    operationalStatus = models.OneToOneField("FHIR_GP_Coding", related_name='Location_operationalStatus', null=True, blank=True, on_delete=models.SET_NULL)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    class ModeChoices(models.TextChoices): INSTANCE = 'instance', 'Instance'; KIND = 'kind', 'Kind'; 
    mode = FHIR_primitive_CodeField(choices=ModeChoices.choices, null=True, blank=True, )
    address = models.OneToOneField("FHIR_GP_Address", related_name='Location_address', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_form = 'TODO'
    form_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_form}, related_name='Location_form', blank=True)
    form_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    managingOrganization = models.ForeignKey("FHIR_Organization", related_name="Location_managingOrganization", null=True, blank=True, on_delete=models.SET_NULL)
    partOf = models.ForeignKey("FHIR_Location", related_name="Location_partOf", null=True, blank=True, on_delete=models.SET_NULL)
    endpoint = models.ManyToManyField("FHIR_Endpoint", related_name="Location_endpoint", blank=True)

class FHIR_Location_identifier(FHIR_GP_Identifier):
    Location = models.ForeignKey(FHIR_Location, related_name='Location_identifier', null=False, on_delete=models.CASCADE)

class FHIR_Location_alias(models.Model):
    Location = models.ForeignKey(FHIR_Location, related_name='Location_alias', null=False, on_delete=models.CASCADE)
    
    alias = FHIR_primitive_StringField(null=True, blank=True, )
    
class FHIR_Location_type(models.Model):
    Location = models.ForeignKey(FHIR_Location, related_name='Location_type', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Location_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Location_contact(FHIR_meta_ExtendedContactDetail):
    Location = models.ForeignKey(FHIR_Location, related_name='Location_contact', null=False, on_delete=models.CASCADE)

class FHIR_Location_position(models.Model):
    Location = models.ForeignKey(FHIR_Location, related_name='Location_position', null=False, on_delete=models.CASCADE)
    longitude = FHIR_primitive_DecimalField(null=True, blank=True, )
    latitude = FHIR_primitive_DecimalField(null=True, blank=True, )
    altitude = FHIR_primitive_DecimalField(null=True, blank=True, )

class FHIR_Location_characteristic(models.Model):
    Location = models.ForeignKey(FHIR_Location, related_name='Location_characteristic', null=False, on_delete=models.CASCADE)
    BINDING_characteristic = 'TODO'
    characteristic_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_characteristic}, related_name='Location_characteristic', blank=True)
    characteristic_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Location_virtualService(FHIR_meta_VirtualServiceDetail):
    Location = models.ForeignKey(FHIR_Location, related_name='Location_virtualService', null=False, on_delete=models.CASCADE)
