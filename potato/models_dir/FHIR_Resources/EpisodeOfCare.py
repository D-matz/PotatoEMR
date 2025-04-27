#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_EpisodeOfCare(models.Model):
    class StatusChoices(models.TextChoices): PLANNED = 'planned', 'Planned'; WAITLIST = 'waitlist', 'Waitlist'; ACTIVE = 'active', 'Active'; ONHOLD = 'onhold', 'Onhold'; FINISHED = 'finished', 'Finished'; CANCELLED = 'cancelled', 'Cancelled'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    subject_Patient = models.ForeignKey("FHIR_Patient", related_name="EpisodeOfCare_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Group = models.ForeignKey("FHIR_Group", related_name="EpisodeOfCare_subject", null=True, blank=True, on_delete=models.SET_NULL)
    managingOrganization = models.ForeignKey("FHIR_Organization", related_name="EpisodeOfCare_managingOrganization", null=True, blank=True, on_delete=models.SET_NULL)
    period = models.OneToOneField("FHIR_GP_Period", related_name='EpisodeOfCare_period', null=True, blank=True, on_delete=models.SET_NULL)
    referralRequest = models.ManyToManyField("FHIR_ServiceRequest", related_name="EpisodeOfCare_referralRequest", blank=True)
    careManager_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="EpisodeOfCare_careManager", null=True, blank=True, on_delete=models.SET_NULL)
    careManager_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="EpisodeOfCare_careManager", null=True, blank=True, on_delete=models.SET_NULL)
    careTeam = models.ManyToManyField("FHIR_CareTeam", related_name="EpisodeOfCare_careTeam", blank=True)
    account = models.ManyToManyField("FHIR_Account", related_name="EpisodeOfCare_account", blank=True)

class FHIR_EpisodeOfCare_identifier(FHIR_GP_Identifier):
    EpisodeOfCare = models.ForeignKey(FHIR_EpisodeOfCare, related_name='EpisodeOfCare_identifier', null=False, on_delete=models.CASCADE)

class FHIR_EpisodeOfCare_statusHistory(models.Model):
    EpisodeOfCare = models.ForeignKey(FHIR_EpisodeOfCare, related_name='EpisodeOfCare_statusHistory', null=False, on_delete=models.CASCADE)
    class StatusChoices(models.TextChoices): PLANNED = 'planned', 'Planned'; WAITLIST = 'waitlist', 'Waitlist'; ACTIVE = 'active', 'Active'; ONHOLD = 'onhold', 'Onhold'; FINISHED = 'finished', 'Finished'; CANCELLED = 'cancelled', 'Cancelled'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    period = models.OneToOneField("FHIR_GP_Period", related_name='EpisodeOfCare_statusHistory_period', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_EpisodeOfCare_type(models.Model):
    EpisodeOfCare = models.ForeignKey(FHIR_EpisodeOfCare, related_name='EpisodeOfCare_type', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='EpisodeOfCare_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_EpisodeOfCare_reason(models.Model):
    EpisodeOfCare = models.ForeignKey(FHIR_EpisodeOfCare, related_name='EpisodeOfCare_reason', null=False, on_delete=models.CASCADE)

class FHIR_EpisodeOfCare_reason_use(models.Model):
    EpisodeOfCare_reason = models.ForeignKey(FHIR_EpisodeOfCare_reason, related_name='EpisodeOfCare_reason_use', null=False, on_delete=models.CASCADE)
    BINDING_use = 'TODO'
    use_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_use}, related_name='EpisodeOfCare_reason_use', blank=True)
    use_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_EpisodeOfCare_reason_value(models.Model):
    EpisodeOfCare_reason = models.ForeignKey(FHIR_EpisodeOfCare_reason, related_name='EpisodeOfCare_reason_value', null=False, on_delete=models.CASCADE)
    BINDING_value = 'TODO'
    value_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_value}, related_name='EpisodeOfCare_reason_value', blank=True)
    value_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value_Condition_ref = models.ForeignKey("FHIR_Condition", related_name="EpisodeOfCare_reason_value_Condition", null=True, blank=True, on_delete=models.SET_NULL)
    value_DiagnosticReport_ref = models.ForeignKey("FHIR_DiagnosticReport", related_name="EpisodeOfCare_reason_value_DiagnosticReport", null=True, blank=True, on_delete=models.SET_NULL)
    value_Procedure_ref = models.ForeignKey("FHIR_Procedure", related_name="EpisodeOfCare_reason_value_Procedure", null=True, blank=True, on_delete=models.SET_NULL)
    value_Observation_ref = models.ForeignKey("FHIR_Observation", related_name="EpisodeOfCare_reason_value_Observation", null=True, blank=True, on_delete=models.SET_NULL)
    value_HealthcareService_ref = models.ForeignKey("FHIR_HealthcareService", related_name="EpisodeOfCare_reason_value_HealthcareService", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_EpisodeOfCare_diagnosis(models.Model):
    EpisodeOfCare = models.ForeignKey(FHIR_EpisodeOfCare, related_name='EpisodeOfCare_diagnosis', null=False, on_delete=models.CASCADE)

class FHIR_EpisodeOfCare_diagnosis_condition(models.Model):
    EpisodeOfCare_diagnosis = models.ForeignKey(FHIR_EpisodeOfCare_diagnosis, related_name='EpisodeOfCare_diagnosis_condition', null=False, on_delete=models.CASCADE)
    BINDING_condition = 'TODO'
    condition_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_condition}, related_name='EpisodeOfCare_diagnosis_condition', blank=True)
    condition_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    condition_Condition_ref = models.ForeignKey("FHIR_Condition", related_name="EpisodeOfCare_diagnosis_condition_Condition", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_EpisodeOfCare_diagnosis_use(models.Model):
    EpisodeOfCare_diagnosis = models.ForeignKey(FHIR_EpisodeOfCare_diagnosis, related_name='EpisodeOfCare_diagnosis_use', null=False, on_delete=models.CASCADE)
    BINDING_use = 'TODO'
    use_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_use}, related_name='EpisodeOfCare_diagnosis_use', blank=True)
    use_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    