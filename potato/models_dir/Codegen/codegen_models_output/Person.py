#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Person(models.Model):
    active = FHIR_primitive_BooleanField(null=True, blank=True, )
    class GenderChoices(models.TextChoices): MALE = 'male', 'Male'; FEMALE = 'female', 'Female'; OTHER = 'other', 'Other'; UNKNOWN = 'unknown', 'Unknown'; 
    gender = FHIR_primitive_CodeField(choices=GenderChoices.choices, null=True, blank=True, )
    birthDate = FHIR_primitive_DateField(null=True, blank=True, )
    deceased = FHIR_primitive_BooleanField(null=True, blank=True, )
    deceased = FHIR_primitive_DateTimeField(null=True, blank=True, )
    BINDING_maritalStatus = "TODO"
    maritalStatus_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_maritalStatus}, related_name='Person_maritalStatus', blank=True)
    maritalStatus_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    managingOrganization = models.ForeignKey("FHIR_Organization", related_name="Person_managingOrganization", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Person_identifier(FHIR_GP_Identifier):
    Person = models.ForeignKey(FHIR_Person, related_name='Person_identifier', null=False, on_delete=models.CASCADE)

class FHIR_Person_name(FHIR_GP_HumanName):
    Person = models.ForeignKey(FHIR_Person, related_name='Person_name', null=False, on_delete=models.CASCADE)

class FHIR_Person_telecom(FHIR_GP_ContactPoint):
    Person = models.ForeignKey(FHIR_Person, related_name='Person_telecom', null=False, on_delete=models.CASCADE)

class FHIR_Person_address(FHIR_GP_Address):
    Person = models.ForeignKey(FHIR_Person, related_name='Person_address', null=False, on_delete=models.CASCADE)

class FHIR_Person_photo(FHIR_GP_Attachment):
    Person = models.ForeignKey(FHIR_Person, related_name='Person_photo', null=False, on_delete=models.CASCADE)

class FHIR_Person_communication(models.Model):
    Person = models.ForeignKey(FHIR_Person, related_name='Person_communication', null=False, on_delete=models.CASCADE)
    BINDING_language = "TODO"
    language_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_language}, related_name='Person_communication_language', blank=True)
    language_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    preferred = FHIR_primitive_BooleanField(null=True, blank=True, )

class FHIR_Person_link(models.Model):
    Person = models.ForeignKey(FHIR_Person, related_name='Person_link', null=False, on_delete=models.CASCADE)
    target_Patient = models.ForeignKey("FHIR_Patient", related_name="Person_link_target", null=True, blank=True, on_delete=models.SET_NULL)
    target_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="Person_link_target", null=True, blank=True, on_delete=models.SET_NULL)
    target_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="Person_link_target", null=True, blank=True, on_delete=models.SET_NULL)
    target_Person = models.ForeignKey("FHIR_Person", related_name="Person_link_target", null=True, blank=True, on_delete=models.SET_NULL)
    class AssuranceChoices(models.TextChoices): LEVEL1 = 'level1', 'Level1'; LEVEL2 = 'level2', 'Level2'; LEVEL3 = 'level3', 'Level3'; LEVEL4 = 'level4', 'Level4'; 
    assurance = FHIR_primitive_CodeField(choices=AssuranceChoices.choices, null=True, blank=True, )
