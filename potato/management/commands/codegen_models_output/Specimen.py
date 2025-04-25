
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Specimen(models.Model):
    accessionIdentifier = models.OneToOneField("FHIR_GP_Identifier", related_name='Specimen_accessionIdentifier', null=True, blank=True, on_delete=models.SET_NULL)
    class StatusChoices(models.TextChoices): AVAILABLE = 'available', 'Available'; UNAVAILABLE = 'unavailable', 'Unavailable'; UNSATISFACTORY = 'unsatisfactory', 'Unsatisfactory'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Specimen_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    subject_Patient = models.ForeignKey("FHIR_Patient", related_name="Specimen_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Group = models.ForeignKey("FHIR_Group", related_name="Specimen_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Device = models.ForeignKey("FHIR_Device", related_name="Specimen_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_BiologicallyDerivedProduct = models.ForeignKey("FHIR_BiologicallyDerivedProduct", related_name="Specimen_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Substance = models.ForeignKey("FHIR_Substance", related_name="Specimen_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Location = models.ForeignKey("FHIR_Location", related_name="Specimen_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_NutritionProduct = models.ForeignKey("FHIR_NutritionProduct", related_name="Specimen_subject", null=True, blank=True, on_delete=models.SET_NULL)
    receivedTime = FHIR_primitive_DateTimeField(null=True, blank=True, )
    parent = models.ManyToManyField("FHIR_Specimen", related_name="Specimen_parent", blank=True)
    request = models.ManyToManyField("FHIR_ServiceRequest", related_name="Specimen_request", blank=True)
    class CombinedChoices(models.TextChoices): GROUPED = 'grouped', 'Grouped'; POOLED = 'pooled', 'Pooled'; 
    combined = FHIR_primitive_CodeField(choices=CombinedChoices.choices, null=True, blank=True, )

class FHIR_Specimen_identifier(FHIR_GP_Identifier):
    Specimen = models.ForeignKey(FHIR_Specimen, related_name='Specimen_identifier', null=False, on_delete=models.CASCADE)

class FHIR_Specimen_role(models.Model):
    Specimen = models.ForeignKey(FHIR_Specimen, related_name='Specimen_role', null=False, on_delete=models.CASCADE)
    BINDING_role = 'TODO'
    role_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_role}, related_name='Specimen_role', blank=True)
    role_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Specimen_feature(models.Model):
    Specimen = models.ForeignKey(FHIR_Specimen, related_name='Specimen_feature', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Specimen_feature_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    description = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_Specimen_collection(models.Model):
    Specimen = models.ForeignKey(FHIR_Specimen, related_name='Specimen_collection', null=False, on_delete=models.CASCADE)
    collector_Organization = models.ForeignKey("FHIR_Organization", related_name="Specimen_collection_collector", null=True, blank=True, on_delete=models.SET_NULL)
    collector_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="Specimen_collection_collector", null=True, blank=True, on_delete=models.SET_NULL)
    collector_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="Specimen_collection_collector", null=True, blank=True, on_delete=models.SET_NULL)
    collector_Patient = models.ForeignKey("FHIR_Patient", related_name="Specimen_collection_collector", null=True, blank=True, on_delete=models.SET_NULL)
    collector_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="Specimen_collection_collector", null=True, blank=True, on_delete=models.SET_NULL)
    collected = FHIR_primitive_DateTimeField(null=True, blank=True, )
    collected = models.OneToOneField("FHIR_GP_Period", related_name='Specimen_collection_collected', null=True, blank=True, on_delete=models.SET_NULL)
    duration = models.OneToOneField("FHIR_GP_Quantity_Duration", related_name='Specimen_collection_duration', null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='Specimen_collection_quantity', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_method = 'TODO'
    method_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_method}, related_name='Specimen_collection_method', blank=True)
    method_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_device = 'TODO'
    device_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_device}, related_name='Specimen_collection_device', blank=True)
    device_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    device_Device_ref = models.ForeignKey("FHIR_Device", related_name="Specimen_collection_device", null=True, blank=True, on_delete=models.SET_NULL)
    procedure = models.ForeignKey("FHIR_Procedure", related_name="Specimen_collection_procedure", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_bodySite = 'TODO'
    bodySite_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_bodySite}, related_name='Specimen_collection_bodySite', blank=True)
    bodySite_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    bodySite_BodyStructure_ref = models.ForeignKey("FHIR_BodyStructure", related_name="Specimen_collection_bodySite", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_fastingStatus = 'TODO'
    fastingStatus_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_fastingStatus}, related_name='Specimen_collection_fastingStatus', blank=True)
    fastingStatus_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    fastingStatus = models.OneToOneField("FHIR_GP_Quantity_Duration", related_name='Specimen_collection_fastingStatus', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Specimen_processing(models.Model):
    Specimen = models.ForeignKey(FHIR_Specimen, related_name='Specimen_processing', null=False, on_delete=models.CASCADE)
    description = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_method = 'TODO'
    method_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_method}, related_name='Specimen_processing_method', blank=True)
    method_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    performer_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="Specimen_processing_performer", null=True, blank=True, on_delete=models.SET_NULL)
    performer_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="Specimen_processing_performer", null=True, blank=True, on_delete=models.SET_NULL)
    performer_Patient = models.ForeignKey("FHIR_Patient", related_name="Specimen_processing_performer", null=True, blank=True, on_delete=models.SET_NULL)
    performer_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="Specimen_processing_performer", null=True, blank=True, on_delete=models.SET_NULL)
    device = models.ForeignKey("FHIR_Device", related_name="Specimen_processing_device", null=True, blank=True, on_delete=models.SET_NULL)
    additive = models.ManyToManyField("FHIR_Substance", related_name="Specimen_processing_additive", blank=True)
    time = FHIR_primitive_DateTimeField(null=True, blank=True, )
    time = models.OneToOneField("FHIR_GP_Period", related_name='Specimen_processing_time', null=True, blank=True, on_delete=models.SET_NULL)
    time = models.OneToOneField("FHIR_GP_Quantity_Duration", related_name='Specimen_processing_time', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Specimen_container(models.Model):
    Specimen = models.ForeignKey(FHIR_Specimen, related_name='Specimen_container', null=False, on_delete=models.CASCADE)
    device = models.ForeignKey("FHIR_Device", related_name="Specimen_container_device", null=True, blank=True, on_delete=models.SET_NULL)
    specimenQuantity = models.OneToOneField("FHIR_GP_Quantity", related_name='Specimen_container_specimenQuantity', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Specimen_condition(models.Model):
    Specimen = models.ForeignKey(FHIR_Specimen, related_name='Specimen_condition', null=False, on_delete=models.CASCADE)
    BINDING_condition = 'TODO'
    condition_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_condition}, related_name='Specimen_condition', blank=True)
    condition_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Specimen_note(FHIR_GP_Annotation):
    Specimen = models.ForeignKey(FHIR_Specimen, related_name='Specimen_note', null=False, on_delete=models.CASCADE)
