from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *

class FHIR_Observation(models.Model):
    #identifier foreign key to this
    #pattern similar to CodeableReference, where you can have general definition or reference specific instance
    #URL to a ObservationDefinition resource definition
    instantiates_canonical = FHIR_primitive_CanonicalField(max_length=1000, null=True, blank=True)
    #reference to a ObservationDefinition in database
    instantiates_reference = models.ForeignKey('FHIR_ObservationDefinition', related_name="observation_instantiates_reference", null=True, on_delete=models.SET_NULL)

    basedOn_carePlan = models.ManyToManyField('FHIR_CarePlan', related_name="observation_basedOn_carePlans", blank=True)
    basedOn_deviceRequest = models.ManyToManyField('FHIR_DeviceRequest', related_name="observation_basedOn_deviceRequests", blank=True)
    basedOn_immunizationRecommendation = models.ManyToManyField('FHIR_ImmunizationRecommendation', related_name="observation_basedOn_immunizationRecommendations", blank=True)
    basedOn_medicationRequest = models.ManyToManyField('FHIR_MedicationRequest', related_name="observation_basedOn_medicationRequests", blank=True)
    basedOn_nutritionOrder = models.ManyToManyField('FHIR_NutritionOrder', related_name="observation_basedOn_nutritionOrders", blank=True)
    basedOn_serviceRequest = models.ManyToManyField('FHIR_ServiceRequest', related_name="observation_basedOn_serviceRequests", blank=True)

    triggeredBy = models.ManyToManyField('self', through='TriggeredByThrough', symmetrical=False, related_name='triggeredBys')

class FHIR_Observation_Identifier(FHIR_GP_Identifier):
    observation = models.ForeignKey(FHIR_Observation, related_name="observation_identifiers", on_delete=models.CASCADE)

class TriggeredByThrough(models.Model):
    from_Observation = models.ForeignKey('FHIR_Observation', on_delete=models.CASCADE, related_name='observation')
    toTriggeredBy_Observation = models.ForeignKey('FHIR_Observation', on_delete=models.CASCADE, related_name='observation_triggeredBy')

    type = FHIR_primitive_CodeField(max_length=7, choices=[
        ('reflex', 'Reflex'),
        ('repeat', 'Repeat'),
        ('re-run', 'Re-run'),
    ], null=False, blank=False)
    reason = models.CharField(max_length=255, null=True, blank=True)

    partOf_medicationAdministration = models.ManyToManyField('FHIR_MedicationAdministration', related_name="observation_partOf_medicationAdministrations", blank=True)
    partOf_medicationDispense = models.ManyToManyField('FHIR_MedicationDispense', related_name="observation_partOf_medicationDispensers", blank=True)
    partOf_medicationStatement = models.ManyToManyField('FHIR_MedicationStatement', related_name="observation_partOf_medicationStatements", blank=True)
    partOf_procedure = models.ManyToManyField('FHIR_Procedure', related_name="observation_partOf_procedures", blank=True)
    partOf_immunization = models.ManyToManyField('FHIR_Immunization', related_name="observation_partOf_immunizations", blank=True)
    partOf_imagingStudy = models.ManyToManyField('FHIR_ImagingStudy', related_name="observation_partOf_imagingStudies", blank=True)
    partOf_genomicStudy = models.ManyToManyField('FHIR_GenomicStudy', related_name="observation_partOf_genomicStudies", blank=True)
