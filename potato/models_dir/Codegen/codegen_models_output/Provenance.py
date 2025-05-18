#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Provenance(models.Model):
                            #skipping Reference(Any) for field target as Provenance target not in referenceAny_targets
    occurred_Period = models.OneToOneField("FHIR_GP_Period", related_name='Provenance_occurred_Period', null=True, blank=True, on_delete=models.SET_NULL)
    occurred_dateTime = FHIR_primitive_DateTimeField(null=True, blank=True, )
    recorded = FHIR_primitive_InstantField(null=True, blank=True, )
    location = models.ForeignKey("FHIR_Location", related_name="Provenance_location", null=True, blank=True, on_delete=models.SET_NULL)
    why = FHIR_primitive_MarkdownField(null=True, blank=True, )
    BINDING_activity = "TODO"
    activity_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_activity}, related_name='Provenance_activity', blank=True)
    activity_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
                            #skipping Reference(Any) for field basedOn as Provenance basedOn not in referenceAny_targets
    patient = models.ForeignKey("FHIR_Patient", related_name="Provenance_patient", null=True, blank=True, on_delete=models.SET_NULL)
    encounter = models.ForeignKey("FHIR_Encounter", related_name="Provenance_encounter", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Provenance_policy(models.Model):
    Provenance = models.ForeignKey(FHIR_Provenance, related_name='Provenance_policy', null=False, on_delete=models.CASCADE)
    
    policy = FHIR_primitive_URIField(null=True, blank=True, )
    
class FHIR_Provenance_agent(models.Model):
    Provenance = models.ForeignKey(FHIR_Provenance, related_name='Provenance_agent', null=False, on_delete=models.CASCADE)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Provenance_agent_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    who_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="Provenance_agent_who", null=True, blank=True, on_delete=models.SET_NULL)
    who_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="Provenance_agent_who", null=True, blank=True, on_delete=models.SET_NULL)
    who_Organization = models.ForeignKey("FHIR_Organization", related_name="Provenance_agent_who", null=True, blank=True, on_delete=models.SET_NULL)
    who_CareTeam = models.ForeignKey("FHIR_CareTeam", related_name="Provenance_agent_who", null=True, blank=True, on_delete=models.SET_NULL)
    who_Patient = models.ForeignKey("FHIR_Patient", related_name="Provenance_agent_who", null=True, blank=True, on_delete=models.SET_NULL)
    who_Device = models.ForeignKey("FHIR_Device", related_name="Provenance_agent_who", null=True, blank=True, on_delete=models.SET_NULL)
    who_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="Provenance_agent_who", null=True, blank=True, on_delete=models.SET_NULL)
    who_Group = models.ForeignKey("FHIR_Group", related_name="Provenance_agent_who", null=True, blank=True, on_delete=models.SET_NULL)
    who_HealthcareService = models.ForeignKey("FHIR_HealthcareService", related_name="Provenance_agent_who", null=True, blank=True, on_delete=models.SET_NULL)
    onBehalfOf_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="Provenance_agent_onBehalfOf", null=True, blank=True, on_delete=models.SET_NULL)
    onBehalfOf_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="Provenance_agent_onBehalfOf", null=True, blank=True, on_delete=models.SET_NULL)
    onBehalfOf_Organization = models.ForeignKey("FHIR_Organization", related_name="Provenance_agent_onBehalfOf", null=True, blank=True, on_delete=models.SET_NULL)
    onBehalfOf_CareTeam = models.ForeignKey("FHIR_CareTeam", related_name="Provenance_agent_onBehalfOf", null=True, blank=True, on_delete=models.SET_NULL)
    onBehalfOf_Patient = models.ForeignKey("FHIR_Patient", related_name="Provenance_agent_onBehalfOf", null=True, blank=True, on_delete=models.SET_NULL)
    onBehalfOf_Group = models.ForeignKey("FHIR_Group", related_name="Provenance_agent_onBehalfOf", null=True, blank=True, on_delete=models.SET_NULL)
    onBehalfOf_HealthcareService = models.ForeignKey("FHIR_HealthcareService", related_name="Provenance_agent_onBehalfOf", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Provenance_agent_role(models.Model):
    Provenance_agent = models.ForeignKey(FHIR_Provenance_agent, related_name='Provenance_agent_role', null=False, on_delete=models.CASCADE)
    BINDING_role = "TODO"
    role_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_role}, related_name='Provenance_agent_role', blank=True)
    role_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Provenance_entity(models.Model):
    Provenance = models.ForeignKey(FHIR_Provenance, related_name='Provenance_entity', null=False, on_delete=models.CASCADE)
    class RoleChoices(models.TextChoices): REVISION = 'revision', 'Revision'; QUOTATION = 'quotation', 'Quotation'; SOURCE = 'source', 'Source'; INSTANTIATES = 'instantiates', 'Instantiates'; REMOVAL = 'removal', 'Removal'; 
    role = FHIR_primitive_CodeField(choices=RoleChoices.choices, null=True, blank=True, )
                            #skipping Reference(Any) for field what as Provenance what not in referenceAny_targets

class FHIR_Provenance_signature(FHIR_GP_Signature):
    Provenance = models.ForeignKey(FHIR_Provenance, related_name='Provenance_signature', null=False, on_delete=models.CASCADE)
