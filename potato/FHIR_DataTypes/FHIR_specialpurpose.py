from .FHIR_primitive import *

#FHIR_SP_Reference note: Resource model using this should also have a foreign key!
#for example:
#    assigner_reference = models.OneToOneField(FHIR_SP_Reference, on_delete=models.CASCADE, related_name="identifier_assigner", null=True, blank=True)
#    assigner_foreignKey = models.ForeignKey(FHIR_Organization, on_delete=models.CASCADE, related_name="test_models")
#https://www.hl7.org/fhir/references.html#reference
#a Reference says there's a relationship between this source resource and another target resource
#it's a foreign key! but we don't know what type of resource it links to
#https://stackoverflow.com/questions/40148630/understanding-django-genericforeignkey-and-genericrelation
#could use generic foreign key...but idk sounds complicated
#easier to put ForeignKey next to FHIR_SP_Reference model when using it in other Resource
#as the Resource model that uses FHIR_SP_Reference knows what resource type it references
#For our database, the Resource can get its target with the ForeignKey
#For FHIR API users, the Resource has a Reference with info for getting its target
class FHIR_SP_Reference(models.Model):
    reference = FHIR_primitive_StringField(max_length=99999) #Literal reference, Relative, internal or absolute URL
    type = FHIR_primitive_URIField(max_length=500)  #  Type the reference refers to (e.g. "Patient")
    # must be a resource in resources , Binding: https://www.hl7.org/fhir/valueset-resource-types.html (Extensible)
    identifier = models.OneToOneField('FHIR_GP_Identifier', on_delete=models.CASCADE, related_name="ref_identifier", null=True, blank=True)
    display = FHIR_primitive_StringField(max_length=8000) #Text alternative for the resource
    def clean(self):
        if not (self.reference or self.identifier or self.display):
            raise ValidationError("One of reference, identifier, or display must exist.")

class FHIR_SP_Meta(models.Model):
    version_id = FHIR_primitive_IdField(max_length=64, blank=True, null=True)
    last_updated = FHIR_primitive_InstantField(max_length=300, blank=True, null=True)
    source = FHIR_primitive_URIField(max_length=255, blank=True, null=True)
    #profile, security, tag - can be 0, 1, or many, so they have ForeignKey to this meta
class FHIR_SP_Meta_Profile(models.Model):
    value = FHIR_primitive_CanonicalField(max_length=255)
    meta = models.ForeignKey(FHIR_SP_Meta, related_name="profiles", on_delete=models.CASCADE)
class FHIR_SP_Meta_Security(models.Model):
    value = FHIR_primitive_StringField(max_length=99999)
    meta = models.ForeignKey(FHIR_SP_Meta, related_name="securitys", on_delete=models.CASCADE)
class FHIR_SP_Meta_Tag(models.Model):
    value = FHIR_primitive_StringField(max_length=255)
    meta = models.ForeignKey(FHIR_SP_Meta, related_name="tags", on_delete=models.CASCADE)
