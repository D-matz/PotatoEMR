#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_AdverseEvent(models.Model):
    class StatusChoices(models.TextChoices): IN_PROGRESS = 'in-progress', 'In-progress'; COMPLETED = 'completed', 'Completed'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    class ActualityChoices(models.TextChoices): ACTUAL = 'actual', 'Actual'; POTENTIAL = 'potential', 'Potential'; 
    actuality = FHIR_primitive_CodeField(choices=ActualityChoices.choices, null=True, blank=True, )
    BINDING_code = "TODO"
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='AdverseEvent_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    subject_Patient = models.ForeignKey("FHIR_Patient", related_name="AdverseEvent_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Group = models.ForeignKey("FHIR_Group", related_name="AdverseEvent_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="AdverseEvent_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="AdverseEvent_subject", null=True, blank=True, on_delete=models.SET_NULL)
    encounter = models.ForeignKey("FHIR_Encounter", related_name="AdverseEvent_encounter", null=True, blank=True, on_delete=models.SET_NULL)
    cause_dateTime = FHIR_primitive_DateTimeField(null=True, blank=True, )
    cause_Period = models.OneToOneField("FHIR_GP_Period", related_name='AdverseEvent_cause_Period', null=True, blank=True, on_delete=models.SET_NULL)
    effect_dateTime = FHIR_primitive_DateTimeField(null=True, blank=True, )
    effect_Period = models.OneToOneField("FHIR_GP_Period", related_name='AdverseEvent_effect_Period', null=True, blank=True, on_delete=models.SET_NULL)
    detected = FHIR_primitive_DateTimeField(null=True, blank=True, )
    recordedDate = FHIR_primitive_DateTimeField(null=True, blank=True, )
    location = models.ForeignKey("FHIR_Location", related_name="AdverseEvent_location", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_seriousness = "TODO"
    seriousness_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_seriousness}, related_name='AdverseEvent_seriousness', blank=True)
    seriousness_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    recorder_Patient = models.ForeignKey("FHIR_Patient", related_name="AdverseEvent_recorder", null=True, blank=True, on_delete=models.SET_NULL)
    recorder_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="AdverseEvent_recorder", null=True, blank=True, on_delete=models.SET_NULL)
    recorder_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="AdverseEvent_recorder", null=True, blank=True, on_delete=models.SET_NULL)
    recorder_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="AdverseEvent_recorder", null=True, blank=True, on_delete=models.SET_NULL)
    study = models.ManyToManyField("FHIR_ResearchStudy", related_name="AdverseEvent_study", blank=True)
    expectedInResearchStudy = FHIR_primitive_BooleanField(null=True, blank=True, )

class FHIR_AdverseEvent_identifier(FHIR_GP_Identifier):
    AdverseEvent = models.ForeignKey(FHIR_AdverseEvent, related_name='AdverseEvent_identifier', null=False, on_delete=models.CASCADE)

class FHIR_AdverseEvent_category(models.Model):
    AdverseEvent = models.ForeignKey(FHIR_AdverseEvent, related_name='AdverseEvent_category', null=False, on_delete=models.CASCADE)
    BINDING_category = "TODO"
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='AdverseEvent_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_AdverseEvent_resultingEffect(models.Model):
    AdverseEvent = models.ForeignKey(FHIR_AdverseEvent, related_name='AdverseEvent_resultingEffect', null=False, on_delete=models.CASCADE)
    BINDING_resultingEffect = "TODO"
    resultingEffect_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_resultingEffect}, related_name='AdverseEvent_resultingEffect', blank=True)
    resultingEffect_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    resultingEffect_Condition_ref = models.ForeignKey("FHIR_Condition", related_name="AdverseEvent_resultingEffect_Condition", null=True, blank=True, on_delete=models.SET_NULL)
    resultingEffect_Observation_ref = models.ForeignKey("FHIR_Observation", related_name="AdverseEvent_resultingEffect_Observation", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_AdverseEvent_outcome(models.Model):
    AdverseEvent = models.ForeignKey(FHIR_AdverseEvent, related_name='AdverseEvent_outcome', null=False, on_delete=models.CASCADE)
    BINDING_outcome = "TODO"
    outcome_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_outcome}, related_name='AdverseEvent_outcome', blank=True)
    outcome_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_AdverseEvent_participant(models.Model):
    AdverseEvent = models.ForeignKey(FHIR_AdverseEvent, related_name='AdverseEvent_participant', null=False, on_delete=models.CASCADE)
    BINDING_function = "TODO"
    function_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_function}, related_name='AdverseEvent_participant_function', blank=True)
    function_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    actor_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="AdverseEvent_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="AdverseEvent_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Organization = models.ForeignKey("FHIR_Organization", related_name="AdverseEvent_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_CareTeam = models.ForeignKey("FHIR_CareTeam", related_name="AdverseEvent_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Patient = models.ForeignKey("FHIR_Patient", related_name="AdverseEvent_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Device = models.ForeignKey("FHIR_Device", related_name="AdverseEvent_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="AdverseEvent_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Group = models.ForeignKey("FHIR_Group", related_name="AdverseEvent_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_AdverseEvent_suspectEntity(models.Model):
    AdverseEvent = models.ForeignKey(FHIR_AdverseEvent, related_name='AdverseEvent_suspectEntity', null=False, on_delete=models.CASCADE)
    BINDING_instance = "TODO"
    instance_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_instance}, related_name='AdverseEvent_suspectEntity_instance', blank=True)
    instance_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    instance_Immunization_ref = models.ForeignKey("FHIR_Immunization", related_name="AdverseEvent_suspectEntity_instance_Immunization", null=True, blank=True, on_delete=models.SET_NULL)
    instance_Procedure_ref = models.ForeignKey("FHIR_Procedure", related_name="AdverseEvent_suspectEntity_instance_Procedure", null=True, blank=True, on_delete=models.SET_NULL)
    instance_Substance_ref = models.ForeignKey("FHIR_Substance", related_name="AdverseEvent_suspectEntity_instance_Substance", null=True, blank=True, on_delete=models.SET_NULL)
    instance_Medication_ref = models.ForeignKey("FHIR_Medication", related_name="AdverseEvent_suspectEntity_instance_Medication", null=True, blank=True, on_delete=models.SET_NULL)
    instance_MedicationAdministration_ref = models.ForeignKey("FHIR_MedicationAdministration", related_name="AdverseEvent_suspectEntity_instance_MedicationAdministration", null=True, blank=True, on_delete=models.SET_NULL)
    instance_MedicationStatement_ref = models.ForeignKey("FHIR_MedicationStatement", related_name="AdverseEvent_suspectEntity_instance_MedicationStatement", null=True, blank=True, on_delete=models.SET_NULL)
    instance_Device_ref = models.ForeignKey("FHIR_Device", related_name="AdverseEvent_suspectEntity_instance_Device", null=True, blank=True, on_delete=models.SET_NULL)
    instance_BiologicallyDerivedProduct_ref = models.ForeignKey("FHIR_BiologicallyDerivedProduct", related_name="AdverseEvent_suspectEntity_instance_BiologicallyDerivedProduct", null=True, blank=True, on_delete=models.SET_NULL)
    instance_ResearchStudy_ref = models.ForeignKey("FHIR_ResearchStudy", related_name="AdverseEvent_suspectEntity_instance_ResearchStudy", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_AdverseEvent_suspectEntity_causality(models.Model):
    AdverseEvent_suspectEntity = models.ForeignKey(FHIR_AdverseEvent_suspectEntity, related_name='AdverseEvent_suspectEntity_causality', null=False, on_delete=models.CASCADE)
    BINDING_assessmentMethod = "TODO"
    assessmentMethod_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_assessmentMethod}, related_name='AdverseEvent_suspectEntity_causality_assessmentMethod', blank=True)
    assessmentMethod_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_entityRelatedness = "TODO"
    entityRelatedness_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_entityRelatedness}, related_name='AdverseEvent_suspectEntity_causality_entityRelatedness', blank=True)
    entityRelatedness_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    author_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="AdverseEvent_suspectEntity_causality_author", null=True, blank=True, on_delete=models.SET_NULL)
    author_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="AdverseEvent_suspectEntity_causality_author", null=True, blank=True, on_delete=models.SET_NULL)
    author_Patient = models.ForeignKey("FHIR_Patient", related_name="AdverseEvent_suspectEntity_causality_author", null=True, blank=True, on_delete=models.SET_NULL)
    author_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="AdverseEvent_suspectEntity_causality_author", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_AdverseEvent_contributingFactor(models.Model):
    AdverseEvent = models.ForeignKey(FHIR_AdverseEvent, related_name='AdverseEvent_contributingFactor', null=False, on_delete=models.CASCADE)
    BINDING_contributingFactor = "TODO"
    contributingFactor_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_contributingFactor}, related_name='AdverseEvent_contributingFactor', blank=True)
    contributingFactor_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    contributingFactor_Condition_ref = models.ForeignKey("FHIR_Condition", related_name="AdverseEvent_contributingFactor_Condition", null=True, blank=True, on_delete=models.SET_NULL)
    contributingFactor_Observation_ref = models.ForeignKey("FHIR_Observation", related_name="AdverseEvent_contributingFactor_Observation", null=True, blank=True, on_delete=models.SET_NULL)
    contributingFactor_AllergyIntolerance_ref = models.ForeignKey("FHIR_AllergyIntolerance", related_name="AdverseEvent_contributingFactor_AllergyIntolerance", null=True, blank=True, on_delete=models.SET_NULL)
    contributingFactor_FamilyMemberHistory_ref = models.ForeignKey("FHIR_FamilyMemberHistory", related_name="AdverseEvent_contributingFactor_FamilyMemberHistory", null=True, blank=True, on_delete=models.SET_NULL)
    contributingFactor_Immunization_ref = models.ForeignKey("FHIR_Immunization", related_name="AdverseEvent_contributingFactor_Immunization", null=True, blank=True, on_delete=models.SET_NULL)
    contributingFactor_Procedure_ref = models.ForeignKey("FHIR_Procedure", related_name="AdverseEvent_contributingFactor_Procedure", null=True, blank=True, on_delete=models.SET_NULL)
    contributingFactor_Device_ref = models.ForeignKey("FHIR_Device", related_name="AdverseEvent_contributingFactor_Device", null=True, blank=True, on_delete=models.SET_NULL)
    contributingFactor_DeviceUsage_ref = models.ForeignKey("FHIR_DeviceUsage", related_name="AdverseEvent_contributingFactor_DeviceUsage", null=True, blank=True, on_delete=models.SET_NULL)
    contributingFactor_DocumentReference_ref = models.ForeignKey("FHIR_DocumentReference", related_name="AdverseEvent_contributingFactor_DocumentReference", null=True, blank=True, on_delete=models.SET_NULL)
    contributingFactor_MedicationAdministration_ref = models.ForeignKey("FHIR_MedicationAdministration", related_name="AdverseEvent_contributingFactor_MedicationAdministration", null=True, blank=True, on_delete=models.SET_NULL)
    contributingFactor_MedicationStatement_ref = models.ForeignKey("FHIR_MedicationStatement", related_name="AdverseEvent_contributingFactor_MedicationStatement", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_AdverseEvent_preventiveAction(models.Model):
    AdverseEvent = models.ForeignKey(FHIR_AdverseEvent, related_name='AdverseEvent_preventiveAction', null=False, on_delete=models.CASCADE)
    BINDING_preventiveAction = "TODO"
    preventiveAction_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_preventiveAction}, related_name='AdverseEvent_preventiveAction', blank=True)
    preventiveAction_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    preventiveAction_Immunization_ref = models.ForeignKey("FHIR_Immunization", related_name="AdverseEvent_preventiveAction_Immunization", null=True, blank=True, on_delete=models.SET_NULL)
    preventiveAction_Procedure_ref = models.ForeignKey("FHIR_Procedure", related_name="AdverseEvent_preventiveAction_Procedure", null=True, blank=True, on_delete=models.SET_NULL)
    preventiveAction_DocumentReference_ref = models.ForeignKey("FHIR_DocumentReference", related_name="AdverseEvent_preventiveAction_DocumentReference", null=True, blank=True, on_delete=models.SET_NULL)
    preventiveAction_MedicationAdministration_ref = models.ForeignKey("FHIR_MedicationAdministration", related_name="AdverseEvent_preventiveAction_MedicationAdministration", null=True, blank=True, on_delete=models.SET_NULL)
    preventiveAction_MedicationRequest_ref = models.ForeignKey("FHIR_MedicationRequest", related_name="AdverseEvent_preventiveAction_MedicationRequest", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_AdverseEvent_mitigatingAction(models.Model):
    AdverseEvent = models.ForeignKey(FHIR_AdverseEvent, related_name='AdverseEvent_mitigatingAction', null=False, on_delete=models.CASCADE)
    BINDING_mitigatingAction = "TODO"
    mitigatingAction_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_mitigatingAction}, related_name='AdverseEvent_mitigatingAction', blank=True)
    mitigatingAction_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    mitigatingAction_Procedure_ref = models.ForeignKey("FHIR_Procedure", related_name="AdverseEvent_mitigatingAction_Procedure", null=True, blank=True, on_delete=models.SET_NULL)
    mitigatingAction_DocumentReference_ref = models.ForeignKey("FHIR_DocumentReference", related_name="AdverseEvent_mitigatingAction_DocumentReference", null=True, blank=True, on_delete=models.SET_NULL)
    mitigatingAction_MedicationAdministration_ref = models.ForeignKey("FHIR_MedicationAdministration", related_name="AdverseEvent_mitigatingAction_MedicationAdministration", null=True, blank=True, on_delete=models.SET_NULL)
    mitigatingAction_MedicationRequest_ref = models.ForeignKey("FHIR_MedicationRequest", related_name="AdverseEvent_mitigatingAction_MedicationRequest", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_AdverseEvent_supportingInfo(models.Model):
    AdverseEvent = models.ForeignKey(FHIR_AdverseEvent, related_name='AdverseEvent_supportingInfo', null=False, on_delete=models.CASCADE)
    BINDING_supportingInfo = "TODO"
    supportingInfo_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_supportingInfo}, related_name='AdverseEvent_supportingInfo', blank=True)
    supportingInfo_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    supportingInfo_Condition_ref = models.ForeignKey("FHIR_Condition", related_name="AdverseEvent_supportingInfo_Condition", null=True, blank=True, on_delete=models.SET_NULL)
    supportingInfo_Observation_ref = models.ForeignKey("FHIR_Observation", related_name="AdverseEvent_supportingInfo_Observation", null=True, blank=True, on_delete=models.SET_NULL)
    supportingInfo_AllergyIntolerance_ref = models.ForeignKey("FHIR_AllergyIntolerance", related_name="AdverseEvent_supportingInfo_AllergyIntolerance", null=True, blank=True, on_delete=models.SET_NULL)
    supportingInfo_FamilyMemberHistory_ref = models.ForeignKey("FHIR_FamilyMemberHistory", related_name="AdverseEvent_supportingInfo_FamilyMemberHistory", null=True, blank=True, on_delete=models.SET_NULL)
    supportingInfo_Immunization_ref = models.ForeignKey("FHIR_Immunization", related_name="AdverseEvent_supportingInfo_Immunization", null=True, blank=True, on_delete=models.SET_NULL)
    supportingInfo_Procedure_ref = models.ForeignKey("FHIR_Procedure", related_name="AdverseEvent_supportingInfo_Procedure", null=True, blank=True, on_delete=models.SET_NULL)
    supportingInfo_DocumentReference_ref = models.ForeignKey("FHIR_DocumentReference", related_name="AdverseEvent_supportingInfo_DocumentReference", null=True, blank=True, on_delete=models.SET_NULL)
    supportingInfo_MedicationAdministration_ref = models.ForeignKey("FHIR_MedicationAdministration", related_name="AdverseEvent_supportingInfo_MedicationAdministration", null=True, blank=True, on_delete=models.SET_NULL)
    supportingInfo_MedicationStatement_ref = models.ForeignKey("FHIR_MedicationStatement", related_name="AdverseEvent_supportingInfo_MedicationStatement", null=True, blank=True, on_delete=models.SET_NULL)
    supportingInfo_QuestionnaireResponse_ref = models.ForeignKey("FHIR_QuestionnaireResponse", related_name="AdverseEvent_supportingInfo_QuestionnaireResponse", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_AdverseEvent_note(FHIR_GP_Annotation):
    AdverseEvent = models.ForeignKey(FHIR_AdverseEvent, related_name='AdverseEvent_note', null=False, on_delete=models.CASCADE)
