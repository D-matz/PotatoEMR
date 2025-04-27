#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Slot(models.Model):
    schedule = models.ForeignKey("FHIR_Schedule", related_name="Slot_schedule", null=True, blank=True, on_delete=models.SET_NULL)
    class StatusChoices(models.TextChoices): BUSY = 'busy', 'Busy'; FREE = 'free', 'Free'; BUSY_UNAVAILABLE = 'busy-unavailable', 'Busy-unavailable'; BUSY_TENTATIVE = 'busy-tentative', 'Busy-tentative'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    start = FHIR_primitive_InstantField(null=True, blank=True, )
    end = FHIR_primitive_InstantField(null=True, blank=True, )
    overbooked = FHIR_primitive_BooleanField(null=True, blank=True, )
    comment = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_Slot_identifier(FHIR_GP_Identifier):
    Slot = models.ForeignKey(FHIR_Slot, related_name='Slot_identifier', null=False, on_delete=models.CASCADE)

class FHIR_Slot_serviceCategory(models.Model):
    Slot = models.ForeignKey(FHIR_Slot, related_name='Slot_serviceCategory', null=False, on_delete=models.CASCADE)
    BINDING_serviceCategory = "TODO"
    serviceCategory_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_serviceCategory}, related_name='Slot_serviceCategory', blank=True)
    serviceCategory_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Slot_serviceType(models.Model):
    Slot = models.ForeignKey(FHIR_Slot, related_name='Slot_serviceType', null=False, on_delete=models.CASCADE)
    BINDING_serviceType = "TODO"
    serviceType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_serviceType}, related_name='Slot_serviceType', blank=True)
    serviceType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    serviceType_HealthcareService_ref = models.ForeignKey("FHIR_HealthcareService", related_name="Slot_serviceType_HealthcareService", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Slot_specialty(models.Model):
    Slot = models.ForeignKey(FHIR_Slot, related_name='Slot_specialty', null=False, on_delete=models.CASCADE)
    BINDING_specialty = "TODO"
    specialty_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_specialty}, related_name='Slot_specialty', blank=True)
    specialty_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Slot_appointmentType(models.Model):
    Slot = models.ForeignKey(FHIR_Slot, related_name='Slot_appointmentType', null=False, on_delete=models.CASCADE)
    BINDING_appointmentType = "TODO"
    appointmentType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_appointmentType}, related_name='Slot_appointmentType', blank=True)
    appointmentType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    