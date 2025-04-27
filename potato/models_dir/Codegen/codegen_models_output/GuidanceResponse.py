#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_GuidanceResponse(models.Model):
    requestIdentifier = models.OneToOneField("FHIR_GP_Identifier", related_name='GuidanceResponse_requestIdentifier', null=True, blank=True, on_delete=models.SET_NULL)
    module = FHIR_primitive_URIField(null=True, blank=True, )
    module = FHIR_primitive_CanonicalField(null=True, blank=True, )
    BINDING_module = "TODO"
    module_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_module}, related_name='GuidanceResponse_module', blank=True)
    module_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    class StatusChoices(models.TextChoices): SUCCESS = 'success', 'Success'; DATA_REQUESTED = 'data-requested', 'Data-requested'; DATA_REQUIRED = 'data-required', 'Data-required'; IN_PROGRESS = 'in-progress', 'In-progress'; FAILURE = 'failure', 'Failure'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    subject_Patient = models.ForeignKey("FHIR_Patient", related_name="GuidanceResponse_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Group = models.ForeignKey("FHIR_Group", related_name="GuidanceResponse_subject", null=True, blank=True, on_delete=models.SET_NULL)
    encounter = models.ForeignKey("FHIR_Encounter", related_name="GuidanceResponse_encounter", null=True, blank=True, on_delete=models.SET_NULL)
    occurrenceDateTime = FHIR_primitive_DateTimeField(null=True, blank=True, )
    performer = models.ForeignKey("FHIR_Device", related_name="GuidanceResponse_performer", null=True, blank=True, on_delete=models.SET_NULL)
    evaluationMessage = models.ForeignKey("FHIR_OperationOutcome", related_name="GuidanceResponse_evaluationMessage", null=True, blank=True, on_delete=models.SET_NULL)
    outputParameters = models.ForeignKey("FHIR_Parameters", related_name="GuidanceResponse_outputParameters", null=True, blank=True, on_delete=models.SET_NULL)
    result_Appointment = models.ManyToManyField("FHIR_Appointment", related_name="GuidanceResponse_result", blank=True)
    result_AppointmentResponse = models.ManyToManyField("FHIR_AppointmentResponse", related_name="GuidanceResponse_result", blank=True)
    result_CarePlan = models.ManyToManyField("FHIR_CarePlan", related_name="GuidanceResponse_result", blank=True)
    result_Claim = models.ManyToManyField("FHIR_Claim", related_name="GuidanceResponse_result", blank=True)
    result_CommunicationRequest = models.ManyToManyField("FHIR_CommunicationRequest", related_name="GuidanceResponse_result", blank=True)
    result_Contract = models.ManyToManyField("FHIR_Contract", related_name="GuidanceResponse_result", blank=True)
    result_CoverageEligibilityRequest = models.ManyToManyField("FHIR_CoverageEligibilityRequest", related_name="GuidanceResponse_result", blank=True)
    result_DeviceRequest = models.ManyToManyField("FHIR_DeviceRequest", related_name="GuidanceResponse_result", blank=True)
    result_EnrollmentRequest = models.ManyToManyField("FHIR_EnrollmentRequest", related_name="GuidanceResponse_result", blank=True)
    result_ImmunizationRecommendation = models.ManyToManyField("FHIR_ImmunizationRecommendation", related_name="GuidanceResponse_result", blank=True)
    result_MedicationRequest = models.ManyToManyField("FHIR_MedicationRequest", related_name="GuidanceResponse_result", blank=True)
    result_NutritionOrder = models.ManyToManyField("FHIR_NutritionOrder", related_name="GuidanceResponse_result", blank=True)
    result_RequestOrchestration = models.ManyToManyField("FHIR_RequestOrchestration", related_name="GuidanceResponse_result", blank=True)
    result_ServiceRequest = models.ManyToManyField("FHIR_ServiceRequest", related_name="GuidanceResponse_result", blank=True)
    result_SupplyRequest = models.ManyToManyField("FHIR_SupplyRequest", related_name="GuidanceResponse_result", blank=True)
    result_Task = models.ManyToManyField("FHIR_Task", related_name="GuidanceResponse_result", blank=True)
    result_VisionPrescription = models.ManyToManyField("FHIR_VisionPrescription", related_name="GuidanceResponse_result", blank=True)

class FHIR_GuidanceResponse_identifier(FHIR_GP_Identifier):
    GuidanceResponse = models.ForeignKey(FHIR_GuidanceResponse, related_name='GuidanceResponse_identifier', null=False, on_delete=models.CASCADE)

class FHIR_GuidanceResponse_note(FHIR_GP_Annotation):
    GuidanceResponse = models.ForeignKey(FHIR_GuidanceResponse, related_name='GuidanceResponse_note', null=False, on_delete=models.CASCADE)
