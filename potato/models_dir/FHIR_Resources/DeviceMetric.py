#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_DeviceMetric(models.Model):
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='DeviceMetric_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_unit = 'TODO'
    unit_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_unit}, related_name='DeviceMetric_unit', blank=True)
    unit_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    device = models.ForeignKey("FHIR_Device", related_name="DeviceMetric_device", null=True, blank=True, on_delete=models.SET_NULL)
    class OperationalstatusChoices(models.TextChoices): ON = 'on', 'On'; OFF = 'off', 'Off'; STANDBY = 'standby', 'Standby'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; 
    operationalStatus = FHIR_primitive_CodeField(choices=OperationalstatusChoices.choices, null=True, blank=True, )
    class ColorChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    color = FHIR_primitive_CodeField(choices=ColorChoices.choices, null=True, blank=True, )
    BINDING_category = 'TODO'
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='DeviceMetric_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    measurementFrequency = models.OneToOneField("FHIR_GP_Quantity", related_name='DeviceMetric_measurementFrequency', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_DeviceMetric_identifier(FHIR_GP_Identifier):
    DeviceMetric = models.ForeignKey(FHIR_DeviceMetric, related_name='DeviceMetric_identifier', null=False, on_delete=models.CASCADE)

class FHIR_DeviceMetric_calibration(models.Model):
    DeviceMetric = models.ForeignKey(FHIR_DeviceMetric, related_name='DeviceMetric_calibration', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='DeviceMetric_calibration_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    class StateChoices(models.TextChoices): NOT_CALIBRATED = 'not-calibrated', 'Not-calibrated'; CALIBRATION_REQUIRED = 'calibration-required', 'Calibration-required'; CALIBRATED = 'calibrated', 'Calibrated'; UNSPECIFIED = 'unspecified', 'Unspecified'; 
    state = FHIR_primitive_CodeField(choices=StateChoices.choices, null=True, blank=True, )
    time = FHIR_primitive_InstantField(null=True, blank=True, )
