#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Device(models.Model):
    definition = models.ForeignKey("FHIR_DeviceDefinition", related_name="Device_definition", null=True, blank=True, on_delete=models.SET_NULL)
    class StatusChoices(models.TextChoices): ACTIVE = 'active', 'Active'; INACTIVE = 'inactive', 'Inactive'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    BINDING_availabilityStatus = "TODO"
    availabilityStatus_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_availabilityStatus}, related_name='Device_availabilityStatus', blank=True)
    availabilityStatus_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    biologicalSourceEvent = models.OneToOneField("FHIR_GP_Identifier", related_name='Device_biologicalSourceEvent', null=True, blank=True, on_delete=models.SET_NULL)
    manufacturer = FHIR_primitive_StringField(null=True, blank=True, )
    manufactureDate = FHIR_primitive_DateTimeField(null=True, blank=True, )
    expirationDate = FHIR_primitive_DateTimeField(null=True, blank=True, )
    lotNumber = FHIR_primitive_StringField(null=True, blank=True, )
    serialNumber = FHIR_primitive_StringField(null=True, blank=True, )
    modelNumber = FHIR_primitive_StringField(null=True, blank=True, )
    partNumber = FHIR_primitive_StringField(null=True, blank=True, )
    location = models.ForeignKey("FHIR_Location", related_name="Device_location", null=True, blank=True, on_delete=models.SET_NULL)
    parent = models.ForeignKey("FHIR_Device", related_name="Device_parent", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Device_identifier(FHIR_GP_Identifier):
    Device = models.ForeignKey(FHIR_Device, related_name='Device_identifier', null=False, on_delete=models.CASCADE)

class FHIR_Device_udiCarrier(models.Model):
    Device = models.ForeignKey(FHIR_Device, related_name='Device_udiCarrier', null=False, on_delete=models.CASCADE)
    deviceIdentifier = FHIR_primitive_StringField(null=True, blank=True, )
    deviceIdentifierSystem = FHIR_primitive_URIField(null=True, blank=True, )
    issuer = FHIR_primitive_URIField(null=True, blank=True, )
    jurisdiction = FHIR_primitive_URIField(null=True, blank=True, )
    carrierAIDC = FHIR_primitive_Base64BinaryField(null=True, blank=True, )
    carrierHRF = FHIR_primitive_StringField(null=True, blank=True, )
    class EntrytypeChoices(models.TextChoices): BARCODE = 'barcode', 'Barcode'; RFID = 'rfid', 'Rfid'; MANUAL = 'manual', 'Manual'; CARD = 'card', 'Card'; SELF_REPORTED = 'self-reported', 'Self-reported'; ELECTRONIC_TRANSMISSION = 'electronic-transmission', 'Electronic-transmission'; UNKNOWN = 'unknown', 'Unknown'; 
    entryType = FHIR_primitive_CodeField(choices=EntrytypeChoices.choices, null=True, blank=True, )

class FHIR_Device_name(models.Model):
    Device = models.ForeignKey(FHIR_Device, related_name='Device_name', null=False, on_delete=models.CASCADE)
    value = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Device_name_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    display = FHIR_primitive_BooleanField(null=True, blank=True, )

class FHIR_Device_category(models.Model):
    Device = models.ForeignKey(FHIR_Device, related_name='Device_category', null=False, on_delete=models.CASCADE)
    BINDING_category = "TODO"
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='Device_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Device_type(models.Model):
    Device = models.ForeignKey(FHIR_Device, related_name='Device_type', null=False, on_delete=models.CASCADE)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Device_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Device_deviceVersion(models.Model):
    Device = models.ForeignKey(FHIR_Device, related_name='Device_deviceVersion', null=False, on_delete=models.CASCADE)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Device_deviceVersion_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    component = models.OneToOneField("FHIR_GP_Identifier", related_name='Device_deviceVersion_component', null=True, blank=True, on_delete=models.SET_NULL)
    installDate = FHIR_primitive_DateTimeField(null=True, blank=True, )
    value = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_Device_conformsTo(models.Model):
    Device = models.ForeignKey(FHIR_Device, related_name='Device_conformsTo', null=False, on_delete=models.CASCADE)
    BINDING_category = "TODO"
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='Device_conformsTo_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_specification = "TODO"
    specification_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_specification}, related_name='Device_conformsTo_specification', blank=True)
    specification_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    version = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_Device_property(models.Model):
    Device = models.ForeignKey(FHIR_Device, related_name='Device_property', null=False, on_delete=models.CASCADE)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Device_property_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value = models.OneToOneField("FHIR_GP_Quantity", related_name='Device_property_value', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_value = "TODO"
    value_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_value}, related_name='Device_property_value', blank=True)
    value_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value = FHIR_primitive_StringField(null=True, blank=True, )
    value = FHIR_primitive_BooleanField(null=True, blank=True, )
    value = models.OneToOneField("FHIR_GP_Range", related_name='Device_property_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_Attachment", related_name='Device_property_value', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Device_additive(models.Model):
    Device = models.ForeignKey(FHIR_Device, related_name='Device_additive', null=False, on_delete=models.CASCADE)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Device_additive_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    type_Substance_ref = models.ForeignKey("FHIR_Substance", related_name="Device_additive_type_Substance", null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='Device_additive_quantity', null=True, blank=True, on_delete=models.SET_NULL)
    performer_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="Device_additive_performer", null=True, blank=True, on_delete=models.SET_NULL)
    performer_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="Device_additive_performer", null=True, blank=True, on_delete=models.SET_NULL)
    performer_Organization = models.ForeignKey("FHIR_Organization", related_name="Device_additive_performer", null=True, blank=True, on_delete=models.SET_NULL)
    performer_Patient = models.ForeignKey("FHIR_Patient", related_name="Device_additive_performer", null=True, blank=True, on_delete=models.SET_NULL)
    performer_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="Device_additive_performer", null=True, blank=True, on_delete=models.SET_NULL)
    performed = FHIR_primitive_DateTimeField(null=True, blank=True, )

class FHIR_Device_contact(FHIR_GP_ContactPoint):
    Device = models.ForeignKey(FHIR_Device, related_name='Device_contact', null=False, on_delete=models.CASCADE)

class FHIR_Device_note(FHIR_GP_Annotation):
    Device = models.ForeignKey(FHIR_Device, related_name='Device_note', null=False, on_delete=models.CASCADE)

class FHIR_Device_safety(models.Model):
    Device = models.ForeignKey(FHIR_Device, related_name='Device_safety', null=False, on_delete=models.CASCADE)
    BINDING_safety = "TODO"
    safety_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_safety}, related_name='Device_safety', blank=True)
    safety_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    