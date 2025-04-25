
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_AdministrableProductDefinition(models.Model):
    class StatusChoices(models.TextChoices): DRAFT = 'draft', 'Draft'; ACTIVE = 'active', 'Active'; RETIRED = 'retired', 'Retired'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    formOf = models.ManyToManyField("FHIR_MedicinalProductDefinition", related_name="AdministrableProductDefinition_formOf", blank=True)
    BINDING_administrableDoseForm = 'TODO'
    administrableDoseForm_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_administrableDoseForm}, related_name='AdministrableProductDefinition_administrableDoseForm', blank=True)
    administrableDoseForm_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_unitOfPresentation = 'TODO'
    unitOfPresentation_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_unitOfPresentation}, related_name='AdministrableProductDefinition_unitOfPresentation', blank=True)
    unitOfPresentation_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    producedFrom = models.ManyToManyField("FHIR_ManufacturedItemDefinition", related_name="AdministrableProductDefinition_producedFrom", blank=True)
    device = models.ForeignKey("FHIR_DeviceDefinition", related_name="AdministrableProductDefinition_device", null=True, blank=True, on_delete=models.SET_NULL)
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_AdministrableProductDefinition_identifier(FHIR_GP_Identifier):
    AdministrableProductDefinition = models.ForeignKey(FHIR_AdministrableProductDefinition, related_name='AdministrableProductDefinition_identifier', null=False, on_delete=models.CASCADE)

class FHIR_AdministrableProductDefinition_ingredient(models.Model):
    AdministrableProductDefinition = models.ForeignKey(FHIR_AdministrableProductDefinition, related_name='AdministrableProductDefinition_ingredient', null=False, on_delete=models.CASCADE)
    BINDING_ingredient = 'TODO'
    ingredient_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_ingredient}, related_name='AdministrableProductDefinition_ingredient', blank=True)
    ingredient_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_AdministrableProductDefinition_property(models.Model):
    AdministrableProductDefinition = models.ForeignKey(FHIR_AdministrableProductDefinition, related_name='AdministrableProductDefinition_property', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='AdministrableProductDefinition_property_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_value = 'TODO'
    value_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_value}, related_name='AdministrableProductDefinition_property_value', blank=True)
    value_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value = models.OneToOneField("FHIR_GP_Quantity", related_name='AdministrableProductDefinition_property_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = FHIR_primitive_DateField(null=True, blank=True, )
    value = FHIR_primitive_BooleanField(null=True, blank=True, )
    value = FHIR_primitive_MarkdownField(null=True, blank=True, )
    value = models.OneToOneField("FHIR_GP_Attachment", related_name='AdministrableProductDefinition_property_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.ForeignKey("FHIR_Binary", related_name="AdministrableProductDefinition_property_value", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_status = 'TODO'
    status_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_status}, related_name='AdministrableProductDefinition_property_status', blank=True)
    status_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_AdministrableProductDefinition_routeOfAdministration(models.Model):
    AdministrableProductDefinition = models.ForeignKey(FHIR_AdministrableProductDefinition, related_name='AdministrableProductDefinition_routeOfAdministration', null=False, on_delete=models.CASCADE)
    BINDING_code = 'TODO'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='AdministrableProductDefinition_routeOfAdministration_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    firstDose = models.OneToOneField("FHIR_GP_Quantity", related_name='AdministrableProductDefinition_routeOfAdministration_firstDose', null=True, blank=True, on_delete=models.SET_NULL)
    maxSingleDose = models.OneToOneField("FHIR_GP_Quantity", related_name='AdministrableProductDefinition_routeOfAdministration_maxSingleDose', null=True, blank=True, on_delete=models.SET_NULL)
    maxDosePerDay = models.OneToOneField("FHIR_GP_Quantity", related_name='AdministrableProductDefinition_routeOfAdministration_maxDosePerDay', null=True, blank=True, on_delete=models.SET_NULL)
    maxDosePerTreatmentPeriod = models.OneToOneField("FHIR_GP_Ratio", related_name='AdministrableProductDefinition_routeOfAdministration_maxDosePerTreatmentPeriod', null=True, blank=True, on_delete=models.SET_NULL)
    maxTreatmentPeriod = models.OneToOneField("FHIR_GP_Quantity_Duration", related_name='AdministrableProductDefinition_routeOfAdministration_maxTreatmentPeriod', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_AdministrableProductDefinition_routeOfAdministration_targetSpecies(models.Model):
    AdministrableProductDefinition_routeOfAdministration = models.ForeignKey(FHIR_AdministrableProductDefinition_routeOfAdministration, related_name='AdministrableProductDefinition_routeOfAdministration_targetSpecies', null=False, on_delete=models.CASCADE)
    BINDING_code = 'TODO'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='AdministrableProductDefinition_routeOfAdministration_targetSpecies_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_AdministrableProductDefinition_routeOfAdministration_targetSpecies_withdrawalPeriod(models.Model):
    AdministrableProductDefinition_routeOfAdministration_targetSpecies = models.ForeignKey(FHIR_AdministrableProductDefinition_routeOfAdministration_targetSpecies, related_name='AdministrableProductDefinition_routeOfAdministration_targetSpecies_withdrawalPeriod', null=False, on_delete=models.CASCADE)
    BINDING_tissue = 'TODO'
    tissue_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_tissue}, related_name='AdministrableProductDefinition_routeOfAdministration_targetSpecies_withdrawalPeriod_tissue', blank=True)
    tissue_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value = models.OneToOneField("FHIR_GP_Quantity", related_name='AdministrableProductDefinition_routeOfAdministration_targetSpecies_withdrawalPeriod_value', null=True, blank=True, on_delete=models.SET_NULL)
    supportingInformation = FHIR_primitive_StringField(null=True, blank=True, )
