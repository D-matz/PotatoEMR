#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Patient(models.Model):
    active = FHIR_primitive_BooleanField(null=True, blank=True, )
    class GenderChoices(models.TextChoices): MALE = 'male', 'Male'; FEMALE = 'female', 'Female'; OTHER = 'other', 'Other'; UNKNOWN = 'unknown', 'Unknown'; 
    gender = FHIR_primitive_CodeField(choices=GenderChoices.choices, null=True, blank=True, )
    birthDate = FHIR_primitive_DateField(null=True, blank=True, )
    deceased = FHIR_primitive_BooleanField(null=True, blank=True, )
    deceased = FHIR_primitive_DateTimeField(null=True, blank=True, )
    BINDING_maritalStatus = "TODO"
    maritalStatus_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_maritalStatus}, related_name='Patient_maritalStatus', blank=True)
    maritalStatus_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    multipleBirth = FHIR_primitive_BooleanField(null=True, blank=True, )
    generalPractitioner_Organization = models.ManyToManyField("FHIR_Organization", related_name="Patient_generalPractitioner", blank=True)
    generalPractitioner_Practitioner = models.ManyToManyField("FHIR_Practitioner", related_name="Patient_generalPractitioner", blank=True)
    generalPractitioner_PractitionerRole = models.ManyToManyField("FHIR_PractitionerRole", related_name="Patient_generalPractitioner", blank=True)
    managingOrganization = models.ForeignKey("FHIR_Organization", related_name="Patient_managingOrganization", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Patient_identifier(FHIR_GP_Identifier):
    Patient = models.ForeignKey(FHIR_Patient, related_name='Patient_identifier', null=False, on_delete=models.CASCADE)

class FHIR_Patient_name(FHIR_GP_HumanName):
    Patient = models.ForeignKey(FHIR_Patient, related_name='Patient_name', null=False, on_delete=models.CASCADE)

class FHIR_Patient_telecom(FHIR_GP_ContactPoint):
    Patient = models.ForeignKey(FHIR_Patient, related_name='Patient_telecom', null=False, on_delete=models.CASCADE)

class FHIR_Patient_address(FHIR_GP_Address):
    Patient = models.ForeignKey(FHIR_Patient, related_name='Patient_address', null=False, on_delete=models.CASCADE)

class FHIR_Patient_photo(FHIR_GP_Attachment):
    Patient = models.ForeignKey(FHIR_Patient, related_name='Patient_photo', null=False, on_delete=models.CASCADE)

class FHIR_Patient_contact(models.Model):
    Patient = models.ForeignKey(FHIR_Patient, related_name='Patient_contact', null=False, on_delete=models.CASCADE)
    name = models.OneToOneField("FHIR_GP_HumanName", related_name='Patient_contact_name', null=True, blank=True, on_delete=models.SET_NULL)
    address = models.OneToOneField("FHIR_GP_Address", related_name='Patient_contact_address', null=True, blank=True, on_delete=models.SET_NULL)
    class GenderChoices(models.TextChoices): MALE = 'male', 'Male'; FEMALE = 'female', 'Female'; OTHER = 'other', 'Other'; UNKNOWN = 'unknown', 'Unknown'; 
    gender = FHIR_primitive_CodeField(choices=GenderChoices.choices, null=True, blank=True, )
    organization = models.ForeignKey("FHIR_Organization", related_name="Patient_contact_organization", null=True, blank=True, on_delete=models.SET_NULL)
    period = models.OneToOneField("FHIR_GP_Period", related_name='Patient_contact_period', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Patient_contact_relationship(models.Model):
    Patient_contact = models.ForeignKey(FHIR_Patient_contact, related_name='Patient_contact_relationship', null=False, on_delete=models.CASCADE)
    BINDING_relationship = "TODO"
    relationship_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_relationship}, related_name='Patient_contact_relationship', blank=True)
    relationship_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Patient_contact_role(models.Model):
    Patient_contact = models.ForeignKey(FHIR_Patient_contact, related_name='Patient_contact_role', null=False, on_delete=models.CASCADE)
    BINDING_role = "TODO"
    role_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_role}, related_name='Patient_contact_role', blank=True)
    role_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Patient_contact_additionalName(FHIR_GP_HumanName):
    Patient_contact = models.ForeignKey(FHIR_Patient_contact, related_name='Patient_contact_additionalName', null=False, on_delete=models.CASCADE)

class FHIR_Patient_contact_telecom(FHIR_GP_ContactPoint):
    Patient_contact = models.ForeignKey(FHIR_Patient_contact, related_name='Patient_contact_telecom', null=False, on_delete=models.CASCADE)

class FHIR_Patient_contact_additionalAddress(FHIR_GP_Address):
    Patient_contact = models.ForeignKey(FHIR_Patient_contact, related_name='Patient_contact_additionalAddress', null=False, on_delete=models.CASCADE)

class FHIR_Patient_communication(models.Model):
    Patient = models.ForeignKey(FHIR_Patient, related_name='Patient_communication', null=False, on_delete=models.CASCADE)
    BINDING_language = "TODO"
    language_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_language}, related_name='Patient_communication_language', blank=True)
    language_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    preferred = FHIR_primitive_BooleanField(null=True, blank=True, )

class FHIR_Patient_link(models.Model):
    Patient = models.ForeignKey(FHIR_Patient, related_name='Patient_link', null=False, on_delete=models.CASCADE)
    other_Patient = models.ForeignKey("FHIR_Patient", related_name="Patient_link_other", null=True, blank=True, on_delete=models.SET_NULL)
    other_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="Patient_link_other", null=True, blank=True, on_delete=models.SET_NULL)
    class TypeChoices(models.TextChoices): REPLACED_BY = 'replaced-by', 'Replaced-by'; REPLACES = 'replaces', 'Replaces'; REFER = 'refer', 'Refer'; SEEALSO = 'seealso', 'Seealso'; 
    type = FHIR_primitive_CodeField(choices=TypeChoices.choices, null=True, blank=True, )
