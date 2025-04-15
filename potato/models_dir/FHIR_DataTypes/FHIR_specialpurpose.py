from .FHIR_primitive import *

#yeah don't do reference as a data type; just use a foreign key
#codeablereference is a foreign key or cc/cc_text

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

#https://build.fhir.org/dosage.html#Dosage
class FHIR_SP_Dosage(models.Model):
    pass