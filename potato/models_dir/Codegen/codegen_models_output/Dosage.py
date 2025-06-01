#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Dosage(models.Model):
    patientInstruction = FHIR_primitive_StringField(null=True, blank=True, )
    timing = models.OneToOneField("FHIR_GP_Timing", related_name='Dosage_timing', null=True, blank=True, on_delete=models.SET_NULL)
    asNeeded = FHIR_primitive_BooleanField(null=True, blank=True, )
    BINDING_site = "TODO"
    site_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_site}, related_name='Dosage_site', blank=True)
    site_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_route = "TODO"
    route_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_route}, related_name='Dosage_route', blank=True)
    route_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_method = "TODO"
    method_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_method}, related_name='Dosage_method', blank=True)
    method_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Dosage_doseAndRate_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    dose_Range = models.OneToOneField("FHIR_GP_Range", related_name='Dosage_doseAndRate_dose_Range', null=True, blank=True, on_delete=models.SET_NULL)
    dose_Quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='Dosage_doseAndRate_dose_Quantity', null=True, blank=True, on_delete=models.SET_NULL)
    rate_Ratio = models.OneToOneField("FHIR_GP_Ratio", related_name='Dosage_doseAndRate_rate_Ratio', null=True, blank=True, on_delete=models.SET_NULL)
    rate_Range = models.OneToOneField("FHIR_GP_Range", related_name='Dosage_doseAndRate_rate_Range', null=True, blank=True, on_delete=models.SET_NULL)
    rate_Quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='Dosage_doseAndRate_rate_Quantity', null=True, blank=True, on_delete=models.SET_NULL)
    maxDosePerAdministration = models.OneToOneField("FHIR_GP_Quantity", related_name='Dosage_maxDosePerAdministration', null=True, blank=True, on_delete=models.SET_NULL)
    maxDosePerLifetime = models.OneToOneField("FHIR_GP_Quantity", related_name='Dosage_maxDosePerLifetime', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Dosage_additionalInstruction(models.Model):
    Dosage = models.ForeignKey(FHIR_Dosage, related_name='Dosage_additionalInstruction', null=False, on_delete=models.CASCADE)
    BINDING_additionalInstruction = "TODO"
    additionalInstruction_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_additionalInstruction}, related_name='Dosage_additionalInstruction', blank=True)
    additionalInstruction_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Dosage_asNeededFor(models.Model):
    Dosage = models.ForeignKey(FHIR_Dosage, related_name='Dosage_asNeededFor', null=False, on_delete=models.CASCADE)
    BINDING_asNeededFor = "TODO"
    asNeededFor_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_asNeededFor}, related_name='Dosage_asNeededFor', blank=True)
    asNeededFor_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Dosage_maxDosePerPeriod(FHIR_GP_Ratio):
    Dosage = models.ForeignKey(FHIR_Dosage, related_name='Dosage_maxDosePerPeriod', null=False, on_delete=models.CASCADE)
