from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_RelatedPerson(models.Model):
    identifier = models.ManyToManyField(Identifier, blank=True)
    active = models.BooleanField(null=True, blank=True)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)  # Replace 'Patient' with the actual Patient model
    relationship = models.ManyToManyField(CodeableConcept, blank=True)
    name = models.ManyToManyField(HumanName, blank=True)
    telecom = models.ManyToManyField(ContactPoint, blank=True)
    gender = models.CharField(
        max_length=20,
        choices=[
            ('male', 'Male'),
            ('female', 'Female'),
            ('other', 'Other'),
            ('unknown', 'Unknown')
        ],
        null=True,
        blank=True
    )
    birthDate = models.DateField(null=True, blank=True)
    address = models.ManyToManyField(Address, blank=True)
    photo = models.ManyToManyField(Attachment, blank=True)
    period = models.ForeignKey(Period, null=True, blank=True, on_delete=models.SET_NULL)
    communication = models.JSONField(null=True, blank=True)  # Store language and preference as JSON

class FHIR_Patient_Identifier(models.Model):
    identifier = models.OneToOneField(FHIR_GP_Identifier, related_name="patient_identifier", null=True, on_delete=models.SET_NULL)
    patient = models.ForeignKey(FHIR_Patient, related_name="patient_identifiers", on_delete=models.CASCADE)
    
