
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_OrganizationAffiliation(models.Model):
    active = FHIR_primitive_BooleanField(null=True, blank=True, )
    period = models.OneToOneField("FHIR_GP_Period", related_name='OrganizationAffiliation_period', null=True, blank=True, on_delete=models.SET_NULL)
    organization = models.ForeignKey("FHIR_Organization", related_name="OrganizationAffiliation_organization", null=True, blank=True, on_delete=models.SET_NULL)
    participatingOrganization = models.ForeignKey("FHIR_Organization", related_name="OrganizationAffiliation_participatingOrganization", null=True, blank=True, on_delete=models.SET_NULL)
    network = models.ManyToManyField("FHIR_Organization", related_name="OrganizationAffiliation_network", blank=True)
    location = models.ManyToManyField("FHIR_Location", related_name="OrganizationAffiliation_location", blank=True)
    healthcareService = models.ManyToManyField("FHIR_HealthcareService", related_name="OrganizationAffiliation_healthcareService", blank=True)
    endpoint = models.ManyToManyField("FHIR_Endpoint", related_name="OrganizationAffiliation_endpoint", blank=True)

class FHIR_OrganizationAffiliation_identifier(FHIR_GP_Identifier):
    OrganizationAffiliation = models.ForeignKey(FHIR_OrganizationAffiliation, related_name='OrganizationAffiliation_identifier', null=False, on_delete=models.CASCADE)

class FHIR_OrganizationAffiliation_code(models.Model):
    OrganizationAffiliation = models.ForeignKey(FHIR_OrganizationAffiliation, related_name='OrganizationAffiliation_code', null=False, on_delete=models.CASCADE)
    BINDING_code = 'TODO'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='OrganizationAffiliation_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_OrganizationAffiliation_specialty(models.Model):
    OrganizationAffiliation = models.ForeignKey(FHIR_OrganizationAffiliation, related_name='OrganizationAffiliation_specialty', null=False, on_delete=models.CASCADE)
    BINDING_specialty = 'TODO'
    specialty_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_specialty}, related_name='OrganizationAffiliation_specialty', blank=True)
    specialty_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_OrganizationAffiliation_contact(FHIR_meta_ExtendedContactDetail):
    OrganizationAffiliation = models.ForeignKey(FHIR_OrganizationAffiliation, related_name='OrganizationAffiliation_contact', null=False, on_delete=models.CASCADE)
