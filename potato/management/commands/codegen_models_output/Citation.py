
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Citation(models.Model):
    url = FHIR_primitive_URIField(null=True, blank=True, )
    version = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = models.OneToOneField("FHIR_GP_Coding", related_name='Citation_versionAlgorithm', null=True, blank=True, on_delete=models.SET_NULL)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    title = FHIR_primitive_StringField(null=True, blank=True, )
    class StatusChoices(models.TextChoices): DRAFT = 'draft', 'Draft'; ACTIVE = 'active', 'Active'; RETIRED = 'retired', 'Retired'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    experimental = FHIR_primitive_BooleanField(null=True, blank=True, )
    date = FHIR_primitive_DateTimeField(null=True, blank=True, )
    publisher = FHIR_primitive_StringField(null=True, blank=True, )
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    purpose = FHIR_primitive_MarkdownField(null=True, blank=True, )
    copyright = FHIR_primitive_MarkdownField(null=True, blank=True, )
    copyrightLabel = FHIR_primitive_StringField(null=True, blank=True, )
    approvalDate = FHIR_primitive_DateField(null=True, blank=True, )
    lastReviewDate = FHIR_primitive_DateField(null=True, blank=True, )
    effectivePeriod = models.OneToOneField("FHIR_GP_Period", related_name='Citation_effectivePeriod', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Citation_identifier(FHIR_GP_Identifier):
    Citation = models.ForeignKey(FHIR_Citation, related_name='Citation_identifier', null=False, on_delete=models.CASCADE)

class FHIR_Citation_jurisdiction(models.Model):
    Citation = models.ForeignKey(FHIR_Citation, related_name='Citation_jurisdiction', null=False, on_delete=models.CASCADE)
    BINDING_jurisdiction = 'TODO'
    jurisdiction_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_jurisdiction}, related_name='Citation_jurisdiction', blank=True)
    jurisdiction_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Citation_summary(models.Model):
    Citation = models.ForeignKey(FHIR_Citation, related_name='Citation_summary', null=False, on_delete=models.CASCADE)
    BINDING_style = 'TODO'
    style_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_style}, related_name='Citation_summary_style', blank=True)
    style_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    text = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_Citation_classification(models.Model):
    Citation = models.ForeignKey(FHIR_Citation, related_name='Citation_classification', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Citation_classification_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_Citation_classification_classifier(models.Model):
    Citation_classification = models.ForeignKey(FHIR_Citation_classification, related_name='Citation_classification_classifier', null=False, on_delete=models.CASCADE)
    BINDING_classifier = 'TODO'
    classifier_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_classifier}, related_name='Citation_classification_classifier', blank=True)
    classifier_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Citation_note(FHIR_GP_Annotation):
    Citation = models.ForeignKey(FHIR_Citation, related_name='Citation_note', null=False, on_delete=models.CASCADE)

class FHIR_Citation_currentState(models.Model):
    Citation = models.ForeignKey(FHIR_Citation, related_name='Citation_currentState', null=False, on_delete=models.CASCADE)
    BINDING_currentState = 'TODO'
    currentState_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_currentState}, related_name='Citation_currentState', blank=True)
    currentState_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Citation_statusDate(models.Model):
    Citation = models.ForeignKey(FHIR_Citation, related_name='Citation_statusDate', null=False, on_delete=models.CASCADE)
    BINDING_activity = 'TODO'
    activity_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_activity}, related_name='Citation_statusDate_activity', blank=True)
    activity_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    actual = FHIR_primitive_BooleanField(null=True, blank=True, )
    period = models.OneToOneField("FHIR_GP_Period", related_name='Citation_statusDate_period', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Citation_relatesTo(models.Model):
    Citation = models.ForeignKey(FHIR_Citation, related_name='Citation_relatesTo', null=False, on_delete=models.CASCADE)
    class TypeChoices(models.TextChoices): DOCUMENTATION = 'documentation', 'Documentation'; JUSTIFICATION = 'justification', 'Justification'; PREDECESSOR = 'predecessor', 'Predecessor'; SUCCESSOR = 'successor', 'Successor'; DERIVED_FROM = 'derived-from', 'Derived-from'; DEPENDS_ON = 'depends-on', 'Depends-on'; COMPOSED_OF = 'composed-of', 'Composed-of'; PART_OF = 'part-of', 'Part-of'; AMENDS = 'amends', 'Amends'; AMENDED_WITH = 'amended-with', 'Amended-with'; APPENDS = 'appends', 'Appends'; APPENDED_WITH = 'appended-with', 'Appended-with'; CITES = 'cites', 'Cites'; CITED_BY = 'cited-by', 'Cited-by'; COMMENTS_ON = 'comments-on', 'Comments-on'; COMMENT_IN = 'comment-in', 'Comment-in'; CONTAINS = 'contains', 'Contains'; CONTAINED_IN = 'contained-in', 'Contained-in'; CORRECTS = 'corrects', 'Corrects'; CORRECTION_IN = 'correction-in', 'Correction-in'; REPLACES = 'replaces', 'Replaces'; REPLACED_WITH = 'replaced-with', 'Replaced-with'; RETRACTS = 'retracts', 'Retracts'; RETRACTED_BY = 'retracted-by', 'Retracted-by'; SIGNS = 'signs', 'Signs'; SIMILAR_TO = 'similar-to', 'Similar-to'; SUPPORTS = 'supports', 'Supports'; SUPPORTED_WITH = 'supported-with', 'Supported-with'; TRANSFORMS = 'transforms', 'Transforms'; TRANSFORMED_INTO = 'transformed-into', 'Transformed-into'; TRANSFORMED_WITH = 'transformed-with', 'Transformed-with'; SPECIFICATION_OF = 'specification-of', 'Specification-of'; CREATED_WITH = 'created-with', 'Created-with'; CITE_AS = 'cite-as', 'Cite-as'; SUMMARIZES = 'summarizes', 'Summarizes'; 
    type = FHIR_primitive_CodeField(choices=TypeChoices.choices, null=True, blank=True, )
    target = FHIR_primitive_URIField(null=True, blank=True, )
    target = models.OneToOneField("FHIR_GP_Attachment", related_name='Citation_relatesTo_target', null=True, blank=True, on_delete=models.SET_NULL)
    target = FHIR_primitive_CanonicalField(null=True, blank=True, )
    target = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_Citation_citedArtifact(models.Model):
    Citation = models.ForeignKey(FHIR_Citation, related_name='Citation_citedArtifact', null=False, on_delete=models.CASCADE)
    dateAccessed = FHIR_primitive_DateTimeField(null=True, blank=True, )
    version = FHIR_primitive_StringField(null=True, blank=True, )
    baseCitation = models.ForeignKey("FHIR_Citation", related_name="Citation_citedArtifact_baseCitation", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Citation_citedArtifact_identifier(FHIR_GP_Identifier):
    Citation_citedArtifact = models.ForeignKey(FHIR_Citation_citedArtifact, related_name='Citation_citedArtifact_identifier', null=False, on_delete=models.CASCADE)

class FHIR_Citation_citedArtifact_relatedIdentifier(FHIR_GP_Identifier):
    Citation_citedArtifact = models.ForeignKey(FHIR_Citation_citedArtifact, related_name='Citation_citedArtifact_relatedIdentifier', null=False, on_delete=models.CASCADE)

class FHIR_Citation_citedArtifact_currentState(models.Model):
    Citation_citedArtifact = models.ForeignKey(FHIR_Citation_citedArtifact, related_name='Citation_citedArtifact_currentState', null=False, on_delete=models.CASCADE)
    BINDING_currentState = 'TODO'
    currentState_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_currentState}, related_name='Citation_citedArtifact_currentState', blank=True)
    currentState_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Citation_citedArtifact_statusDate(models.Model):
    Citation_citedArtifact = models.ForeignKey(FHIR_Citation_citedArtifact, related_name='Citation_citedArtifact_statusDate', null=False, on_delete=models.CASCADE)
    BINDING_activity = 'TODO'
    activity_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_activity}, related_name='Citation_citedArtifact_statusDate_activity', blank=True)
    activity_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    actual = FHIR_primitive_BooleanField(null=True, blank=True, )
    period = models.OneToOneField("FHIR_GP_Period", related_name='Citation_citedArtifact_statusDate_period', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Citation_citedArtifact_title(models.Model):
    Citation_citedArtifact = models.ForeignKey(FHIR_Citation_citedArtifact, related_name='Citation_citedArtifact_title', null=False, on_delete=models.CASCADE)
    class LanguageChoices(models.TextChoices): USED_TO_EXPRESS_THE_SPECIFIC_LANGUAGE = 'Used to express the specific language', 'Used to express the specific language'; 
    language = FHIR_primitive_CodeField(choices=LanguageChoices.choices, null=True, blank=True, )
    text = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_Citation_citedArtifact_title_type(models.Model):
    Citation_citedArtifact_title = models.ForeignKey(FHIR_Citation_citedArtifact_title, related_name='Citation_citedArtifact_title_type', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Citation_citedArtifact_title_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Citation_citedArtifact_abstract(models.Model):
    Citation_citedArtifact = models.ForeignKey(FHIR_Citation_citedArtifact, related_name='Citation_citedArtifact_abstract', null=False, on_delete=models.CASCADE)
    class LanguageChoices(models.TextChoices): USED_TO_EXPRESS_THE_SPECIFIC_LANGUAGE = 'Used to express the specific language', 'Used to express the specific language'; 
    language = FHIR_primitive_CodeField(choices=LanguageChoices.choices, null=True, blank=True, )
    text = FHIR_primitive_MarkdownField(null=True, blank=True, )
    copyright = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_Citation_citedArtifact_abstract_type(models.Model):
    Citation_citedArtifact_abstract = models.ForeignKey(FHIR_Citation_citedArtifact_abstract, related_name='Citation_citedArtifact_abstract_type', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Citation_citedArtifact_abstract_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Citation_citedArtifact_part(models.Model):
    Citation_citedArtifact = models.ForeignKey(FHIR_Citation_citedArtifact, related_name='Citation_citedArtifact_part', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Citation_citedArtifact_part_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_Citation_citedArtifact_relatesTo(models.Model):
    Citation_citedArtifact = models.ForeignKey(FHIR_Citation_citedArtifact, related_name='Citation_citedArtifact_relatesTo', null=False, on_delete=models.CASCADE)
    class TypeChoices(models.TextChoices): DOCUMENTATION = 'documentation', 'Documentation'; JUSTIFICATION = 'justification', 'Justification'; PREDECESSOR = 'predecessor', 'Predecessor'; SUCCESSOR = 'successor', 'Successor'; DERIVED_FROM = 'derived-from', 'Derived-from'; DEPENDS_ON = 'depends-on', 'Depends-on'; COMPOSED_OF = 'composed-of', 'Composed-of'; PART_OF = 'part-of', 'Part-of'; AMENDS = 'amends', 'Amends'; AMENDED_WITH = 'amended-with', 'Amended-with'; APPENDS = 'appends', 'Appends'; APPENDED_WITH = 'appended-with', 'Appended-with'; CITES = 'cites', 'Cites'; CITED_BY = 'cited-by', 'Cited-by'; COMMENTS_ON = 'comments-on', 'Comments-on'; COMMENT_IN = 'comment-in', 'Comment-in'; CONTAINS = 'contains', 'Contains'; CONTAINED_IN = 'contained-in', 'Contained-in'; CORRECTS = 'corrects', 'Corrects'; CORRECTION_IN = 'correction-in', 'Correction-in'; REPLACES = 'replaces', 'Replaces'; REPLACED_WITH = 'replaced-with', 'Replaced-with'; RETRACTS = 'retracts', 'Retracts'; RETRACTED_BY = 'retracted-by', 'Retracted-by'; SIGNS = 'signs', 'Signs'; SIMILAR_TO = 'similar-to', 'Similar-to'; SUPPORTS = 'supports', 'Supports'; SUPPORTED_WITH = 'supported-with', 'Supported-with'; TRANSFORMS = 'transforms', 'Transforms'; TRANSFORMED_INTO = 'transformed-into', 'Transformed-into'; TRANSFORMED_WITH = 'transformed-with', 'Transformed-with'; SPECIFICATION_OF = 'specification-of', 'Specification-of'; CREATED_WITH = 'created-with', 'Created-with'; CITE_AS = 'cite-as', 'Cite-as'; SUMMARIZES = 'summarizes', 'Summarizes'; 
    type = FHIR_primitive_CodeField(choices=TypeChoices.choices, null=True, blank=True, )
    label = FHIR_primitive_StringField(null=True, blank=True, )
    display = FHIR_primitive_StringField(null=True, blank=True, )
    citation = FHIR_primitive_MarkdownField(null=True, blank=True, )
    target = FHIR_primitive_URIField(null=True, blank=True, )
    target = models.OneToOneField("FHIR_GP_Attachment", related_name='Citation_citedArtifact_relatesTo_target', null=True, blank=True, on_delete=models.SET_NULL)
    target = FHIR_primitive_CanonicalField(null=True, blank=True, )

class FHIR_Citation_citedArtifact_relatesTo_classifier(models.Model):
    Citation_citedArtifact_relatesTo = models.ForeignKey(FHIR_Citation_citedArtifact_relatesTo, related_name='Citation_citedArtifact_relatesTo_classifier', null=False, on_delete=models.CASCADE)
    BINDING_classifier = 'TODO'
    classifier_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_classifier}, related_name='Citation_citedArtifact_relatesTo_classifier', blank=True)
    classifier_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Citation_citedArtifact_publicationForm(models.Model):
    Citation_citedArtifact = models.ForeignKey(FHIR_Citation_citedArtifact, related_name='Citation_citedArtifact_publicationForm', null=False, on_delete=models.CASCADE)
    BINDING_citedMedium = 'TODO'
    citedMedium_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_citedMedium}, related_name='Citation_citedArtifact_publicationForm_citedMedium', blank=True)
    citedMedium_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    volume = FHIR_primitive_StringField(null=True, blank=True, )
    issue = FHIR_primitive_StringField(null=True, blank=True, )
    articleDate = FHIR_primitive_DateTimeField(null=True, blank=True, )
    publicationDateText = FHIR_primitive_StringField(null=True, blank=True, )
    publicationDateSeason = FHIR_primitive_StringField(null=True, blank=True, )
    lastRevisionDate = FHIR_primitive_DateTimeField(null=True, blank=True, )
    accessionNumber = FHIR_primitive_StringField(null=True, blank=True, )
    pageString = FHIR_primitive_StringField(null=True, blank=True, )
    firstPage = FHIR_primitive_StringField(null=True, blank=True, )
    lastPage = FHIR_primitive_StringField(null=True, blank=True, )
    pageCount = FHIR_primitive_StringField(null=True, blank=True, )
    copyright = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_Citation_citedArtifact_publicationForm_publishedIn(models.Model):
    Citation_citedArtifact_publicationForm = models.ForeignKey(FHIR_Citation_citedArtifact_publicationForm, related_name='Citation_citedArtifact_publicationForm_publishedIn', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Citation_citedArtifact_publicationForm_publishedIn_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    title = FHIR_primitive_StringField(null=True, blank=True, )
    publisher = models.ForeignKey("FHIR_Organization", related_name="Citation_citedArtifact_publicationForm_publishedIn_publisher", null=True, blank=True, on_delete=models.SET_NULL)
    publisherLocation = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_Citation_citedArtifact_publicationForm_publishedIn_identifier(FHIR_GP_Identifier):
    Citation_citedArtifact_publicationForm_publishedIn = models.ForeignKey(FHIR_Citation_citedArtifact_publicationForm_publishedIn, related_name='Citation_citedArtifact_publicationForm_publishedIn_identifier', null=False, on_delete=models.CASCADE)

class FHIR_Citation_citedArtifact_publicationForm_language(models.Model):
    Citation_citedArtifact_publicationForm = models.ForeignKey(FHIR_Citation_citedArtifact_publicationForm, related_name='Citation_citedArtifact_publicationForm_language', null=False, on_delete=models.CASCADE)
    
    class LanguageChoices(models.TextChoices): LANGUAGES_IN_WHICH_THIS_FORM_OF_THE_ARTICLE_IS_PUBLISHED = 'Language(s) in which this form of the article is published', 'Language(s) in which this form of the article is published'; 
    language = FHIR_primitive_CodeField(choices=LanguageChoices.choices, null=True, blank=True, )
    
class FHIR_Citation_citedArtifact_webLocation(models.Model):
    Citation_citedArtifact = models.ForeignKey(FHIR_Citation_citedArtifact, related_name='Citation_citedArtifact_webLocation', null=False, on_delete=models.CASCADE)
    url = FHIR_primitive_URIField(null=True, blank=True, )

class FHIR_Citation_citedArtifact_webLocation_classifier(models.Model):
    Citation_citedArtifact_webLocation = models.ForeignKey(FHIR_Citation_citedArtifact_webLocation, related_name='Citation_citedArtifact_webLocation_classifier', null=False, on_delete=models.CASCADE)
    BINDING_classifier = 'TODO'
    classifier_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_classifier}, related_name='Citation_citedArtifact_webLocation_classifier', blank=True)
    classifier_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Citation_citedArtifact_classification(models.Model):
    Citation_citedArtifact = models.ForeignKey(FHIR_Citation_citedArtifact, related_name='Citation_citedArtifact_classification', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Citation_citedArtifact_classification_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    artifactAssessment = models.ManyToManyField("FHIR_ArtifactAssessment", related_name="Citation_citedArtifact_classification_artifactAssessment", blank=True)

class FHIR_Citation_citedArtifact_classification_classifier(models.Model):
    Citation_citedArtifact_classification = models.ForeignKey(FHIR_Citation_citedArtifact_classification, related_name='Citation_citedArtifact_classification_classifier', null=False, on_delete=models.CASCADE)
    BINDING_classifier = 'TODO'
    classifier_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_classifier}, related_name='Citation_citedArtifact_classification_classifier', blank=True)
    classifier_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Citation_citedArtifact_contributorship(models.Model):
    Citation_citedArtifact = models.ForeignKey(FHIR_Citation_citedArtifact, related_name='Citation_citedArtifact_contributorship', null=False, on_delete=models.CASCADE)
    complete = FHIR_primitive_BooleanField(null=True, blank=True, )

class FHIR_Citation_citedArtifact_contributorship_entry(models.Model):
    Citation_citedArtifact_contributorship = models.ForeignKey(FHIR_Citation_citedArtifact_contributorship, related_name='Citation_citedArtifact_contributorship_entry', null=False, on_delete=models.CASCADE)
    contributor_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="Citation_citedArtifact_contributorship_entry_contributor", null=True, blank=True, on_delete=models.SET_NULL)
    contributor_Organization = models.ForeignKey("FHIR_Organization", related_name="Citation_citedArtifact_contributorship_entry_contributor", null=True, blank=True, on_delete=models.SET_NULL)
    forenameInitials = FHIR_primitive_StringField(null=True, blank=True, )
    affiliation_Organization = models.ManyToManyField("FHIR_Organization", related_name="Citation_citedArtifact_contributorship_entry_affiliation", blank=True)
    affiliation_PractitionerRole = models.ManyToManyField("FHIR_PractitionerRole", related_name="Citation_citedArtifact_contributorship_entry_affiliation", blank=True)
    BINDING_role = 'TODO'
    role_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_role}, related_name='Citation_citedArtifact_contributorship_entry_role', blank=True)
    role_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    correspondingContact = FHIR_primitive_BooleanField(null=True, blank=True, )
    rankingOrder = FHIR_primitive_PositiveIntField(null=True, blank=True, )

class FHIR_Citation_citedArtifact_contributorship_entry_contributionType(models.Model):
    Citation_citedArtifact_contributorship_entry = models.ForeignKey(FHIR_Citation_citedArtifact_contributorship_entry, related_name='Citation_citedArtifact_contributorship_entry_contributionType', null=False, on_delete=models.CASCADE)
    BINDING_contributionType = 'TODO'
    contributionType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_contributionType}, related_name='Citation_citedArtifact_contributorship_entry_contributionType', blank=True)
    contributionType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Citation_citedArtifact_contributorship_entry_contributionInstance(models.Model):
    Citation_citedArtifact_contributorship_entry = models.ForeignKey(FHIR_Citation_citedArtifact_contributorship_entry, related_name='Citation_citedArtifact_contributorship_entry_contributionInstance', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Citation_citedArtifact_contributorship_entry_contributionInstance_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    time = FHIR_primitive_DateTimeField(null=True, blank=True, )

class FHIR_Citation_citedArtifact_contributorship_summary(models.Model):
    Citation_citedArtifact_contributorship = models.ForeignKey(FHIR_Citation_citedArtifact_contributorship, related_name='Citation_citedArtifact_contributorship_summary', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Citation_citedArtifact_contributorship_summary_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_source = 'TODO'
    source_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_source}, related_name='Citation_citedArtifact_contributorship_summary_source', blank=True)
    source_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_Citation_citedArtifact_contributorship_summary_style(models.Model):
    Citation_citedArtifact_contributorship_summary = models.ForeignKey(FHIR_Citation_citedArtifact_contributorship_summary, related_name='Citation_citedArtifact_contributorship_summary_style', null=False, on_delete=models.CASCADE)
    BINDING_style = 'TODO'
    style_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_style}, related_name='Citation_citedArtifact_contributorship_summary_style', blank=True)
    style_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Citation_citedArtifact_note(FHIR_GP_Annotation):
    Citation_citedArtifact = models.ForeignKey(FHIR_Citation_citedArtifact, related_name='Citation_citedArtifact_note', null=False, on_delete=models.CASCADE)
