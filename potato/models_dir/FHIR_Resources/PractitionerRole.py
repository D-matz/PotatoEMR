#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_PractitionerRole(models.Model):
    active = FHIR_primitive_BooleanField(null=True, blank=True, )
    period = models.OneToOneField("FHIR_GP_Period", related_name='PractitionerRole_period', null=True, blank=True, on_delete=models.SET_NULL)
    practitioner = models.ForeignKey("FHIR_Practitioner", related_name="PractitionerRole_practitioner", null=True, blank=True, on_delete=models.SET_NULL)
    organization = models.ForeignKey("FHIR_Organization", related_name="PractitionerRole_organization", null=True, blank=True, on_delete=models.SET_NULL)
    network = models.ManyToManyField("FHIR_Organization", related_name="PractitionerRole_network", blank=True)
    display = FHIR_primitive_StringField(null=True, blank=True, )
    location = models.ManyToManyField("FHIR_Location", related_name="PractitionerRole_location", blank=True)
    healthcareService = models.ManyToManyField("FHIR_HealthcareService", related_name="PractitionerRole_healthcareService", blank=True)
    endpoint = models.ManyToManyField("FHIR_Endpoint", related_name="PractitionerRole_endpoint", blank=True)

class FHIR_PractitionerRole_identifier(FHIR_GP_Identifier):
    PractitionerRole = models.ForeignKey(FHIR_PractitionerRole, related_name='PractitionerRole_identifier', null=False, on_delete=models.CASCADE)

class FHIR_PractitionerRole_code(models.Model):
    PractitionerRole = models.ForeignKey(FHIR_PractitionerRole, related_name='PractitionerRole_code', null=False, on_delete=models.CASCADE)
    BINDING_code = 'TODO'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='PractitionerRole_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_PractitionerRole_specialty(models.Model):
    PractitionerRole = models.ForeignKey(FHIR_PractitionerRole, related_name='PractitionerRole_specialty', null=False, on_delete=models.CASCADE)
    BINDING_specialty = 'TODO'
    specialty_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_specialty}, related_name='PractitionerRole_specialty', blank=True)
    specialty_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_PractitionerRole_contact(FHIR_meta_ExtendedContactDetail):
    PractitionerRole = models.ForeignKey(FHIR_PractitionerRole, related_name='PractitionerRole_contact', null=False, on_delete=models.CASCADE)

class FHIR_PractitionerRole_characteristic(models.Model):
    PractitionerRole = models.ForeignKey(FHIR_PractitionerRole, related_name='PractitionerRole_characteristic', null=False, on_delete=models.CASCADE)
    BINDING_characteristic = 'TODO'
    characteristic_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_characteristic}, related_name='PractitionerRole_characteristic', blank=True)
    characteristic_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_PractitionerRole_communication(models.Model):
    PractitionerRole = models.ForeignKey(FHIR_PractitionerRole, related_name='PractitionerRole_communication', null=False, on_delete=models.CASCADE)
    BINDING_communication = 'TODO'
    communication_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_communication}, related_name='PractitionerRole_communication', blank=True)
    communication_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    