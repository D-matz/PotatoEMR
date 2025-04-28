#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_HealthcareService(models.Model):
    active = FHIR_primitive_BooleanField(null=True, blank=True, )
    providedBy = models.ForeignKey("FHIR_Organization", related_name="HealthcareService_providedBy", null=True, blank=True, on_delete=models.SET_NULL)
    offeredIn = models.ManyToManyField("FHIR_HealthcareService", related_name="HealthcareService_offeredIn", blank=True)
    location = models.ManyToManyField("FHIR_Location", related_name="HealthcareService_location", blank=True)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    comment = FHIR_primitive_MarkdownField(null=True, blank=True, )
    extraDetails = FHIR_primitive_MarkdownField(null=True, blank=True, )
    photo = models.OneToOneField("FHIR_GP_Attachment", related_name='HealthcareService_photo', null=True, blank=True, on_delete=models.SET_NULL)
    coverageArea = models.ManyToManyField("FHIR_Location", related_name="HealthcareService_coverageArea", blank=True)
    referralRequired = FHIR_primitive_BooleanField(null=True, blank=True, )
    appointmentRequired = FHIR_primitive_BooleanField(null=True, blank=True, )
    endpoint = models.ManyToManyField("FHIR_Endpoint", related_name="HealthcareService_endpoint", blank=True)

class FHIR_HealthcareService_identifier(FHIR_GP_Identifier):
    HealthcareService = models.ForeignKey(FHIR_HealthcareService, related_name='HealthcareService_identifier', null=False, on_delete=models.CASCADE)

class FHIR_HealthcareService_category(models.Model):
    HealthcareService = models.ForeignKey(FHIR_HealthcareService, related_name='HealthcareService_category', null=False, on_delete=models.CASCADE)
    BINDING_category = "TODO"
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='HealthcareService_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_HealthcareService_type(models.Model):
    HealthcareService = models.ForeignKey(FHIR_HealthcareService, related_name='HealthcareService_type', null=False, on_delete=models.CASCADE)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='HealthcareService_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_HealthcareService_specialty(models.Model):
    HealthcareService = models.ForeignKey(FHIR_HealthcareService, related_name='HealthcareService_specialty', null=False, on_delete=models.CASCADE)
    BINDING_specialty = "TODO"
    specialty_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_specialty}, related_name='HealthcareService_specialty', blank=True)
    specialty_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_HealthcareService_contact(FHIR_meta_ExtendedContactDetail):
    HealthcareService = models.ForeignKey(FHIR_HealthcareService, related_name='HealthcareService_contact', null=False, on_delete=models.CASCADE)

class FHIR_HealthcareService_serviceProvisionCode(models.Model):
    HealthcareService = models.ForeignKey(FHIR_HealthcareService, related_name='HealthcareService_serviceProvisionCode', null=False, on_delete=models.CASCADE)
    BINDING_serviceProvisionCode = "TODO"
    serviceProvisionCode_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_serviceProvisionCode}, related_name='HealthcareService_serviceProvisionCode', blank=True)
    serviceProvisionCode_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_HealthcareService_eligibility(models.Model):
    HealthcareService = models.ForeignKey(FHIR_HealthcareService, related_name='HealthcareService_eligibility', null=False, on_delete=models.CASCADE)
    BINDING_code = "TODO"
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='HealthcareService_eligibility_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_value_CodeableConcept = "TODO"
    value_CodeableConcept_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_value_CodeableConcept}, related_name='HealthcareService_eligibility_value_CodeableConcept', blank=True)
    value_CodeableConcept_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value_boolean = FHIR_primitive_BooleanField(null=True, blank=True, )
    value_Quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='HealthcareService_eligibility_value_Quantity', null=True, blank=True, on_delete=models.SET_NULL)
    value_Range = models.OneToOneField("FHIR_GP_Range", related_name='HealthcareService_eligibility_value_Range', null=True, blank=True, on_delete=models.SET_NULL)
    comment = FHIR_primitive_MarkdownField(null=True, blank=True, )
    period = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_HealthcareService_program(models.Model):
    HealthcareService = models.ForeignKey(FHIR_HealthcareService, related_name='HealthcareService_program', null=False, on_delete=models.CASCADE)
    BINDING_program = "TODO"
    program_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_program}, related_name='HealthcareService_program', blank=True)
    program_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_HealthcareService_characteristic(models.Model):
    HealthcareService = models.ForeignKey(FHIR_HealthcareService, related_name='HealthcareService_characteristic', null=False, on_delete=models.CASCADE)
    BINDING_characteristic = "TODO"
    characteristic_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_characteristic}, related_name='HealthcareService_characteristic', blank=True)
    characteristic_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_HealthcareService_communication(models.Model):
    HealthcareService = models.ForeignKey(FHIR_HealthcareService, related_name='HealthcareService_communication', null=False, on_delete=models.CASCADE)
    BINDING_communication = "TODO"
    communication_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_communication}, related_name='HealthcareService_communication', blank=True)
    communication_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_HealthcareService_referralMethod(models.Model):
    HealthcareService = models.ForeignKey(FHIR_HealthcareService, related_name='HealthcareService_referralMethod', null=False, on_delete=models.CASCADE)
    BINDING_referralMethod = "TODO"
    referralMethod_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_referralMethod}, related_name='HealthcareService_referralMethod', blank=True)
    referralMethod_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    