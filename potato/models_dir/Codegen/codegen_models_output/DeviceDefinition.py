#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_DeviceDefinition(models.Model):
    url = FHIR_primitive_URIField(null=True, blank=True, )
    version = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm_string = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm_Coding = models.OneToOneField("FHIR_GP_Coding", related_name='DeviceDefinition_versionAlgorithm_Coding', null=True, blank=True, on_delete=models.SET_NULL)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    title = FHIR_primitive_StringField(null=True, blank=True, )
    class StatusChoices(models.TextChoices): DRAFT = 'draft', 'Draft'; ACTIVE = 'active', 'Active'; RETIRED = 'retired', 'Retired'; UNKNOWN_ = 'unknown ', 'Unknown '; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    experimental = FHIR_primitive_BooleanField(null=True, blank=True, )
    partNumber = FHIR_primitive_StringField(null=True, blank=True, )
    manufacturer = models.ForeignKey("FHIR_Organization", related_name="DeviceDefinition_manufacturer", null=True, blank=True, on_delete=models.SET_NULL)
    modelNumber = FHIR_primitive_StringField(null=True, blank=True, )
    date = FHIR_primitive_DateTimeField(null=True, blank=True, )
    publisher = FHIR_primitive_StringField(null=True, blank=True, )
    purpose = FHIR_primitive_MarkdownField(null=True, blank=True, )
    copyright = FHIR_primitive_MarkdownField(null=True, blank=True, )
    copyrightLabel = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_DeviceDefinition_identifier(FHIR_GP_Identifier):
    DeviceDefinition = models.ForeignKey(FHIR_DeviceDefinition, related_name='DeviceDefinition_identifier', null=False, on_delete=models.CASCADE)

class FHIR_DeviceDefinition_jurisdiction(models.Model):
    DeviceDefinition = models.ForeignKey(FHIR_DeviceDefinition, related_name='DeviceDefinition_jurisdiction', null=False, on_delete=models.CASCADE)
    BINDING_jurisdiction = "TODO"
    jurisdiction_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_jurisdiction}, related_name='DeviceDefinition_jurisdiction', blank=True)
    jurisdiction_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_DeviceDefinition_udiDeviceIdentifier(models.Model):
    DeviceDefinition = models.ForeignKey(FHIR_DeviceDefinition, related_name='DeviceDefinition_udiDeviceIdentifier', null=False, on_delete=models.CASCADE)
    deviceIdentifier = FHIR_primitive_StringField(null=True, blank=True, )
    issuer = FHIR_primitive_URIField(null=True, blank=True, )
    jurisdiction = FHIR_primitive_URIField(null=True, blank=True, )

class FHIR_DeviceDefinition_udiDeviceIdentifier_marketDistribution(models.Model):
    DeviceDefinition_udiDeviceIdentifier = models.ForeignKey(FHIR_DeviceDefinition_udiDeviceIdentifier, related_name='DeviceDefinition_udiDeviceIdentifier_marketDistribution', null=False, on_delete=models.CASCADE)
    marketPeriod = models.OneToOneField("FHIR_GP_Period", related_name='DeviceDefinition_udiDeviceIdentifier_marketDistribution_marketPeriod', null=True, blank=True, on_delete=models.SET_NULL)
    subJurisdiction = FHIR_primitive_URIField(null=True, blank=True, )

class FHIR_DeviceDefinition_regulatoryIdentifier(models.Model):
    DeviceDefinition = models.ForeignKey(FHIR_DeviceDefinition, related_name='DeviceDefinition_regulatoryIdentifier', null=False, on_delete=models.CASCADE)
    class TypeChoices(models.TextChoices): BASIC = 'basic', 'Basic'; MASTER = 'master', 'Master'; LICENSE = 'license', 'License'; 
    type = FHIR_primitive_CodeField(choices=TypeChoices.choices, null=True, blank=True, )
    deviceIdentifier = FHIR_primitive_StringField(null=True, blank=True, )
    issuer = FHIR_primitive_URIField(null=True, blank=True, )
    jurisdiction = FHIR_primitive_URIField(null=True, blank=True, )

class FHIR_DeviceDefinition_deviceName(models.Model):
    DeviceDefinition = models.ForeignKey(FHIR_DeviceDefinition, related_name='DeviceDefinition_deviceName', null=False, on_delete=models.CASCADE)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='DeviceDefinition_deviceName_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_DeviceDefinition_classification(models.Model):
    DeviceDefinition = models.ForeignKey(FHIR_DeviceDefinition, related_name='DeviceDefinition_classification', null=False, on_delete=models.CASCADE)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='DeviceDefinition_classification_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_DeviceDefinition_conformsTo(models.Model):
    DeviceDefinition = models.ForeignKey(FHIR_DeviceDefinition, related_name='DeviceDefinition_conformsTo', null=False, on_delete=models.CASCADE)
    BINDING_category = "TODO"
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='DeviceDefinition_conformsTo_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_specification = "TODO"
    specification_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_specification}, related_name='DeviceDefinition_conformsTo_specification', blank=True)
    specification_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_DeviceDefinition_conformsTo_version(models.Model):
    DeviceDefinition_conformsTo = models.ForeignKey(FHIR_DeviceDefinition_conformsTo, related_name='DeviceDefinition_conformsTo_version', null=False, on_delete=models.CASCADE)
    
    version = FHIR_primitive_StringField(null=True, blank=True, )
    
class FHIR_DeviceDefinition_hasPart(models.Model):
    DeviceDefinition = models.ForeignKey(FHIR_DeviceDefinition, related_name='DeviceDefinition_hasPart', null=False, on_delete=models.CASCADE)
    reference = models.ForeignKey("FHIR_DeviceDefinition", related_name="DeviceDefinition_hasPart_reference", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_DeviceDefinition_packaging(models.Model):
    DeviceDefinition = models.ForeignKey(FHIR_DeviceDefinition, related_name='DeviceDefinition_packaging', null=False, on_delete=models.CASCADE)
    identifier = models.OneToOneField("FHIR_GP_Identifier", related_name='DeviceDefinition_packaging_identifier', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='DeviceDefinition_packaging_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_DeviceDefinition_packaging_distributor(models.Model):
    DeviceDefinition_packaging = models.ForeignKey(FHIR_DeviceDefinition_packaging, related_name='DeviceDefinition_packaging_distributor', null=False, on_delete=models.CASCADE)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    organizationReference = models.ManyToManyField("FHIR_Organization", related_name="DeviceDefinition_packaging_distributor_organizationReference", blank=True)

class FHIR_DeviceDefinition_deviceVersion(models.Model):
    DeviceDefinition = models.ForeignKey(FHIR_DeviceDefinition, related_name='DeviceDefinition_deviceVersion', null=False, on_delete=models.CASCADE)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='DeviceDefinition_deviceVersion_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    component = models.OneToOneField("FHIR_GP_Identifier", related_name='DeviceDefinition_deviceVersion_component', null=True, blank=True, on_delete=models.SET_NULL)
    value = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_DeviceDefinition_safety(models.Model):
    DeviceDefinition = models.ForeignKey(FHIR_DeviceDefinition, related_name='DeviceDefinition_safety', null=False, on_delete=models.CASCADE)
    BINDING_safety = "TODO"
    safety_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_safety}, related_name='DeviceDefinition_safety', blank=True)
    safety_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_DeviceDefinition_outputLanguage(models.Model):
    DeviceDefinition = models.ForeignKey(FHIR_DeviceDefinition, related_name='DeviceDefinition_outputLanguage', null=False, on_delete=models.CASCADE)
    
    class OutputlanguageChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    outputLanguage = FHIR_primitive_CodeField(choices=OutputlanguageChoices.choices, null=True, blank=True, )
    
class FHIR_DeviceDefinition_property(models.Model):
    DeviceDefinition = models.ForeignKey(FHIR_DeviceDefinition, related_name='DeviceDefinition_property', null=False, on_delete=models.CASCADE)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='DeviceDefinition_property_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value_Quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='DeviceDefinition_property_value_Quantity', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_value_CodeableConcept = "TODO"
    value_CodeableConcept_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_value_CodeableConcept}, related_name='DeviceDefinition_property_value_CodeableConcept', blank=True)
    value_CodeableConcept_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value_string = FHIR_primitive_StringField(null=True, blank=True, )
    value_boolean = FHIR_primitive_BooleanField(null=True, blank=True, )
    value_Range = models.OneToOneField("FHIR_GP_Range", related_name='DeviceDefinition_property_value_Range', null=True, blank=True, on_delete=models.SET_NULL)
    value_Attachment = models.OneToOneField("FHIR_GP_Attachment", related_name='DeviceDefinition_property_value_Attachment', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_DeviceDefinition_link(models.Model):
    DeviceDefinition = models.ForeignKey(FHIR_DeviceDefinition, related_name='DeviceDefinition_link', null=False, on_delete=models.CASCADE)
    relation = models.OneToOneField("FHIR_GP_Coding", related_name='DeviceDefinition_link_relation', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_relatedDevice = "TODO"
    relatedDevice_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_relatedDevice}, related_name='DeviceDefinition_link_relatedDevice', blank=True)
    relatedDevice_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    relatedDevice_DeviceDefinition_ref = models.ForeignKey("FHIR_DeviceDefinition", related_name="DeviceDefinition_link_relatedDevice_DeviceDefinition", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_DeviceDefinition_note(FHIR_GP_Annotation):
    DeviceDefinition = models.ForeignKey(FHIR_DeviceDefinition, related_name='DeviceDefinition_note', null=False, on_delete=models.CASCADE)

class FHIR_DeviceDefinition_material(models.Model):
    DeviceDefinition = models.ForeignKey(FHIR_DeviceDefinition, related_name='DeviceDefinition_material', null=False, on_delete=models.CASCADE)
    BINDING_substance = "TODO"
    substance_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_substance}, related_name='DeviceDefinition_material_substance', blank=True)
    substance_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    alternate = FHIR_primitive_BooleanField(null=True, blank=True, )
    allergenicIndicator = FHIR_primitive_BooleanField(null=True, blank=True, )

class FHIR_DeviceDefinition_productionIdentifierInUDI(models.Model):
    DeviceDefinition = models.ForeignKey(FHIR_DeviceDefinition, related_name='DeviceDefinition_productionIdentifierInUDI', null=False, on_delete=models.CASCADE)
    BINDING_productionIdentifierInUDI = "TODO"
    productionIdentifierInUDI_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_productionIdentifierInUDI}, related_name='DeviceDefinition_productionIdentifierInUDI', blank=True)
    productionIdentifierInUDI_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_DeviceDefinition_guideline(models.Model):
    DeviceDefinition = models.ForeignKey(FHIR_DeviceDefinition, related_name='DeviceDefinition_guideline', null=False, on_delete=models.CASCADE)
    usageInstruction = FHIR_primitive_MarkdownField(null=True, blank=True, )
    intendedUse = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_DeviceDefinition_guideline_indication(models.Model):
    DeviceDefinition_guideline = models.ForeignKey(FHIR_DeviceDefinition_guideline, related_name='DeviceDefinition_guideline_indication', null=False, on_delete=models.CASCADE)
    BINDING_indication = "TODO"
    indication_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_indication}, related_name='DeviceDefinition_guideline_indication', blank=True)
    indication_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_DeviceDefinition_guideline_contraindication(models.Model):
    DeviceDefinition_guideline = models.ForeignKey(FHIR_DeviceDefinition_guideline, related_name='DeviceDefinition_guideline_contraindication', null=False, on_delete=models.CASCADE)
    BINDING_contraindication = "TODO"
    contraindication_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_contraindication}, related_name='DeviceDefinition_guideline_contraindication', blank=True)
    contraindication_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_DeviceDefinition_guideline_warning(models.Model):
    DeviceDefinition_guideline = models.ForeignKey(FHIR_DeviceDefinition_guideline, related_name='DeviceDefinition_guideline_warning', null=False, on_delete=models.CASCADE)
    BINDING_warning = "TODO"
    warning_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_warning}, related_name='DeviceDefinition_guideline_warning', blank=True)
    warning_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_DeviceDefinition_correctiveAction(models.Model):
    DeviceDefinition = models.ForeignKey(FHIR_DeviceDefinition, related_name='DeviceDefinition_correctiveAction', null=False, on_delete=models.CASCADE)
    recall = FHIR_primitive_BooleanField(null=True, blank=True, )
    class ScopeChoices(models.TextChoices): MODEL = 'model', 'Model'; LOT_NUMBERS = 'lot-numbers', 'Lot-numbers'; SERIAL_NUMBERS = 'serial-numbers', 'Serial-numbers'; 
    scope = FHIR_primitive_CodeField(choices=ScopeChoices.choices, null=True, blank=True, )
    period = models.OneToOneField("FHIR_GP_Period", related_name='DeviceDefinition_correctiveAction_period', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_DeviceDefinition_chargeItem(models.Model):
    DeviceDefinition = models.ForeignKey(FHIR_DeviceDefinition, related_name='DeviceDefinition_chargeItem', null=False, on_delete=models.CASCADE)
    BINDING_chargeItemCode = "TODO"
    chargeItemCode_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_chargeItemCode}, related_name='DeviceDefinition_chargeItem_chargeItemCode', blank=True)
    chargeItemCode_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    chargeItemCode_ChargeItemDefinition_ref = models.ForeignKey("FHIR_ChargeItemDefinition", related_name="DeviceDefinition_chargeItem_chargeItemCode_ChargeItemDefinition", null=True, blank=True, on_delete=models.SET_NULL)
    count = models.OneToOneField("FHIR_GP_Quantity", related_name='DeviceDefinition_chargeItem_count', null=True, blank=True, on_delete=models.SET_NULL)
    effectivePeriod = models.OneToOneField("FHIR_GP_Period", related_name='DeviceDefinition_chargeItem_effectivePeriod', null=True, blank=True, on_delete=models.SET_NULL)
