
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Substance(models.Model):
    class StatusChoices(models.TextChoices): ACTIVE = 'active', 'Active'; INACTIVE = 'inactive', 'Inactive'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    BINDING_code = 'TODO'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='Substance_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    code_SubstanceDefinition_ref = models.ForeignKey("FHIR_SubstanceDefinition", related_name="Substance_code", null=True, blank=True, on_delete=models.SET_NULL)
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    expiry = FHIR_primitive_DateTimeField(null=True, blank=True, )
    quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='Substance_quantity', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Substance_identifier(FHIR_GP_Identifier):
    Substance = models.ForeignKey(FHIR_Substance, related_name='Substance_identifier', null=False, on_delete=models.CASCADE)

class FHIR_Substance_category(models.Model):
    Substance = models.ForeignKey(FHIR_Substance, related_name='Substance_category', null=False, on_delete=models.CASCADE)
    BINDING_category = 'TODO'
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='Substance_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    