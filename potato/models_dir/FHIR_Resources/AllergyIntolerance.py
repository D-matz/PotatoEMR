
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_AllergyIntolerance(models.Model):
    BINDING_clinicalStatus = 'https://www.hl7.org/fhir/valueset-allergyintolerance-clinical.html'
    clinicalStatus_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_clinicalStatus}, related_name='AllergyIntolerance_clinicalStatus', blank=True)
    clinicalStatus_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_verificationStatus = 'https://www.hl7.org/fhir/valueset-allergyintolerance-verification.html'
    verificationStatus_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_verificationStatus}, related_name='AllergyIntolerance_verificationStatus', blank=True)
    verificationStatus_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_type = 'https://www.hl7.org/fhir/valueset-allergy-intolerance-type.html'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='AllergyIntolerance_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    class CriticalityChoices(models.TextChoices): LOW = 'low', 'Low'; HIGH = 'high', 'High'; UNABLE_TO_ASSESS = 'unable-to-assess', 'Unable-to-assess'; 
    criticality = FHIR_primitive_CodeField(choices=CriticalityChoices.choices, null=True, blank=True, )
    BINDING_code = 'https://www.hl7.org/fhir/valueset-allergyintolerance-code.html'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='AllergyIntolerance_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    patient = models.ForeignKey("FHIR_Patient", related_name="AllergyIntolerance_patient", null=True, blank=True, on_delete=models.SET_NULL)
    encounter = models.ForeignKey("FHIR_Encounter", related_name="AllergyIntolerance_encounter", null=True, blank=True, on_delete=models.SET_NULL)
    onset = FHIR_primitive_DateTimeField(null=True, blank=True, )
    onset = models.OneToOneField("FHIR_GP_Quantity_Age", related_name='AllergyIntolerance_onset', null=True, blank=True, on_delete=models.SET_NULL)
    onset = models.OneToOneField("FHIR_GP_Period", related_name='AllergyIntolerance_onset', null=True, blank=True, on_delete=models.SET_NULL)
    onset = models.OneToOneField("FHIR_GP_Range", related_name='AllergyIntolerance_onset', null=True, blank=True, on_delete=models.SET_NULL)
    onset = FHIR_primitive_StringField(null=True, blank=True, )
    recordedDate = FHIR_primitive_DateTimeField(null=True, blank=True, )
    recorder_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="AllergyIntolerance_recorder", null=True, blank=True, on_delete=models.SET_NULL)
    recorder_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="AllergyIntolerance_recorder", null=True, blank=True, on_delete=models.SET_NULL)
    recorder_Patient = models.ForeignKey("FHIR_Patient", related_name="AllergyIntolerance_recorder", null=True, blank=True, on_delete=models.SET_NULL)
    recorder_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="AllergyIntolerance_recorder", null=True, blank=True, on_delete=models.SET_NULL)
    recorder_Organization = models.ForeignKey("FHIR_Organization", related_name="AllergyIntolerance_recorder", null=True, blank=True, on_delete=models.SET_NULL)
    asserter_Patient = models.ForeignKey("FHIR_Patient", related_name="AllergyIntolerance_asserter", null=True, blank=True, on_delete=models.SET_NULL)
    asserter_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="AllergyIntolerance_asserter", null=True, blank=True, on_delete=models.SET_NULL)
    asserter_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="AllergyIntolerance_asserter", null=True, blank=True, on_delete=models.SET_NULL)
    asserter_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="AllergyIntolerance_asserter", null=True, blank=True, on_delete=models.SET_NULL)
    lastReactionOccurrence = FHIR_primitive_DateTimeField(null=True, blank=True, )

class FHIR_AllergyIntolerance_identifier(FHIR_GP_Identifier):
    AllergyIntolerance = models.ForeignKey(FHIR_AllergyIntolerance, related_name='AllergyIntolerance_identifier', null=False, on_delete=models.CASCADE)

class FHIR_AllergyIntolerance_category(models.Model):
    AllergyIntolerance = models.ForeignKey(FHIR_AllergyIntolerance, related_name='AllergyIntolerance_category', null=False, on_delete=models.CASCADE)
    
    class CategoryChoices(models.TextChoices): FOOD = 'food', 'Food'; MEDICATION = 'medication', 'Medication'; ENVIRONMENT = 'environment', 'Environment'; BIOLOGIC = 'biologic', 'Biologic'; 
    category = FHIR_primitive_CodeField(choices=CategoryChoices.choices, null=True, blank=True, )
    
class FHIR_AllergyIntolerance_note(FHIR_GP_Annotation):
    AllergyIntolerance = models.ForeignKey(FHIR_AllergyIntolerance, related_name='AllergyIntolerance_note', null=False, on_delete=models.CASCADE)

class FHIR_AllergyIntolerance_reaction(models.Model):
    AllergyIntolerance = models.ForeignKey(FHIR_AllergyIntolerance, related_name='AllergyIntolerance_reaction', null=False, on_delete=models.CASCADE)
    BINDING_substance = 'https://www.hl7.org/fhir/valueset-substance-code.html'
    substance_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_substance}, related_name='AllergyIntolerance_reaction_substance', blank=True)
    substance_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    description = FHIR_primitive_StringField(null=True, blank=True, )
    onset = FHIR_primitive_DateTimeField(null=True, blank=True, )
    class SeverityChoices(models.TextChoices): MILD = 'mild', 'Mild'; MODERATE = 'moderate', 'Moderate'; SEVERE_OF_EVENT_AS_A_WHOLE = 'severe (of event as a whole)', 'Severe (of event as a whole)'; 
    severity = FHIR_primitive_CodeField(choices=SeverityChoices.choices, null=True, blank=True, )
    BINDING_exposureRoute = 'https://www.hl7.org/fhir/valueset-route-codes.html'
    exposureRoute_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_exposureRoute}, related_name='AllergyIntolerance_reaction_exposureRoute', blank=True)
    exposureRoute_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_AllergyIntolerance_reaction_manifestation(models.Model):
    AllergyIntolerance_reaction = models.ForeignKey(FHIR_AllergyIntolerance_reaction, related_name='AllergyIntolerance_reaction_manifestation', null=False, on_delete=models.CASCADE)
    BINDING_manifestation = 'https://www.hl7.org/fhir/valueset-clinical-findings.html'
    manifestation_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_manifestation}, related_name='AllergyIntolerance_reaction_manifestation', blank=True)
    manifestation_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    manifestation_Observation_ref = models.ForeignKey("FHIR_Observation", related_name="AllergyIntolerance_reaction_manifestation", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_AllergyIntolerance_reaction_note(FHIR_GP_Annotation):
    AllergyIntolerance_reaction = models.ForeignKey(FHIR_AllergyIntolerance_reaction, related_name='AllergyIntolerance_reaction_note', null=False, on_delete=models.CASCADE)
