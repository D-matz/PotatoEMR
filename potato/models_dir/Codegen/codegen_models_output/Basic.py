#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Basic(models.Model):
    BINDING_code = "TODO"
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='Basic_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    created = FHIR_primitive_DateTimeField(null=True, blank=True, )
    author_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="Basic_author", null=True, blank=True, on_delete=models.SET_NULL)
    author_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="Basic_author", null=True, blank=True, on_delete=models.SET_NULL)
    author_Patient = models.ForeignKey("FHIR_Patient", related_name="Basic_author", null=True, blank=True, on_delete=models.SET_NULL)
    author_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="Basic_author", null=True, blank=True, on_delete=models.SET_NULL)
    author_Organization = models.ForeignKey("FHIR_Organization", related_name="Basic_author", null=True, blank=True, on_delete=models.SET_NULL)
    author_Device = models.ForeignKey("FHIR_Device", related_name="Basic_author", null=True, blank=True, on_delete=models.SET_NULL)
    author_CareTeam = models.ForeignKey("FHIR_CareTeam", related_name="Basic_author", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Basic_identifier(FHIR_GP_Identifier):
    Basic = models.ForeignKey(FHIR_Basic, related_name='Basic_identifier', null=False, on_delete=models.CASCADE)
