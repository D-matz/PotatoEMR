#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_RequestOrchestration(models.Model):
    groupIdentifier = models.OneToOneField("FHIR_GP_Identifier", related_name='RequestOrchestration_groupIdentifier', null=True, blank=True, on_delete=models.SET_NULL)
    class StatusChoices(models.TextChoices): DRAFT = 'draft', 'Draft'; ACTIVE = 'active', 'Active'; ON_HOLD = 'on-hold', 'On-hold'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; ENDED = 'ended', 'Ended'; COMPLETED = 'completed', 'Completed'; REVOKED = 'revoked', 'Revoked'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    class IntentChoices(models.TextChoices): PROPOSAL = 'proposal', 'Proposal'; PLAN = 'plan', 'Plan'; DIRECTIVE = 'directive', 'Directive'; ORDER = 'order', 'Order'; ORIGINAL_ORDER = 'original-order', 'Original-order'; REFLEX_ORDER = 'reflex-order', 'Reflex-order'; FILLER_ORDER = 'filler-order', 'Filler-order'; INSTANCE_ORDER = 'instance-order', 'Instance-order'; OPTION = 'option', 'Option'; 
    intent = FHIR_primitive_CodeField(choices=IntentChoices.choices, null=True, blank=True, )
    class PriorityChoices(models.TextChoices): ROUTINE = 'routine', 'Routine'; URGENT = 'urgent', 'Urgent'; ASAP = 'asap', 'Asap'; STAT = 'stat', 'Stat'; 
    priority = FHIR_primitive_CodeField(choices=PriorityChoices.choices, null=True, blank=True, )
    BINDING_code = "TODO"
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='RequestOrchestration_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    subject_CareTeam = models.ForeignKey("FHIR_CareTeam", related_name="RequestOrchestration_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Device = models.ForeignKey("FHIR_Device", related_name="RequestOrchestration_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Group = models.ForeignKey("FHIR_Group", related_name="RequestOrchestration_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_HealthcareService = models.ForeignKey("FHIR_HealthcareService", related_name="RequestOrchestration_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Location = models.ForeignKey("FHIR_Location", related_name="RequestOrchestration_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Organization = models.ForeignKey("FHIR_Organization", related_name="RequestOrchestration_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Patient = models.ForeignKey("FHIR_Patient", related_name="RequestOrchestration_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="RequestOrchestration_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="RequestOrchestration_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="RequestOrchestration_subject", null=True, blank=True, on_delete=models.SET_NULL)
    encounter = models.ForeignKey("FHIR_Encounter", related_name="RequestOrchestration_encounter", null=True, blank=True, on_delete=models.SET_NULL)
    authoredOn = FHIR_primitive_DateTimeField(null=True, blank=True, )
    author_Device = models.ForeignKey("FHIR_Device", related_name="RequestOrchestration_author", null=True, blank=True, on_delete=models.SET_NULL)
    author_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="RequestOrchestration_author", null=True, blank=True, on_delete=models.SET_NULL)
    author_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="RequestOrchestration_author", null=True, blank=True, on_delete=models.SET_NULL)
    goal = models.ManyToManyField("FHIR_Goal", related_name="RequestOrchestration_goal", blank=True)

class FHIR_RequestOrchestration_identifier(FHIR_GP_Identifier):
    RequestOrchestration = models.ForeignKey(FHIR_RequestOrchestration, related_name='RequestOrchestration_identifier', null=False, on_delete=models.CASCADE)

class FHIR_RequestOrchestration_instantiatesCanonical(models.Model):
    RequestOrchestration = models.ForeignKey(FHIR_RequestOrchestration, related_name='RequestOrchestration_instantiatesCanonical', null=False, on_delete=models.CASCADE)
    
    instantiatesCanonical = FHIR_primitive_CanonicalField(null=True, blank=True, )
    
class FHIR_RequestOrchestration_instantiatesUri(models.Model):
    RequestOrchestration = models.ForeignKey(FHIR_RequestOrchestration, related_name='RequestOrchestration_instantiatesUri', null=False, on_delete=models.CASCADE)
    
    instantiatesUri = FHIR_primitive_URIField(null=True, blank=True, )
    
class FHIR_RequestOrchestration_reason(models.Model):
    RequestOrchestration = models.ForeignKey(FHIR_RequestOrchestration, related_name='RequestOrchestration_reason', null=False, on_delete=models.CASCADE)
    BINDING_reason = "TODO"
    reason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_reason}, related_name='RequestOrchestration_reason', blank=True)
    reason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    reason_Condition_ref = models.ForeignKey("FHIR_Condition", related_name="RequestOrchestration_reason_Condition", null=True, blank=True, on_delete=models.SET_NULL)
    reason_Observation_ref = models.ForeignKey("FHIR_Observation", related_name="RequestOrchestration_reason_Observation", null=True, blank=True, on_delete=models.SET_NULL)
    reason_DiagnosticReport_ref = models.ForeignKey("FHIR_DiagnosticReport", related_name="RequestOrchestration_reason_DiagnosticReport", null=True, blank=True, on_delete=models.SET_NULL)
    reason_DocumentReference_ref = models.ForeignKey("FHIR_DocumentReference", related_name="RequestOrchestration_reason_DocumentReference", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_RequestOrchestration_note(FHIR_GP_Annotation):
    RequestOrchestration = models.ForeignKey(FHIR_RequestOrchestration, related_name='RequestOrchestration_note', null=False, on_delete=models.CASCADE)

class FHIR_RequestOrchestration_action(models.Model):
    RequestOrchestration = models.ForeignKey(FHIR_RequestOrchestration, related_name='RequestOrchestration_action', null=False, on_delete=models.CASCADE)
    linkId = FHIR_primitive_StringField(null=True, blank=True, )
    prefix = FHIR_primitive_StringField(null=True, blank=True, )
    title = FHIR_primitive_StringField(null=True, blank=True, )
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    textEquivalent = FHIR_primitive_MarkdownField(null=True, blank=True, )
    class PriorityChoices(models.TextChoices): ROUTINE = 'routine', 'Routine'; URGENT = 'urgent', 'Urgent'; ASAP = 'asap', 'Asap'; STAT = 'stat', 'Stat'; 
    priority = FHIR_primitive_CodeField(choices=PriorityChoices.choices, null=True, blank=True, )
    goal = models.ManyToManyField("FHIR_Goal", related_name="RequestOrchestration_action_goal", blank=True)
    timing = FHIR_primitive_DateTimeField(null=True, blank=True, )
    timing = models.OneToOneField("FHIR_GP_Quantity_Age", related_name='RequestOrchestration_action_timing', null=True, blank=True, on_delete=models.SET_NULL)
    timing = models.OneToOneField("FHIR_GP_Period", related_name='RequestOrchestration_action_timing', null=True, blank=True, on_delete=models.SET_NULL)
    timing = models.OneToOneField("FHIR_GP_Quantity_Duration", related_name='RequestOrchestration_action_timing', null=True, blank=True, on_delete=models.SET_NULL)
    timing = models.OneToOneField("FHIR_GP_Range", related_name='RequestOrchestration_action_timing', null=True, blank=True, on_delete=models.SET_NULL)
    timing = models.OneToOneField("FHIR_GP_Timing", related_name='RequestOrchestration_action_timing', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_location = "TODO"
    location_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_location}, related_name='RequestOrchestration_action_location', blank=True)
    location_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    location_Location_ref = models.ForeignKey("FHIR_Location", related_name="RequestOrchestration_action_location_Location", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='RequestOrchestration_action_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    class GroupingbehaviorChoices(models.TextChoices): VISUAL_GROUP = 'visual-group', 'Visual-group'; LOGICAL_GROUP = 'logical-group', 'Logical-group'; SENTENCE_GROUP = 'sentence-group', 'Sentence-group'; 
    groupingBehavior = FHIR_primitive_CodeField(choices=GroupingbehaviorChoices.choices, null=True, blank=True, )
    class SelectionbehaviorChoices(models.TextChoices): ANY = 'any', 'Any'; ALL = 'all', 'All'; ALL_OR_NONE = 'all-or-none', 'All-or-none'; EXACTLY_ONE = 'exactly-one', 'Exactly-one'; AT_MOST_ONE = 'at-most-one', 'At-most-one'; ONE_OR_MORE = 'one-or-more', 'One-or-more'; 
    selectionBehavior = FHIR_primitive_CodeField(choices=SelectionbehaviorChoices.choices, null=True, blank=True, )
    class RequiredbehaviorChoices(models.TextChoices): MUST = 'must', 'Must'; COULD = 'could', 'Could'; MUST_UNLESS_DOCUMENTED = 'must-unless-documented', 'Must-unless-documented'; 
    requiredBehavior = FHIR_primitive_CodeField(choices=RequiredbehaviorChoices.choices, null=True, blank=True, )
    class PrecheckbehaviorChoices(models.TextChoices): YES = 'yes', 'Yes'; NO = 'no', 'No'; 
    precheckBehavior = FHIR_primitive_CodeField(choices=PrecheckbehaviorChoices.choices, null=True, blank=True, )
    class CardinalitybehaviorChoices(models.TextChoices): SINGLE = 'single', 'Single'; MULTIPLE = 'multiple', 'Multiple'; 
    cardinalityBehavior = FHIR_primitive_CodeField(choices=CardinalitybehaviorChoices.choices, null=True, blank=True, )
    definition = FHIR_primitive_CanonicalField(null=True, blank=True, )
    definition = FHIR_primitive_URIField(null=True, blank=True, )
    transform = FHIR_primitive_CanonicalField(null=True, blank=True, )

class FHIR_RequestOrchestration_action_code(models.Model):
    RequestOrchestration_action = models.ForeignKey(FHIR_RequestOrchestration_action, related_name='RequestOrchestration_action_code', null=False, on_delete=models.CASCADE)
    BINDING_code = "TODO"
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='RequestOrchestration_action_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_RequestOrchestration_action_condition(models.Model):
    RequestOrchestration_action = models.ForeignKey(FHIR_RequestOrchestration_action, related_name='RequestOrchestration_action_condition', null=False, on_delete=models.CASCADE)
    class KindChoices(models.TextChoices): APPLICABILITY = 'applicability', 'Applicability'; START = 'start', 'Start'; STOP = 'stop', 'Stop'; 
    kind = FHIR_primitive_CodeField(choices=KindChoices.choices, null=True, blank=True, )

class FHIR_RequestOrchestration_action_input(models.Model):
    RequestOrchestration_action = models.ForeignKey(FHIR_RequestOrchestration_action, related_name='RequestOrchestration_action_input', null=False, on_delete=models.CASCADE)
    title = FHIR_primitive_StringField(null=True, blank=True, )
    relatedData = FHIR_primitive_IdField(null=True, blank=True, )

class FHIR_RequestOrchestration_action_output(models.Model):
    RequestOrchestration_action = models.ForeignKey(FHIR_RequestOrchestration_action, related_name='RequestOrchestration_action_output', null=False, on_delete=models.CASCADE)
    title = FHIR_primitive_StringField(null=True, blank=True, )
    relatedData = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_RequestOrchestration_action_relatedAction(models.Model):
    RequestOrchestration_action = models.ForeignKey(FHIR_RequestOrchestration_action, related_name='RequestOrchestration_action_relatedAction', null=False, on_delete=models.CASCADE)
    targetId = FHIR_primitive_IdField(null=True, blank=True, )
    class RelationshipChoices(models.TextChoices): BEFORE = 'before', 'Before'; BEFORE_START = 'before-start', 'Before-start'; BEFORE_END = 'before-end', 'Before-end'; CONCURRENT = 'concurrent', 'Concurrent'; CONCURRENT_WITH_START = 'concurrent-with-start', 'Concurrent-with-start'; CONCURRENT_WITH_END = 'concurrent-with-end', 'Concurrent-with-end'; AFTER = 'after', 'After'; AFTER_START = 'after-start', 'After-start'; AFTER_END = 'after-end', 'After-end'; 
    relationship = FHIR_primitive_CodeField(choices=RelationshipChoices.choices, null=True, blank=True, )
    class EndrelationshipChoices(models.TextChoices): BEFORE = 'before', 'Before'; BEFORE_START = 'before-start', 'Before-start'; BEFORE_END = 'before-end', 'Before-end'; CONCURRENT = 'concurrent', 'Concurrent'; CONCURRENT_WITH_START = 'concurrent-with-start', 'Concurrent-with-start'; CONCURRENT_WITH_END = 'concurrent-with-end', 'Concurrent-with-end'; AFTER = 'after', 'After'; AFTER_START = 'after-start', 'After-start'; AFTER_END = 'after-end', 'After-end'; 
    endRelationship = FHIR_primitive_CodeField(choices=EndrelationshipChoices.choices, null=True, blank=True, )
    offset = models.OneToOneField("FHIR_GP_Quantity_Duration", related_name='RequestOrchestration_action_relatedAction_offset', null=True, blank=True, on_delete=models.SET_NULL)
    offset = models.OneToOneField("FHIR_GP_Range", related_name='RequestOrchestration_action_relatedAction_offset', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_RequestOrchestration_action_participant(models.Model):
    RequestOrchestration_action = models.ForeignKey(FHIR_RequestOrchestration_action, related_name='RequestOrchestration_action_participant', null=False, on_delete=models.CASCADE)
    class TypeChoices(models.TextChoices): CARETEAM = 'careteam', 'Careteam'; DEVICE = 'device', 'Device'; GROUP = 'group', 'Group'; HEALTHCARESERVICE = 'healthcareservice', 'Healthcareservice'; LOCATION = 'location', 'Location'; ORGANIZATION = 'organization', 'Organization'; PATIENT = 'patient', 'Patient'; PRACTITIONER = 'practitioner', 'Practitioner'; PRACTITIONERROLE = 'practitionerrole', 'Practitionerrole'; RELATEDPERSON = 'relatedperson', 'Relatedperson'; 
    type = FHIR_primitive_CodeField(choices=TypeChoices.choices, null=True, blank=True, )
    typeCanonical = FHIR_primitive_CanonicalField(null=True, blank=True, )
    typeReference_CareTeam = models.ForeignKey("FHIR_CareTeam", related_name="RequestOrchestration_action_participant_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_Device = models.ForeignKey("FHIR_Device", related_name="RequestOrchestration_action_participant_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_DeviceDefinition = models.ForeignKey("FHIR_DeviceDefinition", related_name="RequestOrchestration_action_participant_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_Endpoint = models.ForeignKey("FHIR_Endpoint", related_name="RequestOrchestration_action_participant_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_Group = models.ForeignKey("FHIR_Group", related_name="RequestOrchestration_action_participant_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_HealthcareService = models.ForeignKey("FHIR_HealthcareService", related_name="RequestOrchestration_action_participant_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_Location = models.ForeignKey("FHIR_Location", related_name="RequestOrchestration_action_participant_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_Organization = models.ForeignKey("FHIR_Organization", related_name="RequestOrchestration_action_participant_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_Patient = models.ForeignKey("FHIR_Patient", related_name="RequestOrchestration_action_participant_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="RequestOrchestration_action_participant_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="RequestOrchestration_action_participant_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="RequestOrchestration_action_participant_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_role = "TODO"
    role_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_role}, related_name='RequestOrchestration_action_participant_role', blank=True)
    role_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_function = "TODO"
    function_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_function}, related_name='RequestOrchestration_action_participant_function', blank=True)
    function_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    actor = FHIR_primitive_CanonicalField(null=True, blank=True, )
    actor_CareTeam = models.ForeignKey("FHIR_CareTeam", related_name="RequestOrchestration_action_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Device = models.ForeignKey("FHIR_Device", related_name="RequestOrchestration_action_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_DeviceDefinition = models.ForeignKey("FHIR_DeviceDefinition", related_name="RequestOrchestration_action_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Endpoint = models.ForeignKey("FHIR_Endpoint", related_name="RequestOrchestration_action_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Group = models.ForeignKey("FHIR_Group", related_name="RequestOrchestration_action_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_HealthcareService = models.ForeignKey("FHIR_HealthcareService", related_name="RequestOrchestration_action_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Location = models.ForeignKey("FHIR_Location", related_name="RequestOrchestration_action_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Organization = models.ForeignKey("FHIR_Organization", related_name="RequestOrchestration_action_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Patient = models.ForeignKey("FHIR_Patient", related_name="RequestOrchestration_action_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="RequestOrchestration_action_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="RequestOrchestration_action_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="RequestOrchestration_action_participant_actor", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_RequestOrchestration_action_dynamicValue(models.Model):
    RequestOrchestration_action = models.ForeignKey(FHIR_RequestOrchestration_action, related_name='RequestOrchestration_action_dynamicValue', null=False, on_delete=models.CASCADE)
    path = FHIR_primitive_StringField(null=True, blank=True, )
