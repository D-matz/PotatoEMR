#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_BiologicallyDerivedProduct(models.Model):
    BINDING_productCode = 'TODO'
    productCode_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_productCode}, related_name='BiologicallyDerivedProduct_productCode', blank=True)
    productCode_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    parent = models.ManyToManyField("FHIR_BiologicallyDerivedProduct", related_name="BiologicallyDerivedProduct_parent", blank=True)
    request = models.ManyToManyField("FHIR_ServiceRequest", related_name="BiologicallyDerivedProduct_request", blank=True)
    biologicalSourceEvent = models.OneToOneField("FHIR_GP_Identifier", related_name='BiologicallyDerivedProduct_biologicalSourceEvent', null=True, blank=True, on_delete=models.SET_NULL)
    processingFacility = models.ManyToManyField("FHIR_Organization", related_name="BiologicallyDerivedProduct_processingFacility", blank=True)
    division = FHIR_primitive_StringField(null=True, blank=True, )
    productStatus = models.OneToOneField("FHIR_GP_Coding", related_name='BiologicallyDerivedProduct_productStatus', null=True, blank=True, on_delete=models.SET_NULL)
    expirationDate = FHIR_primitive_DateTimeField(null=True, blank=True, )
    storageTempRequirements = models.OneToOneField("FHIR_GP_Range", related_name='BiologicallyDerivedProduct_storageTempRequirements', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_BiologicallyDerivedProduct_productCategory(models.Model):
    BiologicallyDerivedProduct = models.ForeignKey(FHIR_BiologicallyDerivedProduct, related_name='BiologicallyDerivedProduct_productCategory', null=False, on_delete=models.CASCADE)
    BINDING_productCategory = 'TODO'
    productCategory_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_productCategory}, related_name='BiologicallyDerivedProduct_productCategory', blank=True)
    productCategory_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_BiologicallyDerivedProduct_identifier(FHIR_GP_Identifier):
    BiologicallyDerivedProduct = models.ForeignKey(FHIR_BiologicallyDerivedProduct, related_name='BiologicallyDerivedProduct_identifier', null=False, on_delete=models.CASCADE)

class FHIR_BiologicallyDerivedProduct_collection(models.Model):
    BiologicallyDerivedProduct = models.ForeignKey(FHIR_BiologicallyDerivedProduct, related_name='BiologicallyDerivedProduct_collection', null=False, on_delete=models.CASCADE)
    collector_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="BiologicallyDerivedProduct_collection_collector", null=True, blank=True, on_delete=models.SET_NULL)
    collector_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="BiologicallyDerivedProduct_collection_collector", null=True, blank=True, on_delete=models.SET_NULL)
    source_Patient = models.ForeignKey("FHIR_Patient", related_name="BiologicallyDerivedProduct_collection_source", null=True, blank=True, on_delete=models.SET_NULL)
    source_Organization = models.ForeignKey("FHIR_Organization", related_name="BiologicallyDerivedProduct_collection_source", null=True, blank=True, on_delete=models.SET_NULL)
    collected = FHIR_primitive_DateTimeField(null=True, blank=True, )
    collected = models.OneToOneField("FHIR_GP_Period", related_name='BiologicallyDerivedProduct_collection_collected', null=True, blank=True, on_delete=models.SET_NULL)
    procedure = models.ForeignKey("FHIR_Procedure", related_name="BiologicallyDerivedProduct_collection_procedure", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_BiologicallyDerivedProduct_property(models.Model):
    BiologicallyDerivedProduct = models.ForeignKey(FHIR_BiologicallyDerivedProduct, related_name='BiologicallyDerivedProduct_property', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='BiologicallyDerivedProduct_property_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value = FHIR_primitive_BooleanField(null=True, blank=True, )
    BINDING_value = 'TODO'
    value_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_value}, related_name='BiologicallyDerivedProduct_property_value', blank=True)
    value_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value = models.OneToOneField("FHIR_GP_Period", related_name='BiologicallyDerivedProduct_property_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_Quantity", related_name='BiologicallyDerivedProduct_property_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_Range", related_name='BiologicallyDerivedProduct_property_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_Ratio", related_name='BiologicallyDerivedProduct_property_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = FHIR_primitive_StringField(null=True, blank=True, )
    value = models.OneToOneField("FHIR_GP_Attachment", related_name='BiologicallyDerivedProduct_property_value', null=True, blank=True, on_delete=models.SET_NULL)
