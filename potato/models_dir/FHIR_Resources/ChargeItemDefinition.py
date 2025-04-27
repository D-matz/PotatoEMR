#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_ChargeItemDefinition(models.Model):
    url = FHIR_primitive_URIField(null=True, blank=True, )
    version = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = models.OneToOneField("FHIR_GP_Coding", related_name='ChargeItemDefinition_versionAlgorithm', null=True, blank=True, on_delete=models.SET_NULL)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    title = FHIR_primitive_StringField(null=True, blank=True, )
    class StatusChoices(models.TextChoices): DRAFT = 'draft', 'Draft'; ACTIVE = 'active', 'Active'; RETIRED = 'retired', 'Retired'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    experimental = FHIR_primitive_BooleanField(null=True, blank=True, )
    date = FHIR_primitive_DateTimeField(null=True, blank=True, )
    account = models.ManyToManyField("FHIR_Account", related_name="ChargeItemDefinition_account", blank=True)
    publisher = FHIR_primitive_StringField(null=True, blank=True, )
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    purpose = FHIR_primitive_MarkdownField(null=True, blank=True, )
    copyright = FHIR_primitive_MarkdownField(null=True, blank=True, )
    copyrightLabel = FHIR_primitive_StringField(null=True, blank=True, )
    approvalDate = FHIR_primitive_DateField(null=True, blank=True, )
    lastReviewDate = FHIR_primitive_DateField(null=True, blank=True, )
    BINDING_code = 'TODO'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='ChargeItemDefinition_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    instance_Medication = models.ManyToManyField("FHIR_Medication", related_name="ChargeItemDefinition_instance", blank=True)
    instance_Substance = models.ManyToManyField("FHIR_Substance", related_name="ChargeItemDefinition_instance", blank=True)
    instance_SubstanceDefinition = models.ManyToManyField("FHIR_SubstanceDefinition", related_name="ChargeItemDefinition_instance", blank=True)
    instance_Device = models.ManyToManyField("FHIR_Device", related_name="ChargeItemDefinition_instance", blank=True)
    instance_DeviceDefinition = models.ManyToManyField("FHIR_DeviceDefinition", related_name="ChargeItemDefinition_instance", blank=True)
    instance_ActivityDefinition = models.ManyToManyField("FHIR_ActivityDefinition", related_name="ChargeItemDefinition_instance", blank=True)
    instance_PlanDefinition = models.ManyToManyField("FHIR_PlanDefinition", related_name="ChargeItemDefinition_instance", blank=True)
    instance_HealthcareService = models.ManyToManyField("FHIR_HealthcareService", related_name="ChargeItemDefinition_instance", blank=True)

class FHIR_ChargeItemDefinition_identifier(FHIR_GP_Identifier):
    ChargeItemDefinition = models.ForeignKey(FHIR_ChargeItemDefinition, related_name='ChargeItemDefinition_identifier', null=False, on_delete=models.CASCADE)

class FHIR_ChargeItemDefinition_derivedFromUri(models.Model):
    ChargeItemDefinition = models.ForeignKey(FHIR_ChargeItemDefinition, related_name='ChargeItemDefinition_derivedFromUri', null=False, on_delete=models.CASCADE)
    
    derivedFromUri = FHIR_primitive_URIField(null=True, blank=True, )
    
class FHIR_ChargeItemDefinition_partOf(models.Model):
    ChargeItemDefinition = models.ForeignKey(FHIR_ChargeItemDefinition, related_name='ChargeItemDefinition_partOf', null=False, on_delete=models.CASCADE)
    
    partOf = FHIR_primitive_CanonicalField(null=True, blank=True, )
    
class FHIR_ChargeItemDefinition_replaces(models.Model):
    ChargeItemDefinition = models.ForeignKey(FHIR_ChargeItemDefinition, related_name='ChargeItemDefinition_replaces', null=False, on_delete=models.CASCADE)
    
    replaces = FHIR_primitive_CanonicalField(null=True, blank=True, )
    
class FHIR_ChargeItemDefinition_jurisdiction(models.Model):
    ChargeItemDefinition = models.ForeignKey(FHIR_ChargeItemDefinition, related_name='ChargeItemDefinition_jurisdiction', null=False, on_delete=models.CASCADE)
    BINDING_jurisdiction = 'TODO'
    jurisdiction_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_jurisdiction}, related_name='ChargeItemDefinition_jurisdiction', blank=True)
    jurisdiction_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ChargeItemDefinition_applicability(models.Model):
    ChargeItemDefinition = models.ForeignKey(FHIR_ChargeItemDefinition, related_name='ChargeItemDefinition_applicability', null=False, on_delete=models.CASCADE)
    effectivePeriod = models.OneToOneField("FHIR_GP_Period", related_name='ChargeItemDefinition_applicability_effectivePeriod', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ChargeItemDefinition_propertyGroup(models.Model):
    ChargeItemDefinition = models.ForeignKey(FHIR_ChargeItemDefinition, related_name='ChargeItemDefinition_propertyGroup', null=False, on_delete=models.CASCADE)
