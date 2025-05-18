#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_AuditEvent(models.Model):
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='AuditEvent_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    class ActionChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    action = FHIR_primitive_CodeField(choices=ActionChoices.choices, null=True, blank=True, )
    class SeverityChoices(models.TextChoices): EMERGENCY = 'emergency', 'Emergency'; ALERT = 'alert', 'Alert'; CRITICAL = 'critical', 'Critical'; ERROR = 'error', 'Error'; WARNING = 'warning', 'Warning'; NOTICE = 'notice', 'Notice'; INFORMATIONAL = 'informational', 'Informational'; DEBUG = 'debug', 'Debug'; 
    severity = FHIR_primitive_CodeField(choices=SeverityChoices.choices, null=True, blank=True, )
    occurred_Period = models.OneToOneField("FHIR_GP_Period", related_name='AuditEvent_occurred_Period', null=True, blank=True, on_delete=models.SET_NULL)
    occurred_dateTime = FHIR_primitive_DateTimeField(null=True, blank=True, )
    recorded = FHIR_primitive_InstantField(null=True, blank=True, )
                            #skipping Reference(Any) for field basedOn as AuditEvent basedOn not in referenceAny_targets
    patient = models.ForeignKey("FHIR_Patient", related_name="AuditEvent_patient", null=True, blank=True, on_delete=models.SET_NULL)
    encounter = models.ForeignKey("FHIR_Encounter", related_name="AuditEvent_encounter", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_AuditEvent_subtype(models.Model):
    AuditEvent = models.ForeignKey(FHIR_AuditEvent, related_name='AuditEvent_subtype', null=False, on_delete=models.CASCADE)
    BINDING_subtype = "TODO"
    subtype_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_subtype}, related_name='AuditEvent_subtype', blank=True)
    subtype_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_AuditEvent_outcome(models.Model):
    AuditEvent = models.ForeignKey(FHIR_AuditEvent, related_name='AuditEvent_outcome', null=False, on_delete=models.CASCADE)
    code = models.OneToOneField("FHIR_GP_Coding", related_name='AuditEvent_outcome_code', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_AuditEvent_outcome_detail(models.Model):
    AuditEvent_outcome = models.ForeignKey(FHIR_AuditEvent_outcome, related_name='AuditEvent_outcome_detail', null=False, on_delete=models.CASCADE)
    BINDING_detail = "TODO"
    detail_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_detail}, related_name='AuditEvent_outcome_detail', blank=True)
    detail_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_AuditEvent_authorization(models.Model):
    AuditEvent = models.ForeignKey(FHIR_AuditEvent, related_name='AuditEvent_authorization', null=False, on_delete=models.CASCADE)
    BINDING_authorization = "TODO"
    authorization_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_authorization}, related_name='AuditEvent_authorization', blank=True)
    authorization_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_AuditEvent_agent(models.Model):
    AuditEvent = models.ForeignKey(FHIR_AuditEvent, related_name='AuditEvent_agent', null=False, on_delete=models.CASCADE)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='AuditEvent_agent_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    who_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="AuditEvent_agent_who", null=True, blank=True, on_delete=models.SET_NULL)
    who_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="AuditEvent_agent_who", null=True, blank=True, on_delete=models.SET_NULL)
    who_Organization = models.ForeignKey("FHIR_Organization", related_name="AuditEvent_agent_who", null=True, blank=True, on_delete=models.SET_NULL)
    who_CareTeam = models.ForeignKey("FHIR_CareTeam", related_name="AuditEvent_agent_who", null=True, blank=True, on_delete=models.SET_NULL)
    who_Patient = models.ForeignKey("FHIR_Patient", related_name="AuditEvent_agent_who", null=True, blank=True, on_delete=models.SET_NULL)
    who_Device = models.ForeignKey("FHIR_Device", related_name="AuditEvent_agent_who", null=True, blank=True, on_delete=models.SET_NULL)
    who_DeviceDefinition = models.ForeignKey("FHIR_DeviceDefinition", related_name="AuditEvent_agent_who", null=True, blank=True, on_delete=models.SET_NULL)
    who_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="AuditEvent_agent_who", null=True, blank=True, on_delete=models.SET_NULL)
    who_Group = models.ForeignKey("FHIR_Group", related_name="AuditEvent_agent_who", null=True, blank=True, on_delete=models.SET_NULL)
    who_HealthcareService = models.ForeignKey("FHIR_HealthcareService", related_name="AuditEvent_agent_who", null=True, blank=True, on_delete=models.SET_NULL)
    requestor = FHIR_primitive_BooleanField(null=True, blank=True, )
    location = models.ForeignKey("FHIR_Location", related_name="AuditEvent_agent_location", null=True, blank=True, on_delete=models.SET_NULL)
    network_Reference = models.ForeignKey("FHIR_Endpoint", related_name="AuditEvent_agent_network_Reference", null=True, blank=True, on_delete=models.SET_NULL)
    network_uri = FHIR_primitive_URIField(null=True, blank=True, )
    network_string = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_AuditEvent_agent_role(models.Model):
    AuditEvent_agent = models.ForeignKey(FHIR_AuditEvent_agent, related_name='AuditEvent_agent_role', null=False, on_delete=models.CASCADE)
    BINDING_role = "TODO"
    role_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_role}, related_name='AuditEvent_agent_role', blank=True)
    role_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_AuditEvent_agent_policy(models.Model):
    AuditEvent_agent = models.ForeignKey(FHIR_AuditEvent_agent, related_name='AuditEvent_agent_policy', null=False, on_delete=models.CASCADE)
    
    policy = FHIR_primitive_URIField(null=True, blank=True, )
    
class FHIR_AuditEvent_agent_authorization(models.Model):
    AuditEvent_agent = models.ForeignKey(FHIR_AuditEvent_agent, related_name='AuditEvent_agent_authorization', null=False, on_delete=models.CASCADE)
    BINDING_authorization = "TODO"
    authorization_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_authorization}, related_name='AuditEvent_agent_authorization', blank=True)
    authorization_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_AuditEvent_source(models.Model):
    AuditEvent = models.ForeignKey(FHIR_AuditEvent, related_name='AuditEvent_source', null=False, on_delete=models.CASCADE)
    site = models.ForeignKey("FHIR_Location", related_name="AuditEvent_source_site", null=True, blank=True, on_delete=models.SET_NULL)
    observer_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="AuditEvent_source_observer", null=True, blank=True, on_delete=models.SET_NULL)
    observer_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="AuditEvent_source_observer", null=True, blank=True, on_delete=models.SET_NULL)
    observer_Organization = models.ForeignKey("FHIR_Organization", related_name="AuditEvent_source_observer", null=True, blank=True, on_delete=models.SET_NULL)
    observer_CareTeam = models.ForeignKey("FHIR_CareTeam", related_name="AuditEvent_source_observer", null=True, blank=True, on_delete=models.SET_NULL)
    observer_Patient = models.ForeignKey("FHIR_Patient", related_name="AuditEvent_source_observer", null=True, blank=True, on_delete=models.SET_NULL)
    observer_Device = models.ForeignKey("FHIR_Device", related_name="AuditEvent_source_observer", null=True, blank=True, on_delete=models.SET_NULL)
    observer_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="AuditEvent_source_observer", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_AuditEvent_source_type(models.Model):
    AuditEvent_source = models.ForeignKey(FHIR_AuditEvent_source, related_name='AuditEvent_source_type', null=False, on_delete=models.CASCADE)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='AuditEvent_source_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_AuditEvent_entity(models.Model):
    AuditEvent = models.ForeignKey(FHIR_AuditEvent, related_name='AuditEvent_entity', null=False, on_delete=models.CASCADE)
                            #skipping Reference(Any) for field what as AuditEvent what not in referenceAny_targets
    BINDING_role = "TODO"
    role_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_role}, related_name='AuditEvent_entity_role', blank=True)
    role_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    description = FHIR_primitive_StringField(null=True, blank=True, )
    query = FHIR_primitive_Base64BinaryField(null=True, blank=True, )

class FHIR_AuditEvent_entity_securityLabel(models.Model):
    AuditEvent_entity = models.ForeignKey(FHIR_AuditEvent_entity, related_name='AuditEvent_entity_securityLabel', null=False, on_delete=models.CASCADE)
    BINDING_securityLabel = "TODO"
    securityLabel_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_securityLabel}, related_name='AuditEvent_entity_securityLabel', blank=True)
    securityLabel_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_AuditEvent_entity_detail(models.Model):
    AuditEvent_entity = models.ForeignKey(FHIR_AuditEvent_entity, related_name='AuditEvent_entity_detail', null=False, on_delete=models.CASCADE)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='AuditEvent_entity_detail_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value_Quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='AuditEvent_entity_detail_value_Quantity', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_value_CodeableConcept = "TODO"
    value_CodeableConcept_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_value_CodeableConcept}, related_name='AuditEvent_entity_detail_value_CodeableConcept', blank=True)
    value_CodeableConcept_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value_string = FHIR_primitive_StringField(null=True, blank=True, )
    value_boolean = FHIR_primitive_BooleanField(null=True, blank=True, )
    value_Range = models.OneToOneField("FHIR_GP_Range", related_name='AuditEvent_entity_detail_value_Range', null=True, blank=True, on_delete=models.SET_NULL)
    value_Ratio = models.OneToOneField("FHIR_GP_Ratio", related_name='AuditEvent_entity_detail_value_Ratio', null=True, blank=True, on_delete=models.SET_NULL)
    value_time = FHIR_primitive_TimeField(null=True, blank=True, )
    value_dateTime = FHIR_primitive_DateTimeField(null=True, blank=True, )
    value_Period = models.OneToOneField("FHIR_GP_Period", related_name='AuditEvent_entity_detail_value_Period', null=True, blank=True, on_delete=models.SET_NULL)
    value_base64Binary = FHIR_primitive_Base64BinaryField(null=True, blank=True, )
