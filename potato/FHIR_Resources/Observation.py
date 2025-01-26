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

    status = FHIR_primitive_CodeField(max_length=20, choices=[
        ('registered', 'Registered'),
        ('preliminary', 'Preliminary'),
        ('final', 'Final'),
        ('amended', 'Amended'),
        ('corrected', 'Corrected'),
        ('cancelled', 'Cancelled'),
        ('entered-in-error', 'Entered in Error'),
        ('unknown', 'Unknown'),
    ], null=False, blank=False, default='unknown')

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

    status = FHIR_primitive_CodeField(max_length=20, choices=[
        ('registered', 'Registered'),
        ('preliminary', 'Preliminary'),
        ('final', 'Final'),
        ('amended', 'Amended'),
        ('corrected', 'Corrected'),
        ('cancelled', 'Cancelled'),
        ('entered-in-error', 'Entered in Error'),
        ('unknown', 'Unknown'),
    ], null=False, blank=False, default='unknown')

    category = models.ManyToManyField('FHIR_GP_Coding', related_name="observation_category", blank=True,
        limit_choices_to={'binding__binding_rule': 'https://www.hl7.org/fhir/valueset-observation-category.html'})
    code = models.ManyToManyField('FHIR_GP_Coding', related_name="observation_code", blank=True,
        limit_choices_to={'binding__binding_rule': 'https://www.hl7.org/fhir/valueset-observation-codes.html'})
    
    subject_patient = models.ForeignKey('FHIR_Patient', related_name="observation_subject_patient", on_delete=models.SET_NULL, null=True, blank=True)
    subject_group = models.ForeignKey('FHIR_Group', related_name="observation_subject_group", on_delete=models.SET_NULL, null=True, blank=True)
    subject_device = models.ForeignKey('FHIR_Device', related_name="observation_subject_device", on_delete=models.SET_NULL, null=True, blank=True)
    subject_location = models.ForeignKey('FHIR_Location', related_name="observation_subject_location", on_delete=models.SET_NULL, null=True, blank=True)
    subject_organization = models.ForeignKey('FHIR_Organization', related_name="observation_subject_organization", on_delete=models.SET_NULL, null=True, blank=True)
    subject_procedure = models.ForeignKey('FHIR_Procedure', related_name="observation_subject_procedure", on_delete=models.SET_NULL, null=True, blank=True)
    subject_practitioner = models.ForeignKey('FHIR_Practitioner', related_name="observation_subject_practitioner", on_delete=models.SET_NULL, null=True, blank=True)
    subject_practitionerRole = models.ForeignKey('FHIR_PractitionerRole', related_name="observation_subject_practitionerRole", on_delete=models.SET_NULL, null=True, blank=True)
    subject_relatedPerson = models.ForeignKey('FHIR_RelatedPerson', related_name="observation_subject_relatedPerson", on_delete=models.SET_NULL, null=True, blank=True)
    subject_medication = models.ForeignKey('FHIR_Medication', related_name="observation_subject_medication", on_delete=models.SET_NULL, null=True, blank=True)
    subject_substance = models.ForeignKey('FHIR_Substance', related_name="observation_subject_substance", on_delete=models.SET_NULL, null=True, blank=True)
    subject_biologicallyDerivedProduct = models.ForeignKey('FHIR_BiologicallyDerivedProduct', related_name="observation_subject_biologicallyDerivedProduct", on_delete=models.SET_NULL, null=True, blank=True)
    subject_nutritionProduct = models.ForeignKey('FHIR_NutritionProduct', related_name="observation_subject_nutritionProduct", on_delete=models.SET_NULL, null=True, blank=True)

    # Focus field that can reference any FHIR resource...will figure out later

    encounter = models.ForeignKey('FHIR_Encounter', related_name="observation_encounter", on_delete=models.SET_NULL, null=True, blank=True)

    effective_dateTime = FHIR_primitive_DateTimeField(null=True, blank=True)
    effective_period = models.OneToOneField('FHIR_GP_Period', related_name="observation_effective_period", on_delete=models.SET_NULL, null=True, blank=True)
    effective_timing = models.OneToOneField('FHIR_GP_Timing', related_name="observation_effective_timing", on_delete=models.SET_NULL, null=True, blank=True)
    effective_string = FHIR_primitive_StringField(max_length=255, null=True, blank=True)

    