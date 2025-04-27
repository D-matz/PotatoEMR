#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_DeviceUsage(models.Model):
    basedOn = models.ManyToManyField("FHIR_ServiceRequest", related_name="DeviceUsage_basedOn", blank=True)
    class StatusChoices(models.TextChoices): ACTIVE = 'active', 'Active'; COMPLETED = 'completed', 'Completed'; NOT_DONE = 'not-done', 'Not-done'; ENTERED_IN_ERROR_PLUS = 'entered-in-error +', 'Entered-in-error +'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    patient = models.ForeignKey("FHIR_Patient", related_name="DeviceUsage_patient", null=True, blank=True, on_delete=models.SET_NULL)
    derivedFrom_ServiceRequest = models.ManyToManyField("FHIR_ServiceRequest", related_name="DeviceUsage_derivedFrom", blank=True)
    derivedFrom_Procedure = models.ManyToManyField("FHIR_Procedure", related_name="DeviceUsage_derivedFrom", blank=True)
    derivedFrom_Claim = models.ManyToManyField("FHIR_Claim", related_name="DeviceUsage_derivedFrom", blank=True)
    derivedFrom_Observation = models.ManyToManyField("FHIR_Observation", related_name="DeviceUsage_derivedFrom", blank=True)
    derivedFrom_QuestionnaireResponse = models.ManyToManyField("FHIR_QuestionnaireResponse", related_name="DeviceUsage_derivedFrom", blank=True)
    derivedFrom_DocumentReference = models.ManyToManyField("FHIR_DocumentReference", related_name="DeviceUsage_derivedFrom", blank=True)
    context_Encounter = models.ForeignKey("FHIR_Encounter", related_name="DeviceUsage_context", null=True, blank=True, on_delete=models.SET_NULL)
    context_EpisodeOfCare = models.ForeignKey("FHIR_EpisodeOfCare", related_name="DeviceUsage_context", null=True, blank=True, on_delete=models.SET_NULL)
    timing = models.OneToOneField("FHIR_GP_Timing", related_name='DeviceUsage_timing', null=True, blank=True, on_delete=models.SET_NULL)
    timing = models.OneToOneField("FHIR_GP_Period", related_name='DeviceUsage_timing', null=True, blank=True, on_delete=models.SET_NULL)
    timing = FHIR_primitive_DateTimeField(null=True, blank=True, )
    dateAsserted = FHIR_primitive_DateTimeField(null=True, blank=True, )
    BINDING_usageStatus = 'TODO'
    usageStatus_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_usageStatus}, related_name='DeviceUsage_usageStatus', blank=True)
    usageStatus_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    informationSource_Patient = models.ForeignKey("FHIR_Patient", related_name="DeviceUsage_informationSource", null=True, blank=True, on_delete=models.SET_NULL)
    informationSource_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="DeviceUsage_informationSource", null=True, blank=True, on_delete=models.SET_NULL)
    informationSource_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="DeviceUsage_informationSource", null=True, blank=True, on_delete=models.SET_NULL)
    informationSource_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="DeviceUsage_informationSource", null=True, blank=True, on_delete=models.SET_NULL)
    informationSource_Organization = models.ForeignKey("FHIR_Organization", related_name="DeviceUsage_informationSource", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_device = 'TODO'
    device_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_device}, related_name='DeviceUsage_device', blank=True)
    device_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    device_Device_ref = models.ForeignKey("FHIR_Device", related_name="DeviceUsage_device_Device", null=True, blank=True, on_delete=models.SET_NULL)
    device_DeviceDefinition_ref = models.ForeignKey("FHIR_DeviceDefinition", related_name="DeviceUsage_device_DeviceDefinition", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_bodySite = 'TODO'
    bodySite_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_bodySite}, related_name='DeviceUsage_bodySite', blank=True)
    bodySite_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    bodySite_BodyStructure_ref = models.ForeignKey("FHIR_BodyStructure", related_name="DeviceUsage_bodySite_BodyStructure", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_DeviceUsage_identifier(FHIR_GP_Identifier):
    DeviceUsage = models.ForeignKey(FHIR_DeviceUsage, related_name='DeviceUsage_identifier', null=False, on_delete=models.CASCADE)

class FHIR_DeviceUsage_category(models.Model):
    DeviceUsage = models.ForeignKey(FHIR_DeviceUsage, related_name='DeviceUsage_category', null=False, on_delete=models.CASCADE)
    BINDING_category = 'TODO'
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='DeviceUsage_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_DeviceUsage_usageReason(models.Model):
    DeviceUsage = models.ForeignKey(FHIR_DeviceUsage, related_name='DeviceUsage_usageReason', null=False, on_delete=models.CASCADE)
    BINDING_usageReason = 'TODO'
    usageReason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_usageReason}, related_name='DeviceUsage_usageReason', blank=True)
    usageReason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_DeviceUsage_adherence(models.Model):
    DeviceUsage = models.ForeignKey(FHIR_DeviceUsage, related_name='DeviceUsage_adherence', null=False, on_delete=models.CASCADE)
    BINDING_code = 'TODO'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='DeviceUsage_adherence_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_DeviceUsage_adherence_reason(models.Model):
    DeviceUsage_adherence = models.ForeignKey(FHIR_DeviceUsage_adherence, related_name='DeviceUsage_adherence_reason', null=False, on_delete=models.CASCADE)
    BINDING_reason = 'TODO'
    reason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_reason}, related_name='DeviceUsage_adherence_reason', blank=True)
    reason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_DeviceUsage_reason(models.Model):
    DeviceUsage = models.ForeignKey(FHIR_DeviceUsage, related_name='DeviceUsage_reason', null=False, on_delete=models.CASCADE)
    BINDING_reason = 'TODO'
    reason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_reason}, related_name='DeviceUsage_reason', blank=True)
    reason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    reason_Condition_ref = models.ForeignKey("FHIR_Condition", related_name="DeviceUsage_reason_Condition", null=True, blank=True, on_delete=models.SET_NULL)
    reason_Observation_ref = models.ForeignKey("FHIR_Observation", related_name="DeviceUsage_reason_Observation", null=True, blank=True, on_delete=models.SET_NULL)
    reason_DiagnosticReport_ref = models.ForeignKey("FHIR_DiagnosticReport", related_name="DeviceUsage_reason_DiagnosticReport", null=True, blank=True, on_delete=models.SET_NULL)
    reason_DocumentReference_ref = models.ForeignKey("FHIR_DocumentReference", related_name="DeviceUsage_reason_DocumentReference", null=True, blank=True, on_delete=models.SET_NULL)
    reason_Procedure_ref = models.ForeignKey("FHIR_Procedure", related_name="DeviceUsage_reason_Procedure", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_DeviceUsage_note(FHIR_GP_Annotation):
    DeviceUsage = models.ForeignKey(FHIR_DeviceUsage, related_name='DeviceUsage_note', null=False, on_delete=models.CASCADE)
