from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *

class FHIR_AllergyIntolerance(models.Model):

    #identifier foreign key to this
    BINDING_RULE_CLINICAL_STATUS = 'https://www.hl7.org/fhir/valueset-allergyintolerance-clinical.html'
    clinical_status_cc = models.ManyToManyField(FHIR_GP_Coding, related_name='allergyintolerance_clinical_status', limit_choices_to={'codings__binding_rule': BINDING_RULE_CLINICAL_STATUS})
    clinical_status_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

    BINDING_RULE_VERIFICATION = 'https://www.hl7.org/fhir/valueset-allergyintolerance-verification.html'
    verification_status_cc = models.ManyToManyField(FHIR_GP_Coding, related_name='allergyintolerance_verification_status', limit_choices_to={'codings__binding_rule': BINDING_RULE_VERIFICATION})
    verification_status_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

    BINDING_RULE_TYPE = 'https://www.hl7.org/fhir/valueset-allergy-intolerance-type.html'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, related_name='allergyintolerance_type', limit_choices_to={'codings__binding_rule': BINDING_RULE_TYPE})
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

    BINDING_RULE_CATEGORY = 'https://www.hl7.org/fhir/valueset-allergy-intolerance-category.html'
    category_codes = models.ManyToManyField('FHIR_GP_Coding', related_name='allergyintolerance_category', blank=True, limit_choices_to={'codings__binding_rule': BINDING_RULE_CATEGORY})

    BINDING_RULE_CRITICALITY = 'https://www.hl7.org/fhir/valueset-allergy-intolerance-criticality.html'
    criticality_code = models.ForeignKey('FHIR_GP_Coding', related_name='allergyintolerance_criticality', on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'codings__binding_rule': BINDING_RULE_CRITICALITY})

    BINDING_RULE_CODE = 'https://www.hl7.org/fhir/valueset-allergyintolerance-code.html'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, related_name='allergyintolerance_code', limit_choices_to={'codings__binding_rule': BINDING_RULE_CODE})
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

    patient = models.ForeignKey('FHIR_Patient', on_delete=models.CASCADE, null=False)
    encounter = models.ForeignKey('FHIR_Encounter', on_delete=models.SET_NULL, null=True, blank=True)

    onset_dateTime = FHIR_primitive_DateTimeField(null=True, blank=True)
    onset_age = models.OneToOneField(FHIR_GP_Quantity_Age, on_delete=models.SET_NULL, null=True, blank=True)
    onset_period = models.OneToOneField(FHIR_GP_Period, on_delete=models.SET_NULL, null=True, blank=True)
    onset_range = models.OneToOneField(FHIR_GP_Range, on_delete=models.SET_NULL, null=True, blank=True)
    onset_string = FHIR_primitive_StringField(max_length=255, null=True, blank=True)
    recordedDate = FHIR_primitive_DateTimeField(null=True, blank=True)

    recorder_practitioner = models.ForeignKey('FHIR_Practitioner', related_name='recorded_allergies_as_practitioner', on_delete=models.SET_NULL, null=True, blank=True)
    recorder_practitionerRole = models.ForeignKey('FHIR_PractitionerRole', related_name='recorded_allergies_as_role', on_delete=models.SET_NULL, null=True, blank=True)
    recorder_patient = models.ForeignKey('FHIR_Patient', related_name='recorded_allergies_as_patient', on_delete=models.SET_NULL, null=True, blank=True)
    asserter_practitioner = models.ForeignKey('FHIR_Practitioner', related_name='asserted_allergies_as_practitioner', on_delete=models.SET_NULL, null=True, blank=True)
    asserter_practitionerRole = models.ForeignKey('FHIR_PractitionerRole', related_name='asserted_allergies_as_role', on_delete=models.SET_NULL, null=True, blank=True)
    asserter_patient = models.ForeignKey('FHIR_Patient', related_name='asserted_allergies_as_patient', on_delete=models.SET_NULL, null=True, blank=True)


    lastReactionOccurrence = FHIR_primitive_DateTimeField(null=True, blank=True)
    #could add precision to onset_dateTime, recordedDate, lastOccurrence

    def __str__(self):
        return "test"
        #return str(self.code_cc.first())

class FHIR_AllergyIntolerance_Identifier(FHIR_GP_Identifier):
    allergy_intolerance = models.ForeignKey(FHIR_AllergyIntolerance, on_delete=models.CASCADE, related_name='identifiers')

class FHIR_AllergyIntolerance_Participant(models.Model):
    allergy_intolerance = models.ForeignKey(FHIR_AllergyIntolerance, on_delete=models.CASCADE)
    BINDING_RULE_FUNCTION = 'https://www.hl7.org/fhir/valueset-participation-role-type.html'
    function_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={'codings__binding_rule': BINDING_RULE_FUNCTION})
    function_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    actor_practitioner = models.ForeignKey('FHIR_Practitioner', null=True, on_delete=models.SET_NULL)
    actor_practitionerRole = models.ForeignKey('FHIR_PractitionerRole', null=True, on_delete=models.SET_NULL)
    actor_patient = models.ForeignKey('FHIR_Patient', null=True, on_delete=models.SET_NULL)
    actor_relatedPerson = models.ForeignKey('FHIR_RelatedPerson', null=True, on_delete=models.SET_NULL)
    actor_device = models.ForeignKey('FHIR_Device', null=True, on_delete=models.SET_NULL)
    actor_organization = models.ForeignKey('FHIR_Organization', null=True, on_delete=models.SET_NULL)
    actor_careTeam = models.ForeignKey('FHIR_CareTeam', null=True, on_delete=models.SET_NULL)

class FHIR_AllergyIntolerance_Note(FHIR_GP_Annotation):
    allergy_intolerance = models.ForeignKey(FHIR_AllergyIntolerance, on_delete=models.CASCADE, related_name='notes')

class FHIR_AllergyIntolerance_Reaction(models.Model):
    allergy_intolerance = models.ForeignKey(FHIR_AllergyIntolerance, on_delete=models.CASCADE, related_name='reactions')
    BINDING_RULE_SUBSTANCE = 'https://www.hl7.org/fhir/valueset-substance-code.html'
    substance_cc = models.ManyToManyField(FHIR_GP_Coding, related_name='reaction_substance', limit_choices_to={'codings__binding_rule': BINDING_RULE_SUBSTANCE})
    substance_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    #todo binding rule for substance: snomed ct code that is a 105590001 (Substance)
    #when changing binding remember to remove old one
    #manifestation foreign key to this
    description = FHIR_primitive_StringField(max_length=10000, null=True, blank=True)
    onset = FHIR_primitive_DateTimeField(null=True, blank=True)
    BINDING_RULE_SEVERITY = 'https://www.hl7.org/fhir/valueset-reaction-event-severity.html'
    severity = models.ForeignKey('FHIR_GP_Coding', related_name='reaction_severity', limit_choices_to={'codings__binding_rule': BINDING_RULE_SEVERITY}, on_delete=models.SET_NULL, null=True, blank=True)

    BINDING_RULE_EXPOSUREROUTE = 'https://www.hl7.org/fhir/valueset-route-codes.html'
    exposureRoute_cc = models.ManyToManyField(FHIR_GP_Coding, related_name='reaction_exposure_route', limit_choices_to={'codings__binding_rule': BINDING_RULE_EXPOSUREROUTE}, blank=True)
    exposureRoute_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    #todo binding rule for exposureRoute: snomed ct code that is a 105590001 (Substance)
    #when changing binding remember to remove old one

class FHIR_AllergyIntolerance_Reaction_Manifestation(models.Model):
    reaction = models.ForeignKey(FHIR_AllergyIntolerance_Reaction, on_delete=models.CASCADE, related_name='manifestations')
    manifestation_ref = models.ForeignKey('FHIR_Observation', on_delete=models.SET_NULL, null=True, blank=True)
    BINDING_RULE_MANIFESTATION = 'https://www.hl7.org/fhir/valueset-clinical-findings.html'
    manifestation_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={'codings__binding_rule': BINDING_RULE_MANIFESTATION}, blank=True)
    manifestation_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    #todo change to snomed ct code - is a clinical finding

class FHIR_AllergyIntolerance_Reaction_Note(FHIR_GP_Annotation):
    reaction = models.ForeignKey(FHIR_AllergyIntolerance_Reaction, on_delete=models.CASCADE, related_name='reaction_notes')
