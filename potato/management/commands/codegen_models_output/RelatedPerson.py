
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_RelatedPerson(models.Model):
    active = FHIR_primitive_BooleanField(null=True, blank=True, )
    patient = models.ForeignKey("FHIR_Patient", related_name="RelatedPerson_patient", null=True, blank=True, on_delete=models.SET_NULL)
    class GenderChoices(models.TextChoices): MALE = 'male', 'Male'; FEMALE = 'female', 'Female'; OTHER = 'other', 'Other'; UNKNOWN = 'unknown', 'Unknown'; 
    gender = FHIR_primitive_CodeField(choices=GenderChoices.choices, null=True, blank=True, )
    birthDate = FHIR_primitive_DateField(null=True, blank=True, )
    period = models.OneToOneField("FHIR_GP_Period", related_name='RelatedPerson_period', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_RelatedPerson_identifier(FHIR_GP_Identifier):
    RelatedPerson = models.ForeignKey(FHIR_RelatedPerson, related_name='RelatedPerson_identifier', null=False, on_delete=models.CASCADE)

class FHIR_RelatedPerson_relationship(models.Model):
    RelatedPerson = models.ForeignKey(FHIR_RelatedPerson, related_name='RelatedPerson_relationship', null=False, on_delete=models.CASCADE)
    BINDING_relationship = 'TODO'
    relationship_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_relationship}, related_name='RelatedPerson_relationship', blank=True)
    relationship_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_RelatedPerson_role(models.Model):
    RelatedPerson = models.ForeignKey(FHIR_RelatedPerson, related_name='RelatedPerson_role', null=False, on_delete=models.CASCADE)
    BINDING_role = 'TODO'
    role_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_role}, related_name='RelatedPerson_role', blank=True)
    role_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_RelatedPerson_name(FHIR_GP_HumanName):
    RelatedPerson = models.ForeignKey(FHIR_RelatedPerson, related_name='RelatedPerson_name', null=False, on_delete=models.CASCADE)

class FHIR_RelatedPerson_telecom(FHIR_GP_ContactPoint):
    RelatedPerson = models.ForeignKey(FHIR_RelatedPerson, related_name='RelatedPerson_telecom', null=False, on_delete=models.CASCADE)

class FHIR_RelatedPerson_address(FHIR_GP_Address):
    RelatedPerson = models.ForeignKey(FHIR_RelatedPerson, related_name='RelatedPerson_address', null=False, on_delete=models.CASCADE)

class FHIR_RelatedPerson_photo(FHIR_GP_Attachment):
    RelatedPerson = models.ForeignKey(FHIR_RelatedPerson, related_name='RelatedPerson_photo', null=False, on_delete=models.CASCADE)

class FHIR_RelatedPerson_communication(models.Model):
    RelatedPerson = models.ForeignKey(FHIR_RelatedPerson, related_name='RelatedPerson_communication', null=False, on_delete=models.CASCADE)
    BINDING_language = 'TODO'
    language_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_language}, related_name='RelatedPerson_communication_language', blank=True)
    language_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    preferred = FHIR_primitive_BooleanField(null=True, blank=True, )
