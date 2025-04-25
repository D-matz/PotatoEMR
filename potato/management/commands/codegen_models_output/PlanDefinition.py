
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_PlanDefinition(models.Model):
    url = FHIR_primitive_URIField(null=True, blank=True, )
    version = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = models.OneToOneField("FHIR_GP_Coding", related_name='PlanDefinition_versionAlgorithm', null=True, blank=True, on_delete=models.SET_NULL)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    title = FHIR_primitive_StringField(null=True, blank=True, )
    subtitle = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='PlanDefinition_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    class StatusChoices(models.TextChoices): DRAFT = 'draft', 'Draft'; ACTIVE = 'active', 'Active'; RETIRED = 'retired', 'Retired'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    experimental = FHIR_primitive_BooleanField(null=True, blank=True, )
    BINDING_subject = 'TODO'
    subject_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_subject}, related_name='PlanDefinition_subject', blank=True)
    subject_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    subject_Group = models.ForeignKey("FHIR_Group", related_name="PlanDefinition_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_MedicinalProductDefinition = models.ForeignKey("FHIR_MedicinalProductDefinition", related_name="PlanDefinition_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_SubstanceDefinition = models.ForeignKey("FHIR_SubstanceDefinition", related_name="PlanDefinition_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_AdministrableProductDefinition = models.ForeignKey("FHIR_AdministrableProductDefinition", related_name="PlanDefinition_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_ManufacturedItemDefinition = models.ForeignKey("FHIR_ManufacturedItemDefinition", related_name="PlanDefinition_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_PackagedProductDefinition = models.ForeignKey("FHIR_PackagedProductDefinition", related_name="PlanDefinition_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject = FHIR_primitive_CanonicalField(null=True, blank=True, )
    date = FHIR_primitive_DateTimeField(null=True, blank=True, )
    publisher = FHIR_primitive_StringField(null=True, blank=True, )
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    purpose = FHIR_primitive_MarkdownField(null=True, blank=True, )
    usage = FHIR_primitive_MarkdownField(null=True, blank=True, )
    copyright = FHIR_primitive_MarkdownField(null=True, blank=True, )
    copyrightLabel = FHIR_primitive_StringField(null=True, blank=True, )
    approvalDate = FHIR_primitive_DateField(null=True, blank=True, )
    lastReviewDate = FHIR_primitive_DateField(null=True, blank=True, )
    effectivePeriod = models.OneToOneField("FHIR_GP_Period", related_name='PlanDefinition_effectivePeriod', null=True, blank=True, on_delete=models.SET_NULL)
    asNeeded = FHIR_primitive_BooleanField(null=True, blank=True, )
    BINDING_asNeeded = 'TODO'
    asNeeded_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_asNeeded}, related_name='PlanDefinition_asNeeded', blank=True)
    asNeeded_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_PlanDefinition_identifier(FHIR_GP_Identifier):
    PlanDefinition = models.ForeignKey(FHIR_PlanDefinition, related_name='PlanDefinition_identifier', null=False, on_delete=models.CASCADE)

class FHIR_PlanDefinition_jurisdiction(models.Model):
    PlanDefinition = models.ForeignKey(FHIR_PlanDefinition, related_name='PlanDefinition_jurisdiction', null=False, on_delete=models.CASCADE)
    BINDING_jurisdiction = 'TODO'
    jurisdiction_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_jurisdiction}, related_name='PlanDefinition_jurisdiction', blank=True)
    jurisdiction_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_PlanDefinition_topic(models.Model):
    PlanDefinition = models.ForeignKey(FHIR_PlanDefinition, related_name='PlanDefinition_topic', null=False, on_delete=models.CASCADE)
    BINDING_topic = 'TODO'
    topic_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_topic}, related_name='PlanDefinition_topic', blank=True)
    topic_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_PlanDefinition_library(models.Model):
    PlanDefinition = models.ForeignKey(FHIR_PlanDefinition, related_name='PlanDefinition_library', null=False, on_delete=models.CASCADE)
    
    library = FHIR_primitive_CanonicalField(null=True, blank=True, )
    
class FHIR_PlanDefinition_goal(models.Model):
    PlanDefinition = models.ForeignKey(FHIR_PlanDefinition, related_name='PlanDefinition_goal', null=False, on_delete=models.CASCADE)
    BINDING_category = 'TODO'
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='PlanDefinition_goal_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_description = 'TODO'
    description_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_description}, related_name='PlanDefinition_goal_description', blank=True)
    description_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_priority = 'TODO'
    priority_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_priority}, related_name='PlanDefinition_goal_priority', blank=True)
    priority_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_start = 'TODO'
    start_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_start}, related_name='PlanDefinition_goal_start', blank=True)
    start_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_PlanDefinition_goal_addresses(models.Model):
    PlanDefinition_goal = models.ForeignKey(FHIR_PlanDefinition_goal, related_name='PlanDefinition_goal_addresses', null=False, on_delete=models.CASCADE)
    BINDING_addresses = 'TODO'
    addresses_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_addresses}, related_name='PlanDefinition_goal_addresses', blank=True)
    addresses_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_PlanDefinition_goal_target(models.Model):
    PlanDefinition_goal = models.ForeignKey(FHIR_PlanDefinition_goal, related_name='PlanDefinition_goal_target', null=False, on_delete=models.CASCADE)
    BINDING_measure = 'TODO'
    measure_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_measure}, related_name='PlanDefinition_goal_target_measure', blank=True)
    measure_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    detail = models.OneToOneField("FHIR_GP_Quantity", related_name='PlanDefinition_goal_target_detail', null=True, blank=True, on_delete=models.SET_NULL)
    detail = models.OneToOneField("FHIR_GP_Range", related_name='PlanDefinition_goal_target_detail', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_detail = 'TODO'
    detail_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_detail}, related_name='PlanDefinition_goal_target_detail', blank=True)
    detail_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    detail = FHIR_primitive_StringField(null=True, blank=True, )
    detail = FHIR_primitive_BooleanField(null=True, blank=True, )
    detail = models.OneToOneField("FHIR_GP_Ratio", related_name='PlanDefinition_goal_target_detail', null=True, blank=True, on_delete=models.SET_NULL)
    due = models.OneToOneField("FHIR_GP_Quantity_Duration", related_name='PlanDefinition_goal_target_due', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_PlanDefinition_actor(models.Model):
    PlanDefinition = models.ForeignKey(FHIR_PlanDefinition, related_name='PlanDefinition_actor', null=False, on_delete=models.CASCADE)
    title = FHIR_primitive_StringField(null=True, blank=True, )
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_PlanDefinition_actor_option(models.Model):
    PlanDefinition_actor = models.ForeignKey(FHIR_PlanDefinition_actor, related_name='PlanDefinition_actor_option', null=False, on_delete=models.CASCADE)
    class TypeChoices(models.TextChoices): CARETEAM = 'careteam', 'Careteam'; DEVICE = 'device', 'Device'; GROUP = 'group', 'Group'; HEALTHCARESERVICE = 'healthcareservice', 'Healthcareservice'; LOCATION = 'location', 'Location'; ORGANIZATION = 'organization', 'Organization'; PATIENT = 'patient', 'Patient'; PRACTITIONER = 'practitioner', 'Practitioner'; PRACTITIONERROLE = 'practitionerrole', 'Practitionerrole'; RELATEDPERSON = 'relatedperson', 'Relatedperson'; 
    type = FHIR_primitive_CodeField(choices=TypeChoices.choices, null=True, blank=True, )
    typeCanonical = FHIR_primitive_CanonicalField(null=True, blank=True, )
    typeReference_BiologicallyDerivedProduct = models.ForeignKey("FHIR_BiologicallyDerivedProduct", related_name="PlanDefinition_actor_option_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_CareTeam = models.ForeignKey("FHIR_CareTeam", related_name="PlanDefinition_actor_option_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_Device = models.ForeignKey("FHIR_Device", related_name="PlanDefinition_actor_option_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_DeviceDefinition = models.ForeignKey("FHIR_DeviceDefinition", related_name="PlanDefinition_actor_option_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_Endpoint = models.ForeignKey("FHIR_Endpoint", related_name="PlanDefinition_actor_option_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_Group = models.ForeignKey("FHIR_Group", related_name="PlanDefinition_actor_option_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_HealthcareService = models.ForeignKey("FHIR_HealthcareService", related_name="PlanDefinition_actor_option_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_Location = models.ForeignKey("FHIR_Location", related_name="PlanDefinition_actor_option_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_Medication = models.ForeignKey("FHIR_Medication", related_name="PlanDefinition_actor_option_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_Organization = models.ForeignKey("FHIR_Organization", related_name="PlanDefinition_actor_option_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_Patient = models.ForeignKey("FHIR_Patient", related_name="PlanDefinition_actor_option_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="PlanDefinition_actor_option_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="PlanDefinition_actor_option_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="PlanDefinition_actor_option_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_Specimen = models.ForeignKey("FHIR_Specimen", related_name="PlanDefinition_actor_option_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_Substance = models.ForeignKey("FHIR_Substance", related_name="PlanDefinition_actor_option_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_role = 'TODO'
    role_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_role}, related_name='PlanDefinition_actor_option_role', blank=True)
    role_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_PlanDefinition_action(models.Model):
    PlanDefinition = models.ForeignKey(FHIR_PlanDefinition, related_name='PlanDefinition_action', null=False, on_delete=models.CASCADE)
    linkId = FHIR_primitive_StringField(null=True, blank=True, )
    prefix = FHIR_primitive_StringField(null=True, blank=True, )
    title = FHIR_primitive_StringField(null=True, blank=True, )
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    textEquivalent = FHIR_primitive_MarkdownField(null=True, blank=True, )
    class PriorityChoices(models.TextChoices): ROUTINE = 'routine', 'Routine'; URGENT = 'urgent', 'Urgent'; ASAP = 'asap', 'Asap'; STAT = 'stat', 'Stat'; 
    priority = FHIR_primitive_CodeField(choices=PriorityChoices.choices, null=True, blank=True, )
    BINDING_code = 'TODO'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='PlanDefinition_action_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_subject = 'TODO'
    subject_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_subject}, related_name='PlanDefinition_action_subject', blank=True)
    subject_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    subject = models.ForeignKey("FHIR_Group", related_name="PlanDefinition_action_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject = FHIR_primitive_CanonicalField(null=True, blank=True, )
    timing = models.OneToOneField("FHIR_GP_Quantity_Age", related_name='PlanDefinition_action_timing', null=True, blank=True, on_delete=models.SET_NULL)
    timing = models.OneToOneField("FHIR_GP_Quantity_Duration", related_name='PlanDefinition_action_timing', null=True, blank=True, on_delete=models.SET_NULL)
    timing = models.OneToOneField("FHIR_GP_Range", related_name='PlanDefinition_action_timing', null=True, blank=True, on_delete=models.SET_NULL)
    timing = models.OneToOneField("FHIR_GP_Timing", related_name='PlanDefinition_action_timing', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_location = 'TODO'
    location_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_location}, related_name='PlanDefinition_action_location', blank=True)
    location_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    location_Location_ref = models.ForeignKey("FHIR_Location", related_name="PlanDefinition_action_location", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='PlanDefinition_action_type', blank=True)
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

class FHIR_PlanDefinition_action_reason(models.Model):
    PlanDefinition_action = models.ForeignKey(FHIR_PlanDefinition_action, related_name='PlanDefinition_action_reason', null=False, on_delete=models.CASCADE)
    BINDING_reason = 'TODO'
    reason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_reason}, related_name='PlanDefinition_action_reason', blank=True)
    reason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_PlanDefinition_action_goalId(models.Model):
    PlanDefinition_action = models.ForeignKey(FHIR_PlanDefinition_action, related_name='PlanDefinition_action_goalId', null=False, on_delete=models.CASCADE)
    
    goalId = FHIR_primitive_StringField(null=True, blank=True, )
    
class FHIR_PlanDefinition_action_condition(models.Model):
    PlanDefinition_action = models.ForeignKey(FHIR_PlanDefinition_action, related_name='PlanDefinition_action_condition', null=False, on_delete=models.CASCADE)
    class KindChoices(models.TextChoices): APPLICABILITY = 'applicability', 'Applicability'; START = 'start', 'Start'; STOP = 'stop', 'Stop'; 
    kind = FHIR_primitive_CodeField(choices=KindChoices.choices, null=True, blank=True, )

class FHIR_PlanDefinition_action_input(models.Model):
    PlanDefinition_action = models.ForeignKey(FHIR_PlanDefinition_action, related_name='PlanDefinition_action_input', null=False, on_delete=models.CASCADE)
    title = FHIR_primitive_StringField(null=True, blank=True, )
    relatedData = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_PlanDefinition_action_output(models.Model):
    PlanDefinition_action = models.ForeignKey(FHIR_PlanDefinition_action, related_name='PlanDefinition_action_output', null=False, on_delete=models.CASCADE)
    title = FHIR_primitive_StringField(null=True, blank=True, )
    relatedData = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_PlanDefinition_action_relatedAction(models.Model):
    PlanDefinition_action = models.ForeignKey(FHIR_PlanDefinition_action, related_name='PlanDefinition_action_relatedAction', null=False, on_delete=models.CASCADE)
    targetId = FHIR_primitive_StringField(null=True, blank=True, )
    class RelationshipChoices(models.TextChoices): BEFORE = 'before', 'Before'; BEFORE_START = 'before-start', 'Before-start'; BEFORE_END = 'before-end', 'Before-end'; CONCURRENT = 'concurrent', 'Concurrent'; CONCURRENT_WITH_START = 'concurrent-with-start', 'Concurrent-with-start'; CONCURRENT_WITH_END = 'concurrent-with-end', 'Concurrent-with-end'; AFTER = 'after', 'After'; AFTER_START = 'after-start', 'After-start'; AFTER_END = 'after-end', 'After-end'; 
    relationship = FHIR_primitive_CodeField(choices=RelationshipChoices.choices, null=True, blank=True, )
    class EndrelationshipChoices(models.TextChoices): BEFORE = 'before', 'Before'; BEFORE_START = 'before-start', 'Before-start'; BEFORE_END = 'before-end', 'Before-end'; CONCURRENT = 'concurrent', 'Concurrent'; CONCURRENT_WITH_START = 'concurrent-with-start', 'Concurrent-with-start'; CONCURRENT_WITH_END = 'concurrent-with-end', 'Concurrent-with-end'; AFTER = 'after', 'After'; AFTER_START = 'after-start', 'After-start'; AFTER_END = 'after-end', 'After-end'; 
    endRelationship = FHIR_primitive_CodeField(choices=EndrelationshipChoices.choices, null=True, blank=True, )
    offset = models.OneToOneField("FHIR_GP_Quantity_Duration", related_name='PlanDefinition_action_relatedAction_offset', null=True, blank=True, on_delete=models.SET_NULL)
    offset = models.OneToOneField("FHIR_GP_Range", related_name='PlanDefinition_action_relatedAction_offset', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_PlanDefinition_action_participant(models.Model):
    PlanDefinition_action = models.ForeignKey(FHIR_PlanDefinition_action, related_name='PlanDefinition_action_participant', null=False, on_delete=models.CASCADE)
    actorId = FHIR_primitive_StringField(null=True, blank=True, )
    class TypeChoices(models.TextChoices): CARETEAM = 'careteam', 'Careteam'; DEVICE = 'device', 'Device'; GROUP = 'group', 'Group'; HEALTHCARESERVICE = 'healthcareservice', 'Healthcareservice'; LOCATION = 'location', 'Location'; ORGANIZATION = 'organization', 'Organization'; PATIENT = 'patient', 'Patient'; PRACTITIONER = 'practitioner', 'Practitioner'; PRACTITIONERROLE = 'practitionerrole', 'Practitionerrole'; RELATEDPERSON = 'relatedperson', 'Relatedperson'; 
    type = FHIR_primitive_CodeField(choices=TypeChoices.choices, null=True, blank=True, )
    typeCanonical = FHIR_primitive_CanonicalField(null=True, blank=True, )
    typeReference_BiologicallyDerivedProduct = models.ForeignKey("FHIR_BiologicallyDerivedProduct", related_name="PlanDefinition_action_participant_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_CareTeam = models.ForeignKey("FHIR_CareTeam", related_name="PlanDefinition_action_participant_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_Device = models.ForeignKey("FHIR_Device", related_name="PlanDefinition_action_participant_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_DeviceDefinition = models.ForeignKey("FHIR_DeviceDefinition", related_name="PlanDefinition_action_participant_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_Endpoint = models.ForeignKey("FHIR_Endpoint", related_name="PlanDefinition_action_participant_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_Group = models.ForeignKey("FHIR_Group", related_name="PlanDefinition_action_participant_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_HealthcareService = models.ForeignKey("FHIR_HealthcareService", related_name="PlanDefinition_action_participant_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_Location = models.ForeignKey("FHIR_Location", related_name="PlanDefinition_action_participant_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_Medication = models.ForeignKey("FHIR_Medication", related_name="PlanDefinition_action_participant_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_Organization = models.ForeignKey("FHIR_Organization", related_name="PlanDefinition_action_participant_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_Patient = models.ForeignKey("FHIR_Patient", related_name="PlanDefinition_action_participant_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="PlanDefinition_action_participant_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="PlanDefinition_action_participant_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="PlanDefinition_action_participant_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_Specimen = models.ForeignKey("FHIR_Specimen", related_name="PlanDefinition_action_participant_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_Substance = models.ForeignKey("FHIR_Substance", related_name="PlanDefinition_action_participant_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_role = 'TODO'
    role_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_role}, related_name='PlanDefinition_action_participant_role', blank=True)
    role_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_function = 'TODO'
    function_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_function}, related_name='PlanDefinition_action_participant_function', blank=True)
    function_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_PlanDefinition_action_dynamicValue(models.Model):
    PlanDefinition_action = models.ForeignKey(FHIR_PlanDefinition_action, related_name='PlanDefinition_action_dynamicValue', null=False, on_delete=models.CASCADE)
    path = FHIR_primitive_StringField(null=True, blank=True, )
