#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_FormularyItem(models.Model):
    BINDING_code = "TODO"
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='FormularyItem_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    class StatusChoices(models.TextChoices): ACTIVE = 'active', 'Active'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; INACTIVE = 'inactive', 'Inactive'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )

class FHIR_FormularyItem_identifier(FHIR_GP_Identifier):
    FormularyItem = models.ForeignKey(FHIR_FormularyItem, related_name='FormularyItem_identifier', null=False, on_delete=models.CASCADE)
