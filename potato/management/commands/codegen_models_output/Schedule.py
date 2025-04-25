
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Schedule(models.Model):
    active = FHIR_primitive_BooleanField(null=True, blank=True, )
    name = FHIR_primitive_StringField(null=True, blank=True, )
    actor_Patient = models.ManyToManyField("FHIR_Patient", related_name="Schedule_actor", blank=True)
    actor_Practitioner = models.ManyToManyField("FHIR_Practitioner", related_name="Schedule_actor", blank=True)
    actor_PractitionerRole = models.ManyToManyField("FHIR_PractitionerRole", related_name="Schedule_actor", blank=True)
    actor_CareTeam = models.ManyToManyField("FHIR_CareTeam", related_name="Schedule_actor", blank=True)
    actor_RelatedPerson = models.ManyToManyField("FHIR_RelatedPerson", related_name="Schedule_actor", blank=True)
    actor_Device = models.ManyToManyField("FHIR_Device", related_name="Schedule_actor", blank=True)
    actor_HealthcareService = models.ManyToManyField("FHIR_HealthcareService", related_name="Schedule_actor", blank=True)
    actor_Location = models.ManyToManyField("FHIR_Location", related_name="Schedule_actor", blank=True)
    planningHorizon = models.OneToOneField("FHIR_GP_Period", related_name='Schedule_planningHorizon', null=True, blank=True, on_delete=models.SET_NULL)
    comment = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_Schedule_identifier(FHIR_GP_Identifier):
    Schedule = models.ForeignKey(FHIR_Schedule, related_name='Schedule_identifier', null=False, on_delete=models.CASCADE)

class FHIR_Schedule_serviceCategory(models.Model):
    Schedule = models.ForeignKey(FHIR_Schedule, related_name='Schedule_serviceCategory', null=False, on_delete=models.CASCADE)
    BINDING_serviceCategory = 'TODO'
    serviceCategory_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_serviceCategory}, related_name='Schedule_serviceCategory', blank=True)
    serviceCategory_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Schedule_serviceType(models.Model):
    Schedule = models.ForeignKey(FHIR_Schedule, related_name='Schedule_serviceType', null=False, on_delete=models.CASCADE)
    BINDING_serviceType = 'TODO'
    serviceType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_serviceType}, related_name='Schedule_serviceType', blank=True)
    serviceType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    serviceType_HealthcareService_ref = models.ForeignKey("FHIR_HealthcareService", related_name="Schedule_serviceType", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Schedule_specialty(models.Model):
    Schedule = models.ForeignKey(FHIR_Schedule, related_name='Schedule_specialty', null=False, on_delete=models.CASCADE)
    BINDING_specialty = 'TODO'
    specialty_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_specialty}, related_name='Schedule_specialty', blank=True)
    specialty_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    