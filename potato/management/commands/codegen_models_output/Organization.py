
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Organization(models.Model):
    active = FHIR_primitive_BooleanField(null=True, blank=True, )
    name = FHIR_primitive_StringField(null=True, blank=True, )
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    partOf = models.ForeignKey("FHIR_Organization", related_name="Organization_partOf", null=True, blank=True, on_delete=models.SET_NULL)
    endpoint = models.ManyToManyField("FHIR_Endpoint", related_name="Organization_endpoint", blank=True)

class FHIR_Organization_identifier(FHIR_GP_Identifier):
    Organization = models.ForeignKey(FHIR_Organization, related_name='Organization_identifier', null=False, on_delete=models.CASCADE)

class FHIR_Organization_type(models.Model):
    Organization = models.ForeignKey(FHIR_Organization, related_name='Organization_type', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Organization_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Organization_alias(models.Model):
    Organization = models.ForeignKey(FHIR_Organization, related_name='Organization_alias', null=False, on_delete=models.CASCADE)
    
    alias = FHIR_primitive_StringField(null=True, blank=True, )
    
class FHIR_Organization_contact(FHIR_meta_ExtendedContactDetail):
    Organization = models.ForeignKey(FHIR_Organization, related_name='Organization_contact', null=False, on_delete=models.CASCADE)

class FHIR_Organization_qualification(models.Model):
    Organization = models.ForeignKey(FHIR_Organization, related_name='Organization_qualification', null=False, on_delete=models.CASCADE)
    BINDING_code = 'TODO'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='Organization_qualification_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_status = 'TODO'
    status_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_status}, related_name='Organization_qualification_status', blank=True)
    status_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    period = models.OneToOneField("FHIR_GP_Period", related_name='Organization_qualification_period', null=True, blank=True, on_delete=models.SET_NULL)
    issuer = models.ForeignKey("FHIR_Organization", related_name="Organization_qualification_issuer", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Organization_qualification_identifier(FHIR_GP_Identifier):
    Organization_qualification = models.ForeignKey(FHIR_Organization_qualification, related_name='Organization_qualification_identifier', null=False, on_delete=models.CASCADE)
