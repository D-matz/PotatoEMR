#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Binary(models.Model):
    class ContenttypeChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    contentType = FHIR_primitive_CodeField(choices=ContenttypeChoices.choices, null=True, blank=True, )
                            #skipping Reference(Any) for field securityContext as Binary securityContext not in referenceAny_targets
    data = FHIR_primitive_Base64BinaryField(null=True, blank=True, )
