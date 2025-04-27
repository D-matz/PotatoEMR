#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_ImagingSelection(models.Model):
    class StatusChoices(models.TextChoices): AVAILABLE = 'available', 'Available'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; INACTIVE = 'inactive', 'Inactive'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    BINDING_code = 'TODO'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='ImagingSelection_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    subject_Patient = models.ForeignKey("FHIR_Patient", related_name="ImagingSelection_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Group = models.ForeignKey("FHIR_Group", related_name="ImagingSelection_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Device = models.ForeignKey("FHIR_Device", related_name="ImagingSelection_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Procedure = models.ForeignKey("FHIR_Procedure", related_name="ImagingSelection_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="ImagingSelection_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Medication = models.ForeignKey("FHIR_Medication", related_name="ImagingSelection_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Substance = models.ForeignKey("FHIR_Substance", related_name="ImagingSelection_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Specimen = models.ForeignKey("FHIR_Specimen", related_name="ImagingSelection_subject", null=True, blank=True, on_delete=models.SET_NULL)
    issued = FHIR_primitive_InstantField(null=True, blank=True, )
    basedOn_CarePlan = models.ManyToManyField("FHIR_CarePlan", related_name="ImagingSelection_basedOn", blank=True)
    basedOn_ServiceRequest = models.ManyToManyField("FHIR_ServiceRequest", related_name="ImagingSelection_basedOn", blank=True)
    basedOn_Appointment = models.ManyToManyField("FHIR_Appointment", related_name="ImagingSelection_basedOn", blank=True)
    basedOn_Task = models.ManyToManyField("FHIR_Task", related_name="ImagingSelection_basedOn", blank=True)
    derivedFrom_ImagingStudy = models.ForeignKey("FHIR_ImagingStudy", related_name="ImagingSelection_derivedFrom", null=True, blank=True, on_delete=models.SET_NULL)
    derivedFrom_DocumentReference = models.ForeignKey("FHIR_DocumentReference", related_name="ImagingSelection_derivedFrom", null=True, blank=True, on_delete=models.SET_NULL)
    studyUid = FHIR_primitive_IdField(null=True, blank=True, )
    seriesUid = FHIR_primitive_IdField(null=True, blank=True, )
    seriesNumber = FHIR_primitive_UnsignedIntField(null=True, blank=True, )
    frameOfReferenceUid = FHIR_primitive_IdField(null=True, blank=True, )
    focus = models.ManyToManyField("FHIR_ImagingSelection", related_name="ImagingSelection_focus", blank=True)
    endpoint = models.ManyToManyField("FHIR_Endpoint", related_name="ImagingSelection_endpoint", blank=True)

class FHIR_ImagingSelection_identifier(FHIR_GP_Identifier):
    ImagingSelection = models.ForeignKey(FHIR_ImagingSelection, related_name='ImagingSelection_identifier', null=False, on_delete=models.CASCADE)

class FHIR_ImagingSelection_category(models.Model):
    ImagingSelection = models.ForeignKey(FHIR_ImagingSelection, related_name='ImagingSelection_category', null=False, on_delete=models.CASCADE)
    BINDING_category = 'TODO'
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='ImagingSelection_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ImagingSelection_performer(models.Model):
    ImagingSelection = models.ForeignKey(FHIR_ImagingSelection, related_name='ImagingSelection_performer', null=False, on_delete=models.CASCADE)
    BINDING_function = 'TODO'
    function_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_function}, related_name='ImagingSelection_performer_function', blank=True)
    function_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    actor_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="ImagingSelection_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="ImagingSelection_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Device = models.ForeignKey("FHIR_Device", related_name="ImagingSelection_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Organization = models.ForeignKey("FHIR_Organization", related_name="ImagingSelection_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_CareTeam = models.ForeignKey("FHIR_CareTeam", related_name="ImagingSelection_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Patient = models.ForeignKey("FHIR_Patient", related_name="ImagingSelection_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="ImagingSelection_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_HealthcareService = models.ForeignKey("FHIR_HealthcareService", related_name="ImagingSelection_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ImagingSelection_bodySite(models.Model):
    ImagingSelection = models.ForeignKey(FHIR_ImagingSelection, related_name='ImagingSelection_bodySite', null=False, on_delete=models.CASCADE)
    BINDING_bodySite = 'TODO'
    bodySite_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_bodySite}, related_name='ImagingSelection_bodySite', blank=True)
    bodySite_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    bodySite_BodyStructure_ref = models.ForeignKey("FHIR_BodyStructure", related_name="ImagingSelection_bodySite_BodyStructure", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ImagingSelection_instance(models.Model):
    ImagingSelection = models.ForeignKey(FHIR_ImagingSelection, related_name='ImagingSelection_instance', null=False, on_delete=models.CASCADE)
    uid = FHIR_primitive_IdField(null=True, blank=True, )
    number = FHIR_primitive_UnsignedIntField(null=True, blank=True, )
    sopClass = FHIR_primitive_OID_Field(null=True, blank=True, )

class FHIR_ImagingSelection_instance_subset(models.Model):
    ImagingSelection_instance = models.ForeignKey(FHIR_ImagingSelection_instance, related_name='ImagingSelection_instance_subset', null=False, on_delete=models.CASCADE)
    
    subset = FHIR_primitive_StringField(null=True, blank=True, )
    
class FHIR_ImagingSelection_instance_imageRegion2D(models.Model):
    ImagingSelection_instance = models.ForeignKey(FHIR_ImagingSelection_instance, related_name='ImagingSelection_instance_imageRegion2D', null=False, on_delete=models.CASCADE)
    class RegiontypeChoices(models.TextChoices): POINT = 'point', 'Point'; POLYLINE = 'polyline', 'Polyline'; MULTIPOINT = 'multipoint', 'Multipoint'; CIRCLE = 'circle', 'Circle'; ELLIPSE = 'ellipse', 'Ellipse'; 
    regionType = FHIR_primitive_CodeField(choices=RegiontypeChoices.choices, null=True, blank=True, )

class FHIR_ImagingSelection_instance_imageRegion2D_coordinate(models.Model):
    ImagingSelection_instance_imageRegion2D = models.ForeignKey(FHIR_ImagingSelection_instance_imageRegion2D, related_name='ImagingSelection_instance_imageRegion2D_coordinate', null=False, on_delete=models.CASCADE)
    
    coordinate = FHIR_primitive_DecimalField(null=True, blank=True, )
    
class FHIR_ImagingSelection_imageRegion3D(models.Model):
    ImagingSelection = models.ForeignKey(FHIR_ImagingSelection, related_name='ImagingSelection_imageRegion3D', null=False, on_delete=models.CASCADE)
    class RegiontypeChoices(models.TextChoices): POINT = 'point', 'Point'; MULTIPOINT = 'multipoint', 'Multipoint'; POLYLINE = 'polyline', 'Polyline'; POLYGON = 'polygon', 'Polygon'; ELLIPSE = 'ellipse', 'Ellipse'; ELLIPSOID = 'ellipsoid', 'Ellipsoid'; 
    regionType = FHIR_primitive_CodeField(choices=RegiontypeChoices.choices, null=True, blank=True, )

class FHIR_ImagingSelection_imageRegion3D_coordinate(models.Model):
    ImagingSelection_imageRegion3D = models.ForeignKey(FHIR_ImagingSelection_imageRegion3D, related_name='ImagingSelection_imageRegion3D_coordinate', null=False, on_delete=models.CASCADE)
    
    coordinate = FHIR_primitive_DecimalField(null=True, blank=True, )
    