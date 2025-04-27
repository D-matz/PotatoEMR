#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Contract(models.Model):
    url = FHIR_primitive_URIField(null=True, blank=True, )
    version = FHIR_primitive_StringField(null=True, blank=True, )
    class StatusChoices(models.TextChoices): AMENDED = 'amended', 'Amended'; APPENDED = 'appended', 'Appended'; CANCELLED = 'cancelled', 'Cancelled'; DISPUTED = 'disputed', 'Disputed'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; EXECUTABLE_PLUS = 'executable +', 'Executable +'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    BINDING_legalState = 'TODO'
    legalState_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_legalState}, related_name='Contract_legalState', blank=True)
    legalState_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    instantiatesCanonical = models.ForeignKey("FHIR_Contract", related_name="Contract_instantiatesCanonical", null=True, blank=True, on_delete=models.SET_NULL)
    instantiatesUri = FHIR_primitive_URIField(null=True, blank=True, )
    BINDING_contentDerivative = 'TODO'
    contentDerivative_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_contentDerivative}, related_name='Contract_contentDerivative', blank=True)
    contentDerivative_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    issued = FHIR_primitive_DateTimeField(null=True, blank=True, )
    applies = models.OneToOneField("FHIR_GP_Period", related_name='Contract_applies', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_expirationType = 'TODO'
    expirationType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_expirationType}, related_name='Contract_expirationType', blank=True)
    expirationType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    authority = models.ManyToManyField("FHIR_Organization", related_name="Contract_authority", blank=True)
    domain = models.ManyToManyField("FHIR_Location", related_name="Contract_domain", blank=True)
    site = models.ManyToManyField("FHIR_Location", related_name="Contract_site", blank=True)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    title = FHIR_primitive_StringField(null=True, blank=True, )
    subtitle = FHIR_primitive_StringField(null=True, blank=True, )
    author_Patient = models.ForeignKey("FHIR_Patient", related_name="Contract_author", null=True, blank=True, on_delete=models.SET_NULL)
    author_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="Contract_author", null=True, blank=True, on_delete=models.SET_NULL)
    author_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="Contract_author", null=True, blank=True, on_delete=models.SET_NULL)
    author_Organization = models.ForeignKey("FHIR_Organization", related_name="Contract_author", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_scope = 'TODO'
    scope_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_scope}, related_name='Contract_scope', blank=True)
    scope_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_topic = 'TODO'
    topic_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_topic}, related_name='Contract_topic', blank=True)
    topic_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Contract_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    relevantHistory = models.ManyToManyField("FHIR_Provenance", related_name="Contract_relevantHistory", blank=True)
    legallyBinding = models.OneToOneField("FHIR_GP_Attachment", related_name='Contract_legallyBinding', null=True, blank=True, on_delete=models.SET_NULL)
    legallyBinding_Composition = models.ForeignKey("FHIR_Composition", related_name="Contract_legallyBinding", null=True, blank=True, on_delete=models.SET_NULL)
    legallyBinding_DocumentReference = models.ForeignKey("FHIR_DocumentReference", related_name="Contract_legallyBinding", null=True, blank=True, on_delete=models.SET_NULL)
    legallyBinding_QuestionnaireResponse = models.ForeignKey("FHIR_QuestionnaireResponse", related_name="Contract_legallyBinding", null=True, blank=True, on_delete=models.SET_NULL)
    legallyBinding_Contract = models.ForeignKey("FHIR_Contract", related_name="Contract_legallyBinding", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Contract_identifier(FHIR_GP_Identifier):
    Contract = models.ForeignKey(FHIR_Contract, related_name='Contract_identifier', null=False, on_delete=models.CASCADE)

class FHIR_Contract_alias(models.Model):
    Contract = models.ForeignKey(FHIR_Contract, related_name='Contract_alias', null=False, on_delete=models.CASCADE)
    
    alias = FHIR_primitive_StringField(null=True, blank=True, )
    
class FHIR_Contract_subType(models.Model):
    Contract = models.ForeignKey(FHIR_Contract, related_name='Contract_subType', null=False, on_delete=models.CASCADE)
    BINDING_subType = 'TODO'
    subType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_subType}, related_name='Contract_subType', blank=True)
    subType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Contract_contentDefinition(models.Model):
    Contract = models.ForeignKey(FHIR_Contract, related_name='Contract_contentDefinition', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Contract_contentDefinition_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_subType = 'TODO'
    subType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_subType}, related_name='Contract_contentDefinition_subType', blank=True)
    subType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    publisher_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="Contract_contentDefinition_publisher", null=True, blank=True, on_delete=models.SET_NULL)
    publisher_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="Contract_contentDefinition_publisher", null=True, blank=True, on_delete=models.SET_NULL)
    publisher_Organization = models.ForeignKey("FHIR_Organization", related_name="Contract_contentDefinition_publisher", null=True, blank=True, on_delete=models.SET_NULL)
    publicationDate = FHIR_primitive_DateTimeField(null=True, blank=True, )
    class PublicationstatusChoices(models.TextChoices): AMENDED = 'amended', 'Amended'; APPENDED = 'appended', 'Appended'; CANCELLED = 'cancelled', 'Cancelled'; DISPUTED = 'disputed', 'Disputed'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; EXECUTABLE_PLUS = 'executable +', 'Executable +'; 
    publicationStatus = FHIR_primitive_CodeField(choices=PublicationstatusChoices.choices, null=True, blank=True, )
    copyright = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_Contract_term(models.Model):
    Contract = models.ForeignKey(FHIR_Contract, related_name='Contract_term', null=False, on_delete=models.CASCADE)
    identifier = models.OneToOneField("FHIR_GP_Identifier", related_name='Contract_term_identifier', null=True, blank=True, on_delete=models.SET_NULL)
    issued = FHIR_primitive_DateTimeField(null=True, blank=True, )
    applies = models.OneToOneField("FHIR_GP_Period", related_name='Contract_term_applies', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_topic = 'TODO'
    topic_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_topic}, related_name='Contract_term_topic', blank=True)
    topic_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Contract_term_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_subType = 'TODO'
    subType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_subType}, related_name='Contract_term_subType', blank=True)
    subType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    text = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_Contract_term_securityLabel(models.Model):
    Contract_term = models.ForeignKey(FHIR_Contract_term, related_name='Contract_term_securityLabel', null=False, on_delete=models.CASCADE)
    classification = models.OneToOneField("FHIR_GP_Coding", related_name='Contract_term_securityLabel_classification', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Contract_term_securityLabel_number(models.Model):
    Contract_term_securityLabel = models.ForeignKey(FHIR_Contract_term_securityLabel, related_name='Contract_term_securityLabel_number', null=False, on_delete=models.CASCADE)
    
    number = FHIR_primitive_UnsignedIntField(null=True, blank=True, )
    
class FHIR_Contract_term_securityLabel_category(FHIR_GP_Coding):
    Contract_term_securityLabel = models.ForeignKey(FHIR_Contract_term_securityLabel, related_name='Contract_term_securityLabel_category', null=False, on_delete=models.CASCADE)

class FHIR_Contract_term_securityLabel_control(FHIR_GP_Coding):
    Contract_term_securityLabel = models.ForeignKey(FHIR_Contract_term_securityLabel, related_name='Contract_term_securityLabel_control', null=False, on_delete=models.CASCADE)

class FHIR_Contract_term_offer(models.Model):
    Contract_term = models.ForeignKey(FHIR_Contract_term, related_name='Contract_term_offer', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Contract_term_offer_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_decision = 'TODO'
    decision_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_decision}, related_name='Contract_term_offer_decision', blank=True)
    decision_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    text = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_Contract_term_offer_identifier(FHIR_GP_Identifier):
    Contract_term_offer = models.ForeignKey(FHIR_Contract_term_offer, related_name='Contract_term_offer_identifier', null=False, on_delete=models.CASCADE)

class FHIR_Contract_term_offer_party(models.Model):
    Contract_term_offer = models.ForeignKey(FHIR_Contract_term_offer, related_name='Contract_term_offer_party', null=False, on_delete=models.CASCADE)
    reference_Patient = models.ManyToManyField("FHIR_Patient", related_name="Contract_term_offer_party_reference", blank=True)
    reference_RelatedPerson = models.ManyToManyField("FHIR_RelatedPerson", related_name="Contract_term_offer_party_reference", blank=True)
    reference_Practitioner = models.ManyToManyField("FHIR_Practitioner", related_name="Contract_term_offer_party_reference", blank=True)
    reference_PractitionerRole = models.ManyToManyField("FHIR_PractitionerRole", related_name="Contract_term_offer_party_reference", blank=True)
    reference_Device = models.ManyToManyField("FHIR_Device", related_name="Contract_term_offer_party_reference", blank=True)
    reference_Group = models.ManyToManyField("FHIR_Group", related_name="Contract_term_offer_party_reference", blank=True)
    reference_Organization = models.ManyToManyField("FHIR_Organization", related_name="Contract_term_offer_party_reference", blank=True)
    BINDING_role = 'TODO'
    role_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_role}, related_name='Contract_term_offer_party_role', blank=True)
    role_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_Contract_term_offer_decisionMode(models.Model):
    Contract_term_offer = models.ForeignKey(FHIR_Contract_term_offer, related_name='Contract_term_offer_decisionMode', null=False, on_delete=models.CASCADE)
    BINDING_decisionMode = 'TODO'
    decisionMode_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_decisionMode}, related_name='Contract_term_offer_decisionMode', blank=True)
    decisionMode_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Contract_term_offer_answer(models.Model):
    Contract_term_offer = models.ForeignKey(FHIR_Contract_term_offer, related_name='Contract_term_offer_answer', null=False, on_delete=models.CASCADE)
    value = FHIR_primitive_BooleanField(null=True, blank=True, )
    value = FHIR_primitive_DecimalField(null=True, blank=True, )
    value = FHIR_primitive_DateField(null=True, blank=True, )
    value = FHIR_primitive_DateTimeField(null=True, blank=True, )
    value = FHIR_primitive_TimeField(null=True, blank=True, )
    value = FHIR_primitive_StringField(null=True, blank=True, )
    value = FHIR_primitive_URIField(null=True, blank=True, )
    value = models.OneToOneField("FHIR_GP_Attachment", related_name='Contract_term_offer_answer_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_Coding", related_name='Contract_term_offer_answer_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_Quantity", related_name='Contract_term_offer_answer_value', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Contract_term_offer_linkId(models.Model):
    Contract_term_offer = models.ForeignKey(FHIR_Contract_term_offer, related_name='Contract_term_offer_linkId', null=False, on_delete=models.CASCADE)
    
    linkId = FHIR_primitive_StringField(null=True, blank=True, )
    
class FHIR_Contract_term_offer_securityLabelNumber(models.Model):
    Contract_term_offer = models.ForeignKey(FHIR_Contract_term_offer, related_name='Contract_term_offer_securityLabelNumber', null=False, on_delete=models.CASCADE)
    
    securityLabelNumber = FHIR_primitive_UnsignedIntField(null=True, blank=True, )
    
class FHIR_Contract_term_asset(models.Model):
    Contract_term = models.ForeignKey(FHIR_Contract_term, related_name='Contract_term_asset', null=False, on_delete=models.CASCADE)
    BINDING_scope = 'TODO'
    scope_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_scope}, related_name='Contract_term_asset_scope', blank=True)
    scope_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    relationship = models.OneToOneField("FHIR_GP_Coding", related_name='Contract_term_asset_relationship', null=True, blank=True, on_delete=models.SET_NULL)
    condition = FHIR_primitive_StringField(null=True, blank=True, )
    text = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_Contract_term_asset_type(models.Model):
    Contract_term_asset = models.ForeignKey(FHIR_Contract_term_asset, related_name='Contract_term_asset_type', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Contract_term_asset_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Contract_term_asset_subtype(models.Model):
    Contract_term_asset = models.ForeignKey(FHIR_Contract_term_asset, related_name='Contract_term_asset_subtype', null=False, on_delete=models.CASCADE)
    BINDING_subtype = 'TODO'
    subtype_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_subtype}, related_name='Contract_term_asset_subtype', blank=True)
    subtype_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Contract_term_asset_context(models.Model):
    Contract_term_asset = models.ForeignKey(FHIR_Contract_term_asset, related_name='Contract_term_asset_context', null=False, on_delete=models.CASCADE)
    text = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_Contract_term_asset_context_code(models.Model):
    Contract_term_asset_context = models.ForeignKey(FHIR_Contract_term_asset_context, related_name='Contract_term_asset_context_code', null=False, on_delete=models.CASCADE)
    BINDING_code = 'TODO'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='Contract_term_asset_context_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Contract_term_asset_periodType(models.Model):
    Contract_term_asset = models.ForeignKey(FHIR_Contract_term_asset, related_name='Contract_term_asset_periodType', null=False, on_delete=models.CASCADE)
    BINDING_periodType = 'TODO'
    periodType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_periodType}, related_name='Contract_term_asset_periodType', blank=True)
    periodType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Contract_term_asset_period(FHIR_GP_Period):
    Contract_term_asset = models.ForeignKey(FHIR_Contract_term_asset, related_name='Contract_term_asset_period', null=False, on_delete=models.CASCADE)

class FHIR_Contract_term_asset_usePeriod(FHIR_GP_Period):
    Contract_term_asset = models.ForeignKey(FHIR_Contract_term_asset, related_name='Contract_term_asset_usePeriod', null=False, on_delete=models.CASCADE)

class FHIR_Contract_term_asset_linkId(models.Model):
    Contract_term_asset = models.ForeignKey(FHIR_Contract_term_asset, related_name='Contract_term_asset_linkId', null=False, on_delete=models.CASCADE)
    
    linkId = FHIR_primitive_StringField(null=True, blank=True, )
    
class FHIR_Contract_term_asset_securityLabelNumber(models.Model):
    Contract_term_asset = models.ForeignKey(FHIR_Contract_term_asset, related_name='Contract_term_asset_securityLabelNumber', null=False, on_delete=models.CASCADE)
    
    securityLabelNumber = FHIR_primitive_UnsignedIntField(null=True, blank=True, )
    
class FHIR_Contract_term_asset_valuedItem(models.Model):
    Contract_term_asset = models.ForeignKey(FHIR_Contract_term_asset, related_name='Contract_term_asset_valuedItem', null=False, on_delete=models.CASCADE)
    BINDING_entity = 'TODO'
    entity_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_entity}, related_name='Contract_term_asset_valuedItem_entity', blank=True)
    entity_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    identifier = models.OneToOneField("FHIR_GP_Identifier", related_name='Contract_term_asset_valuedItem_identifier', null=True, blank=True, on_delete=models.SET_NULL)
    effectiveTime = FHIR_primitive_DateTimeField(null=True, blank=True, )
    quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='Contract_term_asset_valuedItem_quantity', null=True, blank=True, on_delete=models.SET_NULL)
    unitPrice = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='Contract_term_asset_valuedItem_unitPrice', null=True, blank=True, on_delete=models.SET_NULL)
    factor = FHIR_primitive_DecimalField(null=True, blank=True, )
    points = FHIR_primitive_DecimalField(null=True, blank=True, )
    net = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='Contract_term_asset_valuedItem_net', null=True, blank=True, on_delete=models.SET_NULL)
    payment = FHIR_primitive_StringField(null=True, blank=True, )
    paymentDate = FHIR_primitive_DateTimeField(null=True, blank=True, )
    responsible_Organization = models.ForeignKey("FHIR_Organization", related_name="Contract_term_asset_valuedItem_responsible", null=True, blank=True, on_delete=models.SET_NULL)
    responsible_Patient = models.ForeignKey("FHIR_Patient", related_name="Contract_term_asset_valuedItem_responsible", null=True, blank=True, on_delete=models.SET_NULL)
    responsible_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="Contract_term_asset_valuedItem_responsible", null=True, blank=True, on_delete=models.SET_NULL)
    responsible_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="Contract_term_asset_valuedItem_responsible", null=True, blank=True, on_delete=models.SET_NULL)
    responsible_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="Contract_term_asset_valuedItem_responsible", null=True, blank=True, on_delete=models.SET_NULL)
    recipient_Organization = models.ForeignKey("FHIR_Organization", related_name="Contract_term_asset_valuedItem_recipient", null=True, blank=True, on_delete=models.SET_NULL)
    recipient_Patient = models.ForeignKey("FHIR_Patient", related_name="Contract_term_asset_valuedItem_recipient", null=True, blank=True, on_delete=models.SET_NULL)
    recipient_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="Contract_term_asset_valuedItem_recipient", null=True, blank=True, on_delete=models.SET_NULL)
    recipient_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="Contract_term_asset_valuedItem_recipient", null=True, blank=True, on_delete=models.SET_NULL)
    recipient_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="Contract_term_asset_valuedItem_recipient", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Contract_term_asset_valuedItem_linkId(models.Model):
    Contract_term_asset_valuedItem = models.ForeignKey(FHIR_Contract_term_asset_valuedItem, related_name='Contract_term_asset_valuedItem_linkId', null=False, on_delete=models.CASCADE)
    
    linkId = FHIR_primitive_StringField(null=True, blank=True, )
    
class FHIR_Contract_term_asset_valuedItem_securityLabelNumber(models.Model):
    Contract_term_asset_valuedItem = models.ForeignKey(FHIR_Contract_term_asset_valuedItem, related_name='Contract_term_asset_valuedItem_securityLabelNumber', null=False, on_delete=models.CASCADE)
    
    securityLabelNumber = FHIR_primitive_UnsignedIntField(null=True, blank=True, )
    
class FHIR_Contract_term_action(models.Model):
    Contract_term = models.ForeignKey(FHIR_Contract_term, related_name='Contract_term_action', null=False, on_delete=models.CASCADE)
    doNotPerform = FHIR_primitive_BooleanField(null=True, blank=True, )
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Contract_term_action_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_intent = 'TODO'
    intent_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_intent}, related_name='Contract_term_action_intent', blank=True)
    intent_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_status = 'TODO'
    status_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_status}, related_name='Contract_term_action_status', blank=True)
    status_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    context_Encounter = models.ForeignKey("FHIR_Encounter", related_name="Contract_term_action_context", null=True, blank=True, on_delete=models.SET_NULL)
    context_EpisodeOfCare = models.ForeignKey("FHIR_EpisodeOfCare", related_name="Contract_term_action_context", null=True, blank=True, on_delete=models.SET_NULL)
    occurrence = FHIR_primitive_DateTimeField(null=True, blank=True, )
    occurrence = models.OneToOneField("FHIR_GP_Period", related_name='Contract_term_action_occurrence', null=True, blank=True, on_delete=models.SET_NULL)
    occurrence = models.OneToOneField("FHIR_GP_Timing", related_name='Contract_term_action_occurrence', null=True, blank=True, on_delete=models.SET_NULL)
    requester_Patient = models.ManyToManyField("FHIR_Patient", related_name="Contract_term_action_requester", blank=True)
    requester_RelatedPerson = models.ManyToManyField("FHIR_RelatedPerson", related_name="Contract_term_action_requester", blank=True)
    requester_Practitioner = models.ManyToManyField("FHIR_Practitioner", related_name="Contract_term_action_requester", blank=True)
    requester_PractitionerRole = models.ManyToManyField("FHIR_PractitionerRole", related_name="Contract_term_action_requester", blank=True)
    requester_Device = models.ManyToManyField("FHIR_Device", related_name="Contract_term_action_requester", blank=True)
    requester_Group = models.ManyToManyField("FHIR_Group", related_name="Contract_term_action_requester", blank=True)
    requester_Organization = models.ManyToManyField("FHIR_Organization", related_name="Contract_term_action_requester", blank=True)
    BINDING_performerRole = 'TODO'
    performerRole_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_performerRole}, related_name='Contract_term_action_performerRole', blank=True)
    performerRole_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    performer_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="Contract_term_action_performer", null=True, blank=True, on_delete=models.SET_NULL)
    performer_Patient = models.ForeignKey("FHIR_Patient", related_name="Contract_term_action_performer", null=True, blank=True, on_delete=models.SET_NULL)
    performer_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="Contract_term_action_performer", null=True, blank=True, on_delete=models.SET_NULL)
    performer_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="Contract_term_action_performer", null=True, blank=True, on_delete=models.SET_NULL)
    performer_CareTeam = models.ForeignKey("FHIR_CareTeam", related_name="Contract_term_action_performer", null=True, blank=True, on_delete=models.SET_NULL)
    performer_Device = models.ForeignKey("FHIR_Device", related_name="Contract_term_action_performer", null=True, blank=True, on_delete=models.SET_NULL)
    performer_Substance = models.ForeignKey("FHIR_Substance", related_name="Contract_term_action_performer", null=True, blank=True, on_delete=models.SET_NULL)
    performer_Organization = models.ForeignKey("FHIR_Organization", related_name="Contract_term_action_performer", null=True, blank=True, on_delete=models.SET_NULL)
    performer_Location = models.ForeignKey("FHIR_Location", related_name="Contract_term_action_performer", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Contract_term_action_subject(models.Model):
    Contract_term_action = models.ForeignKey(FHIR_Contract_term_action, related_name='Contract_term_action_subject', null=False, on_delete=models.CASCADE)
    reference_Patient = models.ManyToManyField("FHIR_Patient", related_name="Contract_term_action_subject_reference", blank=True)
    reference_RelatedPerson = models.ManyToManyField("FHIR_RelatedPerson", related_name="Contract_term_action_subject_reference", blank=True)
    reference_Practitioner = models.ManyToManyField("FHIR_Practitioner", related_name="Contract_term_action_subject_reference", blank=True)
    reference_PractitionerRole = models.ManyToManyField("FHIR_PractitionerRole", related_name="Contract_term_action_subject_reference", blank=True)
    reference_Device = models.ManyToManyField("FHIR_Device", related_name="Contract_term_action_subject_reference", blank=True)
    reference_Group = models.ManyToManyField("FHIR_Group", related_name="Contract_term_action_subject_reference", blank=True)
    reference_Organization = models.ManyToManyField("FHIR_Organization", related_name="Contract_term_action_subject_reference", blank=True)
    BINDING_role = 'TODO'
    role_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_role}, related_name='Contract_term_action_subject_role', blank=True)
    role_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_Contract_term_action_linkId(models.Model):
    Contract_term_action = models.ForeignKey(FHIR_Contract_term_action, related_name='Contract_term_action_linkId', null=False, on_delete=models.CASCADE)
    
    linkId = FHIR_primitive_StringField(null=True, blank=True, )
    
class FHIR_Contract_term_action_contextLinkId(models.Model):
    Contract_term_action = models.ForeignKey(FHIR_Contract_term_action, related_name='Contract_term_action_contextLinkId', null=False, on_delete=models.CASCADE)
    
    contextLinkId = FHIR_primitive_StringField(null=True, blank=True, )
    
class FHIR_Contract_term_action_requesterLinkId(models.Model):
    Contract_term_action = models.ForeignKey(FHIR_Contract_term_action, related_name='Contract_term_action_requesterLinkId', null=False, on_delete=models.CASCADE)
    
    requesterLinkId = FHIR_primitive_StringField(null=True, blank=True, )
    
class FHIR_Contract_term_action_performerType(models.Model):
    Contract_term_action = models.ForeignKey(FHIR_Contract_term_action, related_name='Contract_term_action_performerType', null=False, on_delete=models.CASCADE)
    BINDING_performerType = 'TODO'
    performerType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_performerType}, related_name='Contract_term_action_performerType', blank=True)
    performerType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Contract_term_action_performerLinkId(models.Model):
    Contract_term_action = models.ForeignKey(FHIR_Contract_term_action, related_name='Contract_term_action_performerLinkId', null=False, on_delete=models.CASCADE)
    
    performerLinkId = FHIR_primitive_StringField(null=True, blank=True, )
    
class FHIR_Contract_term_action_reason(models.Model):
    Contract_term_action = models.ForeignKey(FHIR_Contract_term_action, related_name='Contract_term_action_reason', null=False, on_delete=models.CASCADE)
    BINDING_reason = 'TODO'
    reason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_reason}, related_name='Contract_term_action_reason', blank=True)
    reason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    reason_Condition_ref = models.ForeignKey("FHIR_Condition", related_name="Contract_term_action_reason_Condition", null=True, blank=True, on_delete=models.SET_NULL)
    reason_Observation_ref = models.ForeignKey("FHIR_Observation", related_name="Contract_term_action_reason_Observation", null=True, blank=True, on_delete=models.SET_NULL)
    reason_DiagnosticReport_ref = models.ForeignKey("FHIR_DiagnosticReport", related_name="Contract_term_action_reason_DiagnosticReport", null=True, blank=True, on_delete=models.SET_NULL)
    reason_DocumentReference_ref = models.ForeignKey("FHIR_DocumentReference", related_name="Contract_term_action_reason_DocumentReference", null=True, blank=True, on_delete=models.SET_NULL)
    reason_Questionnaire_ref = models.ForeignKey("FHIR_Questionnaire", related_name="Contract_term_action_reason_Questionnaire", null=True, blank=True, on_delete=models.SET_NULL)
    reason_QuestionnaireResponse_ref = models.ForeignKey("FHIR_QuestionnaireResponse", related_name="Contract_term_action_reason_QuestionnaireResponse", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Contract_term_action_reasonLinkId(models.Model):
    Contract_term_action = models.ForeignKey(FHIR_Contract_term_action, related_name='Contract_term_action_reasonLinkId', null=False, on_delete=models.CASCADE)
    
    reasonLinkId = FHIR_primitive_StringField(null=True, blank=True, )
    
class FHIR_Contract_term_action_note(FHIR_GP_Annotation):
    Contract_term_action = models.ForeignKey(FHIR_Contract_term_action, related_name='Contract_term_action_note', null=False, on_delete=models.CASCADE)

class FHIR_Contract_term_action_securityLabelNumber(models.Model):
    Contract_term_action = models.ForeignKey(FHIR_Contract_term_action, related_name='Contract_term_action_securityLabelNumber', null=False, on_delete=models.CASCADE)
    
    securityLabelNumber = FHIR_primitive_UnsignedIntField(null=True, blank=True, )
    
class FHIR_Contract_signer(models.Model):
    Contract = models.ForeignKey(FHIR_Contract, related_name='Contract_signer', null=False, on_delete=models.CASCADE)
    type = models.OneToOneField("FHIR_GP_Coding", related_name='Contract_signer_type', null=True, blank=True, on_delete=models.SET_NULL)
    party_Organization = models.ForeignKey("FHIR_Organization", related_name="Contract_signer_party", null=True, blank=True, on_delete=models.SET_NULL)
    party_Patient = models.ForeignKey("FHIR_Patient", related_name="Contract_signer_party", null=True, blank=True, on_delete=models.SET_NULL)
    party_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="Contract_signer_party", null=True, blank=True, on_delete=models.SET_NULL)
    party_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="Contract_signer_party", null=True, blank=True, on_delete=models.SET_NULL)
    party_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="Contract_signer_party", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Contract_signer_signature(FHIR_GP_Signature):
    Contract_signer = models.ForeignKey(FHIR_Contract_signer, related_name='Contract_signer_signature', null=False, on_delete=models.CASCADE)

class FHIR_Contract_friendly(models.Model):
    Contract = models.ForeignKey(FHIR_Contract, related_name='Contract_friendly', null=False, on_delete=models.CASCADE)
    content = models.OneToOneField("FHIR_GP_Attachment", related_name='Contract_friendly_content', null=True, blank=True, on_delete=models.SET_NULL)
    content_Composition = models.ForeignKey("FHIR_Composition", related_name="Contract_friendly_content", null=True, blank=True, on_delete=models.SET_NULL)
    content_DocumentReference = models.ForeignKey("FHIR_DocumentReference", related_name="Contract_friendly_content", null=True, blank=True, on_delete=models.SET_NULL)
    content_QuestionnaireResponse = models.ForeignKey("FHIR_QuestionnaireResponse", related_name="Contract_friendly_content", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Contract_legal(models.Model):
    Contract = models.ForeignKey(FHIR_Contract, related_name='Contract_legal', null=False, on_delete=models.CASCADE)
    content = models.OneToOneField("FHIR_GP_Attachment", related_name='Contract_legal_content', null=True, blank=True, on_delete=models.SET_NULL)
    content_Composition = models.ForeignKey("FHIR_Composition", related_name="Contract_legal_content", null=True, blank=True, on_delete=models.SET_NULL)
    content_DocumentReference = models.ForeignKey("FHIR_DocumentReference", related_name="Contract_legal_content", null=True, blank=True, on_delete=models.SET_NULL)
    content_QuestionnaireResponse = models.ForeignKey("FHIR_QuestionnaireResponse", related_name="Contract_legal_content", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Contract_rule(models.Model):
    Contract = models.ForeignKey(FHIR_Contract, related_name='Contract_rule', null=False, on_delete=models.CASCADE)
    content = models.OneToOneField("FHIR_GP_Attachment", related_name='Contract_rule_content', null=True, blank=True, on_delete=models.SET_NULL)
    content = models.ForeignKey("FHIR_DocumentReference", related_name="Contract_rule_content", null=True, blank=True, on_delete=models.SET_NULL)
