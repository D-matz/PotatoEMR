from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Practitioner(models.Model):
    # identifiers are added as a foreign key relationship
    active = FHIR_primitive_BooleanField(null=True, blank=True)
    # names are added as a foreign key relationship
    # telecoms are added as a foreign key relationship
    class GenderChoices(models.TextChoices): MALE = 'male', 'Male'; FEMALE = 'female', 'Female'; OTHER = 'other', 'Other'; UNKNOWN = 'unknown', 'Unknown'
    gender = FHIR_primitive_CodeField(max_length=10, choices=GenderChoices.choices, null=True, blank=True)
    birthDate = FHIR_primitive_DateField(null=True, blank=True)
    deceasedBoolean = FHIR_primitive_BooleanField(null=True, blank=True)
    deceasedDateTime = FHIR_primitive_DateTimeField(null=True, blank=True)

    # addresses are added as a foreign key relationship
    # photos are added as a foreign key relationship
    # qualifications are added as a foreign key relationship
    # communications are added as a foreign key relationship

    def __str__(self):
        return str(self.practitioner_names.first())

class FHIR_Practitioner_Identifier(FHIR_GP_Identifier):
    practitioner = models.ForeignKey(FHIR_Practitioner, related_name="practitioner_identifiers", on_delete=models.CASCADE)

class FHIR_Practitioner_Name(FHIR_GP_HumanName):
    practitioner = models.ForeignKey(FHIR_Practitioner, related_name="practitioner_names", on_delete=models.CASCADE)

class FHIR_Practitioner_Telecom(FHIR_GP_ContactPoint):
    practitioner = models.ForeignKey(FHIR_Practitioner, related_name="practitioner_telecoms", on_delete=models.CASCADE)

class FHIR_Practitioner_Address(FHIR_GP_Address):
    practitioner = models.ForeignKey(FHIR_Practitioner, related_name="practitioner_addresses", on_delete=models.CASCADE)

class FHIR_Practitioner_Photo(FHIR_GP_Attachment):
    practitioner = models.ForeignKey(FHIR_Practitioner, related_name="practitioner_photos", on_delete=models.CASCADE)

class FHIR_Practitioner_Qualification(models.Model):
    practitioner = models.ForeignKey(FHIR_Practitioner, related_name="practitioner_qualifications", on_delete=models.CASCADE)
    # identifiers are added as a foreign key relationship

    BINDING_RULE_CODE = "hl7VS-degreeLicenseCertificate"
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={'codings__binding_rule': BINDING_RULE_CODE})
    code_cctext = FHIR_primitive_StringField(max_length=255, null=True, blank=True)

    BINDING_RULE_STATUS = "Qualification Status"
    status_cc = models.ManyToManyField(FHIR_GP_Coding,
                                     limit_choices_to={'codings__binding_rule': BINDING_RULE_STATUS},
                                     related_name="qualification_status",
                                     blank=True)
    status_cctext = FHIR_primitive_StringField(max_length=255, null=True, blank=True)

    period = models.OneToOneField(FHIR_GP_Period, on_delete=models.CASCADE, null=True, blank=True)
    issuer = models.ForeignKey('FHIR_Organization', related_name="qualification_issuers", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Practitioner_Qualification_Identifier(FHIR_GP_Identifier):
    qualification = models.ForeignKey(FHIR_Practitioner_Qualification, related_name="qualification_identifiers", on_delete=models.CASCADE)

class FHIR_Practitioner_Communication(models.Model):
    practitioner = models.ForeignKey(FHIR_Practitioner, related_name="practitioner_communications", on_delete=models.CASCADE)

    BINDING_RULE_LANGUAGE = "All Languages"
    language_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={'codings__binding_rule': BINDING_RULE_LANGUAGE})
    language_cctext = FHIR_primitive_StringField(max_length=255, null=True, blank=True)

    preferred = FHIR_primitive_BooleanField(null=True, blank=True)
