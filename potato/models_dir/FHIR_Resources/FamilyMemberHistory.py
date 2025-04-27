#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_FamilyMemberHistory(models.Model):
    class StatusChoices(models.TextChoices): PARTIAL = 'partial', 'Partial'; COMPLETED = 'completed', 'Completed'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; HEALTH_UNKNOWN = 'health-unknown', 'Health-unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    BINDING_dataAbsentReason = 'TODO'
    dataAbsentReason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_dataAbsentReason}, related_name='FamilyMemberHistory_dataAbsentReason', blank=True)
    dataAbsentReason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    patient = models.ForeignKey("FHIR_Patient", related_name="FamilyMemberHistory_patient", null=True, blank=True, on_delete=models.SET_NULL)
    date = FHIR_primitive_DateTimeField(null=True, blank=True, )
    name = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_relationship = 'TODO'
    relationship_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_relationship}, related_name='FamilyMemberHistory_relationship', blank=True)
    relationship_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_sex = 'TODO'
    sex_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_sex}, related_name='FamilyMemberHistory_sex', blank=True)
    sex_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    born = models.OneToOneField("FHIR_GP_Period", related_name='FamilyMemberHistory_born', null=True, blank=True, on_delete=models.SET_NULL)
    born = FHIR_primitive_DateField(null=True, blank=True, )
    born = FHIR_primitive_StringField(null=True, blank=True, )
    age = models.OneToOneField("FHIR_GP_Quantity_Age", related_name='FamilyMemberHistory_age', null=True, blank=True, on_delete=models.SET_NULL)
    age = models.OneToOneField("FHIR_GP_Range", related_name='FamilyMemberHistory_age', null=True, blank=True, on_delete=models.SET_NULL)
    age = FHIR_primitive_StringField(null=True, blank=True, )
    estimatedAge = FHIR_primitive_BooleanField(null=True, blank=True, )
    deceased = FHIR_primitive_BooleanField(null=True, blank=True, )
    deceased = models.OneToOneField("FHIR_GP_Quantity_Age", related_name='FamilyMemberHistory_deceased', null=True, blank=True, on_delete=models.SET_NULL)
    deceased = models.OneToOneField("FHIR_GP_Range", related_name='FamilyMemberHistory_deceased', null=True, blank=True, on_delete=models.SET_NULL)
    deceased = FHIR_primitive_DateField(null=True, blank=True, )
    deceased = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_FamilyMemberHistory_identifier(FHIR_GP_Identifier):
    FamilyMemberHistory = models.ForeignKey(FHIR_FamilyMemberHistory, related_name='FamilyMemberHistory_identifier', null=False, on_delete=models.CASCADE)

class FHIR_FamilyMemberHistory_participant(models.Model):
    FamilyMemberHistory = models.ForeignKey(FHIR_FamilyMemberHistory, related_name='FamilyMemberHistory_participant', null=False, on_delete=models.CASCADE)
    BINDING_function = 'TODO'
    function_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_function}, related_name='FamilyMemberHistory_participant_function', blank=True)
    function_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    actor_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="FamilyMemberHistory_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="FamilyMemberHistory_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Patient = models.ForeignKey("FHIR_Patient", related_name="FamilyMemberHistory_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="FamilyMemberHistory_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Device = models.ForeignKey("FHIR_Device", related_name="FamilyMemberHistory_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Organization = models.ForeignKey("FHIR_Organization", related_name="FamilyMemberHistory_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_CareTeam = models.ForeignKey("FHIR_CareTeam", related_name="FamilyMemberHistory_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Group = models.ForeignKey("FHIR_Group", related_name="FamilyMemberHistory_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_FamilyMemberHistory_reason(models.Model):
    FamilyMemberHistory = models.ForeignKey(FHIR_FamilyMemberHistory, related_name='FamilyMemberHistory_reason', null=False, on_delete=models.CASCADE)
    BINDING_reason = 'TODO'
    reason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_reason}, related_name='FamilyMemberHistory_reason', blank=True)
    reason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    reason_Condition_ref = models.ForeignKey("FHIR_Condition", related_name="FamilyMemberHistory_reason_Condition", null=True, blank=True, on_delete=models.SET_NULL)
    reason_Observation_ref = models.ForeignKey("FHIR_Observation", related_name="FamilyMemberHistory_reason_Observation", null=True, blank=True, on_delete=models.SET_NULL)
    reason_AllergyIntolerance_ref = models.ForeignKey("FHIR_AllergyIntolerance", related_name="FamilyMemberHistory_reason_AllergyIntolerance", null=True, blank=True, on_delete=models.SET_NULL)
    reason_QuestionnaireResponse_ref = models.ForeignKey("FHIR_QuestionnaireResponse", related_name="FamilyMemberHistory_reason_QuestionnaireResponse", null=True, blank=True, on_delete=models.SET_NULL)
    reason_DiagnosticReport_ref = models.ForeignKey("FHIR_DiagnosticReport", related_name="FamilyMemberHistory_reason_DiagnosticReport", null=True, blank=True, on_delete=models.SET_NULL)
    reason_DocumentReference_ref = models.ForeignKey("FHIR_DocumentReference", related_name="FamilyMemberHistory_reason_DocumentReference", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_FamilyMemberHistory_note(FHIR_GP_Annotation):
    FamilyMemberHistory = models.ForeignKey(FHIR_FamilyMemberHistory, related_name='FamilyMemberHistory_note', null=False, on_delete=models.CASCADE)

class FHIR_FamilyMemberHistory_condition(models.Model):
    FamilyMemberHistory = models.ForeignKey(FHIR_FamilyMemberHistory, related_name='FamilyMemberHistory_condition', null=False, on_delete=models.CASCADE)
    BINDING_code = 'TODO'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='FamilyMemberHistory_condition_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_outcome = 'TODO'
    outcome_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_outcome}, related_name='FamilyMemberHistory_condition_outcome', blank=True)
    outcome_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    contributedToDeath = FHIR_primitive_BooleanField(null=True, blank=True, )
    onset = models.OneToOneField("FHIR_GP_Quantity_Age", related_name='FamilyMemberHistory_condition_onset', null=True, blank=True, on_delete=models.SET_NULL)
    onset = models.OneToOneField("FHIR_GP_Range", related_name='FamilyMemberHistory_condition_onset', null=True, blank=True, on_delete=models.SET_NULL)
    onset = models.OneToOneField("FHIR_GP_Period", related_name='FamilyMemberHistory_condition_onset', null=True, blank=True, on_delete=models.SET_NULL)
    onset = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_FamilyMemberHistory_condition_note(FHIR_GP_Annotation):
    FamilyMemberHistory_condition = models.ForeignKey(FHIR_FamilyMemberHistory_condition, related_name='FamilyMemberHistory_condition_note', null=False, on_delete=models.CASCADE)

class FHIR_FamilyMemberHistory_procedure(models.Model):
    FamilyMemberHistory = models.ForeignKey(FHIR_FamilyMemberHistory, related_name='FamilyMemberHistory_procedure', null=False, on_delete=models.CASCADE)
    BINDING_code = 'TODO'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='FamilyMemberHistory_procedure_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_outcome = 'TODO'
    outcome_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_outcome}, related_name='FamilyMemberHistory_procedure_outcome', blank=True)
    outcome_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    contributedToDeath = FHIR_primitive_BooleanField(null=True, blank=True, )
    performed = models.OneToOneField("FHIR_GP_Quantity_Age", related_name='FamilyMemberHistory_procedure_performed', null=True, blank=True, on_delete=models.SET_NULL)
    performed = models.OneToOneField("FHIR_GP_Range", related_name='FamilyMemberHistory_procedure_performed', null=True, blank=True, on_delete=models.SET_NULL)
    performed = models.OneToOneField("FHIR_GP_Period", related_name='FamilyMemberHistory_procedure_performed', null=True, blank=True, on_delete=models.SET_NULL)
    performed = FHIR_primitive_StringField(null=True, blank=True, )
    performed = FHIR_primitive_DateTimeField(null=True, blank=True, )

class FHIR_FamilyMemberHistory_procedure_note(FHIR_GP_Annotation):
    FamilyMemberHistory_procedure = models.ForeignKey(FHIR_FamilyMemberHistory_procedure, related_name='FamilyMemberHistory_procedure_note', null=False, on_delete=models.CASCADE)
