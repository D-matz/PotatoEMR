#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Linkage(models.Model):
    active = FHIR_primitive_BooleanField(null=True, blank=True, )
    author_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="Linkage_author", null=True, blank=True, on_delete=models.SET_NULL)
    author_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="Linkage_author", null=True, blank=True, on_delete=models.SET_NULL)
    author_Organization = models.ForeignKey("FHIR_Organization", related_name="Linkage_author", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Linkage_item(models.Model):
    Linkage = models.ForeignKey(FHIR_Linkage, related_name='Linkage_item', null=False, on_delete=models.CASCADE)
    class TypeChoices(models.TextChoices): SOURCE = 'source', 'Source'; ALTERNATE = 'alternate', 'Alternate'; HISTORICAL = 'historical', 'Historical'; 
    type = FHIR_primitive_CodeField(choices=TypeChoices.choices, null=True, blank=True, )
                            #skipping Reference(Any) for field resource as Linkage resource not in referenceAny_targets
