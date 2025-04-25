
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Practitioner(models.Model):
    active = FHIR_primitive_BooleanField(null=True, blank=True, )
    class GenderChoices(models.TextChoices): MALE = 'male', 'Male'; FEMALE = 'female', 'Female'; OTHER = 'other', 'Other'; UNKNOWN = 'unknown', 'Unknown'; 
    gender = FHIR_primitive_CodeField(choices=GenderChoices.choices, null=True, blank=True, )
    birthDate = FHIR_primitive_DateField(null=True, blank=True, )
    deceased = FHIR_primitive_BooleanField(null=True, blank=True, )
    deceased = FHIR_primitive_DateTimeField(null=True, blank=True, )

class FHIR_Practitioner_identifier(FHIR_GP_Identifier):
    Practitioner = models.ForeignKey(FHIR_Practitioner, related_name='Practitioner_identifier', null=False, on_delete=models.CASCADE)

class FHIR_Practitioner_name(FHIR_GP_HumanName):
    Practitioner = models.ForeignKey(FHIR_Practitioner, related_name='Practitioner_name', null=False, on_delete=models.CASCADE)

class FHIR_Practitioner_telecom(FHIR_GP_ContactPoint):
    Practitioner = models.ForeignKey(FHIR_Practitioner, related_name='Practitioner_telecom', null=False, on_delete=models.CASCADE)

class FHIR_Practitioner_address(FHIR_GP_Address):
    Practitioner = models.ForeignKey(FHIR_Practitioner, related_name='Practitioner_address', null=False, on_delete=models.CASCADE)

class FHIR_Practitioner_photo(FHIR_GP_Attachment):
    Practitioner = models.ForeignKey(FHIR_Practitioner, related_name='Practitioner_photo', null=False, on_delete=models.CASCADE)

class FHIR_Practitioner_qualification(models.Model):
    Practitioner = models.ForeignKey(FHIR_Practitioner, related_name='Practitioner_qualification', null=False, on_delete=models.CASCADE)
    BINDING_code = 'TODO'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='Practitioner_qualification_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_status = 'TODO'
    status_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_status}, related_name='Practitioner_qualification_status', blank=True)
    status_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    period = models.OneToOneField("FHIR_GP_Period", related_name='Practitioner_qualification_period', null=True, blank=True, on_delete=models.SET_NULL)
    issuer = models.ForeignKey("FHIR_Organization", related_name="Practitioner_qualification_issuer", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Practitioner_qualification_identifier(FHIR_GP_Identifier):
    Practitioner_qualification = models.ForeignKey(FHIR_Practitioner_qualification, related_name='Practitioner_qualification_identifier', null=False, on_delete=models.CASCADE)

class FHIR_Practitioner_communication(models.Model):
    Practitioner = models.ForeignKey(FHIR_Practitioner, related_name='Practitioner_communication', null=False, on_delete=models.CASCADE)
    BINDING_language = 'TODO'
    language_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_language}, related_name='Practitioner_communication_language', blank=True)
    language_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    preferred = FHIR_primitive_BooleanField(null=True, blank=True, )
