
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Binary(models.Model):
    class ContenttypeChoices(models.TextChoices): MIMETYPE_OF_THE_BINARY_CONTENT = 'MimeType of the binary content', 'Mimetype of the binary content'; 
    contentType = FHIR_primitive_CodeField(choices=ContenttypeChoices.choices, null=True, blank=True, )
    data = FHIR_primitive_Base64BinaryField(null=True, blank=True, )
