
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_ArtifactAssessment(models.Model):
    title = FHIR_primitive_StringField(null=True, blank=True, )
    citeAs = FHIR_primitive_MarkdownField(null=True, blank=True, )
    artifact = FHIR_primitive_CanonicalField(null=True, blank=True, )
    artifact = FHIR_primitive_URIField(null=True, blank=True, )
    date = FHIR_primitive_DateTimeField(null=True, blank=True, )
    copyright = FHIR_primitive_MarkdownField(null=True, blank=True, )
    approvalDate = FHIR_primitive_DateField(null=True, blank=True, )
    lastReviewDate = FHIR_primitive_DateField(null=True, blank=True, )
    class WorkflowstatusChoices(models.TextChoices): SUBMITTED = 'submitted', 'Submitted'; TRIAGED = 'triaged', 'Triaged'; WAITING_FOR_INPUT = 'waiting-for-input', 'Waiting-for-input'; RESOLVED_NO_CHANGE = 'resolved-no-change', 'Resolved-no-change'; RESOLVED_CHANGE_REQUIRED = 'resolved-change-required', 'Resolved-change-required'; DEFERRED = 'deferred', 'Deferred'; DUPLICATE = 'duplicate', 'Duplicate'; APPLIED = 'applied', 'Applied'; PUBLISHED = 'published', 'Published'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; 
    workflowStatus = FHIR_primitive_CodeField(choices=WorkflowstatusChoices.choices, null=True, blank=True, )
    class DispositionChoices(models.TextChoices): UNRESOLVED = 'unresolved', 'Unresolved'; NOT_PERSUASIVE = 'not-persuasive', 'Not-persuasive'; PERSUASIVE = 'persuasive', 'Persuasive'; PERSUASIVE_WITH_MODIFICATION = 'persuasive-with-modification', 'Persuasive-with-modification'; NOT_PERSUASIVE_WITH_MODIFICATION = 'not-persuasive-with-modification', 'Not-persuasive-with-modification'; 
    disposition = FHIR_primitive_CodeField(choices=DispositionChoices.choices, null=True, blank=True, )

class FHIR_ArtifactAssessment_identifier(FHIR_GP_Identifier):
    ArtifactAssessment = models.ForeignKey(FHIR_ArtifactAssessment, related_name='ArtifactAssessment_identifier', null=False, on_delete=models.CASCADE)

class FHIR_ArtifactAssessment_relatesTo(models.Model):
    ArtifactAssessment = models.ForeignKey(FHIR_ArtifactAssessment, related_name='ArtifactAssessment_relatesTo', null=False, on_delete=models.CASCADE)
    class TypeChoices(models.TextChoices): DOCUMENTATION = 'documentation', 'Documentation'; JUSTIFICATION = 'justification', 'Justification'; PREDECESSOR = 'predecessor', 'Predecessor'; SUCCESSOR = 'successor', 'Successor'; DERIVED_FROM = 'derived-from', 'Derived-from'; DEPENDS_ON = 'depends-on', 'Depends-on'; COMPOSED_OF = 'composed-of', 'Composed-of'; PART_OF = 'part-of', 'Part-of'; AMENDS = 'amends', 'Amends'; AMENDED_WITH = 'amended-with', 'Amended-with'; APPENDS = 'appends', 'Appends'; APPENDED_WITH = 'appended-with', 'Appended-with'; CITES = 'cites', 'Cites'; CITED_BY = 'cited-by', 'Cited-by'; COMMENTS_ON = 'comments-on', 'Comments-on'; COMMENT_IN = 'comment-in', 'Comment-in'; CONTAINS = 'contains', 'Contains'; CONTAINED_IN = 'contained-in', 'Contained-in'; CORRECTS = 'corrects', 'Corrects'; CORRECTION_IN = 'correction-in', 'Correction-in'; REPLACES = 'replaces', 'Replaces'; REPLACED_WITH = 'replaced-with', 'Replaced-with'; RETRACTS = 'retracts', 'Retracts'; RETRACTED_BY = 'retracted-by', 'Retracted-by'; SIGNS = 'signs', 'Signs'; SIMILAR_TO = 'similar-to', 'Similar-to'; SUPPORTS = 'supports', 'Supports'; SUPPORTED_WITH = 'supported-with', 'Supported-with'; TRANSFORMS = 'transforms', 'Transforms'; TRANSFORMED_INTO = 'transformed-into', 'Transformed-into'; TRANSFORMED_WITH = 'transformed-with', 'Transformed-with'; SPECIFICATION_OF = 'specification-of', 'Specification-of'; CREATED_WITH = 'created-with', 'Created-with'; CITE_AS = 'cite-as', 'Cite-as'; SUMMARIZES = 'summarizes', 'Summarizes'; 
    type = FHIR_primitive_CodeField(choices=TypeChoices.choices, null=True, blank=True, )
    target = FHIR_primitive_URIField(null=True, blank=True, )
    target = models.OneToOneField("FHIR_GP_Attachment", related_name='ArtifactAssessment_relatesTo_target', null=True, blank=True, on_delete=models.SET_NULL)
    target = FHIR_primitive_CanonicalField(null=True, blank=True, )
    target = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_ArtifactAssessment_content(models.Model):
    ArtifactAssessment = models.ForeignKey(FHIR_ArtifactAssessment, related_name='ArtifactAssessment_content', null=False, on_delete=models.CASCADE)
    summary = FHIR_primitive_MarkdownField(null=True, blank=True, )
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='ArtifactAssessment_content_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='ArtifactAssessment_content_quantity', null=True, blank=True, on_delete=models.SET_NULL)
    author_Patient = models.ManyToManyField("FHIR_Patient", related_name="ArtifactAssessment_content_author", blank=True)
    author_Practitioner = models.ManyToManyField("FHIR_Practitioner", related_name="ArtifactAssessment_content_author", blank=True)
    author_PractitionerRole = models.ManyToManyField("FHIR_PractitionerRole", related_name="ArtifactAssessment_content_author", blank=True)
    author_Organization = models.ManyToManyField("FHIR_Organization", related_name="ArtifactAssessment_content_author", blank=True)
    author_Device = models.ManyToManyField("FHIR_Device", related_name="ArtifactAssessment_content_author", blank=True)
    freeToShare = FHIR_primitive_BooleanField(null=True, blank=True, )

class FHIR_ArtifactAssessment_content_classifier(models.Model):
    ArtifactAssessment_content = models.ForeignKey(FHIR_ArtifactAssessment_content, related_name='ArtifactAssessment_content_classifier', null=False, on_delete=models.CASCADE)
    BINDING_classifier = 'TODO'
    classifier_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_classifier}, related_name='ArtifactAssessment_content_classifier', blank=True)
    classifier_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ArtifactAssessment_content_path(models.Model):
    ArtifactAssessment_content = models.ForeignKey(FHIR_ArtifactAssessment_content, related_name='ArtifactAssessment_content_path', null=False, on_delete=models.CASCADE)
    
    path = FHIR_primitive_URIField(null=True, blank=True, )
    