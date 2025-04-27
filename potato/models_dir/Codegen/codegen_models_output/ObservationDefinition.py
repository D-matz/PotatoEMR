#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_ObservationDefinition(models.Model):
    url = FHIR_primitive_URIField(null=True, blank=True, )
    identifier = models.OneToOneField("FHIR_GP_Identifier", related_name='ObservationDefinition_identifier', null=True, blank=True, on_delete=models.SET_NULL)
    version = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = models.OneToOneField("FHIR_GP_Coding", related_name='ObservationDefinition_versionAlgorithm', null=True, blank=True, on_delete=models.SET_NULL)
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
    effectivePeriod = models.OneToOneField("FHIR_GP_Period", related_name='ObservationDefinition_effectivePeriod', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_performerType = "TODO"
    performerType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_performerType}, related_name='ObservationDefinition_performerType', blank=True)
    performerType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_code = "TODO"
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='ObservationDefinition_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    multipleResultsAllowed = FHIR_primitive_BooleanField(null=True, blank=True, )
    BINDING_bodySite = "TODO"
    bodySite_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_bodySite}, related_name='ObservationDefinition_bodySite', blank=True)
    bodySite_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_method = "TODO"
    method_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_method}, related_name='ObservationDefinition_method', blank=True)
    method_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    specimen = models.ManyToManyField("FHIR_SpecimenDefinition", related_name="ObservationDefinition_specimen", blank=True)
    device_DeviceDefinition = models.ManyToManyField("FHIR_DeviceDefinition", related_name="ObservationDefinition_device", blank=True)
    device_Device = models.ManyToManyField("FHIR_Device", related_name="ObservationDefinition_device", blank=True)
    preferredReportName = FHIR_primitive_StringField(null=True, blank=True, )
    hasMember_ObservationDefinition = models.ManyToManyField("FHIR_ObservationDefinition", related_name="ObservationDefinition_hasMember", blank=True)
    hasMember_Questionnaire = models.ManyToManyField("FHIR_Questionnaire", related_name="ObservationDefinition_hasMember", blank=True)

class FHIR_ObservationDefinition_jurisdiction(models.Model):
    ObservationDefinition = models.ForeignKey(FHIR_ObservationDefinition, related_name='ObservationDefinition_jurisdiction', null=False, on_delete=models.CASCADE)
    BINDING_jurisdiction = "TODO"
    jurisdiction_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_jurisdiction}, related_name='ObservationDefinition_jurisdiction', blank=True)
    jurisdiction_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ObservationDefinition_derivedFromCanonical(models.Model):
    ObservationDefinition = models.ForeignKey(FHIR_ObservationDefinition, related_name='ObservationDefinition_derivedFromCanonical', null=False, on_delete=models.CASCADE)
    
    derivedFromCanonical = FHIR_primitive_CanonicalField(null=True, blank=True, )
    
class FHIR_ObservationDefinition_derivedFromUri(models.Model):
    ObservationDefinition = models.ForeignKey(FHIR_ObservationDefinition, related_name='ObservationDefinition_derivedFromUri', null=False, on_delete=models.CASCADE)
    
    derivedFromUri = FHIR_primitive_URIField(null=True, blank=True, )
    
class FHIR_ObservationDefinition_subject(models.Model):
    ObservationDefinition = models.ForeignKey(FHIR_ObservationDefinition, related_name='ObservationDefinition_subject', null=False, on_delete=models.CASCADE)
    BINDING_subject = "TODO"
    subject_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_subject}, related_name='ObservationDefinition_subject', blank=True)
    subject_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ObservationDefinition_category(models.Model):
    ObservationDefinition = models.ForeignKey(FHIR_ObservationDefinition, related_name='ObservationDefinition_category', null=False, on_delete=models.CASCADE)
    BINDING_category = "TODO"
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='ObservationDefinition_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ObservationDefinition_permittedDataType(models.Model):
    ObservationDefinition = models.ForeignKey(FHIR_ObservationDefinition, related_name='ObservationDefinition_permittedDataType', null=False, on_delete=models.CASCADE)
    
    class PermitteddatatypeChoices(models.TextChoices): QUANTITY = 'Quantity', 'Quantity'; CODEABLECONCEPT = 'CodeableConcept', 'Codeableconcept'; STRING = 'string', 'String'; BOOLEAN = 'boolean', 'Boolean'; INTEGER = 'integer', 'Integer'; RANGE = 'Range', 'Range'; RATIO = 'Ratio', 'Ratio'; SAMPLEDDATA = 'SampledData', 'Sampleddata'; TIME = 'time', 'Time'; DATETIME = 'dateTime', 'Datetime'; PERIOD = 'Period', 'Period'; 
    permittedDataType = FHIR_primitive_CodeField(choices=PermitteddatatypeChoices.choices, null=True, blank=True, )
    
class FHIR_ObservationDefinition_permittedUnit(FHIR_GP_Coding):
    ObservationDefinition = models.ForeignKey(FHIR_ObservationDefinition, related_name='ObservationDefinition_permittedUnit', null=False, on_delete=models.CASCADE)

class FHIR_ObservationDefinition_qualifiedValue(models.Model):
    ObservationDefinition = models.ForeignKey(FHIR_ObservationDefinition, related_name='ObservationDefinition_qualifiedValue', null=False, on_delete=models.CASCADE)
    BINDING_context = "TODO"
    context_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_context}, related_name='ObservationDefinition_qualifiedValue_context', blank=True)
    context_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    class GenderChoices(models.TextChoices): MALE = 'male', 'Male'; FEMALE = 'female', 'Female'; OTHER = 'other', 'Other'; UNKNOWN = 'unknown', 'Unknown'; 
    gender = FHIR_primitive_CodeField(choices=GenderChoices.choices, null=True, blank=True, )
    age = models.OneToOneField("FHIR_GP_Range", related_name='ObservationDefinition_qualifiedValue_age', null=True, blank=True, on_delete=models.SET_NULL)
    gestationalAge = models.OneToOneField("FHIR_GP_Range", related_name='ObservationDefinition_qualifiedValue_gestationalAge', null=True, blank=True, on_delete=models.SET_NULL)
    condition = FHIR_primitive_StringField(null=True, blank=True, )
    class RangecategoryChoices(models.TextChoices): REFERENCE = 'reference', 'Reference'; CRITICAL = 'critical', 'Critical'; ABSOLUTE = 'absolute', 'Absolute'; 
    rangeCategory = FHIR_primitive_CodeField(choices=RangecategoryChoices.choices, null=True, blank=True, )
    range = models.OneToOneField("FHIR_GP_Range", related_name='ObservationDefinition_qualifiedValue_range', null=True, blank=True, on_delete=models.SET_NULL)
    validCodedValueSet = FHIR_primitive_CanonicalField(null=True, blank=True, )
    normalCodedValueSet = FHIR_primitive_CanonicalField(null=True, blank=True, )
    abnormalCodedValueSet = FHIR_primitive_CanonicalField(null=True, blank=True, )
    criticalCodedValueSet = FHIR_primitive_CanonicalField(null=True, blank=True, )

class FHIR_ObservationDefinition_qualifiedValue_appliesTo(models.Model):
    ObservationDefinition_qualifiedValue = models.ForeignKey(FHIR_ObservationDefinition_qualifiedValue, related_name='ObservationDefinition_qualifiedValue_appliesTo', null=False, on_delete=models.CASCADE)
    BINDING_appliesTo = "TODO"
    appliesTo_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_appliesTo}, related_name='ObservationDefinition_qualifiedValue_appliesTo', blank=True)
    appliesTo_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ObservationDefinition_qualifiedValue_interpretation(models.Model):
    ObservationDefinition_qualifiedValue = models.ForeignKey(FHIR_ObservationDefinition_qualifiedValue, related_name='ObservationDefinition_qualifiedValue_interpretation', null=False, on_delete=models.CASCADE)
    BINDING_interpretation = "TODO"
    interpretation_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_interpretation}, related_name='ObservationDefinition_qualifiedValue_interpretation', blank=True)
    interpretation_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ObservationDefinition_component(models.Model):
    ObservationDefinition = models.ForeignKey(FHIR_ObservationDefinition, related_name='ObservationDefinition_component', null=False, on_delete=models.CASCADE)
    BINDING_code = "TODO"
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='ObservationDefinition_component_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_ObservationDefinition_component_permittedDataType(models.Model):
    ObservationDefinition_component = models.ForeignKey(FHIR_ObservationDefinition_component, related_name='ObservationDefinition_component_permittedDataType', null=False, on_delete=models.CASCADE)
    
    class PermitteddatatypeChoices(models.TextChoices): QUANTITY = 'Quantity', 'Quantity'; CODEABLECONCEPT = 'CodeableConcept', 'Codeableconcept'; STRING = 'string', 'String'; BOOLEAN = 'boolean', 'Boolean'; INTEGER = 'integer', 'Integer'; RANGE = 'Range', 'Range'; RATIO = 'Ratio', 'Ratio'; SAMPLEDDATA = 'SampledData', 'Sampleddata'; TIME = 'time', 'Time'; DATETIME = 'dateTime', 'Datetime'; PERIOD = 'Period', 'Period'; 
    permittedDataType = FHIR_primitive_CodeField(choices=PermitteddatatypeChoices.choices, null=True, blank=True, )
    
class FHIR_ObservationDefinition_component_permittedUnit(FHIR_GP_Coding):
    ObservationDefinition_component = models.ForeignKey(FHIR_ObservationDefinition_component, related_name='ObservationDefinition_component_permittedUnit', null=False, on_delete=models.CASCADE)
