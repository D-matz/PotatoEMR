#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Permission(models.Model):
    class StatusChoices(models.TextChoices): ACTIVE = 'active', 'Active'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; DRAFT = 'draft', 'Draft'; REJECTED = 'rejected', 'Rejected'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    asserter_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="Permission_asserter", null=True, blank=True, on_delete=models.SET_NULL)
    asserter_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="Permission_asserter", null=True, blank=True, on_delete=models.SET_NULL)
    asserter_Organization = models.ForeignKey("FHIR_Organization", related_name="Permission_asserter", null=True, blank=True, on_delete=models.SET_NULL)
    asserter_CareTeam = models.ForeignKey("FHIR_CareTeam", related_name="Permission_asserter", null=True, blank=True, on_delete=models.SET_NULL)
    asserter_Patient = models.ForeignKey("FHIR_Patient", related_name="Permission_asserter", null=True, blank=True, on_delete=models.SET_NULL)
    asserter_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="Permission_asserter", null=True, blank=True, on_delete=models.SET_NULL)
    asserter_HealthcareService = models.ForeignKey("FHIR_HealthcareService", related_name="Permission_asserter", null=True, blank=True, on_delete=models.SET_NULL)
    validity = models.OneToOneField("FHIR_GP_Period", related_name='Permission_validity', null=True, blank=True, on_delete=models.SET_NULL)
    class CombiningChoices(models.TextChoices): DENY_OVERRIDES = 'deny-overrides', 'Deny-overrides'; PERMIT_OVERRIDES = 'permit-overrides', 'Permit-overrides'; ORDERED_DENY_OVERRIDES = 'ordered-deny-overrides', 'Ordered-deny-overrides'; ORDERED_PERMIT_OVERRIDES = 'ordered-permit-overrides', 'Ordered-permit-overrides'; DENY_UNLESS_PERMIT = 'deny-unless-permit', 'Deny-unless-permit'; PERMIT_UNLESS_DENY = 'permit-unless-deny', 'Permit-unless-deny'; 
    combining = FHIR_primitive_CodeField(choices=CombiningChoices.choices, null=True, blank=True, )

class FHIR_Permission_identifier(FHIR_GP_Identifier):
    Permission = models.ForeignKey(FHIR_Permission, related_name='Permission_identifier', null=False, on_delete=models.CASCADE)

class FHIR_Permission_date(models.Model):
    Permission = models.ForeignKey(FHIR_Permission, related_name='Permission_date', null=False, on_delete=models.CASCADE)
    
    date = FHIR_primitive_DateTimeField(null=True, blank=True, )
    
class FHIR_Permission_justification(models.Model):
    Permission = models.ForeignKey(FHIR_Permission, related_name='Permission_justification', null=False, on_delete=models.CASCADE)
                            #skipping Reference(Any) for field evidence as Permission evidence not in referenceAny_targets

class FHIR_Permission_justification_basis(models.Model):
    Permission_justification = models.ForeignKey(FHIR_Permission_justification, related_name='Permission_justification_basis', null=False, on_delete=models.CASCADE)
    BINDING_basis = "TODO"
    basis_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_basis}, related_name='Permission_justification_basis', blank=True)
    basis_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Permission_rule(models.Model):
    Permission = models.ForeignKey(FHIR_Permission, related_name='Permission_rule', null=False, on_delete=models.CASCADE)
    import_field = models.ForeignKey("FHIR_Permission", related_name="Permission_rule_import", null=True, blank=True, on_delete=models.SET_NULL)
    class TypeChoices(models.TextChoices): DENY = 'deny', 'Deny'; PERMIT = 'permit', 'Permit'; 
    type = FHIR_primitive_CodeField(choices=TypeChoices.choices, null=True, blank=True, )

class FHIR_Permission_rule_data(models.Model):
    Permission_rule = models.ForeignKey(FHIR_Permission_rule, related_name='Permission_rule_data', null=False, on_delete=models.CASCADE)
    period = models.OneToOneField("FHIR_GP_Period", related_name='Permission_rule_data_period', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Permission_rule_data_resource(models.Model):
    Permission_rule_data = models.ForeignKey(FHIR_Permission_rule_data, related_name='Permission_rule_data_resource', null=False, on_delete=models.CASCADE)
    class MeaningChoices(models.TextChoices): INSTANCE = 'instance', 'Instance'; RELATED = 'related', 'Related'; DEPENDENTS = 'dependents', 'Dependents'; AUTHOREDBY = 'authoredby', 'Authoredby'; 
    meaning = FHIR_primitive_CodeField(choices=MeaningChoices.choices, null=True, blank=True, )
                            #skipping Reference(Any) for field reference as Permission reference not in referenceAny_targets

class FHIR_Permission_rule_data_security(FHIR_GP_Coding):
    Permission_rule_data = models.ForeignKey(FHIR_Permission_rule_data, related_name='Permission_rule_data_security', null=False, on_delete=models.CASCADE)

class FHIR_Permission_rule_activity(models.Model):
    Permission_rule = models.ForeignKey(FHIR_Permission_rule, related_name='Permission_rule_activity', null=False, on_delete=models.CASCADE)

class FHIR_Permission_rule_activity_actor(models.Model):
    Permission_rule_activity = models.ForeignKey(FHIR_Permission_rule_activity, related_name='Permission_rule_activity_actor', null=False, on_delete=models.CASCADE)
    BINDING_role = "TODO"
    role_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_role}, related_name='Permission_rule_activity_actor_role', blank=True)
    role_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    reference_Device = models.ForeignKey("FHIR_Device", related_name="Permission_rule_activity_actor_reference", null=True, blank=True, on_delete=models.SET_NULL)
    reference_Group = models.ForeignKey("FHIR_Group", related_name="Permission_rule_activity_actor_reference", null=True, blank=True, on_delete=models.SET_NULL)
    reference_CareTeam = models.ForeignKey("FHIR_CareTeam", related_name="Permission_rule_activity_actor_reference", null=True, blank=True, on_delete=models.SET_NULL)
    reference_Organization = models.ForeignKey("FHIR_Organization", related_name="Permission_rule_activity_actor_reference", null=True, blank=True, on_delete=models.SET_NULL)
    reference_Patient = models.ForeignKey("FHIR_Patient", related_name="Permission_rule_activity_actor_reference", null=True, blank=True, on_delete=models.SET_NULL)
    reference_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="Permission_rule_activity_actor_reference", null=True, blank=True, on_delete=models.SET_NULL)
    reference_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="Permission_rule_activity_actor_reference", null=True, blank=True, on_delete=models.SET_NULL)
    reference_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="Permission_rule_activity_actor_reference", null=True, blank=True, on_delete=models.SET_NULL)
    reference_DeviceDefinition = models.ForeignKey("FHIR_DeviceDefinition", related_name="Permission_rule_activity_actor_reference", null=True, blank=True, on_delete=models.SET_NULL)
    reference_Group = models.ForeignKey("FHIR_Group", related_name="Permission_rule_activity_actor_reference", null=True, blank=True, on_delete=models.SET_NULL)
    reference_HealthcareService = models.ForeignKey("FHIR_HealthcareService", related_name="Permission_rule_activity_actor_reference", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Permission_rule_activity_action(models.Model):
    Permission_rule_activity = models.ForeignKey(FHIR_Permission_rule_activity, related_name='Permission_rule_activity_action', null=False, on_delete=models.CASCADE)
    BINDING_action = "TODO"
    action_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_action}, related_name='Permission_rule_activity_action', blank=True)
    action_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Permission_rule_activity_purpose(models.Model):
    Permission_rule_activity = models.ForeignKey(FHIR_Permission_rule_activity, related_name='Permission_rule_activity_purpose', null=False, on_delete=models.CASCADE)
    BINDING_purpose = "TODO"
    purpose_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_purpose}, related_name='Permission_rule_activity_purpose', blank=True)
    purpose_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Permission_rule_limit(models.Model):
    Permission_rule = models.ForeignKey(FHIR_Permission_rule, related_name='Permission_rule_limit', null=False, on_delete=models.CASCADE)

class FHIR_Permission_rule_limit_control(models.Model):
    Permission_rule_limit = models.ForeignKey(FHIR_Permission_rule_limit, related_name='Permission_rule_limit_control', null=False, on_delete=models.CASCADE)
    BINDING_control = "TODO"
    control_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_control}, related_name='Permission_rule_limit_control', blank=True)
    control_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Permission_rule_limit_tag(FHIR_GP_Coding):
    Permission_rule_limit = models.ForeignKey(FHIR_Permission_rule_limit, related_name='Permission_rule_limit_tag', null=False, on_delete=models.CASCADE)

class FHIR_Permission_rule_limit_element(models.Model):
    Permission_rule_limit = models.ForeignKey(FHIR_Permission_rule_limit, related_name='Permission_rule_limit_element', null=False, on_delete=models.CASCADE)
    
    element = FHIR_primitive_StringField(null=True, blank=True, )
    