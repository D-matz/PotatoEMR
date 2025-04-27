#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_MeasureReport(models.Model):
    BINDING_category = 'TODO'
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='MeasureReport_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    messages = models.ForeignKey("FHIR_OperationOutcome", related_name="MeasureReport_messages", null=True, blank=True, on_delete=models.SET_NULL)
    class StatusChoices(models.TextChoices): COMPLETE = 'complete', 'Complete'; PENDING = 'pending', 'Pending'; ERROR = 'error', 'Error'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    class TypeChoices(models.TextChoices): INDIVIDUAL = 'individual', 'Individual'; SUBJECT_LIST = 'subject-list', 'Subject-list'; SUMMARY = 'summary', 'Summary'; DATA_EXCHANGE = 'data-exchange', 'Data-exchange'; 
    type = FHIR_primitive_CodeField(choices=TypeChoices.choices, null=True, blank=True, )
    class DataupdatetypeChoices(models.TextChoices): INCREMENTAL = 'incremental', 'Incremental'; SNAPSHOT = 'snapshot', 'Snapshot'; 
    dataUpdateType = FHIR_primitive_CodeField(choices=DataupdatetypeChoices.choices, null=True, blank=True, )
    measure = FHIR_primitive_CanonicalField(null=True, blank=True, )
    subject_CareTeam = models.ForeignKey("FHIR_CareTeam", related_name="MeasureReport_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Device = models.ForeignKey("FHIR_Device", related_name="MeasureReport_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Group = models.ForeignKey("FHIR_Group", related_name="MeasureReport_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_HealthcareService = models.ForeignKey("FHIR_HealthcareService", related_name="MeasureReport_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Location = models.ForeignKey("FHIR_Location", related_name="MeasureReport_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Organization = models.ForeignKey("FHIR_Organization", related_name="MeasureReport_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Patient = models.ForeignKey("FHIR_Patient", related_name="MeasureReport_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="MeasureReport_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="MeasureReport_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="MeasureReport_subject", null=True, blank=True, on_delete=models.SET_NULL)
    date = FHIR_primitive_DateTimeField(null=True, blank=True, )
    reporter_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="MeasureReport_reporter", null=True, blank=True, on_delete=models.SET_NULL)
    reporter_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="MeasureReport_reporter", null=True, blank=True, on_delete=models.SET_NULL)
    reporter_Organization = models.ForeignKey("FHIR_Organization", related_name="MeasureReport_reporter", null=True, blank=True, on_delete=models.SET_NULL)
    reportingVendor = models.ForeignKey("FHIR_Organization", related_name="MeasureReport_reportingVendor", null=True, blank=True, on_delete=models.SET_NULL)
    location = models.ManyToManyField("FHIR_Location", related_name="MeasureReport_location", blank=True)
    period = models.OneToOneField("FHIR_GP_Period", related_name='MeasureReport_period', null=True, blank=True, on_delete=models.SET_NULL)
    inputParameters = models.ForeignKey("FHIR_Parameters", related_name="MeasureReport_inputParameters", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_scoring = 'TODO'
    scoring_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_scoring}, related_name='MeasureReport_scoring', blank=True)
    scoring_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_improvementNotation = 'TODO'
    improvementNotation_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_improvementNotation}, related_name='MeasureReport_improvementNotation', blank=True)
    improvementNotation_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_MeasureReport_identifier(FHIR_GP_Identifier):
    MeasureReport = models.ForeignKey(FHIR_MeasureReport, related_name='MeasureReport_identifier', null=False, on_delete=models.CASCADE)

class FHIR_MeasureReport_group(models.Model):
    MeasureReport = models.ForeignKey(FHIR_MeasureReport, related_name='MeasureReport_group', null=False, on_delete=models.CASCADE)
    linkId = FHIR_primitive_StringField(null=True, blank=True, )
    calculatedDate = FHIR_primitive_DateTimeField(null=True, blank=True, )
    BINDING_code = 'TODO'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='MeasureReport_group_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    subject_CareTeam = models.ForeignKey("FHIR_CareTeam", related_name="MeasureReport_group_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Device = models.ForeignKey("FHIR_Device", related_name="MeasureReport_group_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Group = models.ForeignKey("FHIR_Group", related_name="MeasureReport_group_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_HealthcareService = models.ForeignKey("FHIR_HealthcareService", related_name="MeasureReport_group_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Location = models.ForeignKey("FHIR_Location", related_name="MeasureReport_group_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Organization = models.ForeignKey("FHIR_Organization", related_name="MeasureReport_group_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Patient = models.ForeignKey("FHIR_Patient", related_name="MeasureReport_group_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="MeasureReport_group_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="MeasureReport_group_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="MeasureReport_group_subject", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_scoring = 'TODO'
    scoring_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_scoring}, related_name='MeasureReport_group_scoring', blank=True)
    scoring_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_improvementNotation = 'TODO'
    improvementNotation_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_improvementNotation}, related_name='MeasureReport_group_improvementNotation', blank=True)
    improvementNotation_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    improvementNotationGuidance = FHIR_primitive_MarkdownField(null=True, blank=True, )
    measureScore = models.OneToOneField("FHIR_GP_Quantity", related_name='MeasureReport_group_measureScore', null=True, blank=True, on_delete=models.SET_NULL)
    measureScore = FHIR_primitive_DateTimeField(null=True, blank=True, )
    BINDING_measureScore = 'TODO'
    measureScore_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_measureScore}, related_name='MeasureReport_group_measureScore', blank=True)
    measureScore_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    measureScore = models.OneToOneField("FHIR_GP_Period", related_name='MeasureReport_group_measureScore', null=True, blank=True, on_delete=models.SET_NULL)
    measureScore = models.OneToOneField("FHIR_GP_Range", related_name='MeasureReport_group_measureScore', null=True, blank=True, on_delete=models.SET_NULL)
    measureScore = models.OneToOneField("FHIR_GP_Quantity_Duration", related_name='MeasureReport_group_measureScore', null=True, blank=True, on_delete=models.SET_NULL)
    measureScore = FHIR_primitive_BooleanField(null=True, blank=True, )

class FHIR_MeasureReport_group_population(models.Model):
    MeasureReport_group = models.ForeignKey(FHIR_MeasureReport_group, related_name='MeasureReport_group_population', null=False, on_delete=models.CASCADE)
    linkId = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_code = 'TODO'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='MeasureReport_group_population_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    countQuantity = models.OneToOneField("FHIR_GP_Quantity", related_name='MeasureReport_group_population_countQuantity', null=True, blank=True, on_delete=models.SET_NULL)
    subjectResults = models.ForeignKey("FHIR_List", related_name="MeasureReport_group_population_subjectResults", null=True, blank=True, on_delete=models.SET_NULL)
    subjectReport = models.ManyToManyField("FHIR_MeasureReport", related_name="MeasureReport_group_population_subjectReport", blank=True)
    subjects = models.ForeignKey("FHIR_Group", related_name="MeasureReport_group_population_subjects", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_MeasureReport_group_stratifier(models.Model):
    MeasureReport_group = models.ForeignKey(FHIR_MeasureReport_group, related_name='MeasureReport_group_stratifier', null=False, on_delete=models.CASCADE)
    linkId = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_code = 'TODO'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='MeasureReport_group_stratifier_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_MeasureReport_group_stratifier_stratum(models.Model):
    MeasureReport_group_stratifier = models.ForeignKey(FHIR_MeasureReport_group_stratifier, related_name='MeasureReport_group_stratifier_stratum', null=False, on_delete=models.CASCADE)
    BINDING_value = 'TODO'
    value_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_value}, related_name='MeasureReport_group_stratifier_stratum_value', blank=True)
    value_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value = FHIR_primitive_BooleanField(null=True, blank=True, )
    value = models.OneToOneField("FHIR_GP_Quantity", related_name='MeasureReport_group_stratifier_stratum_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_Range", related_name='MeasureReport_group_stratifier_stratum_value', null=True, blank=True, on_delete=models.SET_NULL)
    measureScore = models.OneToOneField("FHIR_GP_Quantity", related_name='MeasureReport_group_stratifier_stratum_measureScore', null=True, blank=True, on_delete=models.SET_NULL)
    measureScore = FHIR_primitive_DateTimeField(null=True, blank=True, )
    BINDING_measureScore = 'TODO'
    measureScore_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_measureScore}, related_name='MeasureReport_group_stratifier_stratum_measureScore', blank=True)
    measureScore_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    measureScore = models.OneToOneField("FHIR_GP_Period", related_name='MeasureReport_group_stratifier_stratum_measureScore', null=True, blank=True, on_delete=models.SET_NULL)
    measureScore = models.OneToOneField("FHIR_GP_Range", related_name='MeasureReport_group_stratifier_stratum_measureScore', null=True, blank=True, on_delete=models.SET_NULL)
    measureScore = models.OneToOneField("FHIR_GP_Quantity_Duration", related_name='MeasureReport_group_stratifier_stratum_measureScore', null=True, blank=True, on_delete=models.SET_NULL)
    measureScore = FHIR_primitive_BooleanField(null=True, blank=True, )

class FHIR_MeasureReport_group_stratifier_stratum_component(models.Model):
    MeasureReport_group_stratifier_stratum = models.ForeignKey(FHIR_MeasureReport_group_stratifier_stratum, related_name='MeasureReport_group_stratifier_stratum_component', null=False, on_delete=models.CASCADE)
    linkId = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_code = 'TODO'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='MeasureReport_group_stratifier_stratum_component_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    BINDING_value = 'TODO'
    value_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_value}, related_name='MeasureReport_group_stratifier_stratum_component_value', blank=True)
    value_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value = FHIR_primitive_BooleanField(null=True, blank=True, )
    value = models.OneToOneField("FHIR_GP_Quantity", related_name='MeasureReport_group_stratifier_stratum_component_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_Range", related_name='MeasureReport_group_stratifier_stratum_component_value', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_MeasureReport_group_stratifier_stratum_population(models.Model):
    MeasureReport_group_stratifier_stratum = models.ForeignKey(FHIR_MeasureReport_group_stratifier_stratum, related_name='MeasureReport_group_stratifier_stratum_population', null=False, on_delete=models.CASCADE)
    linkId = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_code = 'TODO'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='MeasureReport_group_stratifier_stratum_population_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    countQuantity = models.OneToOneField("FHIR_GP_Quantity", related_name='MeasureReport_group_stratifier_stratum_population_countQuantity', null=True, blank=True, on_delete=models.SET_NULL)
    subjectResults = models.ForeignKey("FHIR_List", related_name="MeasureReport_group_stratifier_stratum_population_subjectResults", null=True, blank=True, on_delete=models.SET_NULL)
    subjectReport = models.ManyToManyField("FHIR_MeasureReport", related_name="MeasureReport_group_stratifier_stratum_population_subjectReport", blank=True)
    subjects = models.ForeignKey("FHIR_Group", related_name="MeasureReport_group_stratifier_stratum_population_subjects", null=True, blank=True, on_delete=models.SET_NULL)
