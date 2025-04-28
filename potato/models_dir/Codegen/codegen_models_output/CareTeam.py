#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_CareTeam(models.Model):
    class StatusChoices(models.TextChoices): PROPOSED = 'proposed', 'Proposed'; ACTIVE = 'active', 'Active'; SUSPENDED = 'suspended', 'Suspended'; INACTIVE = 'inactive', 'Inactive'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    name = FHIR_primitive_StringField(null=True, blank=True, )
    subject_Patient = models.ForeignKey("FHIR_Patient", related_name="CareTeam_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Group = models.ForeignKey("FHIR_Group", related_name="CareTeam_subject", null=True, blank=True, on_delete=models.SET_NULL)
    period = models.OneToOneField("FHIR_GP_Period", related_name='CareTeam_period', null=True, blank=True, on_delete=models.SET_NULL)
    managingOrganization = models.ManyToManyField("FHIR_Organization", related_name="CareTeam_managingOrganization", blank=True)

class FHIR_CareTeam_identifier(FHIR_GP_Identifier):
    CareTeam = models.ForeignKey(FHIR_CareTeam, related_name='CareTeam_identifier', null=False, on_delete=models.CASCADE)

class FHIR_CareTeam_category(models.Model):
    CareTeam = models.ForeignKey(FHIR_CareTeam, related_name='CareTeam_category', null=False, on_delete=models.CASCADE)
    BINDING_category = "TODO"
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='CareTeam_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_CareTeam_participant(models.Model):
    CareTeam = models.ForeignKey(FHIR_CareTeam, related_name='CareTeam_participant', null=False, on_delete=models.CASCADE)
    BINDING_role = "TODO"
    role_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_role}, related_name='CareTeam_participant_role', blank=True)
    role_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    member_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="CareTeam_participant_member", null=True, blank=True, on_delete=models.SET_NULL)
    member_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="CareTeam_participant_member", null=True, blank=True, on_delete=models.SET_NULL)
    member_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="CareTeam_participant_member", null=True, blank=True, on_delete=models.SET_NULL)
    member_Patient = models.ForeignKey("FHIR_Patient", related_name="CareTeam_participant_member", null=True, blank=True, on_delete=models.SET_NULL)
    member_Organization = models.ForeignKey("FHIR_Organization", related_name="CareTeam_participant_member", null=True, blank=True, on_delete=models.SET_NULL)
    member_CareTeam = models.ForeignKey("FHIR_CareTeam", related_name="CareTeam_participant_member", null=True, blank=True, on_delete=models.SET_NULL)
    member_Group = models.ForeignKey("FHIR_Group", related_name="CareTeam_participant_member", null=True, blank=True, on_delete=models.SET_NULL)
    onBehalfOf_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="CareTeam_participant_onBehalfOf", null=True, blank=True, on_delete=models.SET_NULL)
    onBehalfOf_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="CareTeam_participant_onBehalfOf", null=True, blank=True, on_delete=models.SET_NULL)
    onBehalfOf_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="CareTeam_participant_onBehalfOf", null=True, blank=True, on_delete=models.SET_NULL)
    onBehalfOf_Patient = models.ForeignKey("FHIR_Patient", related_name="CareTeam_participant_onBehalfOf", null=True, blank=True, on_delete=models.SET_NULL)
    onBehalfOf_Organization = models.ForeignKey("FHIR_Organization", related_name="CareTeam_participant_onBehalfOf", null=True, blank=True, on_delete=models.SET_NULL)
    onBehalfOf_CareTeam = models.ForeignKey("FHIR_CareTeam", related_name="CareTeam_participant_onBehalfOf", null=True, blank=True, on_delete=models.SET_NULL)
    onBehalfOf_Group = models.ForeignKey("FHIR_Group", related_name="CareTeam_participant_onBehalfOf", null=True, blank=True, on_delete=models.SET_NULL)
    effective_Period = models.OneToOneField("FHIR_GP_Period", related_name='CareTeam_participant_effective_Period', null=True, blank=True, on_delete=models.SET_NULL)
    effective_Timing = models.OneToOneField("FHIR_GP_Timing", related_name='CareTeam_participant_effective_Timing', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_CareTeam_reason(models.Model):
    CareTeam = models.ForeignKey(FHIR_CareTeam, related_name='CareTeam_reason', null=False, on_delete=models.CASCADE)
    BINDING_reason = "TODO"
    reason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_reason}, related_name='CareTeam_reason', blank=True)
    reason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    reason_Condition_ref = models.ForeignKey("FHIR_Condition", related_name="CareTeam_reason_Condition", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_CareTeam_telecom(FHIR_GP_ContactPoint):
    CareTeam = models.ForeignKey(FHIR_CareTeam, related_name='CareTeam_telecom', null=False, on_delete=models.CASCADE)

class FHIR_CareTeam_note(FHIR_GP_Annotation):
    CareTeam = models.ForeignKey(FHIR_CareTeam, related_name='CareTeam_note', null=False, on_delete=models.CASCADE)
