#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_MedicinalProductDefinition(models.Model):
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='MedicinalProductDefinition_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_domain = 'TODO'
    domain_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_domain}, related_name='MedicinalProductDefinition_domain', blank=True)
    domain_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    version = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_status = 'TODO'
    status_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_status}, related_name='MedicinalProductDefinition_status', blank=True)
    status_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    statusDate = FHIR_primitive_DateTimeField(null=True, blank=True, )
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    BINDING_combinedPharmaceuticalDoseForm = 'TODO'
    combinedPharmaceuticalDoseForm_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_combinedPharmaceuticalDoseForm}, related_name='MedicinalProductDefinition_combinedPharmaceuticalDoseForm', blank=True)
    combinedPharmaceuticalDoseForm_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    indication = FHIR_primitive_MarkdownField(null=True, blank=True, )
    BINDING_legalStatusOfSupply = 'TODO'
    legalStatusOfSupply_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_legalStatusOfSupply}, related_name='MedicinalProductDefinition_legalStatusOfSupply', blank=True)
    legalStatusOfSupply_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_additionalMonitoringIndicator = 'TODO'
    additionalMonitoringIndicator_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_additionalMonitoringIndicator}, related_name='MedicinalProductDefinition_additionalMonitoringIndicator', blank=True)
    additionalMonitoringIndicator_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_pediatricUseIndicator = 'TODO'
    pediatricUseIndicator_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_pediatricUseIndicator}, related_name='MedicinalProductDefinition_pediatricUseIndicator', blank=True)
    pediatricUseIndicator_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    comprisedOf_ManufacturedItemDefinition = models.ManyToManyField("FHIR_ManufacturedItemDefinition", related_name="MedicinalProductDefinition_comprisedOf", blank=True)
    comprisedOf_DeviceDefinition = models.ManyToManyField("FHIR_DeviceDefinition", related_name="MedicinalProductDefinition_comprisedOf", blank=True)
    attachedDocument = models.ManyToManyField("FHIR_DocumentReference", related_name="MedicinalProductDefinition_attachedDocument", blank=True)
    masterFile = models.ManyToManyField("FHIR_DocumentReference", related_name="MedicinalProductDefinition_masterFile", blank=True)
    clinicalTrial = models.ManyToManyField("FHIR_ResearchStudy", related_name="MedicinalProductDefinition_clinicalTrial", blank=True)

class FHIR_MedicinalProductDefinition_identifier(FHIR_GP_Identifier):
    MedicinalProductDefinition = models.ForeignKey(FHIR_MedicinalProductDefinition, related_name='MedicinalProductDefinition_identifier', null=False, on_delete=models.CASCADE)

class FHIR_MedicinalProductDefinition_route(models.Model):
    MedicinalProductDefinition = models.ForeignKey(FHIR_MedicinalProductDefinition, related_name='MedicinalProductDefinition_route', null=False, on_delete=models.CASCADE)
    BINDING_route = 'TODO'
    route_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_route}, related_name='MedicinalProductDefinition_route', blank=True)
    route_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_MedicinalProductDefinition_specialMeasures(models.Model):
    MedicinalProductDefinition = models.ForeignKey(FHIR_MedicinalProductDefinition, related_name='MedicinalProductDefinition_specialMeasures', null=False, on_delete=models.CASCADE)
    BINDING_specialMeasures = 'TODO'
    specialMeasures_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_specialMeasures}, related_name='MedicinalProductDefinition_specialMeasures', blank=True)
    specialMeasures_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_MedicinalProductDefinition_classification(models.Model):
    MedicinalProductDefinition = models.ForeignKey(FHIR_MedicinalProductDefinition, related_name='MedicinalProductDefinition_classification', null=False, on_delete=models.CASCADE)
    BINDING_classification = 'TODO'
    classification_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_classification}, related_name='MedicinalProductDefinition_classification', blank=True)
    classification_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_MedicinalProductDefinition_packagedMedicinalProduct(models.Model):
    MedicinalProductDefinition = models.ForeignKey(FHIR_MedicinalProductDefinition, related_name='MedicinalProductDefinition_packagedMedicinalProduct', null=False, on_delete=models.CASCADE)
    BINDING_packagedMedicinalProduct = 'TODO'
    packagedMedicinalProduct_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_packagedMedicinalProduct}, related_name='MedicinalProductDefinition_packagedMedicinalProduct', blank=True)
    packagedMedicinalProduct_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_MedicinalProductDefinition_ingredient(models.Model):
    MedicinalProductDefinition = models.ForeignKey(FHIR_MedicinalProductDefinition, related_name='MedicinalProductDefinition_ingredient', null=False, on_delete=models.CASCADE)
    BINDING_ingredient = 'TODO'
    ingredient_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_ingredient}, related_name='MedicinalProductDefinition_ingredient', blank=True)
    ingredient_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_MedicinalProductDefinition_impurity(models.Model):
    MedicinalProductDefinition = models.ForeignKey(FHIR_MedicinalProductDefinition, related_name='MedicinalProductDefinition_impurity', null=False, on_delete=models.CASCADE)
    BINDING_impurity = 'TODO'
    impurity_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_impurity}, related_name='MedicinalProductDefinition_impurity', blank=True)
    impurity_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    impurity_SubstanceDefinition_ref = models.ForeignKey("FHIR_SubstanceDefinition", related_name="MedicinalProductDefinition_impurity_SubstanceDefinition", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_MedicinalProductDefinition_contact(models.Model):
    MedicinalProductDefinition = models.ForeignKey(FHIR_MedicinalProductDefinition, related_name='MedicinalProductDefinition_contact', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='MedicinalProductDefinition_contact_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    contact_Organization = models.ForeignKey("FHIR_Organization", related_name="MedicinalProductDefinition_contact_contact", null=True, blank=True, on_delete=models.SET_NULL)
    contact_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="MedicinalProductDefinition_contact_contact", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_MedicinalProductDefinition_code(FHIR_GP_Coding):
    MedicinalProductDefinition = models.ForeignKey(FHIR_MedicinalProductDefinition, related_name='MedicinalProductDefinition_code', null=False, on_delete=models.CASCADE)

class FHIR_MedicinalProductDefinition_name(models.Model):
    MedicinalProductDefinition = models.ForeignKey(FHIR_MedicinalProductDefinition, related_name='MedicinalProductDefinition_name', null=False, on_delete=models.CASCADE)
    productName = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='MedicinalProductDefinition_name_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_MedicinalProductDefinition_name_part(models.Model):
    MedicinalProductDefinition_name = models.ForeignKey(FHIR_MedicinalProductDefinition_name, related_name='MedicinalProductDefinition_name_part', null=False, on_delete=models.CASCADE)
    part = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='MedicinalProductDefinition_name_part_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_MedicinalProductDefinition_name_usage(models.Model):
    MedicinalProductDefinition_name = models.ForeignKey(FHIR_MedicinalProductDefinition_name, related_name='MedicinalProductDefinition_name_usage', null=False, on_delete=models.CASCADE)
    BINDING_country = 'TODO'
    country_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_country}, related_name='MedicinalProductDefinition_name_usage_country', blank=True)
    country_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_jurisdiction = 'TODO'
    jurisdiction_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_jurisdiction}, related_name='MedicinalProductDefinition_name_usage_jurisdiction', blank=True)
    jurisdiction_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_language = 'TODO'
    language_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_language}, related_name='MedicinalProductDefinition_name_usage_language', blank=True)
    language_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_MedicinalProductDefinition_crossReference(models.Model):
    MedicinalProductDefinition = models.ForeignKey(FHIR_MedicinalProductDefinition, related_name='MedicinalProductDefinition_crossReference', null=False, on_delete=models.CASCADE)
    BINDING_product = 'TODO'
    product_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_product}, related_name='MedicinalProductDefinition_crossReference_product', blank=True)
    product_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    product_MedicinalProductDefinition_ref = models.ForeignKey("FHIR_MedicinalProductDefinition", related_name="MedicinalProductDefinition_crossReference_product_MedicinalProductDefinition", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='MedicinalProductDefinition_crossReference_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_MedicinalProductDefinition_operation(models.Model):
    MedicinalProductDefinition = models.ForeignKey(FHIR_MedicinalProductDefinition, related_name='MedicinalProductDefinition_operation', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='MedicinalProductDefinition_operation_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    type_ActivityDefinition_ref = models.ForeignKey("FHIR_ActivityDefinition", related_name="MedicinalProductDefinition_operation_type_ActivityDefinition", null=True, blank=True, on_delete=models.SET_NULL)
    type_PlanDefinition_ref = models.ForeignKey("FHIR_PlanDefinition", related_name="MedicinalProductDefinition_operation_type_PlanDefinition", null=True, blank=True, on_delete=models.SET_NULL)
    effectiveDate = models.OneToOneField("FHIR_GP_Period", related_name='MedicinalProductDefinition_operation_effectiveDate', null=True, blank=True, on_delete=models.SET_NULL)
    organization = models.ManyToManyField("FHIR_Organization", related_name="MedicinalProductDefinition_operation_organization", blank=True)
    BINDING_confidentialityIndicator = 'TODO'
    confidentialityIndicator_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_confidentialityIndicator}, related_name='MedicinalProductDefinition_operation_confidentialityIndicator', blank=True)
    confidentialityIndicator_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_MedicinalProductDefinition_characteristic(models.Model):
    MedicinalProductDefinition = models.ForeignKey(FHIR_MedicinalProductDefinition, related_name='MedicinalProductDefinition_characteristic', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='MedicinalProductDefinition_characteristic_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_value = 'TODO'
    value_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_value}, related_name='MedicinalProductDefinition_characteristic_value', blank=True)
    value_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value = FHIR_primitive_MarkdownField(null=True, blank=True, )
    value = models.OneToOneField("FHIR_GP_Quantity", related_name='MedicinalProductDefinition_characteristic_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = FHIR_primitive_DateField(null=True, blank=True, )
    value = FHIR_primitive_BooleanField(null=True, blank=True, )
    value = models.OneToOneField("FHIR_GP_Attachment", related_name='MedicinalProductDefinition_characteristic_value', null=True, blank=True, on_delete=models.SET_NULL)
