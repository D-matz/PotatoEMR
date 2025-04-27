#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_DeviceAssociation(models.Model):
    device = models.ForeignKey("FHIR_Device", related_name="DeviceAssociation_device", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_status = "TODO"
    status_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_status}, related_name='DeviceAssociation_status', blank=True)
    status_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    subject_Patient = models.ForeignKey("FHIR_Patient", related_name="DeviceAssociation_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Group = models.ForeignKey("FHIR_Group", related_name="DeviceAssociation_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Organization = models.ForeignKey("FHIR_Organization", related_name="DeviceAssociation_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="DeviceAssociation_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="DeviceAssociation_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="DeviceAssociation_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Device = models.ForeignKey("FHIR_Device", related_name="DeviceAssociation_subject", null=True, blank=True, on_delete=models.SET_NULL)
    bodyStructure = models.ForeignKey("FHIR_BodyStructure", related_name="DeviceAssociation_bodyStructure", null=True, blank=True, on_delete=models.SET_NULL)
    period = models.OneToOneField("FHIR_GP_Period", related_name='DeviceAssociation_period', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_DeviceAssociation_identifier(FHIR_GP_Identifier):
    DeviceAssociation = models.ForeignKey(FHIR_DeviceAssociation, related_name='DeviceAssociation_identifier', null=False, on_delete=models.CASCADE)

class FHIR_DeviceAssociation_relationship(models.Model):
    DeviceAssociation = models.ForeignKey(FHIR_DeviceAssociation, related_name='DeviceAssociation_relationship', null=False, on_delete=models.CASCADE)
    BINDING_relationship = "TODO"
    relationship_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_relationship}, related_name='DeviceAssociation_relationship', blank=True)
    relationship_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_DeviceAssociation_statusReason(models.Model):
    DeviceAssociation = models.ForeignKey(FHIR_DeviceAssociation, related_name='DeviceAssociation_statusReason', null=False, on_delete=models.CASCADE)
    BINDING_statusReason = "TODO"
    statusReason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_statusReason}, related_name='DeviceAssociation_statusReason', blank=True)
    statusReason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_DeviceAssociation_operation(models.Model):
    DeviceAssociation = models.ForeignKey(FHIR_DeviceAssociation, related_name='DeviceAssociation_operation', null=False, on_delete=models.CASCADE)
    BINDING_status = "TODO"
    status_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_status}, related_name='DeviceAssociation_operation_status', blank=True)
    status_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    operator_Patient = models.ManyToManyField("FHIR_Patient", related_name="DeviceAssociation_operation_operator", blank=True)
    operator_Practitioner = models.ManyToManyField("FHIR_Practitioner", related_name="DeviceAssociation_operation_operator", blank=True)
    operator_RelatedPerson = models.ManyToManyField("FHIR_RelatedPerson", related_name="DeviceAssociation_operation_operator", blank=True)
    period = models.OneToOneField("FHIR_GP_Period", related_name='DeviceAssociation_operation_period', null=True, blank=True, on_delete=models.SET_NULL)
