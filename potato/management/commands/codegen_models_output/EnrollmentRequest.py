
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_EnrollmentRequest(models.Model):
    class StatusChoices(models.TextChoices): ACTIVE = 'active', 'Active'; CANCELLED = 'cancelled', 'Cancelled'; DRAFT = 'draft', 'Draft'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    created = FHIR_primitive_DateTimeField(null=True, blank=True, )
    insurer = models.ForeignKey("FHIR_Organization", related_name="EnrollmentRequest_insurer", null=True, blank=True, on_delete=models.SET_NULL)
    provider_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="EnrollmentRequest_provider", null=True, blank=True, on_delete=models.SET_NULL)
    provider_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="EnrollmentRequest_provider", null=True, blank=True, on_delete=models.SET_NULL)
    provider_Organization = models.ForeignKey("FHIR_Organization", related_name="EnrollmentRequest_provider", null=True, blank=True, on_delete=models.SET_NULL)
    candidate = models.ForeignKey("FHIR_Patient", related_name="EnrollmentRequest_candidate", null=True, blank=True, on_delete=models.SET_NULL)
    coverage = models.ForeignKey("FHIR_Coverage", related_name="EnrollmentRequest_coverage", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_EnrollmentRequest_identifier(FHIR_GP_Identifier):
    EnrollmentRequest = models.ForeignKey(FHIR_EnrollmentRequest, related_name='EnrollmentRequest_identifier', null=False, on_delete=models.CASCADE)
