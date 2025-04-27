#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Account(models.Model):
    class StatusChoices(models.TextChoices): ACTIVE = 'active', 'Active'; INACTIVE = 'inactive', 'Inactive'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; ON_HOLD = 'on-hold', 'On-hold'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    BINDING_billingStatus = "TODO"
    billingStatus_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_billingStatus}, related_name='Account_billingStatus', blank=True)
    billingStatus_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Account_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    subject_Patient = models.ManyToManyField("FHIR_Patient", related_name="Account_subject", blank=True)
    subject_Device = models.ManyToManyField("FHIR_Device", related_name="Account_subject", blank=True)
    subject_Practitioner = models.ManyToManyField("FHIR_Practitioner", related_name="Account_subject", blank=True)
    subject_PractitionerRole = models.ManyToManyField("FHIR_PractitionerRole", related_name="Account_subject", blank=True)
    subject_Location = models.ManyToManyField("FHIR_Location", related_name="Account_subject", blank=True)
    subject_HealthcareService = models.ManyToManyField("FHIR_HealthcareService", related_name="Account_subject", blank=True)
    subject_Organization = models.ManyToManyField("FHIR_Organization", related_name="Account_subject", blank=True)
    servicePeriod = models.OneToOneField("FHIR_GP_Period", related_name='Account_servicePeriod', null=True, blank=True, on_delete=models.SET_NULL)
    covers_Encounter = models.ManyToManyField("FHIR_Encounter", related_name="Account_covers", blank=True)
    covers_EpisodeOfCare = models.ManyToManyField("FHIR_EpisodeOfCare", related_name="Account_covers", blank=True)
    owner = models.ForeignKey("FHIR_Organization", related_name="Account_owner", null=True, blank=True, on_delete=models.SET_NULL)
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    parent = models.ForeignKey("FHIR_Account", related_name="Account_parent", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_currency = "TODO"
    currency_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_currency}, related_name='Account_currency', blank=True)
    currency_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    calculatedAt = FHIR_primitive_InstantField(null=True, blank=True, )

class FHIR_Account_identifier(FHIR_GP_Identifier):
    Account = models.ForeignKey(FHIR_Account, related_name='Account_identifier', null=False, on_delete=models.CASCADE)

class FHIR_Account_coverage(models.Model):
    Account = models.ForeignKey(FHIR_Account, related_name='Account_coverage', null=False, on_delete=models.CASCADE)
    coverage = models.ForeignKey("FHIR_Coverage", related_name="Account_coverage_coverage", null=True, blank=True, on_delete=models.SET_NULL)
    priority = FHIR_primitive_PositiveIntField(null=True, blank=True, )

class FHIR_Account_guarantor(models.Model):
    Account = models.ForeignKey(FHIR_Account, related_name='Account_guarantor', null=False, on_delete=models.CASCADE)
    party_Patient = models.ForeignKey("FHIR_Patient", related_name="Account_guarantor_party", null=True, blank=True, on_delete=models.SET_NULL)
    party_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="Account_guarantor_party", null=True, blank=True, on_delete=models.SET_NULL)
    party_Organization = models.ForeignKey("FHIR_Organization", related_name="Account_guarantor_party", null=True, blank=True, on_delete=models.SET_NULL)
    onHold = FHIR_primitive_BooleanField(null=True, blank=True, )
    period = models.OneToOneField("FHIR_GP_Period", related_name='Account_guarantor_period', null=True, blank=True, on_delete=models.SET_NULL)
    account = models.ForeignKey("FHIR_Account", related_name="Account_guarantor_account", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Account_diagnosis(models.Model):
    Account = models.ForeignKey(FHIR_Account, related_name='Account_diagnosis', null=False, on_delete=models.CASCADE)
    sequence = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    BINDING_condition = "TODO"
    condition_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_condition}, related_name='Account_diagnosis_condition', blank=True)
    condition_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    condition_Condition_ref = models.ForeignKey("FHIR_Condition", related_name="Account_diagnosis_condition_Condition", null=True, blank=True, on_delete=models.SET_NULL)
    dateOfDiagnosis = FHIR_primitive_DateTimeField(null=True, blank=True, )
    onAdmission = FHIR_primitive_BooleanField(null=True, blank=True, )

class FHIR_Account_diagnosis_type(models.Model):
    Account_diagnosis = models.ForeignKey(FHIR_Account_diagnosis, related_name='Account_diagnosis_type', null=False, on_delete=models.CASCADE)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Account_diagnosis_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Account_diagnosis_packageCode(models.Model):
    Account_diagnosis = models.ForeignKey(FHIR_Account_diagnosis, related_name='Account_diagnosis_packageCode', null=False, on_delete=models.CASCADE)
    BINDING_packageCode = "TODO"
    packageCode_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_packageCode}, related_name='Account_diagnosis_packageCode', blank=True)
    packageCode_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Account_procedure(models.Model):
    Account = models.ForeignKey(FHIR_Account, related_name='Account_procedure', null=False, on_delete=models.CASCADE)
    sequence = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    BINDING_code = "TODO"
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='Account_procedure_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    code_Procedure_ref = models.ForeignKey("FHIR_Procedure", related_name="Account_procedure_code_Procedure", null=True, blank=True, on_delete=models.SET_NULL)
    dateOfService = FHIR_primitive_DateTimeField(null=True, blank=True, )
    device = models.ManyToManyField("FHIR_Device", related_name="Account_procedure_device", blank=True)

class FHIR_Account_procedure_type(models.Model):
    Account_procedure = models.ForeignKey(FHIR_Account_procedure, related_name='Account_procedure_type', null=False, on_delete=models.CASCADE)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Account_procedure_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Account_procedure_packageCode(models.Model):
    Account_procedure = models.ForeignKey(FHIR_Account_procedure, related_name='Account_procedure_packageCode', null=False, on_delete=models.CASCADE)
    BINDING_packageCode = "TODO"
    packageCode_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_packageCode}, related_name='Account_procedure_packageCode', blank=True)
    packageCode_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Account_balance(models.Model):
    Account = models.ForeignKey(FHIR_Account, related_name='Account_balance', null=False, on_delete=models.CASCADE)
    BINDING_aggregate = "TODO"
    aggregate_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_aggregate}, related_name='Account_balance_aggregate', blank=True)
    aggregate_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_term = "TODO"
    term_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_term}, related_name='Account_balance_term', blank=True)
    term_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    estimate = FHIR_primitive_BooleanField(null=True, blank=True, )
    amount = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='Account_balance_amount', null=True, blank=True, on_delete=models.SET_NULL)
