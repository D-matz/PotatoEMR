
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Parameters(models.Model):

class FHIR_Parameters_parameter(models.Model):
    Parameters = models.ForeignKey(FHIR_Parameters, related_name='Parameters_parameter', null=False, on_delete=models.CASCADE)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    value = FHIR_primitive_Base64BinaryField(null=True, blank=True, )
    value = FHIR_primitive_BooleanField(null=True, blank=True, )
    value = FHIR_primitive_CanonicalField(null=True, blank=True, )
    class ValueChoices(models.TextChoices): IF_PARAMETER_IS_A_DATA_TYPE = 'If parameter is a data type', 'If parameter is a data type'; 
    value = FHIR_primitive_CodeField(choices=ValueChoices.choices, null=True, blank=True, )
    value = FHIR_primitive_DateField(null=True, blank=True, )
    value = FHIR_primitive_DateTimeField(null=True, blank=True, )
    value = FHIR_primitive_DecimalField(null=True, blank=True, )
    value = FHIR_primitive_IdField(null=True, blank=True, )
    value = FHIR_primitive_InstantField(null=True, blank=True, )
    value = FHIR_primitive_MarkdownField(null=True, blank=True, )
    value = FHIR_primitive_OID_Field(null=True, blank=True, )
    value = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    value = FHIR_primitive_StringField(null=True, blank=True, )
    value = FHIR_primitive_TimeField(null=True, blank=True, )
    value = FHIR_primitive_UnsignedIntField(null=True, blank=True, )
    value = FHIR_primitive_URIField(null=True, blank=True, )
    value = FHIR_primitive_URLField(null=True, blank=True, )
    value = FHIR_primitive_UUIDField(null=True, blank=True, )
    value = models.OneToOneField("FHIR_GP_Address", related_name='Parameters_parameter_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_Quantity_Age", related_name='Parameters_parameter_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_Annotation", related_name='Parameters_parameter_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_Attachment", related_name='Parameters_parameter_value', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_value = 'TODO'
    value_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_value}, related_name='Parameters_parameter_value', blank=True)
    value_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value = models.OneToOneField("FHIR_GP_Coding", related_name='Parameters_parameter_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_ContactPoint", related_name='Parameters_parameter_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_Quantity_Distance", related_name='Parameters_parameter_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_Quantity_Duration", related_name='Parameters_parameter_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_HumanName", related_name='Parameters_parameter_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_Identifier", related_name='Parameters_parameter_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='Parameters_parameter_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_Period", related_name='Parameters_parameter_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_Quantity", related_name='Parameters_parameter_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_Range", related_name='Parameters_parameter_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_Ratio", related_name='Parameters_parameter_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_SampledData", related_name='Parameters_parameter_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_Signature", related_name='Parameters_parameter_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_Timing", related_name='Parameters_parameter_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_meta_ExtendedContactDetail", related_name='Parameters_parameter_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_SP_Dosage", related_name='Parameters_parameter_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_SP_Meta", related_name='Parameters_parameter_value', null=True, blank=True, on_delete=models.SET_NULL)
