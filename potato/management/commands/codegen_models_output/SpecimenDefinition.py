
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_SpecimenDefinition(models.Model):
    url = FHIR_primitive_URIField(null=True, blank=True, )
    identifier = models.OneToOneField("FHIR_GP_Identifier", related_name='SpecimenDefinition_identifier', null=True, blank=True, on_delete=models.SET_NULL)
    version = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = models.OneToOneField("FHIR_GP_Coding", related_name='SpecimenDefinition_versionAlgorithm', null=True, blank=True, on_delete=models.SET_NULL)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    title = FHIR_primitive_StringField(null=True, blank=True, )
    class StatusChoices(models.TextChoices): DRAFT = 'draft', 'Draft'; ACTIVE = 'active', 'Active'; RETIRED = 'retired', 'Retired'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    experimental = FHIR_primitive_BooleanField(null=True, blank=True, )
    BINDING_subject = 'TODO'
    subject_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_subject}, related_name='SpecimenDefinition_subject', blank=True)
    subject_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    subject = models.ForeignKey("FHIR_Group", related_name="SpecimenDefinition_subject", null=True, blank=True, on_delete=models.SET_NULL)
    date = FHIR_primitive_DateTimeField(null=True, blank=True, )
    publisher = FHIR_primitive_StringField(null=True, blank=True, )
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    purpose = FHIR_primitive_MarkdownField(null=True, blank=True, )
    copyright = FHIR_primitive_MarkdownField(null=True, blank=True, )
    copyrightLabel = FHIR_primitive_StringField(null=True, blank=True, )
    approvalDate = FHIR_primitive_DateField(null=True, blank=True, )
    lastReviewDate = FHIR_primitive_DateField(null=True, blank=True, )
    effectivePeriod = models.OneToOneField("FHIR_GP_Period", related_name='SpecimenDefinition_effectivePeriod', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_typeCollected = 'TODO'
    typeCollected_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_typeCollected}, related_name='SpecimenDefinition_typeCollected', blank=True)
    typeCollected_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    timeAspect = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_SpecimenDefinition_derivedFromCanonical(models.Model):
    SpecimenDefinition = models.ForeignKey(FHIR_SpecimenDefinition, related_name='SpecimenDefinition_derivedFromCanonical', null=False, on_delete=models.CASCADE)
    
    derivedFromCanonical = FHIR_primitive_CanonicalField(null=True, blank=True, )
    
class FHIR_SpecimenDefinition_derivedFromUri(models.Model):
    SpecimenDefinition = models.ForeignKey(FHIR_SpecimenDefinition, related_name='SpecimenDefinition_derivedFromUri', null=False, on_delete=models.CASCADE)
    
    derivedFromUri = FHIR_primitive_URIField(null=True, blank=True, )
    
class FHIR_SpecimenDefinition_jurisdiction(models.Model):
    SpecimenDefinition = models.ForeignKey(FHIR_SpecimenDefinition, related_name='SpecimenDefinition_jurisdiction', null=False, on_delete=models.CASCADE)
    BINDING_jurisdiction = 'TODO'
    jurisdiction_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_jurisdiction}, related_name='SpecimenDefinition_jurisdiction', blank=True)
    jurisdiction_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_SpecimenDefinition_patientPreparation(models.Model):
    SpecimenDefinition = models.ForeignKey(FHIR_SpecimenDefinition, related_name='SpecimenDefinition_patientPreparation', null=False, on_delete=models.CASCADE)
    BINDING_patientPreparation = 'TODO'
    patientPreparation_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_patientPreparation}, related_name='SpecimenDefinition_patientPreparation', blank=True)
    patientPreparation_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_SpecimenDefinition_collection(models.Model):
    SpecimenDefinition = models.ForeignKey(FHIR_SpecimenDefinition, related_name='SpecimenDefinition_collection', null=False, on_delete=models.CASCADE)
    BINDING_collection = 'TODO'
    collection_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_collection}, related_name='SpecimenDefinition_collection', blank=True)
    collection_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_SpecimenDefinition_typeTested(models.Model):
    SpecimenDefinition = models.ForeignKey(FHIR_SpecimenDefinition, related_name='SpecimenDefinition_typeTested', null=False, on_delete=models.CASCADE)
    isDerived = FHIR_primitive_BooleanField(null=True, blank=True, )
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='SpecimenDefinition_typeTested_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    class PreferenceChoices(models.TextChoices): PREFERRED = 'preferred', 'Preferred'; ALTERNATE = 'alternate', 'Alternate'; 
    preference = FHIR_primitive_CodeField(choices=PreferenceChoices.choices, null=True, blank=True, )
    requirement = FHIR_primitive_MarkdownField(null=True, blank=True, )
    retentionTime = models.OneToOneField("FHIR_GP_Quantity_Duration", related_name='SpecimenDefinition_typeTested_retentionTime', null=True, blank=True, on_delete=models.SET_NULL)
    singleUse = FHIR_primitive_BooleanField(null=True, blank=True, )

class FHIR_SpecimenDefinition_typeTested_container(models.Model):
    SpecimenDefinition_typeTested = models.ForeignKey(FHIR_SpecimenDefinition_typeTested, related_name='SpecimenDefinition_typeTested_container', null=False, on_delete=models.CASCADE)
    BINDING_material = 'TODO'
    material_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_material}, related_name='SpecimenDefinition_typeTested_container_material', blank=True)
    material_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='SpecimenDefinition_typeTested_container_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_cap = 'TODO'
    cap_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_cap}, related_name='SpecimenDefinition_typeTested_container_cap', blank=True)
    cap_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    capacity = models.OneToOneField("FHIR_GP_Quantity", related_name='SpecimenDefinition_typeTested_container_capacity', null=True, blank=True, on_delete=models.SET_NULL)
    minimumVolume = models.OneToOneField("FHIR_GP_Quantity", related_name='SpecimenDefinition_typeTested_container_minimumVolume', null=True, blank=True, on_delete=models.SET_NULL)
    minimumVolume = FHIR_primitive_StringField(null=True, blank=True, )
    preparation = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_SpecimenDefinition_typeTested_container_additive(models.Model):
    SpecimenDefinition_typeTested_container = models.ForeignKey(FHIR_SpecimenDefinition_typeTested_container, related_name='SpecimenDefinition_typeTested_container_additive', null=False, on_delete=models.CASCADE)
    BINDING_additive = 'TODO'
    additive_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_additive}, related_name='SpecimenDefinition_typeTested_container_additive_additive', blank=True)
    additive_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    additive = models.ForeignKey("FHIR_SubstanceDefinition", related_name="SpecimenDefinition_typeTested_container_additive_additive", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_SpecimenDefinition_typeTested_rejectionCriterion(models.Model):
    SpecimenDefinition_typeTested = models.ForeignKey(FHIR_SpecimenDefinition_typeTested, related_name='SpecimenDefinition_typeTested_rejectionCriterion', null=False, on_delete=models.CASCADE)
    BINDING_rejectionCriterion = 'TODO'
    rejectionCriterion_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_rejectionCriterion}, related_name='SpecimenDefinition_typeTested_rejectionCriterion', blank=True)
    rejectionCriterion_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_SpecimenDefinition_typeTested_handling(models.Model):
    SpecimenDefinition_typeTested = models.ForeignKey(FHIR_SpecimenDefinition_typeTested, related_name='SpecimenDefinition_typeTested_handling', null=False, on_delete=models.CASCADE)
    BINDING_temperatureQualifier = 'TODO'
    temperatureQualifier_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_temperatureQualifier}, related_name='SpecimenDefinition_typeTested_handling_temperatureQualifier', blank=True)
    temperatureQualifier_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    temperatureRange = models.OneToOneField("FHIR_GP_Range", related_name='SpecimenDefinition_typeTested_handling_temperatureRange', null=True, blank=True, on_delete=models.SET_NULL)
    maxDuration = models.OneToOneField("FHIR_GP_Quantity_Duration", related_name='SpecimenDefinition_typeTested_handling_maxDuration', null=True, blank=True, on_delete=models.SET_NULL)
    instruction = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_SpecimenDefinition_typeTested_testingDestination(models.Model):
    SpecimenDefinition_typeTested = models.ForeignKey(FHIR_SpecimenDefinition_typeTested, related_name='SpecimenDefinition_typeTested_testingDestination', null=False, on_delete=models.CASCADE)
    BINDING_testingDestination = 'TODO'
    testingDestination_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_testingDestination}, related_name='SpecimenDefinition_typeTested_testingDestination', blank=True)
    testingDestination_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    