from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_primitive import *
from ..FHIR_DataTypes.FHIR_metadata import *

class FHIR_PractitionerRole(models.Model):
    #identifier foreign key to this
    active = FHIR_primitive_BooleanField(null=True, blank=True)
    period = models.OneToOneField(FHIR_GP_Period, on_delete=models.CASCADE, null=True, blank=True)
    practitioner = models.ForeignKey('FHIR_Practitioner', related_name="practitioner_roles", null=True, blank=True, on_delete=models.SET_NULL)
    organization = models.ForeignKey('FHIR_Organization', related_name="organization_roles", null=True, blank=True, on_delete=models.SET_NULL)
    network = models.ManyToManyField('FHIR_Organization', related_name="network_practitioner_roles", blank=True)
    #code foreign key to this
    display = FHIR_primitive_StringField(max_length=255, null=True, blank=True)
    #specialty foreign key to this
    location = models.ManyToManyField('FHIR_Location', related_name="location_practitioner_roles", blank=True)
    healthcare_service = models.ManyToManyField('FHIR_HealthcareService', related_name="healthcare_service_practitioner_roles", blank=True)
    #contact foreign key to this
    #characteristic foreign key to this
    #communication foreign key to this
    availability = models.OneToOneField('FHIR_Availability', on_delete=models.CASCADE, null=True, blank=True)
    endpoints = models.ManyToManyField('FHIR_Endpoint', related_name="endpoint_practitioner_roles", blank=True)

    def __str__(self):
        return str(self.practitioner) + " roles"

class FHIR_PractitionerRole_Identifier(FHIR_GP_Identifier):
    practitioner_role = models.ForeignKey(FHIR_PractitionerRole, related_name="practitioner_role_identifiers", on_delete=models.CASCADE)

class FHIR_PractitionerRole_Code(models.Model):
    practitioner_role = models.ForeignKey(FHIR_PractitionerRole, related_name="practitioner_role_codes", on_delete=models.CASCADE)
    BINDING_RULE_CODE = "Practitioner Role"
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={'codings__binding_rule': BINDING_RULE_CODE})
    code_cctext = FHIR_primitive_StringField(max_length=255, null=True, blank=True)

class FHIR_PractitionerRole_Specialty(models.Model):
    practitioner_role = models.ForeignKey(FHIR_PractitionerRole, related_name="practitioner_role_specialties", on_delete=models.CASCADE)
    BINDING_RULE_SPECIALTY = "Practice Setting Code Value Set"
    specialty_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={'codings__binding_rule': BINDING_RULE_SPECIALTY})
    specialty_cctext = FHIR_primitive_StringField(max_length=255, null=True, blank=True)

class FHIR_PractitionerRole_Contact(FHIR_meta_ExtendedContactDetail):
    practitioner_role = models.ForeignKey(FHIR_PractitionerRole, related_name="practitioner_role_contacts", on_delete=models.CASCADE)

class FHIR_PractitionerRole_Characteristic(models.Model):
    practitioner_role = models.ForeignKey(FHIR_PractitionerRole, related_name="practitioner_role_characteristics", on_delete=models.CASCADE)
    BINDING_RULE_CHARACTERISTIC = "Service Mode"
    characteristic_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={'codings__binding_rule': BINDING_RULE_CHARACTERISTIC})
    characteristic_cctext = FHIR_primitive_StringField(max_length=255, null=True, blank=True)

class FHIR_PractitionerRole_Communication(models.Model):
    practitioner_role = models.ForeignKey(FHIR_PractitionerRole, related_name="practitioner_role_communications", on_delete=models.CASCADE)
    BINDING_RULE_LANGUAGE = "All Languages"
    language_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={'codings__binding_rule': BINDING_RULE_LANGUAGE})
    language_cctext = FHIR_primitive_StringField(max_length=255, null=True, blank=True)
