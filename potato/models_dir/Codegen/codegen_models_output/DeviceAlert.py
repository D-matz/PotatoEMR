#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_DeviceAlert(models.Model):
    class StatusChoices(models.TextChoices): IN_PROGRESS = 'in-progress', 'In-progress'; COMPLETED = 'completed', 'Completed'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    class TypeChoices(models.TextChoices): PHYSIOLOGICAL = 'physiological', 'Physiological'; TECHNICAL = 'technical', 'Technical'; 
    type = FHIR_primitive_CodeField(choices=TypeChoices.choices, null=True, blank=True, )
    class PriorityChoices(models.TextChoices): HIGH = 'high', 'High'; MEDIUM = 'medium', 'Medium'; LOW = 'low', 'Low'; INFO = 'info', 'Info'; 
    priority = FHIR_primitive_CodeField(choices=PriorityChoices.choices, null=True, blank=True, )
    subject_Patient = models.ForeignKey("FHIR_Patient", related_name="DeviceAlert_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Device = models.ForeignKey("FHIR_Device", related_name="DeviceAlert_subject", null=True, blank=True, on_delete=models.SET_NULL)
    source_Device = models.ForeignKey("FHIR_Device", related_name="DeviceAlert_source", null=True, blank=True, on_delete=models.SET_NULL)
    source_DeviceMetric = models.ForeignKey("FHIR_DeviceMetric", related_name="DeviceAlert_source", null=True, blank=True, on_delete=models.SET_NULL)
    derivedFrom = models.ManyToManyField("FHIR_Observation", related_name="DeviceAlert_derivedFrom", blank=True)
    label = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_DeviceAlert_identifier(FHIR_GP_Identifier):
    DeviceAlert = models.ForeignKey(FHIR_DeviceAlert, related_name='DeviceAlert_identifier', null=False, on_delete=models.CASCADE)

class FHIR_DeviceAlert_condition(models.Model):
    DeviceAlert = models.ForeignKey(FHIR_DeviceAlert, related_name='DeviceAlert_condition', null=False, on_delete=models.CASCADE)
    BINDING_code = "TODO"
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='DeviceAlert_condition_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    acknowledged = FHIR_primitive_BooleanField(null=True, blank=True, )
    presence = FHIR_primitive_BooleanField(null=True, blank=True, )
    timing = models.OneToOneField("FHIR_GP_Period", related_name='DeviceAlert_condition_timing', null=True, blank=True, on_delete=models.SET_NULL)
    limit = models.OneToOneField("FHIR_GP_Range", related_name='DeviceAlert_condition_limit', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_DeviceAlert_signal(models.Model):
    DeviceAlert = models.ForeignKey(FHIR_DeviceAlert, related_name='DeviceAlert_signal', null=False, on_delete=models.CASCADE)
    class ActivationstateChoices(models.TextChoices): ON = 'on', 'On'; OFF = 'off', 'Off'; PAUSED = 'paused', 'Paused'; 
    activationState = FHIR_primitive_CodeField(choices=ActivationstateChoices.choices, null=True, blank=True, )
    class PresenceChoices(models.TextChoices): ON = 'on', 'On'; LATCHED = 'latched', 'Latched'; OFF = 'off', 'Off'; ACK = 'ack', 'Ack'; 
    presence = FHIR_primitive_CodeField(choices=PresenceChoices.choices, null=True, blank=True, )
    BINDING_annunciator = "TODO"
    annunciator_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_annunciator}, related_name='DeviceAlert_signal_annunciator', blank=True)
    annunciator_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    annunciator_Device_ref = models.ForeignKey("FHIR_Device", related_name="DeviceAlert_signal_annunciator_Device", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_manifestation = "TODO"
    manifestation_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_manifestation}, related_name='DeviceAlert_signal_manifestation', blank=True)
    manifestation_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    indication = models.OneToOneField("FHIR_GP_Period", related_name='DeviceAlert_signal_indication', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_DeviceAlert_signal_type(models.Model):
    DeviceAlert_signal = models.ForeignKey(FHIR_DeviceAlert_signal, related_name='DeviceAlert_signal_type', null=False, on_delete=models.CASCADE)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='DeviceAlert_signal_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    