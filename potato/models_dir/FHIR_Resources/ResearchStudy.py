#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_ResearchStudy(models.Model):
    url = FHIR_primitive_URIField(null=True, blank=True, )
    version = FHIR_primitive_StringField(null=True, blank=True, )
    name = FHIR_primitive_StringField(null=True, blank=True, )
    title = FHIR_primitive_StringField(null=True, blank=True, )
    protocol = models.ManyToManyField("FHIR_PlanDefinition", related_name="ResearchStudy_protocol", blank=True)
    partOf = models.ManyToManyField("FHIR_ResearchStudy", related_name="ResearchStudy_partOf", blank=True)
    citeAs = FHIR_primitive_MarkdownField(null=True, blank=True, )
    date = FHIR_primitive_DateTimeField(null=True, blank=True, )
    class StatusChoices(models.TextChoices): DRAFT = 'draft', 'Draft'; ACTIVE = 'active', 'Active'; RETIRED = 'retired', 'Retired'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    BINDING_primaryPurposeType = "TODO"
    primaryPurposeType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_primaryPurposeType}, related_name='ResearchStudy_primaryPurposeType', blank=True)
    primaryPurposeType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_phase = "TODO"
    phase_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_phase}, related_name='ResearchStudy_phase', blank=True)
    phase_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    descriptionSummary = FHIR_primitive_MarkdownField(null=True, blank=True, )
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    period = models.OneToOneField("FHIR_GP_Period", related_name='ResearchStudy_period', null=True, blank=True, on_delete=models.SET_NULL)
    site_Location = models.ManyToManyField("FHIR_Location", related_name="ResearchStudy_site", blank=True)
    site_ResearchStudy = models.ManyToManyField("FHIR_ResearchStudy", related_name="ResearchStudy_site", blank=True)
    site_Organization = models.ManyToManyField("FHIR_Organization", related_name="ResearchStudy_site", blank=True)
    BINDING_whyStopped = "TODO"
    whyStopped_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_whyStopped}, related_name='ResearchStudy_whyStopped', blank=True)
    whyStopped_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    result_Citation = models.ManyToManyField("FHIR_Citation", related_name="ResearchStudy_result", blank=True)
    result_Composition = models.ManyToManyField("FHIR_Composition", related_name="ResearchStudy_result", blank=True)
    result_DiagnosticReport = models.ManyToManyField("FHIR_DiagnosticReport", related_name="ResearchStudy_result", blank=True)
    result_Evidence = models.ManyToManyField("FHIR_Evidence", related_name="ResearchStudy_result", blank=True)

class FHIR_ResearchStudy_identifier(FHIR_GP_Identifier):
    ResearchStudy = models.ForeignKey(FHIR_ResearchStudy, related_name='ResearchStudy_identifier', null=False, on_delete=models.CASCADE)

class FHIR_ResearchStudy_label(models.Model):
    ResearchStudy = models.ForeignKey(FHIR_ResearchStudy, related_name='ResearchStudy_label', null=False, on_delete=models.CASCADE)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='ResearchStudy_label_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_ResearchStudy_relatesTo(models.Model):
    ResearchStudy = models.ForeignKey(FHIR_ResearchStudy, related_name='ResearchStudy_relatesTo', null=False, on_delete=models.CASCADE)
    class TypeChoices(models.TextChoices): DOCUMENTATION = 'documentation', 'Documentation'; JUSTIFICATION = 'justification', 'Justification'; PREDECESSOR = 'predecessor', 'Predecessor'; SUCCESSOR = 'successor', 'Successor'; DERIVED_FROM = 'derived-from', 'Derived-from'; DEPENDS_ON = 'depends-on', 'Depends-on'; COMPOSED_OF = 'composed-of', 'Composed-of'; PART_OF = 'part-of', 'Part-of'; AMENDS = 'amends', 'Amends'; AMENDED_WITH = 'amended-with', 'Amended-with'; APPENDS = 'appends', 'Appends'; APPENDED_WITH = 'appended-with', 'Appended-with'; CITES = 'cites', 'Cites'; CITED_BY = 'cited-by', 'Cited-by'; COMMENTS_ON = 'comments-on', 'Comments-on'; COMMENT_IN = 'comment-in', 'Comment-in'; CONTAINS = 'contains', 'Contains'; CONTAINED_IN = 'contained-in', 'Contained-in'; CORRECTS = 'corrects', 'Corrects'; CORRECTION_IN = 'correction-in', 'Correction-in'; REPLACES = 'replaces', 'Replaces'; REPLACED_WITH = 'replaced-with', 'Replaced-with'; RETRACTS = 'retracts', 'Retracts'; RETRACTED_BY = 'retracted-by', 'Retracted-by'; SIGNS = 'signs', 'Signs'; SIMILAR_TO = 'similar-to', 'Similar-to'; SUPPORTS = 'supports', 'Supports'; SUPPORTED_WITH = 'supported-with', 'Supported-with'; TRANSFORMS = 'transforms', 'Transforms'; TRANSFORMED_INTO = 'transformed-into', 'Transformed-into'; TRANSFORMED_WITH = 'transformed-with', 'Transformed-with'; SPECIFICATION_OF = 'specification-of', 'Specification-of'; CREATED_WITH = 'created-with', 'Created-with'; CITE_AS = 'cite-as', 'Cite-as'; SUMMARIZES = 'summarizes', 'Summarizes'; 
    type = FHIR_primitive_CodeField(choices=TypeChoices.choices, null=True, blank=True, )
    target_uri = FHIR_primitive_URIField(null=True, blank=True, )
    target_Attachment = models.OneToOneField("FHIR_GP_Attachment", related_name='ResearchStudy_relatesTo_target_Attachment', null=True, blank=True, on_delete=models.SET_NULL)
    target_canonical = FHIR_primitive_CanonicalField(null=True, blank=True, )
    target_markdown = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_ResearchStudy_studyDesign(models.Model):
    ResearchStudy = models.ForeignKey(FHIR_ResearchStudy, related_name='ResearchStudy_studyDesign', null=False, on_delete=models.CASCADE)
    BINDING_studyDesign = "TODO"
    studyDesign_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_studyDesign}, related_name='ResearchStudy_studyDesign', blank=True)
    studyDesign_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ResearchStudy_focus(models.Model):
    ResearchStudy = models.ForeignKey(FHIR_ResearchStudy, related_name='ResearchStudy_focus', null=False, on_delete=models.CASCADE)
    BINDING_focus = "TODO"
    focus_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_focus}, related_name='ResearchStudy_focus', blank=True)
    focus_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    focus_Medication_ref = models.ForeignKey("FHIR_Medication", related_name="ResearchStudy_focus_Medication", null=True, blank=True, on_delete=models.SET_NULL)
    focus_MedicinalProductDefinition_ref = models.ForeignKey("FHIR_MedicinalProductDefinition", related_name="ResearchStudy_focus_MedicinalProductDefinition", null=True, blank=True, on_delete=models.SET_NULL)
    focus_SubstanceDefinition_ref = models.ForeignKey("FHIR_SubstanceDefinition", related_name="ResearchStudy_focus_SubstanceDefinition", null=True, blank=True, on_delete=models.SET_NULL)
    focus_DeviceDefinition_ref = models.ForeignKey("FHIR_DeviceDefinition", related_name="ResearchStudy_focus_DeviceDefinition", null=True, blank=True, on_delete=models.SET_NULL)
    focus_PlanDefinition_ref = models.ForeignKey("FHIR_PlanDefinition", related_name="ResearchStudy_focus_PlanDefinition", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ResearchStudy_condition(models.Model):
    ResearchStudy = models.ForeignKey(FHIR_ResearchStudy, related_name='ResearchStudy_condition', null=False, on_delete=models.CASCADE)
    BINDING_condition = "TODO"
    condition_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_condition}, related_name='ResearchStudy_condition', blank=True)
    condition_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ResearchStudy_keyword(models.Model):
    ResearchStudy = models.ForeignKey(FHIR_ResearchStudy, related_name='ResearchStudy_keyword', null=False, on_delete=models.CASCADE)
    BINDING_keyword = "TODO"
    keyword_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_keyword}, related_name='ResearchStudy_keyword', blank=True)
    keyword_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ResearchStudy_region(models.Model):
    ResearchStudy = models.ForeignKey(FHIR_ResearchStudy, related_name='ResearchStudy_region', null=False, on_delete=models.CASCADE)
    BINDING_region = "TODO"
    region_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_region}, related_name='ResearchStudy_region', blank=True)
    region_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ResearchStudy_note(FHIR_GP_Annotation):
    ResearchStudy = models.ForeignKey(FHIR_ResearchStudy, related_name='ResearchStudy_note', null=False, on_delete=models.CASCADE)

class FHIR_ResearchStudy_classifier(models.Model):
    ResearchStudy = models.ForeignKey(FHIR_ResearchStudy, related_name='ResearchStudy_classifier', null=False, on_delete=models.CASCADE)
    BINDING_classifier = "TODO"
    classifier_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_classifier}, related_name='ResearchStudy_classifier', blank=True)
    classifier_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ResearchStudy_associatedParty(models.Model):
    ResearchStudy = models.ForeignKey(FHIR_ResearchStudy, related_name='ResearchStudy_associatedParty', null=False, on_delete=models.CASCADE)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_role = "TODO"
    role_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_role}, related_name='ResearchStudy_associatedParty_role', blank=True)
    role_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    party_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="ResearchStudy_associatedParty_party", null=True, blank=True, on_delete=models.SET_NULL)
    party_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="ResearchStudy_associatedParty_party", null=True, blank=True, on_delete=models.SET_NULL)
    party_Organization = models.ForeignKey("FHIR_Organization", related_name="ResearchStudy_associatedParty_party", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ResearchStudy_associatedParty_period(FHIR_GP_Period):
    ResearchStudy_associatedParty = models.ForeignKey(FHIR_ResearchStudy_associatedParty, related_name='ResearchStudy_associatedParty_period', null=False, on_delete=models.CASCADE)

class FHIR_ResearchStudy_associatedParty_classifier(models.Model):
    ResearchStudy_associatedParty = models.ForeignKey(FHIR_ResearchStudy_associatedParty, related_name='ResearchStudy_associatedParty_classifier', null=False, on_delete=models.CASCADE)
    BINDING_classifier = "TODO"
    classifier_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_classifier}, related_name='ResearchStudy_associatedParty_classifier', blank=True)
    classifier_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ResearchStudy_progressStatus(models.Model):
    ResearchStudy = models.ForeignKey(FHIR_ResearchStudy, related_name='ResearchStudy_progressStatus', null=False, on_delete=models.CASCADE)
    BINDING_state = "TODO"
    state_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_state}, related_name='ResearchStudy_progressStatus_state', blank=True)
    state_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    actual = FHIR_primitive_BooleanField(null=True, blank=True, )
    period = models.OneToOneField("FHIR_GP_Period", related_name='ResearchStudy_progressStatus_period', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ResearchStudy_recruitment(models.Model):
    ResearchStudy = models.ForeignKey(FHIR_ResearchStudy, related_name='ResearchStudy_recruitment', null=False, on_delete=models.CASCADE)
    targetNumber = FHIR_primitive_UnsignedIntField(null=True, blank=True, )
    actualNumber = FHIR_primitive_UnsignedIntField(null=True, blank=True, )
    eligibility = models.ForeignKey("FHIR_Group", related_name="ResearchStudy_recruitment_eligibility", null=True, blank=True, on_delete=models.SET_NULL)
    actualGroup = models.ForeignKey("FHIR_Group", related_name="ResearchStudy_recruitment_actualGroup", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ResearchStudy_comparisonGroup(models.Model):
    ResearchStudy = models.ForeignKey(FHIR_ResearchStudy, related_name='ResearchStudy_comparisonGroup', null=False, on_delete=models.CASCADE)
    targetNumber = FHIR_primitive_UnsignedIntField(null=True, blank=True, )
    actualNumber = FHIR_primitive_UnsignedIntField(null=True, blank=True, )
    eligibility = models.ForeignKey("FHIR_Group", related_name="ResearchStudy_comparisonGroup_eligibility", null=True, blank=True, on_delete=models.SET_NULL)
    observedGroup = models.ForeignKey("FHIR_Group", related_name="ResearchStudy_comparisonGroup_observedGroup", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ResearchStudy_objective(models.Model):
    ResearchStudy = models.ForeignKey(FHIR_ResearchStudy, related_name='ResearchStudy_objective', null=False, on_delete=models.CASCADE)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='ResearchStudy_objective_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_ResearchStudy_objective_outcomeMeasure(models.Model):
    ResearchStudy_objective = models.ForeignKey(FHIR_ResearchStudy_objective, related_name='ResearchStudy_objective_outcomeMeasure', null=False, on_delete=models.CASCADE)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='ResearchStudy_objective_outcomeMeasure_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    endpoint = models.ForeignKey("FHIR_EvidenceVariable", related_name="ResearchStudy_objective_outcomeMeasure_endpoint", null=True, blank=True, on_delete=models.SET_NULL)
    population = models.ForeignKey("FHIR_Group", related_name="ResearchStudy_objective_outcomeMeasure_population", null=True, blank=True, on_delete=models.SET_NULL)
    intervention = models.ForeignKey("FHIR_Group", related_name="ResearchStudy_objective_outcomeMeasure_intervention", null=True, blank=True, on_delete=models.SET_NULL)
    comparator = models.ForeignKey("FHIR_Group", related_name="ResearchStudy_objective_outcomeMeasure_comparator", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_summaryMeasure = "TODO"
    summaryMeasure_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_summaryMeasure}, related_name='ResearchStudy_objective_outcomeMeasure_summaryMeasure', blank=True)
    summaryMeasure_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_ResearchStudy_objective_outcomeMeasure_eventHandling(models.Model):
    ResearchStudy_objective_outcomeMeasure = models.ForeignKey(FHIR_ResearchStudy_objective_outcomeMeasure, related_name='ResearchStudy_objective_outcomeMeasure_eventHandling', null=False, on_delete=models.CASCADE)
    BINDING_event = "TODO"
    event_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_event}, related_name='ResearchStudy_objective_outcomeMeasure_eventHandling_event', blank=True)
    event_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_group = "TODO"
    group_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_group}, related_name='ResearchStudy_objective_outcomeMeasure_eventHandling_group', blank=True)
    group_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_handling = "TODO"
    handling_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_handling}, related_name='ResearchStudy_objective_outcomeMeasure_eventHandling_handling', blank=True)
    handling_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
