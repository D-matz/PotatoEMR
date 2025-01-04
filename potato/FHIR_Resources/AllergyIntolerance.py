from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *

class FHIR_AllergyIntolerance(models.Model):
    class CategoryChoices(models.TextChoices): FOOD='food','Food'; MEDICATION='medication','Medication'; ENVIRONMENT='environment','Environment'; BIOLOGIC='biologic','Biologic'
    class CriticalityChoices(models.TextChoices): LOW='low','Low'; HIGH='high','High'; UNABLE='unable-to-assess','Unable to Assess'
    class SeverityChoices(models.TextChoices): MILD='mild','Mild'; MODERATE='moderate','Moderate'; SEVERE='severe','Severe'
    
    clinical_status = models.OneToOneField(FHIR_GP_CodeableConcept, on_delete=models.SET_NULL, null=True, blank=True, related_name='allergy_clinical_status')
    verification_status = models.OneToOneField(FHIR_GP_CodeableConcept, on_delete=models.SET_NULL, null=True, blank=True, related_name='allergy_verification_status')
    type = models.OneToOneField(FHIR_GP_CodeableConcept, on_delete=models.SET_NULL, null=True, blank=True, related_name='allergy_type')
    category = FHIR_primitive_CodeField(max_length=20, choices=CategoryChoices.choices, null=True, blank=True)
    criticality = FHIR_primitive_CodeField(max_length=20, choices=CriticalityChoices.choices, null=True, blank=True)
    code = models.OneToOneField(FHIR_GP_CodeableConcept, on_delete=models.SET_NULL, null=True, blank=True, related_name='allergy_code')
    patient = models.ForeignKey('FHIR_Patient', on_delete=models.CASCADE)
    encounter = models.ForeignKey('FHIR_Encounter', on_delete=models.SET_NULL, null=True, blank=True)
    onset_dateTime = FHIR_primitive_DateTimeField(null=True, blank=True)
    onset_age = models.OneToOneField(FHIR_GP_Quantity_Age, on_delete=models.SET_NULL, null=True, blank=True, related_name='allergy_onset_age')
    onset_period = models.OneToOneField(FHIR_GP_Period, on_delete=models.SET_NULL, null=True, blank=True, related_name='allergy_onset_period')
    onset_range = models.OneToOneField(FHIR_GP_Range, on_delete=models.SET_NULL, null=True, blank=True, related_name='allergy_onset_range')
    onset_string = FHIR_primitive_StringField(max_length=255, null=True, blank=True)
    recorded_date = FHIR_primitive_DateTimeField(null=True, blank=True)
    last_occurrence = FHIR_primitive_DateTimeField(null=True, blank=True)


class FHIR_AllergyIntolerance_Category(models.Model):
    allergy_intolerance = models.ForeignKey(FHIR_AllergyIntolerance, on_delete=models.CASCADE, related_name='categories')
    value = FHIR_primitive_CodeField(max_length=20, choices=FHIR_AllergyIntolerance.CategoryChoices.choices)

class FHIR_AllergyIntolerance_Identifier(FHIR_GP_Identifier):
    allergy_intolerance = models.ForeignKey(FHIR_AllergyIntolerance, on_delete=models.CASCADE, related_name='identifiers')

class FHIR_AllergyIntolerance_Note(FHIR_GP_Annotation):
    allergy_intolerance = models.ForeignKey(FHIR_AllergyIntolerance, on_delete=models.CASCADE, related_name='notes')

class FHIR_AllergyIntolerance_Participant(models.Model):
    allergy_intolerance = models.ForeignKey(FHIR_AllergyIntolerance, on_delete=models.CASCADE)
    function = models.OneToOneField(FHIR_GP_CodeableConcept, on_delete=models.SET_NULL, null=True, blank=True)
    actor_practitioner = models.ForeignKey('FHIR_Practitioner', null=True, on_delete=models.SET_NULL)
    actor_practitionerRole = models.ForeignKey('FHIR_PractitionerRole', null=True, on_delete=models.SET_NULL)
    actor_patient = models.ForeignKey('FHIR_Patient', null=True, on_delete=models.SET_NULL)
    actor_relatedPerson = models.ForeignKey('FHIR_RelatedPerson', null=True, on_delete=models.SET_NULL)
    actor_device = models.ForeignKey('FHIR_Device', null=True, on_delete=models.SET_NULL)
    actor_organization = models.ForeignKey('FHIR_Organization', null=True, on_delete=models.SET_NULL)
    actor_careTeam = models.ForeignKey('FHIR_CareTeam', null=True, on_delete=models.SET_NULL)

class FHIR_AllergyIntolerance_Reaction(models.Model):
    allergy_intolerance = models.ForeignKey(FHIR_AllergyIntolerance, on_delete=models.CASCADE)
    substance = models.OneToOneField(FHIR_GP_CodeableConcept, on_delete=models.SET_NULL, null=True, blank=True, related_name='reaction_substance')
    description = FHIR_primitive_StringField(max_length=1000, null=True, blank=True)
    onset = FHIR_primitive_DateTimeField(null=True, blank=True)
    severity = FHIR_primitive_CodeField(max_length=10, choices=FHIR_AllergyIntolerance.SeverityChoices.choices, null=True, blank=True)
    exposure_route = models.OneToOneField(FHIR_GP_CodeableConcept, on_delete=models.SET_NULL, null=True, blank=True, related_name='reaction_exposure_route')

class FHIR_AllergyIntolerance_Reaction_Manifestation(models.Model):
    reaction = models.ForeignKey(FHIR_AllergyIntolerance_Reaction, on_delete=models.CASCADE, related_name='manifestations')
    observation = models.ForeignKey('FHIR_Observation', on_delete=models.CASCADE)
    concept = models.OneToOneField(FHIR_GP_CodeableConcept, on_delete=models.CASCADE)

class FHIR_AllergyIntolerance_Reaction_Note(FHIR_GP_Annotation):
    reaction = models.ForeignKey(FHIR_AllergyIntolerance_Reaction, on_delete=models.CASCADE, related_name='notes')
    