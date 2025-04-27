#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Parameters(models.Model):pass

class FHIR_Parameters_parameter(models.Model):
    Parameters = models.ForeignKey(FHIR_Parameters, related_name='Parameters_parameter', null=False, on_delete=models.CASCADE)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    value_base64Binary = FHIR_primitive_Base64BinaryField(null=True, blank=True, )
    value_boolean = FHIR_primitive_BooleanField(null=True, blank=True, )
    value_canonical = FHIR_primitive_CanonicalField(null=True, blank=True, )
    class Value_codeChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    value_code = FHIR_primitive_CodeField(choices=Value_codeChoices.choices, null=True, blank=True, )
    value_date = FHIR_primitive_DateField(null=True, blank=True, )
    value_dateTime = FHIR_primitive_DateTimeField(null=True, blank=True, )
    value_decimal = FHIR_primitive_DecimalField(null=True, blank=True, )
    value_id = FHIR_primitive_IdField(null=True, blank=True, )
    value_instant = FHIR_primitive_InstantField(null=True, blank=True, )
    value_markdown = FHIR_primitive_MarkdownField(null=True, blank=True, )
    value_oid = FHIR_primitive_OID_Field(null=True, blank=True, )
    value_positiveInt = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    value_string = FHIR_primitive_StringField(null=True, blank=True, )
    value_time = FHIR_primitive_TimeField(null=True, blank=True, )
    value_unsignedInt = FHIR_primitive_UnsignedIntField(null=True, blank=True, )
    value_uri = FHIR_primitive_URIField(null=True, blank=True, )
    value_url = FHIR_primitive_URLField(null=True, blank=True, )
    value_uuid = FHIR_primitive_UUIDField(null=True, blank=True, )
    value_Address = models.OneToOneField("FHIR_GP_Address", related_name='Parameters_parameter_value_Address', null=True, blank=True, on_delete=models.SET_NULL)
    value_Age = models.OneToOneField("FHIR_GP_Quantity_Age", related_name='Parameters_parameter_value_Age', null=True, blank=True, on_delete=models.SET_NULL)
    value_Annotation = models.OneToOneField("FHIR_GP_Annotation", related_name='Parameters_parameter_value_Annotation', null=True, blank=True, on_delete=models.SET_NULL)
    value_Attachment = models.OneToOneField("FHIR_GP_Attachment", related_name='Parameters_parameter_value_Attachment', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_value_CodeableConcept = "TODO"
    value_CodeableConcept_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_value_CodeableConcept}, related_name='Parameters_parameter_value_CodeableConcept', blank=True)
    value_CodeableConcept_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value_Coding = models.OneToOneField("FHIR_GP_Coding", related_name='Parameters_parameter_value_Coding', null=True, blank=True, on_delete=models.SET_NULL)
    value_ContactPoint = models.OneToOneField("FHIR_GP_ContactPoint", related_name='Parameters_parameter_value_ContactPoint', null=True, blank=True, on_delete=models.SET_NULL)
    value_Distance = models.OneToOneField("FHIR_GP_Quantity_Distance", related_name='Parameters_parameter_value_Distance', null=True, blank=True, on_delete=models.SET_NULL)
    value_Duration = models.OneToOneField("FHIR_GP_Quantity_Duration", related_name='Parameters_parameter_value_Duration', null=True, blank=True, on_delete=models.SET_NULL)
    value_HumanName = models.OneToOneField("FHIR_GP_HumanName", related_name='Parameters_parameter_value_HumanName', null=True, blank=True, on_delete=models.SET_NULL)
    value_Identifier = models.OneToOneField("FHIR_GP_Identifier", related_name='Parameters_parameter_value_Identifier', null=True, blank=True, on_delete=models.SET_NULL)
    value_Money = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='Parameters_parameter_value_Money', null=True, blank=True, on_delete=models.SET_NULL)
    value_Period = models.OneToOneField("FHIR_GP_Period", related_name='Parameters_parameter_value_Period', null=True, blank=True, on_delete=models.SET_NULL)
    value_Quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='Parameters_parameter_value_Quantity', null=True, blank=True, on_delete=models.SET_NULL)
    value_Range = models.OneToOneField("FHIR_GP_Range", related_name='Parameters_parameter_value_Range', null=True, blank=True, on_delete=models.SET_NULL)
    value_Ratio = models.OneToOneField("FHIR_GP_Ratio", related_name='Parameters_parameter_value_Ratio', null=True, blank=True, on_delete=models.SET_NULL)
    value_SampledData = models.OneToOneField("FHIR_GP_SampledData", related_name='Parameters_parameter_value_SampledData', null=True, blank=True, on_delete=models.SET_NULL)
    value_Signature = models.OneToOneField("FHIR_GP_Signature", related_name='Parameters_parameter_value_Signature', null=True, blank=True, on_delete=models.SET_NULL)
    value_Timing = models.OneToOneField("FHIR_GP_Timing", related_name='Parameters_parameter_value_Timing', null=True, blank=True, on_delete=models.SET_NULL)
    value_ExtendedContactDetail = models.OneToOneField("FHIR_meta_ExtendedContactDetail", related_name='Parameters_parameter_value_ExtendedContactDetail', null=True, blank=True, on_delete=models.SET_NULL)
    value_Dosage = models.OneToOneField("FHIR_SP_Dosage", related_name='Parameters_parameter_value_Dosage', null=True, blank=True, on_delete=models.SET_NULL)
    value_Meta = models.OneToOneField("FHIR_SP_Meta", related_name='Parameters_parameter_value_Meta', null=True, blank=True, on_delete=models.SET_NULL)
