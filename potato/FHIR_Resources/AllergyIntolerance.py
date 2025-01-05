from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *

class FHIR_AllergyIntolerance(models.Model):
    clinical_status = models.OneToOneField(FHIR_GP_CodeableConcept, on_delete=models.SET_NULL, null=True, blank=True, related_name='allergyintolerance_clinicalstatus')
    clinical_status.Binding = ["http://terminology.hl7.org/CodeSystem/allergyintolerance-clinical"]
    verification_status = models.OneToOneField(FHIR_GP_CodeableConcept, on_delete=models.SET_NULL, null=True, blank=True, related_name='allergyintolerance_verificationstatus')
    verification_status.Binding = ["http://terminology.hl7.org/CodeSystem/allergyintolerance-verification"]
    type = models.OneToOneField(FHIR_GP_CodeableConcept, on_delete=models.SET_NULL, null=True, blank=True, related_name='allergyintolerance_type')
    type.Binding = ["http://hl7.org/fhir/allergy-intolerance-type"]
    category = models.ManyToManyField(FHIR_GP_CodeableConcept, through='FHIR_AllergyIntolerance_CategoryThrough', blank=True, related_name='allergyintolerance_category')
    criticality = models.ForeignKey(FHIR_GP_CodeableConcept, on_delete=models.SET_NULL, null=True, blank=True, related_name='allergyintolerance_criticality')
    code = models.OneToOneField(FHIR_GP_CodeableConcept, on_delete=models.SET_NULL, null=True, blank=True, related_name='allergyintolerance_code')
    patient = models.ForeignKey('FHIR_Patient', on_delete=models.CASCADE, null=False)
    encounter = models.ForeignKey('FHIR_Encounter', on_delete=models.SET_NULL, null=True, blank=True)
    onset_dateTime = FHIR_primitive_DateTimeField(null=True, blank=True)
    onset_age = models.OneToOneField(FHIR_GP_Quantity_Age, on_delete=models.SET_NULL, null=True, blank=True)
    onset_period = models.OneToOneField(FHIR_GP_Period, on_delete=models.SET_NULL, null=True, blank=True)
    onset_range = models.OneToOneField(FHIR_GP_Range, on_delete=models.SET_NULL, null=True, blank=True)
    onset_string = FHIR_primitive_StringField(max_length=255, null=True, blank=True)
    recordedDate = FHIR_primitive_DateTimeField(null=True, blank=True)
    lastOccurrence = FHIR_primitive_DateTimeField(null=True, blank=True)
    #could add precision to onset_dateTime, recordedDate, lastOccurrence

class FHIR_AllergyIntolerance_Identifier(FHIR_GP_Identifier):
    allergy_intolerance = models.ForeignKey(FHIR_AllergyIntolerance, on_delete=models.CASCADE, related_name='identifiers')

class FHIR_AllergyIntolerance_CategoryThrough(models.Model):
    #no change to default ManyToManyField except for enforcing Binding on category codings
    allergy_intolerance = models.ForeignKey('FHIR_AllergyIntolerance', on_delete=models.CASCADE)
    category = models.ForeignKey(FHIR_GP_CodeableConcept, on_delete=models.CASCADE)
    category.Binding = ["http://hl7.org/fhir/allergy-intolerance-category"]

class FHIR_AllergyIntolerance_Participant(models.Model):
    allergy_intolerance = models.ForeignKey(FHIR_AllergyIntolerance, on_delete=models.CASCADE)
    function = models.OneToOneField(FHIR_GP_CodeableConcept, on_delete=models.SET_NULL, null=True, blank=True, related_name='allergyintolerance_participant_function')
    function.Binding = ["http://terminology.hl7.org/CodeSystem/provenance-participant-type", "http://dicom.nema.org/resources/ontology/DCM", "	http://terminology.hl7.org/CodeSystem/extra-security-role-type"]
    actor_practitioner = models.ForeignKey('FHIR_Practitioner', null=True, on_delete=models.SET_NULL)
    actor_practitionerRole = models.ForeignKey('FHIR_PractitionerRole', null=True, on_delete=models.SET_NULL) 
    actor_patient = models.ForeignKey('FHIR_Patient', null=True, on_delete=models.SET_NULL)
    actor_relatedPerson = models.ForeignKey('FHIR_RelatedPerson', null=True, on_delete=models.SET_NULL)
    actor_device = models.ForeignKey('FHIR_Device', null=True, on_delete=models.SET_NULL)
    actor_organization = models.ForeignKey('FHIR_Organization', null=True, on_delete=models.SET_NULL)
    actor_careTeam = models.ForeignKey('FHIR_CareTeam', null=True, on_delete=models.SET_NULL)

class FHIR_AllergyIntolerance_Note(FHIR_GP_Annotation):
    allergy_intolerance = models.ForeignKey(FHIR_AllergyIntolerance, on_delete=models.CASCADE)

class FHIR_AllergyIntolerance_Reaction(models.Model):
    allergy_intolerance = models.ForeignKey(FHIR_AllergyIntolerance, on_delete=models.CASCADE)
    substance = models.OneToOneField(FHIR_GP_CodeableConcept, on_delete=models.SET_NULL, null=True, blank=True, related_name='allergyintolerance_reaction_substance')
    substance.Binding = ["http://snomed.info/sct"]
    manifestation = models.ManyToManyField('FHIR_Observation')
    manifestation.idkwhatdependsonobservation = ["http://snomed.info/sct"]
    description = FHIR_primitive_StringField(max_length=10000, null=True, blank=True)
    onset = FHIR_primitive_DateTimeField(null=True, blank=True)
    severity = FHIR_primitive_CodeField(max_length=10)
    exposureRoute = models.OneToOneField(FHIR_GP_CodeableConcept, on_delete=models.SET_NULL, null=True, blank=True, related_name='allergyintolerance_reaction_exposureroute')
    exposureRoute.Binding = ["http://snomed.info/sct"]

class FHIR_AllergyIntolerance_Reaction_Note(FHIR_GP_Annotation):
    reaction = models.ForeignKey(FHIR_AllergyIntolerance_Reaction, on_delete=models.CASCADE)
