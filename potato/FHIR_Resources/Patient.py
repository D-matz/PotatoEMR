from ..FHIR_DataTypes.FHIR_primitive import *
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from .Practitioner import *
from .PractitionerRole import *
from .Organization import *
from .RelatedPerson import *

class FHIR_Patient(models.Model):
    #Identifier ForeignKey to this
    active = FHIR_primitive_BooleanField(null=True, help_text="Whether this patient's record is in active use")
    #name ForeignKey to this
    #telecom ForeignKey to this
    class GenderChoices(models.TextChoices): MALE = 'male', 'Male'; FEMALE = 'female', 'Female'; OTHER = 'other', 'Other'; UNKNOWN = 'unknown', 'Unknown'
    gender = FHIR_primitive_CodeField(max_length=10, choices=GenderChoices.choices, null=True, help_text="male | female | other | unknown")
    birth_date = models.OneToOneField(FHIR_primitive_DateField, on_delete=models.CASCADE, null=False, related_name="patient_birthDate")
    deceased_boolean = FHIR_primitive_BooleanField(null=True, help_text="Indicates if the individual is deceased")
    deceased_date_time = FHIR_primitive_DateTimeField() #help_text="DateTime of death if applicable"
    #address foreign key to this
    class MaritalStatus(models.TextChoices): ANNULLED = 'A', 'Annulled'; DIVORCED = 'D', 'Divorced'; INTERLOCUTORY = 'I', 'Interlocutory'; LEGALLY_SEPARATED = 'L', 'Legally Separated'; MARRIED = 'M', 'Married'; COMMON_LAW = 'C', 'Common Law'; POLYGAMOUS = 'P', 'Polygamous'; DOMESTIC_PARTNER = 'T', 'Domestic Partner'; UNMARRIED = 'U', 'Unmarried'; NEVER_MARRIED = 'S', 'Never Married'; WIDOWED = 'W', 'Widowed'; UNKNOWN = 'UNK', 'Unknown'
    marital_status = FHIR_primitive_CodeField(max_length=50, choices=MaritalStatus.choices, null=True, help_text="Marital (civil) status of a patient")
    multiple_birth_boolean = FHIR_primitive_BooleanField(null=True, help_text="Whether patient is part of a multiple birth")
    multiple_birth_integer = FHIR_primitive_PositiveIntField(null=True, blank=True, help_text="Order in the multiple birth")
    #photo foreign key to this
    #contact (backbone with multiple fields) foreign key to this
    #communication (backbone with multiple fields) foreign key to this
    #generalPactitioner foreign key to this
    managing_organization_reference = models.OneToOneField(FHIR_SP_Reference, on_delete=models.CASCADE, null=True, blank=True, related_name="patient_managingOrganization")
    managing_organization_foreignKey = models.ForeignKey(FHIR_Organization, on_delete=models.CASCADE, null=True, blank=True, related_name="patient_managingOrganization_organization")
    #link (backbone with multiple fields) foreign key to this
    def __str__(self):
        patient_names = [name.name.text for name in self.patient_names.all() if name.name.text]
        return ', '.join(patient_names) if patient_names else "Unnamed Patient"

class FHIR_Patient_Identifier(models.Model):
    identifier = models.OneToOneField(FHIR_GP_Identifier, related_name="patient_identifier", null=True, on_delete=models.SET_NULL)
    patient = models.ForeignKey(FHIR_Patient, related_name="patient_identifiers", on_delete=models.CASCADE)
class FHIR_Patient_Name(models.Model):
    name = models.OneToOneField(FHIR_GP_HumanName, related_name="patient_name", null=False, on_delete=models.CASCADE)
    patient = models.ForeignKey(FHIR_Patient, related_name="patient_names", on_delete=models.CASCADE)
    def __str__(self):
        if self.name.text:
            return self.name.text
        return "Unnamed patient"
class FHIR_Patient_Telecom(models.Model):
    telecom = models.OneToOneField(FHIR_GP_ContactPoint, related_name="patient_telecom", null=True, on_delete=models.SET_NULL)
    patient = models.ForeignKey(FHIR_Patient, related_name="patient_telecoms", on_delete=models.CASCADE)
class FHIR_Patient_Address(models.Model):
    address = models.OneToOneField(FHIR_GP_Address, related_name="patient_address", null=True, on_delete=models.SET_NULL)
    patient = models.ForeignKey(FHIR_Patient, related_name="patient_addresses", on_delete=models.CASCADE)
class FHIR_Patient_Photo(models.Model):
    photo = models.OneToOneField(FHIR_GP_Attachment, related_name="patient_photo", null=True, on_delete=models.SET_NULL)
    patient = models.ForeignKey(FHIR_Patient, related_name="patient_photos", on_delete=models.CASCADE)
class FHIR_Patient_Contact(models.Model):
    #relationship ForeignKey to this
    name = models.OneToOneField(FHIR_GP_HumanName, related_name="patient_contact_name", null=True, on_delete=models.SET_NULL)
    #telecom ForeignKey to this
    address = models.OneToOneField(FHIR_GP_Address, related_name="patient_contact_address", null=True, on_delete=models.SET_NULL)
    class Gender(models.TextChoices): MALE = 'male', 'Male'; FEMALE = 'female', 'Female'; OTHER = 'other', 'Other'; UNKNOWN = 'unknown', 'Unknown'
    gender = FHIR_primitive_CodeField(max_length=10, choices=Gender.choices, null=True, help_text="male | female | other | unknown")
    organization_reference = models.OneToOneField(FHIR_Organization, on_delete=models.CASCADE, null=True, blank=True)
    organization_foreigkey = models.ForeignKey(FHIR_Organization, on_delete=models.CASCADE, related_name="patient_contact_organization")
    period = models.OneToOneField(FHIR_GP_Period, null=True, blank=True, on_delete=models.CASCADE)
    patient = models.ForeignKey(FHIR_Patient, related_name="patient_contacts", on_delete=models.CASCADE)
class FHIR_Patient_Contact_Relationship(models.Model):
    relationship = models.OneToOneField(FHIR_GP_CodeableConcept, related_name="patient_contact_relationship", null=True, on_delete=models.SET_NULL)
    patient_contact = models.ForeignKey(FHIR_Patient_Contact, related_name="patient_contact_relationships", on_delete=models.CASCADE)
class FHIR_Patient_Contact_Telecom(models.Model):
    telecom = models.OneToOneField(FHIR_GP_ContactPoint, related_name="patient_conctact_telecom", null=True, on_delete=models.SET_NULL)
    patient_contact = models.ForeignKey(FHIR_Patient_Contact, related_name="patient_contact_telecoms", on_delete=models.CASCADE)
class FHIR_Patient_Communication(models.Model):
    language = models.OneToOneField(FHIR_GP_CodeableConcept, null=False, on_delete=models.CASCADE)
    preferred = FHIR_primitive_BooleanField()
    patient = models.ForeignKey(FHIR_Patient, related_name="patient_communications", on_delete=models.CASCADE)
class FHIR_Patient_GeneralPractitioner(models.Model):
    general_practitioner_reference = models.OneToOneField(FHIR_SP_Reference, on_delete=models.CASCADE, null=True, blank=True, related_name="patient_generalPractitioner")
    general_practitioner_practitioner = models.ForeignKey(FHIR_Practitioner, blank=True, related_name="patient_generalPractitioner_practitioner", on_delete=models.CASCADE)
    general_practitioner_practitionerRole = models.ForeignKey(FHIR_PractitionerRole, blank=True, related_name="patient_generalPractitioner_practitionerRole", on_delete=models.CASCADE)
    general_practitioner_organization = models.ForeignKey(FHIR_Organization, blank=True, related_name="patient_generalPractitioner_organization", on_delete=models.CASCADE)
class FHIR_Patient_Link(models.Model):
    class LinkType(models.TextChoices):REPLACED_BY = 'replaced-by', 'Replaced by'; REPLACES = 'replaces', 'Replaces'; REFER = 'refer', 'Refer'; SEEALSO = 'seealso', 'See also'
    link_type = FHIR_primitive_CodeField(max_length=20, choices=LinkType.choices, null=False)
    other_reference = models.OneToOneField(FHIR_SP_Reference, on_delete=models.CASCADE, null=True, blank=True, related_name="link_other")
    other_patient_foreignKey = models.ForeignKey(FHIR_Patient, on_delete=models.CASCADE, related_name="link_other_patient")
    other_relatedPerson_foreignKey = models.ForeignKey(FHIR_RelatedPerson, on_delete=models.CASCADE, related_name="link_other_relatedPerson")
