
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Questionnaire(models.Model):
    url = FHIR_primitive_URIField(null=True, blank=True, )
    version = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = models.OneToOneField("FHIR_GP_Coding", related_name='Questionnaire_versionAlgorithm', null=True, blank=True, on_delete=models.SET_NULL)
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
    effectivePeriod = models.OneToOneField("FHIR_GP_Period", related_name='Questionnaire_effectivePeriod', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Questionnaire_identifier(FHIR_GP_Identifier):
    Questionnaire = models.ForeignKey(FHIR_Questionnaire, related_name='Questionnaire_identifier', null=False, on_delete=models.CASCADE)

class FHIR_Questionnaire_derivedFrom(models.Model):
    Questionnaire = models.ForeignKey(FHIR_Questionnaire, related_name='Questionnaire_derivedFrom', null=False, on_delete=models.CASCADE)
    
    derivedFrom = FHIR_primitive_CanonicalField(null=True, blank=True, )
    
class FHIR_Questionnaire_subjectType(models.Model):
    Questionnaire = models.ForeignKey(FHIR_Questionnaire, related_name='Questionnaire_subjectType', null=False, on_delete=models.CASCADE)
    
    class SubjecttypeChoices(models.TextChoices): RESOURCE_THAT_CAN_BE_SUBJECT_OF_QUESTIONNAIRERESPONSE = 'Resource that can be subject of QuestionnaireResponse', 'Resource that can be subject of questionnaireresponse'; 
    subjectType = FHIR_primitive_CodeField(choices=SubjecttypeChoices.choices, null=True, blank=True, )
    
class FHIR_Questionnaire_jurisdiction(models.Model):
    Questionnaire = models.ForeignKey(FHIR_Questionnaire, related_name='Questionnaire_jurisdiction', null=False, on_delete=models.CASCADE)
    BINDING_jurisdiction = 'TODO'
    jurisdiction_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_jurisdiction}, related_name='Questionnaire_jurisdiction', blank=True)
    jurisdiction_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Questionnaire_code(FHIR_GP_Coding):
    Questionnaire = models.ForeignKey(FHIR_Questionnaire, related_name='Questionnaire_code', null=False, on_delete=models.CASCADE)

class FHIR_Questionnaire_item(models.Model):
    Questionnaire = models.ForeignKey(FHIR_Questionnaire, related_name='Questionnaire_item', null=False, on_delete=models.CASCADE)
    linkId = FHIR_primitive_StringField(null=True, blank=True, )
    definition = FHIR_primitive_URIField(null=True, blank=True, )
    prefix = FHIR_primitive_StringField(null=True, blank=True, )
    text = FHIR_primitive_StringField(null=True, blank=True, )
    class TypeChoices(models.TextChoices): GROUP = 'group', 'Group'; DISPLAY = 'display', 'Display'; BOOLEAN = 'boolean', 'Boolean'; DECIMAL = 'decimal', 'Decimal'; INTEGER = 'integer', 'Integer'; DATE = 'date', 'Date'; DATETIME_+ = 'dateTime +', 'Datetime +'; 
    type = FHIR_primitive_CodeField(choices=TypeChoices.choices, null=True, blank=True, )
    class EnablebehaviorChoices(models.TextChoices): ALL = 'all', 'All'; ANY = 'any', 'Any'; 
    enableBehavior = FHIR_primitive_CodeField(choices=EnablebehaviorChoices.choices, null=True, blank=True, )
    class DisableddisplayChoices(models.TextChoices): HIDDEN = 'hidden', 'Hidden'; PROTECTED = 'protected', 'Protected'; 
    disabledDisplay = FHIR_primitive_CodeField(choices=DisableddisplayChoices.choices, null=True, blank=True, )
    required = FHIR_primitive_BooleanField(null=True, blank=True, )
    repeats = FHIR_primitive_BooleanField(null=True, blank=True, )
    readOnly = FHIR_primitive_BooleanField(null=True, blank=True, )
    class AnswerconstraintChoices(models.TextChoices): OPTIONSONLY = 'optionsOnly', 'Optionsonly'; OPTIONSORTYPE = 'optionsOrType', 'Optionsortype'; OPTIONSORSTRING = 'optionsOrString', 'Optionsorstring'; 
    answerConstraint = FHIR_primitive_CodeField(choices=AnswerconstraintChoices.choices, null=True, blank=True, )
    answerValueSet = FHIR_primitive_CanonicalField(null=True, blank=True, )

class FHIR_Questionnaire_item_code(FHIR_GP_Coding):
    Questionnaire_item = models.ForeignKey(FHIR_Questionnaire_item, related_name='Questionnaire_item_code', null=False, on_delete=models.CASCADE)

class FHIR_Questionnaire_item_enableWhen(models.Model):
    Questionnaire_item = models.ForeignKey(FHIR_Questionnaire_item, related_name='Questionnaire_item_enableWhen', null=False, on_delete=models.CASCADE)
    question = FHIR_primitive_StringField(null=True, blank=True, )
    class OperatorChoices(models.TextChoices): EXISTS = 'exists', 'Exists'; = = '=', '='; != = '!=', '!='; > = '>', '>'; < = '<', '<'; >= = '>=', '>='; <= = '<=', '<='; 
    operator = FHIR_primitive_CodeField(choices=OperatorChoices.choices, null=True, blank=True, )
    answer = FHIR_primitive_BooleanField(null=True, blank=True, )
    answer = FHIR_primitive_DecimalField(null=True, blank=True, )
    answer = FHIR_primitive_DateField(null=True, blank=True, )
    answer = FHIR_primitive_DateTimeField(null=True, blank=True, )
    answer = FHIR_primitive_TimeField(null=True, blank=True, )
    answer = FHIR_primitive_StringField(null=True, blank=True, )
    answer = models.OneToOneField("FHIR_GP_Coding", related_name='Questionnaire_item_enableWhen_answer', null=True, blank=True, on_delete=models.SET_NULL)
    answer = models.OneToOneField("FHIR_GP_Quantity", related_name='Questionnaire_item_enableWhen_answer', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Questionnaire_item_answerOption(models.Model):
    Questionnaire_item = models.ForeignKey(FHIR_Questionnaire_item, related_name='Questionnaire_item_answerOption', null=False, on_delete=models.CASCADE)
    value = FHIR_primitive_DecimalField(null=True, blank=True, )
    value = FHIR_primitive_DateField(null=True, blank=True, )
    value = FHIR_primitive_DateTimeField(null=True, blank=True, )
    value = FHIR_primitive_TimeField(null=True, blank=True, )
    value = FHIR_primitive_StringField(null=True, blank=True, )
    value = FHIR_primitive_URIField(null=True, blank=True, )
    value = models.OneToOneField("FHIR_GP_Coding", related_name='Questionnaire_item_answerOption_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_Quantity", related_name='Questionnaire_item_answerOption_value', null=True, blank=True, on_delete=models.SET_NULL)
    initialSelected = FHIR_primitive_BooleanField(null=True, blank=True, )

class FHIR_Questionnaire_item_initial(models.Model):
    Questionnaire_item = models.ForeignKey(FHIR_Questionnaire_item, related_name='Questionnaire_item_initial', null=False, on_delete=models.CASCADE)
    value = FHIR_primitive_BooleanField(null=True, blank=True, )
    value = FHIR_primitive_DecimalField(null=True, blank=True, )
    value = FHIR_primitive_DateField(null=True, blank=True, )
    value = FHIR_primitive_DateTimeField(null=True, blank=True, )
    value = FHIR_primitive_TimeField(null=True, blank=True, )
    value = FHIR_primitive_StringField(null=True, blank=True, )
    value = FHIR_primitive_URIField(null=True, blank=True, )
    value = models.OneToOneField("FHIR_GP_Attachment", related_name='Questionnaire_item_initial_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_Coding", related_name='Questionnaire_item_initial_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_Quantity", related_name='Questionnaire_item_initial_value', null=True, blank=True, on_delete=models.SET_NULL)
