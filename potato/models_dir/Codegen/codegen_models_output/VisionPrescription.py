#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_VisionPrescription(models.Model):
    basedOn_CarePlan = models.ManyToManyField("FHIR_CarePlan", related_name="VisionPrescription_basedOn", blank=True)
    basedOn_RequestOrchestration = models.ManyToManyField("FHIR_RequestOrchestration", related_name="VisionPrescription_basedOn", blank=True)
    basedOn_NutritionOrder = models.ManyToManyField("FHIR_NutritionOrder", related_name="VisionPrescription_basedOn", blank=True)
    basedOn_ServiceRequest = models.ManyToManyField("FHIR_ServiceRequest", related_name="VisionPrescription_basedOn", blank=True)
    class StatusChoices(models.TextChoices): ACTIVE = 'active', 'Active'; CANCELLED = 'cancelled', 'Cancelled'; DRAFT = 'draft', 'Draft'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    created = FHIR_primitive_DateTimeField(null=True, blank=True, )
    patient = models.ForeignKey("FHIR_Patient", related_name="VisionPrescription_patient", null=True, blank=True, on_delete=models.SET_NULL)
    encounter = models.ForeignKey("FHIR_Encounter", related_name="VisionPrescription_encounter", null=True, blank=True, on_delete=models.SET_NULL)
    dateWritten = FHIR_primitive_DateTimeField(null=True, blank=True, )
    prescriber_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="VisionPrescription_prescriber", null=True, blank=True, on_delete=models.SET_NULL)
    prescriber_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="VisionPrescription_prescriber", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_VisionPrescription_identifier(FHIR_GP_Identifier):
    VisionPrescription = models.ForeignKey(FHIR_VisionPrescription, related_name='VisionPrescription_identifier', null=False, on_delete=models.CASCADE)

class FHIR_VisionPrescription_lensSpecification(models.Model):
    VisionPrescription = models.ForeignKey(FHIR_VisionPrescription, related_name='VisionPrescription_lensSpecification', null=False, on_delete=models.CASCADE)
    BINDING_product = "TODO"
    product_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_product}, related_name='VisionPrescription_lensSpecification_product', blank=True)
    product_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    class EyeChoices(models.TextChoices): RIGHT = 'right', 'Right'; LEFT = 'left', 'Left'; 
    eye = FHIR_primitive_CodeField(choices=EyeChoices.choices, null=True, blank=True, )
    sphere = FHIR_primitive_DecimalField(null=True, blank=True, )
    cylinder = FHIR_primitive_DecimalField(null=True, blank=True, )
    add = FHIR_primitive_DecimalField(null=True, blank=True, )
    power = FHIR_primitive_DecimalField(null=True, blank=True, )
    backCurve = FHIR_primitive_DecimalField(null=True, blank=True, )
    diameter = FHIR_primitive_DecimalField(null=True, blank=True, )
    duration = models.OneToOneField("FHIR_GP_Quantity", related_name='VisionPrescription_lensSpecification_duration', null=True, blank=True, on_delete=models.SET_NULL)
    color = FHIR_primitive_StringField(null=True, blank=True, )
    brand = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_VisionPrescription_lensSpecification_prism(models.Model):
    VisionPrescription_lensSpecification = models.ForeignKey(FHIR_VisionPrescription_lensSpecification, related_name='VisionPrescription_lensSpecification_prism', null=False, on_delete=models.CASCADE)
    amount = FHIR_primitive_DecimalField(null=True, blank=True, )
    class BaseChoices(models.TextChoices): UP = 'up', 'Up'; DOWN = 'down', 'Down'; IN = 'in', 'In'; OUT = 'out', 'Out'; 
    base = FHIR_primitive_CodeField(choices=BaseChoices.choices, null=True, blank=True, )

class FHIR_VisionPrescription_lensSpecification_note(FHIR_GP_Annotation):
    VisionPrescription_lensSpecification = models.ForeignKey(FHIR_VisionPrescription_lensSpecification, related_name='VisionPrescription_lensSpecification_note', null=False, on_delete=models.CASCADE)
