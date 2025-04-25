
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_RegulatedAuthorization(models.Model):
    subject_MedicinalProductDefinition = models.ManyToManyField("FHIR_MedicinalProductDefinition", related_name="RegulatedAuthorization_subject", blank=True)
    subject_BiologicallyDerivedProduct = models.ManyToManyField("FHIR_BiologicallyDerivedProduct", related_name="RegulatedAuthorization_subject", blank=True)
    subject_NutritionProduct = models.ManyToManyField("FHIR_NutritionProduct", related_name="RegulatedAuthorization_subject", blank=True)
    subject_PackagedProductDefinition = models.ManyToManyField("FHIR_PackagedProductDefinition", related_name="RegulatedAuthorization_subject", blank=True)
    subject_ManufacturedItemDefinition = models.ManyToManyField("FHIR_ManufacturedItemDefinition", related_name="RegulatedAuthorization_subject", blank=True)
    subject_Ingredient = models.ManyToManyField("FHIR_Ingredient", related_name="RegulatedAuthorization_subject", blank=True)
    subject_SubstanceDefinition = models.ManyToManyField("FHIR_SubstanceDefinition", related_name="RegulatedAuthorization_subject", blank=True)
    subject_DeviceDefinition = models.ManyToManyField("FHIR_DeviceDefinition", related_name="RegulatedAuthorization_subject", blank=True)
    subject_ResearchStudy = models.ManyToManyField("FHIR_ResearchStudy", related_name="RegulatedAuthorization_subject", blank=True)
    subject_ActivityDefinition = models.ManyToManyField("FHIR_ActivityDefinition", related_name="RegulatedAuthorization_subject", blank=True)
    subject_PlanDefinition = models.ManyToManyField("FHIR_PlanDefinition", related_name="RegulatedAuthorization_subject", blank=True)
    subject_ObservationDefinition = models.ManyToManyField("FHIR_ObservationDefinition", related_name="RegulatedAuthorization_subject", blank=True)
    subject_Practitioner = models.ManyToManyField("FHIR_Practitioner", related_name="RegulatedAuthorization_subject", blank=True)
    subject_Organization = models.ManyToManyField("FHIR_Organization", related_name="RegulatedAuthorization_subject", blank=True)
    subject_Location = models.ManyToManyField("FHIR_Location", related_name="RegulatedAuthorization_subject", blank=True)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='RegulatedAuthorization_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    BINDING_status = 'TODO'
    status_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_status}, related_name='RegulatedAuthorization_status', blank=True)
    status_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    statusDate = FHIR_primitive_DateTimeField(null=True, blank=True, )
    validityPeriod = models.OneToOneField("FHIR_GP_Period", related_name='RegulatedAuthorization_validityPeriod', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_intendedUse = 'TODO'
    intendedUse_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_intendedUse}, related_name='RegulatedAuthorization_intendedUse', blank=True)
    intendedUse_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    holder = models.ForeignKey("FHIR_Organization", related_name="RegulatedAuthorization_holder", null=True, blank=True, on_delete=models.SET_NULL)
    regulator = models.ForeignKey("FHIR_Organization", related_name="RegulatedAuthorization_regulator", null=True, blank=True, on_delete=models.SET_NULL)
    attachedDocument = models.ManyToManyField("FHIR_DocumentReference", related_name="RegulatedAuthorization_attachedDocument", blank=True)

class FHIR_RegulatedAuthorization_identifier(FHIR_GP_Identifier):
    RegulatedAuthorization = models.ForeignKey(FHIR_RegulatedAuthorization, related_name='RegulatedAuthorization_identifier', null=False, on_delete=models.CASCADE)

class FHIR_RegulatedAuthorization_region(models.Model):
    RegulatedAuthorization = models.ForeignKey(FHIR_RegulatedAuthorization, related_name='RegulatedAuthorization_region', null=False, on_delete=models.CASCADE)
    BINDING_region = 'TODO'
    region_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_region}, related_name='RegulatedAuthorization_region', blank=True)
    region_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_RegulatedAuthorization_indication(models.Model):
    RegulatedAuthorization = models.ForeignKey(FHIR_RegulatedAuthorization, related_name='RegulatedAuthorization_indication', null=False, on_delete=models.CASCADE)
    BINDING_indication = 'TODO'
    indication_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_indication}, related_name='RegulatedAuthorization_indication', blank=True)
    indication_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    indication_ClinicalUseDefinition_ref = models.ForeignKey("FHIR_ClinicalUseDefinition", related_name="RegulatedAuthorization_indication", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_RegulatedAuthorization_basis(models.Model):
    RegulatedAuthorization = models.ForeignKey(FHIR_RegulatedAuthorization, related_name='RegulatedAuthorization_basis', null=False, on_delete=models.CASCADE)
    BINDING_basis = 'TODO'
    basis_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_basis}, related_name='RegulatedAuthorization_basis', blank=True)
    basis_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_RegulatedAuthorization_case(models.Model):
    RegulatedAuthorization = models.ForeignKey(FHIR_RegulatedAuthorization, related_name='RegulatedAuthorization_case', null=False, on_delete=models.CASCADE)
    identifier = models.OneToOneField("FHIR_GP_Identifier", related_name='RegulatedAuthorization_case_identifier', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='RegulatedAuthorization_case_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_status = 'TODO'
    status_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_status}, related_name='RegulatedAuthorization_case_status', blank=True)
    status_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    date = models.OneToOneField("FHIR_GP_Period", related_name='RegulatedAuthorization_case_date', null=True, blank=True, on_delete=models.SET_NULL)
    date = FHIR_primitive_DateTimeField(null=True, blank=True, )
