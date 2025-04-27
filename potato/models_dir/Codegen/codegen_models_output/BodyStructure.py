#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_BodyStructure(models.Model):
    active = FHIR_primitive_BooleanField(null=True, blank=True, )
    BINDING_morphology = "TODO"
    morphology_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_morphology}, related_name='BodyStructure_morphology', blank=True)
    morphology_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    patient = models.ForeignKey("FHIR_Patient", related_name="BodyStructure_patient", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_BodyStructure_identifier(FHIR_GP_Identifier):
    BodyStructure = models.ForeignKey(FHIR_BodyStructure, related_name='BodyStructure_identifier', null=False, on_delete=models.CASCADE)

class FHIR_BodyStructure_includedStructure(models.Model):
    BodyStructure = models.ForeignKey(FHIR_BodyStructure, related_name='BodyStructure_includedStructure', null=False, on_delete=models.CASCADE)
    BINDING_structure = "TODO"
    structure_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_structure}, related_name='BodyStructure_includedStructure_structure', blank=True)
    structure_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_laterality = "TODO"
    laterality_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_laterality}, related_name='BodyStructure_includedStructure_laterality', blank=True)
    laterality_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    spatialReference = models.ManyToManyField("FHIR_ImagingSelection", related_name="BodyStructure_includedStructure_spatialReference", blank=True)

class FHIR_BodyStructure_includedStructure_bodyLandmarkOrientation(models.Model):
    BodyStructure_includedStructure = models.ForeignKey(FHIR_BodyStructure_includedStructure, related_name='BodyStructure_includedStructure_bodyLandmarkOrientation', null=False, on_delete=models.CASCADE)

class FHIR_BodyStructure_includedStructure_bodyLandmarkOrientation_landmarkDescription(models.Model):
    BodyStructure_includedStructure_bodyLandmarkOrientation = models.ForeignKey(FHIR_BodyStructure_includedStructure_bodyLandmarkOrientation, related_name='BodyStructure_includedStructure_bodyLandmarkOrientation_landmarkDescription', null=False, on_delete=models.CASCADE)
    BINDING_landmarkDescription = "TODO"
    landmarkDescription_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_landmarkDescription}, related_name='BodyStructure_includedStructure_bodyLandmarkOrientation_landmarkDescription', blank=True)
    landmarkDescription_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_BodyStructure_includedStructure_bodyLandmarkOrientation_clockFacePosition(models.Model):
    BodyStructure_includedStructure_bodyLandmarkOrientation = models.ForeignKey(FHIR_BodyStructure_includedStructure_bodyLandmarkOrientation, related_name='BodyStructure_includedStructure_bodyLandmarkOrientation_clockFacePosition', null=False, on_delete=models.CASCADE)
    BINDING_clockFacePosition = "TODO"
    clockFacePosition_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_clockFacePosition}, related_name='BodyStructure_includedStructure_bodyLandmarkOrientation_clockFacePosition', blank=True)
    clockFacePosition_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_BodyStructure_includedStructure_bodyLandmarkOrientation_distanceFromLandmark(models.Model):
    BodyStructure_includedStructure_bodyLandmarkOrientation = models.ForeignKey(FHIR_BodyStructure_includedStructure_bodyLandmarkOrientation, related_name='BodyStructure_includedStructure_bodyLandmarkOrientation_distanceFromLandmark', null=False, on_delete=models.CASCADE)

class FHIR_BodyStructure_includedStructure_bodyLandmarkOrientation_distanceFromLandmark_device(models.Model):
    BodyStructure_includedStructure_bodyLandmarkOrientation_distanceFromLandmark = models.ForeignKey(FHIR_BodyStructure_includedStructure_bodyLandmarkOrientation_distanceFromLandmark, related_name='BodyStructure_includedStructure_bodyLandmarkOrientation_distanceFromLandmark_device', null=False, on_delete=models.CASCADE)
    BINDING_device = "TODO"
    device_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_device}, related_name='BodyStructure_includedStructure_bodyLandmarkOrientation_distanceFromLandmark_device', blank=True)
    device_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    device_Device_ref = models.ForeignKey("FHIR_Device", related_name="BodyStructure_includedStructure_bodyLandmarkOrientation_distanceFromLandmark_device_Device", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_BodyStructure_includedStructure_bodyLandmarkOrientation_distanceFromLandmark_value(FHIR_GP_Quantity):
    BodyStructure_includedStructure_bodyLandmarkOrientation_distanceFromLandmark = models.ForeignKey(FHIR_BodyStructure_includedStructure_bodyLandmarkOrientation_distanceFromLandmark, related_name='BodyStructure_includedStructure_bodyLandmarkOrientation_distanceFromLandmark_value', null=False, on_delete=models.CASCADE)

class FHIR_BodyStructure_includedStructure_bodyLandmarkOrientation_surfaceOrientation(models.Model):
    BodyStructure_includedStructure_bodyLandmarkOrientation = models.ForeignKey(FHIR_BodyStructure_includedStructure_bodyLandmarkOrientation, related_name='BodyStructure_includedStructure_bodyLandmarkOrientation_surfaceOrientation', null=False, on_delete=models.CASCADE)
    BINDING_surfaceOrientation = "TODO"
    surfaceOrientation_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_surfaceOrientation}, related_name='BodyStructure_includedStructure_bodyLandmarkOrientation_surfaceOrientation', blank=True)
    surfaceOrientation_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_BodyStructure_includedStructure_qualifier(models.Model):
    BodyStructure_includedStructure = models.ForeignKey(FHIR_BodyStructure_includedStructure, related_name='BodyStructure_includedStructure_qualifier', null=False, on_delete=models.CASCADE)
    BINDING_qualifier = "TODO"
    qualifier_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_qualifier}, related_name='BodyStructure_includedStructure_qualifier', blank=True)
    qualifier_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_BodyStructure_image(FHIR_GP_Attachment):
    BodyStructure = models.ForeignKey(FHIR_BodyStructure, related_name='BodyStructure_image', null=False, on_delete=models.CASCADE)
