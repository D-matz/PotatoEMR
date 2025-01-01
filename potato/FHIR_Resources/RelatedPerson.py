from ..FHIR_DataTypes.FHIR_primitive import *
from ..FHIR_DataTypes.FHIR_generalpurpose import *

class FHIR_RelatedPerson(models.Model):
    pass

class FHIR_RelatedPerson_Identifier(FHIR_GP_Identifier):
    relatedPerson = models.ForeignKey('FHIR_RelatedPerson', related_name="RelatedPerson_identifiers", on_delete=models.CASCADE)
