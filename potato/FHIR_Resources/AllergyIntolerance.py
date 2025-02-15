from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *

class FHIR_AllergyIntolerance(models.Model):

    #identifier foreign key to this
    BINDING_RULE_CLINICAL_STATUS = 'https://www.hl7.org/fhir/valueset-allergyintolerance-clinical.html'
    clinical_status_cc = models.ManyToManyField('FHIR_GP_Coding', related_name='allergyintolerance_clinicalstatus', blank=True, limit_choices_to={'binding__binding_rule': BINDING_RULE_CLINICAL_STATUS})
    clinical_status_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

    BINDING_RULE_VERIFICATION = 'https://www.hl7.org/fhir/valueset-allergyintolerance-verification.html'
    verification_status_cc = models.ManyToManyField('FHIR_GP_Coding', related_name='allergyintolerance_verificationstatus', blank=True, limit_choices_to={'binding__binding_rule': BINDING_RULE_VERIFICATION})
    verification_status_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

    BINDING_RULE_TYPE = 'https://www.hl7.org/fhir/valueset-allergy-intolerance-type.html'
    type_cc = models.ManyToManyField('FHIR_GP_Coding', related_name='allergyintolerance_type', blank=True, limit_choices_to={'binding__binding_rule': BINDING_RULE_TYPE})

    BINDING_RULE_CATEGORY = 'https://www.hl7.org/fhir/valueset-allergy-intolerance-category.html'
    category_codes = models.ManyToManyField('FHIR_GP_Coding', related_name='allergyintolerance_category', blank=True, limit_choices_to={'binding__binding_rule': BINDING_RULE_CATEGORY})

    BINDING_RULE_CRITICALITY = 'https://www.hl7.org/fhir/valueset-allergy-intolerance-criticality.html'
    criticality_code = models.ForeignKey('FHIR_GP_Coding', related_name='allergyintolerance_criticality', on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'binding__binding_rule': BINDING_RULE_CRITICALITY})

    BINDING_RULE_CODE = 'https://www.hl7.org/fhir/valueset-allergyintolerance-code.html'
    code_cc = models.ManyToManyField('FHIR_GP_Coding', related_name='allergyintolerance_code', blank=True, limit_choices_to={'binding__binding_rule': BINDING_RULE_CODE})   
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

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

    def __str__(self):
        return str(self.code_cc.first())

class FHIR_AllergyIntolerance_Identifier(FHIR_GP_Identifier):
    allergy_intolerance = models.ForeignKey(FHIR_AllergyIntolerance, on_delete=models.CASCADE, related_name='identifiers')

class FHIR_AllergyIntolerance_Participant(models.Model):
    allergy_intolerance = models.ForeignKey(FHIR_AllergyIntolerance, on_delete=models.CASCADE)
    function_cc = models.ManyToManyField('FHIR_GP_Coding', related_name='allergyintolerance_participant_function',
        limit_choices_to={'binding__binding_rule': 'https://www.hl7.org/fhir/valueset-participation-role-type.html'})
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
    substance_cc = models.ManyToManyField('FHIR_GP_Coding', related_name='allergyintolerance_reaction_substance', blank=True,
        limit_choices_to={'binding__binding_rule': 'https://www.hl7.org/fhir/valueset-substance-code.html'})
    substance_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    #todo binding rule for substance: snomed ct code that is a 105590001 (Substance)
    #when changing binding remember to remove old one
    #manifestation foreign key to this
    description = FHIR_primitive_StringField(max_length=10000, null=True, blank=True)
    onset = FHIR_primitive_DateTimeField(null=True, blank=True)
    severity = models.ForeignKey('FHIR_GP_Coding', related_name='allergyintolerance_reaction_severity', on_delete=models.SET_NULL, null=True, blank=True,
        limit_choices_to={'binding__binding_rule': 'https://www.hl7.org/fhir/valueset-reaction-event-severity.html'})
    exposureRoute_cc = models.ManyToManyField('FHIR_GP_Coding', related_name='allergyintolerance_reaction_exposureroute', blank=True,
        limit_choices_to={'binding__binding_rule': 'https://www.hl7.org/fhir/valueset-route-codes.html'})
    exposureRoute_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    #todo binding rule for exposureRoute: snomed ct code that is a 105590001 (Substance)
    #when changing binding remember to remove old one
# @receiver(m2m_changed, sender=FHIR_AllergyIntolerance_Reaction.substance_cc.through)
# def update_substance_cctext(sender, instance, **kwargs):
#     substances = instance.substance_cc.all()
#     if len(substances) == 1:
#         substance = substances[0]
#         instance.substance_cctext = substance.display if substance.display else substance.code
#         instance.save()
    
class FHIR_AllergyIntolerance_Reaction_Manifestation(models.Model):
    reaction = models.ForeignKey(FHIR_AllergyIntolerance_Reaction, on_delete=models.CASCADE, related_name='manifestations')
    manifestation_ref = models.ForeignKey('FHIR_Observation', on_delete=models.SET_NULL, null=True, blank=True)
    manifestation_cc = models.ManyToManyField('FHIR_GP_Coding', related_name='allergyintolerance_reaction_manifestation_cc', blank=True,
        limit_choices_to={'binding__binding_rule': 'https://www.hl7.org/fhir/valueset-clinical-findings.html'})
    manifestation_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    #todo change to snomed ct code - is a clinical finding
# @receiver(m2m_changed, sender=FHIR_AllergyIntolerance_Reaction_Manifestation.manifestation_cc.through)
# def update_substance_cctext(sender, instance, **kwargs):
#     ccs = instance.manifestation_cc.all()
#     print("using ccs", ccs)
#     if len(ccs) == 1:
#         cc = ccs[0]
#         instance.manifestation_cctext = cc.display if cc.display else cc.code
#         instance.save()

class FHIR_AllergyIntolerance_Reaction_Note(FHIR_GP_Annotation):
    reaction = models.ForeignKey(FHIR_AllergyIntolerance_Reaction, on_delete=models.CASCADE, related_name='reaction_notes')
