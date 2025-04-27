#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_EnrollmentResponse(models.Model):
    class StatusChoices(models.TextChoices): ACTIVE = 'active', 'Active'; CANCELLED = 'cancelled', 'Cancelled'; DRAFT = 'draft', 'Draft'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    request = models.ForeignKey("FHIR_EnrollmentRequest", related_name="EnrollmentResponse_request", null=True, blank=True, on_delete=models.SET_NULL)
    class OutcomeChoices(models.TextChoices): QUEUED = 'queued', 'Queued'; COMPLETE = 'complete', 'Complete'; ERROR = 'error', 'Error'; PARTIAL = 'partial', 'Partial'; 
    outcome = FHIR_primitive_CodeField(choices=OutcomeChoices.choices, null=True, blank=True, )
    disposition = FHIR_primitive_StringField(null=True, blank=True, )
    created = FHIR_primitive_DateTimeField(null=True, blank=True, )
    organization = models.ForeignKey("FHIR_Organization", related_name="EnrollmentResponse_organization", null=True, blank=True, on_delete=models.SET_NULL)
    requestProvider_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="EnrollmentResponse_requestProvider", null=True, blank=True, on_delete=models.SET_NULL)
    requestProvider_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="EnrollmentResponse_requestProvider", null=True, blank=True, on_delete=models.SET_NULL)
    requestProvider_Organization = models.ForeignKey("FHIR_Organization", related_name="EnrollmentResponse_requestProvider", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_EnrollmentResponse_identifier(FHIR_GP_Identifier):
    EnrollmentResponse = models.ForeignKey(FHIR_EnrollmentResponse, related_name='EnrollmentResponse_identifier', null=False, on_delete=models.CASCADE)
