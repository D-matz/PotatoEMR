#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_ImagingStudy(models.Model):
    class StatusChoices(models.TextChoices): REGISTERED = 'registered', 'Registered'; AVAILABLE = 'available', 'Available'; CANCELLED = 'cancelled', 'Cancelled'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; UNKNOWN = 'unknown', 'Unknown'; INACTIVE = 'inactive', 'Inactive'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    subject_Patient = models.ForeignKey("FHIR_Patient", related_name="ImagingStudy_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Device = models.ForeignKey("FHIR_Device", related_name="ImagingStudy_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Group = models.ForeignKey("FHIR_Group", related_name="ImagingStudy_subject", null=True, blank=True, on_delete=models.SET_NULL)
    encounter = models.ForeignKey("FHIR_Encounter", related_name="ImagingStudy_encounter", null=True, blank=True, on_delete=models.SET_NULL)
    started = FHIR_primitive_DateTimeField(null=True, blank=True, )
    basedOn_CarePlan = models.ManyToManyField("FHIR_CarePlan", related_name="ImagingStudy_basedOn", blank=True)
    basedOn_ServiceRequest = models.ManyToManyField("FHIR_ServiceRequest", related_name="ImagingStudy_basedOn", blank=True)
    basedOn_Appointment = models.ManyToManyField("FHIR_Appointment", related_name="ImagingStudy_basedOn", blank=True)
    basedOn_Task = models.ManyToManyField("FHIR_Task", related_name="ImagingStudy_basedOn", blank=True)
    partOf = models.ManyToManyField("FHIR_Procedure", related_name="ImagingStudy_partOf", blank=True)
    referrer_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="ImagingStudy_referrer", null=True, blank=True, on_delete=models.SET_NULL)
    referrer_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="ImagingStudy_referrer", null=True, blank=True, on_delete=models.SET_NULL)
    endpoint = models.ManyToManyField("FHIR_Endpoint", related_name="ImagingStudy_endpoint", blank=True)
    location = models.ForeignKey("FHIR_Location", related_name="ImagingStudy_location", null=True, blank=True, on_delete=models.SET_NULL)
    description = FHIR_primitive_StringField(null=True, blank=True, )
    numberOfSeries = FHIR_primitive_UnsignedIntField(null=True, blank=True, )
    numberOfInstances = FHIR_primitive_UnsignedIntField(null=True, blank=True, )

class FHIR_ImagingStudy_identifier(FHIR_GP_Identifier):
    ImagingStudy = models.ForeignKey(FHIR_ImagingStudy, related_name='ImagingStudy_identifier', null=False, on_delete=models.CASCADE)

class FHIR_ImagingStudy_modality(models.Model):
    ImagingStudy = models.ForeignKey(FHIR_ImagingStudy, related_name='ImagingStudy_modality', null=False, on_delete=models.CASCADE)
    BINDING_modality = "TODO"
    modality_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_modality}, related_name='ImagingStudy_modality', blank=True)
    modality_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ImagingStudy_procedure(models.Model):
    ImagingStudy = models.ForeignKey(FHIR_ImagingStudy, related_name='ImagingStudy_procedure', null=False, on_delete=models.CASCADE)
    BINDING_procedure = "TODO"
    procedure_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_procedure}, related_name='ImagingStudy_procedure', blank=True)
    procedure_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    procedure_PlanDefinition_ref = models.ForeignKey("FHIR_PlanDefinition", related_name="ImagingStudy_procedure_PlanDefinition", null=True, blank=True, on_delete=models.SET_NULL)
    procedure_ActivityDefinition_ref = models.ForeignKey("FHIR_ActivityDefinition", related_name="ImagingStudy_procedure_ActivityDefinition", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ImagingStudy_reason(models.Model):
    ImagingStudy = models.ForeignKey(FHIR_ImagingStudy, related_name='ImagingStudy_reason', null=False, on_delete=models.CASCADE)
    BINDING_reason = "TODO"
    reason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_reason}, related_name='ImagingStudy_reason', blank=True)
    reason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    reason_Condition_ref = models.ForeignKey("FHIR_Condition", related_name="ImagingStudy_reason_Condition", null=True, blank=True, on_delete=models.SET_NULL)
    reason_Observation_ref = models.ForeignKey("FHIR_Observation", related_name="ImagingStudy_reason_Observation", null=True, blank=True, on_delete=models.SET_NULL)
    reason_DiagnosticReport_ref = models.ForeignKey("FHIR_DiagnosticReport", related_name="ImagingStudy_reason_DiagnosticReport", null=True, blank=True, on_delete=models.SET_NULL)
    reason_DocumentReference_ref = models.ForeignKey("FHIR_DocumentReference", related_name="ImagingStudy_reason_DocumentReference", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ImagingStudy_note(FHIR_GP_Annotation):
    ImagingStudy = models.ForeignKey(FHIR_ImagingStudy, related_name='ImagingStudy_note', null=False, on_delete=models.CASCADE)

class FHIR_ImagingStudy_series(models.Model):
    ImagingStudy = models.ForeignKey(FHIR_ImagingStudy, related_name='ImagingStudy_series', null=False, on_delete=models.CASCADE)
    uid = FHIR_primitive_IdField(null=True, blank=True, )
    number = FHIR_primitive_UnsignedIntField(null=True, blank=True, )
    BINDING_modality = "TODO"
    modality_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_modality}, related_name='ImagingStudy_series_modality', blank=True)
    modality_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    description = FHIR_primitive_StringField(null=True, blank=True, )
    numberOfInstances = FHIR_primitive_UnsignedIntField(null=True, blank=True, )
    endpoint = models.ManyToManyField("FHIR_Endpoint", related_name="ImagingStudy_series_endpoint", blank=True)
    BINDING_bodySite = "TODO"
    bodySite_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_bodySite}, related_name='ImagingStudy_series_bodySite', blank=True)
    bodySite_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    bodySite_BodyStructure_ref = models.ForeignKey("FHIR_BodyStructure", related_name="ImagingStudy_series_bodySite_BodyStructure", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_laterality = "TODO"
    laterality_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_laterality}, related_name='ImagingStudy_series_laterality', blank=True)
    laterality_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    specimen = models.ManyToManyField("FHIR_Specimen", related_name="ImagingStudy_series_specimen", blank=True)
    started = FHIR_primitive_DateTimeField(null=True, blank=True, )

class FHIR_ImagingStudy_series_performer(models.Model):
    ImagingStudy_series = models.ForeignKey(FHIR_ImagingStudy_series, related_name='ImagingStudy_series_performer', null=False, on_delete=models.CASCADE)
    BINDING_function = "TODO"
    function_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_function}, related_name='ImagingStudy_series_performer_function', blank=True)
    function_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    actor_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="ImagingStudy_series_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="ImagingStudy_series_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Organization = models.ForeignKey("FHIR_Organization", related_name="ImagingStudy_series_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_CareTeam = models.ForeignKey("FHIR_CareTeam", related_name="ImagingStudy_series_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Patient = models.ForeignKey("FHIR_Patient", related_name="ImagingStudy_series_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Device = models.ForeignKey("FHIR_Device", related_name="ImagingStudy_series_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="ImagingStudy_series_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_HealthcareService = models.ForeignKey("FHIR_HealthcareService", related_name="ImagingStudy_series_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ImagingStudy_series_instance(models.Model):
    ImagingStudy_series = models.ForeignKey(FHIR_ImagingStudy_series, related_name='ImagingStudy_series_instance', null=False, on_delete=models.CASCADE)
    uid = FHIR_primitive_IdField(null=True, blank=True, )
    sopClass = FHIR_primitive_OID_Field(null=True, blank=True, )
    number = FHIR_primitive_UnsignedIntField(null=True, blank=True, )
    title = FHIR_primitive_StringField(null=True, blank=True, )
