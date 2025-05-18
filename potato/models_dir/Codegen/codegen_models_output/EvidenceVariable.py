#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_EvidenceVariable(models.Model):
    url = FHIR_primitive_URIField(null=True, blank=True, )
    version = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm_string = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm_Coding = models.OneToOneField("FHIR_GP_Coding", related_name='EvidenceVariable_versionAlgorithm_Coding', null=True, blank=True, on_delete=models.SET_NULL)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    title = FHIR_primitive_StringField(null=True, blank=True, )
    shortTitle = FHIR_primitive_StringField(null=True, blank=True, )
    citeAs = FHIR_primitive_MarkdownField(null=True, blank=True, )
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
    effectivePeriod = models.OneToOneField("FHIR_GP_Period", related_name='EvidenceVariable_effectivePeriod', null=True, blank=True, on_delete=models.SET_NULL)
    actual = FHIR_primitive_BooleanField(null=True, blank=True, )
    BINDING_definition = "TODO"
    definition_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_definition}, related_name='EvidenceVariable_definition', blank=True)
    definition_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    definition_Group_ref = models.ForeignKey("FHIR_Group", related_name="EvidenceVariable_definition_Group", null=True, blank=True, on_delete=models.SET_NULL)
    class HandlingChoices(models.TextChoices): BOOLEAN = 'boolean', 'Boolean'; CONTINUOUS = 'continuous', 'Continuous'; DICHOTOMOUS = 'dichotomous', 'Dichotomous'; ORDINAL = 'ordinal', 'Ordinal'; POLYCHOTOMOUS = 'polychotomous', 'Polychotomous'; EXTENSION = 'extension', 'Extension'; 
    handling = FHIR_primitive_CodeField(choices=HandlingChoices.choices, null=True, blank=True, )
    period = models.OneToOneField("FHIR_GP_Period", related_name='EvidenceVariable_period', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_EvidenceVariable_identifier(FHIR_GP_Identifier):
    EvidenceVariable = models.ForeignKey(FHIR_EvidenceVariable, related_name='EvidenceVariable_identifier', null=False, on_delete=models.CASCADE)

class FHIR_EvidenceVariable_note(FHIR_GP_Annotation):
    EvidenceVariable = models.ForeignKey(FHIR_EvidenceVariable, related_name='EvidenceVariable_note', null=False, on_delete=models.CASCADE)

class FHIR_EvidenceVariable_relatesTo(models.Model):
    EvidenceVariable = models.ForeignKey(FHIR_EvidenceVariable, related_name='EvidenceVariable_relatesTo', null=False, on_delete=models.CASCADE)
    class TypeChoices(models.TextChoices): DOCUMENTATION = 'documentation', 'Documentation'; JUSTIFICATION = 'justification', 'Justification'; PREDECESSOR = 'predecessor', 'Predecessor'; SUCCESSOR = 'successor', 'Successor'; DERIVED_FROM = 'derived-from', 'Derived-from'; DEPENDS_ON = 'depends-on', 'Depends-on'; COMPOSED_OF = 'composed-of', 'Composed-of'; PART_OF = 'part-of', 'Part-of'; AMENDS = 'amends', 'Amends'; AMENDED_WITH = 'amended-with', 'Amended-with'; APPENDS = 'appends', 'Appends'; APPENDED_WITH = 'appended-with', 'Appended-with'; CITES = 'cites', 'Cites'; CITED_BY = 'cited-by', 'Cited-by'; COMMENTS_ON = 'comments-on', 'Comments-on'; COMMENT_IN = 'comment-in', 'Comment-in'; CONTAINS = 'contains', 'Contains'; CONTAINED_IN = 'contained-in', 'Contained-in'; CORRECTS = 'corrects', 'Corrects'; CORRECTION_IN = 'correction-in', 'Correction-in'; REPLACES = 'replaces', 'Replaces'; REPLACED_WITH = 'replaced-with', 'Replaced-with'; RETRACTS = 'retracts', 'Retracts'; RETRACTED_BY = 'retracted-by', 'Retracted-by'; SIGNS = 'signs', 'Signs'; SIMILAR_TO = 'similar-to', 'Similar-to'; SUPPORTS = 'supports', 'Supports'; SUPPORTED_WITH = 'supported-with', 'Supported-with'; TRANSFORMS = 'transforms', 'Transforms'; TRANSFORMED_INTO = 'transformed-into', 'Transformed-into'; TRANSFORMED_WITH = 'transformed-with', 'Transformed-with'; SPECIFICATION_OF = 'specification-of', 'Specification-of'; CREATED_WITH = 'created-with', 'Created-with'; CITE_AS = 'cite-as', 'Cite-as'; SUMMARIZES = 'summarizes', 'Summarizes'; 
    type = FHIR_primitive_CodeField(choices=TypeChoices.choices, null=True, blank=True, )
    target_uri = FHIR_primitive_URIField(null=True, blank=True, )
    target_Attachment = models.OneToOneField("FHIR_GP_Attachment", related_name='EvidenceVariable_relatesTo_target_Attachment', null=True, blank=True, on_delete=models.SET_NULL)
    target_canonical = FHIR_primitive_CanonicalField(null=True, blank=True, )
                            #skipping Reference(Any) for field target_Reference as EvidenceVariable target_Reference not in referenceAny_targets
    target_markdown = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_EvidenceVariable_definitionModifier(models.Model):
    EvidenceVariable = models.ForeignKey(FHIR_EvidenceVariable, related_name='EvidenceVariable_definitionModifier', null=False, on_delete=models.CASCADE)
    BINDING_code = "TODO"
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='EvidenceVariable_definitionModifier_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_value_CodeableConcept = "TODO"
    value_CodeableConcept_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_value_CodeableConcept}, related_name='EvidenceVariable_definitionModifier_value_CodeableConcept', blank=True)
    value_CodeableConcept_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value_boolean = FHIR_primitive_BooleanField(null=True, blank=True, )
    value_Quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='EvidenceVariable_definitionModifier_value_Quantity', null=True, blank=True, on_delete=models.SET_NULL)
    value_Range = models.OneToOneField("FHIR_GP_Range", related_name='EvidenceVariable_definitionModifier_value_Range', null=True, blank=True, on_delete=models.SET_NULL)
    value_Period = models.OneToOneField("FHIR_GP_Period", related_name='EvidenceVariable_definitionModifier_value_Period', null=True, blank=True, on_delete=models.SET_NULL)
                            #skipping Reference(Any) for field value_Reference as EvidenceVariable value_Reference not in referenceAny_targets
    value_uri = FHIR_primitive_URIField(null=True, blank=True, )

class FHIR_EvidenceVariable_category(models.Model):
    EvidenceVariable = models.ForeignKey(FHIR_EvidenceVariable, related_name='EvidenceVariable_category', null=False, on_delete=models.CASCADE)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_value_CodeableConcept = "TODO"
    value_CodeableConcept_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_value_CodeableConcept}, related_name='EvidenceVariable_category_value_CodeableConcept', blank=True)
    value_CodeableConcept_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value_Quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='EvidenceVariable_category_value_Quantity', null=True, blank=True, on_delete=models.SET_NULL)
    value_Range = models.OneToOneField("FHIR_GP_Range", related_name='EvidenceVariable_category_value_Range', null=True, blank=True, on_delete=models.SET_NULL)
    value_Reference = models.ForeignKey("FHIR_Group", related_name="EvidenceVariable_category_value_Reference", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_EvidenceVariable_classifier(models.Model):
    EvidenceVariable = models.ForeignKey(FHIR_EvidenceVariable, related_name='EvidenceVariable_classifier', null=False, on_delete=models.CASCADE)
    BINDING_classifier = "TODO"
    classifier_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_classifier}, related_name='EvidenceVariable_classifier', blank=True)
    classifier_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_EvidenceVariable_dataStorage(models.Model):
    EvidenceVariable = models.ForeignKey(FHIR_EvidenceVariable, related_name='EvidenceVariable_dataStorage', null=False, on_delete=models.CASCADE)
    BINDING_datatype = "TODO"
    datatype_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_datatype}, related_name='EvidenceVariable_dataStorage_datatype', blank=True)
    datatype_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    path = FHIR_primitive_StringField(null=True, blank=True, )
    delimiter = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_EvidenceVariable_constraint(models.Model):
    EvidenceVariable = models.ForeignKey(FHIR_EvidenceVariable, related_name='EvidenceVariable_constraint', null=False, on_delete=models.CASCADE)
    BINDING_conditional = "TODO"
    conditional_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_conditional}, related_name='EvidenceVariable_constraint_conditional', blank=True)
    conditional_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    minimumQuantity = models.OneToOneField("FHIR_GP_Quantity", related_name='EvidenceVariable_constraint_minimumQuantity', null=True, blank=True, on_delete=models.SET_NULL)
    maximumQuantity = models.OneToOneField("FHIR_GP_Quantity", related_name='EvidenceVariable_constraint_maximumQuantity', null=True, blank=True, on_delete=models.SET_NULL)
    earliestDateTime = FHIR_primitive_DateTimeField(null=True, blank=True, )
    latestDateTime = FHIR_primitive_DateTimeField(null=True, blank=True, )
    minimumStringLength = FHIR_primitive_UnsignedIntField(null=True, blank=True, )
    maximumStringLength = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    BINDING_code = "TODO"
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='EvidenceVariable_constraint_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    expectedValueSet = models.ForeignKey("FHIR_ValueSet", related_name="EvidenceVariable_constraint_expectedValueSet", null=True, blank=True, on_delete=models.SET_NULL)
    expectedUnitsValueSet = models.ForeignKey("FHIR_ValueSet", related_name="EvidenceVariable_constraint_expectedUnitsValueSet", null=True, blank=True, on_delete=models.SET_NULL)
    anyValueAllowed = FHIR_primitive_BooleanField(null=True, blank=True, )

class FHIR_EvidenceVariable_missingDataMeaning(models.Model):
    EvidenceVariable = models.ForeignKey(FHIR_EvidenceVariable, related_name='EvidenceVariable_missingDataMeaning', null=False, on_delete=models.CASCADE)
    BINDING_missingDataMeaning = "TODO"
    missingDataMeaning_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_missingDataMeaning}, related_name='EvidenceVariable_missingDataMeaning', blank=True)
    missingDataMeaning_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_EvidenceVariable_unacceptableDataHandling(models.Model):
    EvidenceVariable = models.ForeignKey(FHIR_EvidenceVariable, related_name='EvidenceVariable_unacceptableDataHandling', null=False, on_delete=models.CASCADE)
    BINDING_unacceptableDataHandling = "TODO"
    unacceptableDataHandling_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_unacceptableDataHandling}, related_name='EvidenceVariable_unacceptableDataHandling', blank=True)
    unacceptableDataHandling_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    