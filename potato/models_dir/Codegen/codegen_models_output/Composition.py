#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Composition(models.Model):
    url = FHIR_primitive_URIField(null=True, blank=True, )
    version = FHIR_primitive_StringField(null=True, blank=True, )
    class StatusChoices(models.TextChoices): REGISTERED = 'registered', 'Registered'; PARTIAL = 'partial', 'Partial'; PRELIMINARY = 'preliminary', 'Preliminary'; FINAL = 'final', 'Final'; AMENDED = 'amended', 'Amended'; CORRECTED = 'corrected', 'Corrected'; APPENDED = 'appended', 'Appended'; CANCELLED = 'cancelled', 'Cancelled'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; DEPRECATED = 'deprecated', 'Deprecated'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Composition_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    encounter = models.ForeignKey("FHIR_Encounter", related_name="Composition_encounter", null=True, blank=True, on_delete=models.SET_NULL)
    date = FHIR_primitive_DateTimeField(null=True, blank=True, )
    author_Practitioner = models.ManyToManyField("FHIR_Practitioner", related_name="Composition_author", blank=True)
    author_PractitionerRole = models.ManyToManyField("FHIR_PractitionerRole", related_name="Composition_author", blank=True)
    author_CareTeam = models.ManyToManyField("FHIR_CareTeam", related_name="Composition_author", blank=True)
    author_Device = models.ManyToManyField("FHIR_Device", related_name="Composition_author", blank=True)
    author_Patient = models.ManyToManyField("FHIR_Patient", related_name="Composition_author", blank=True)
    author_RelatedPerson = models.ManyToManyField("FHIR_RelatedPerson", related_name="Composition_author", blank=True)
    author_Organization = models.ManyToManyField("FHIR_Organization", related_name="Composition_author", blank=True)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    title = FHIR_primitive_StringField(null=True, blank=True, )
    custodian = models.ForeignKey("FHIR_Organization", related_name="Composition_custodian", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Composition_identifier(FHIR_GP_Identifier):
    Composition = models.ForeignKey(FHIR_Composition, related_name='Composition_identifier', null=False, on_delete=models.CASCADE)

class FHIR_Composition_category(models.Model):
    Composition = models.ForeignKey(FHIR_Composition, related_name='Composition_category', null=False, on_delete=models.CASCADE)
    BINDING_category = "TODO"
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='Composition_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Composition_note(FHIR_GP_Annotation):
    Composition = models.ForeignKey(FHIR_Composition, related_name='Composition_note', null=False, on_delete=models.CASCADE)

class FHIR_Composition_attester(models.Model):
    Composition = models.ForeignKey(FHIR_Composition, related_name='Composition_attester', null=False, on_delete=models.CASCADE)
    BINDING_mode = "TODO"
    mode_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_mode}, related_name='Composition_attester_mode', blank=True)
    mode_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    time = FHIR_primitive_DateTimeField(null=True, blank=True, )
    party_Patient = models.ForeignKey("FHIR_Patient", related_name="Composition_attester_party", null=True, blank=True, on_delete=models.SET_NULL)
    party_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="Composition_attester_party", null=True, blank=True, on_delete=models.SET_NULL)
    party_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="Composition_attester_party", null=True, blank=True, on_delete=models.SET_NULL)
    party_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="Composition_attester_party", null=True, blank=True, on_delete=models.SET_NULL)
    party_Organization = models.ForeignKey("FHIR_Organization", related_name="Composition_attester_party", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Composition_relatesTo(models.Model):
    Composition = models.ForeignKey(FHIR_Composition, related_name='Composition_relatesTo', null=False, on_delete=models.CASCADE)
    class TypeChoices(models.TextChoices): DOCUMENTATION = 'documentation', 'Documentation'; JUSTIFICATION = 'justification', 'Justification'; PREDECESSOR = 'predecessor', 'Predecessor'; SUCCESSOR = 'successor', 'Successor'; DERIVED_FROM = 'derived-from', 'Derived-from'; DEPENDS_ON = 'depends-on', 'Depends-on'; COMPOSED_OF = 'composed-of', 'Composed-of'; PART_OF = 'part-of', 'Part-of'; AMENDS = 'amends', 'Amends'; AMENDED_WITH = 'amended-with', 'Amended-with'; APPENDS = 'appends', 'Appends'; APPENDED_WITH = 'appended-with', 'Appended-with'; CITES = 'cites', 'Cites'; CITED_BY = 'cited-by', 'Cited-by'; COMMENTS_ON = 'comments-on', 'Comments-on'; COMMENT_IN = 'comment-in', 'Comment-in'; CONTAINS = 'contains', 'Contains'; CONTAINED_IN = 'contained-in', 'Contained-in'; CORRECTS = 'corrects', 'Corrects'; CORRECTION_IN = 'correction-in', 'Correction-in'; REPLACES = 'replaces', 'Replaces'; REPLACED_WITH = 'replaced-with', 'Replaced-with'; RETRACTS = 'retracts', 'Retracts'; RETRACTED_BY = 'retracted-by', 'Retracted-by'; SIGNS = 'signs', 'Signs'; SIMILAR_TO = 'similar-to', 'Similar-to'; SUPPORTS = 'supports', 'Supports'; SUPPORTED_WITH = 'supported-with', 'Supported-with'; TRANSFORMS = 'transforms', 'Transforms'; TRANSFORMED_INTO = 'transformed-into', 'Transformed-into'; TRANSFORMED_WITH = 'transformed-with', 'Transformed-with'; SPECIFICATION_OF = 'specification-of', 'Specification-of'; CREATED_WITH = 'created-with', 'Created-with'; CITE_AS = 'cite-as', 'Cite-as'; SUMMARIZES = 'summarizes', 'Summarizes'; 
    type = FHIR_primitive_CodeField(choices=TypeChoices.choices, null=True, blank=True, )
    target = FHIR_primitive_URIField(null=True, blank=True, )
    target = models.OneToOneField("FHIR_GP_Attachment", related_name='Composition_relatesTo_target', null=True, blank=True, on_delete=models.SET_NULL)
    target = FHIR_primitive_CanonicalField(null=True, blank=True, )
    target = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_Composition_event(models.Model):
    Composition = models.ForeignKey(FHIR_Composition, related_name='Composition_event', null=False, on_delete=models.CASCADE)
    period = models.OneToOneField("FHIR_GP_Period", related_name='Composition_event_period', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Composition_event_detail(models.Model):
    Composition_event = models.ForeignKey(FHIR_Composition_event, related_name='Composition_event_detail', null=False, on_delete=models.CASCADE)
    BINDING_detail = "TODO"
    detail_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_detail}, related_name='Composition_event_detail', blank=True)
    detail_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_Composition_section(models.Model):
    Composition = models.ForeignKey(FHIR_Composition, related_name='Composition_section', null=False, on_delete=models.CASCADE)
    title = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_code = "TODO"
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='Composition_section_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    author_Practitioner = models.ManyToManyField("FHIR_Practitioner", related_name="Composition_section_author", blank=True)
    author_PractitionerRole = models.ManyToManyField("FHIR_PractitionerRole", related_name="Composition_section_author", blank=True)
    author_CareTeam = models.ManyToManyField("FHIR_CareTeam", related_name="Composition_section_author", blank=True)
    author_Device = models.ManyToManyField("FHIR_Device", related_name="Composition_section_author", blank=True)
    author_Patient = models.ManyToManyField("FHIR_Patient", related_name="Composition_section_author", blank=True)
    author_RelatedPerson = models.ManyToManyField("FHIR_RelatedPerson", related_name="Composition_section_author", blank=True)
    author_Organization = models.ManyToManyField("FHIR_Organization", related_name="Composition_section_author", blank=True)
    BINDING_orderedBy = "TODO"
    orderedBy_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_orderedBy}, related_name='Composition_section_orderedBy', blank=True)
    orderedBy_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_emptyReason = "TODO"
    emptyReason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_emptyReason}, related_name='Composition_section_emptyReason', blank=True)
    emptyReason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
