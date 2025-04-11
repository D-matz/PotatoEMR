from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Location(models.Model):
    name = FHIR_primitive_StringField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name

class FHIR_Location_Identifier(FHIR_GP_Identifier):
    location = models.ForeignKey(FHIR_Location, on_delete=models.CASCADE, related_name='identifiers')
