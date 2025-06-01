from .FHIR_primitive import *
from .FHIR_generalpurpose import *

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


class FHIR_SP_Dosage(models.Model):
    sequence = FHIR_primitive_SignedIntField(null=True, blank=True, )
    text = FHIR_primitive_StringField(null=True, blank=True, )
    patientInstruction = FHIR_primitive_StringField(null=True, blank=True, )
    timing = models.OneToOneField("FHIR_GP_Timing", related_name='Dosage_timing', null=True, blank=True, on_delete=models.SET_NULL)
    asNeeded = FHIR_primitive_BooleanField(null=True, blank=True, )
    BINDING_site = "https://hl7.org/fhir/valueset-approach-site-codes.html"
    site_cc = models.ManyToManyField("FHIR_GP_Coding", limit_choices_to={"codings__binding_rule": BINDING_site}, related_name='Dosage_site', blank=True)
    site_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_route = "https://hl7.org/fhir/valueset-route-codes.html"
    route_cc = models.ManyToManyField("FHIR_GP_Coding", limit_choices_to={"codings__binding_rule": BINDING_route}, related_name='Dosage_route', blank=True)
    route_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_method = "https://hl7.org/fhir/valueset-administration-method-codes.html"
    method_cc = models.ManyToManyField("FHIR_GP_Coding", limit_choices_to={"codings__binding_rule": BINDING_method}, related_name='Dosage_method', blank=True)
    method_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    maxDosePerAdministration = models.OneToOneField("FHIR_GP_Quantity", related_name='Dosage_maxDosePerAdministration', null=True, blank=True, on_delete=models.SET_NULL)
    maxDosePerLifetime = models.OneToOneField("FHIR_GP_Quantity", related_name='Dosage_maxDosePerLifetime', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_SP_Dosage_additionalInstruction(models.Model):
    Dosage = models.ForeignKey(FHIR_SP_Dosage, related_name='Dosage_additionalInstruction', null=False, on_delete=models.CASCADE)
    BINDING_additionalInstruction = "TODO"
    additionalInstruction_cc = models.ManyToManyField("FHIR_GP_Coding", limit_choices_to={"codings__binding_rule": BINDING_additionalInstruction}, related_name='Dosage_additionalInstruction', blank=True)
    additionalInstruction_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_SP_Dosage_asNeededFor(models.Model):
    Dosage = models.ForeignKey(FHIR_SP_Dosage, related_name='Dosage_asNeededFor', null=False, on_delete=models.CASCADE)
    BINDING_asNeededFor = "TODO"
    asNeededFor_cc = models.ManyToManyField("FHIR_GP_Coding", limit_choices_to={"codings__binding_rule": BINDING_asNeededFor}, related_name='Dosage_asNeededFor', blank=True)
    asNeededFor_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_SP_Dosage_doseAndRate(models.Model):
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField("FHIR_GP_Coding", limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Dosage_doseAndRate_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    dose_Range = models.OneToOneField("FHIR_GP_Range", related_name='Dosage_doseAndRate_dose_Range', null=True, blank=True, on_delete=models.SET_NULL)
    dose_Quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='Dosage_doseAndRate_dose_Quantity', null=True, blank=True, on_delete=models.SET_NULL)
    rate_Ratio = models.OneToOneField("FHIR_GP_Ratio", related_name='Dosage_doseAndRate_rate_Ratio', null=True, blank=True, on_delete=models.SET_NULL)
    rate_Range = models.OneToOneField("FHIR_GP_Range", related_name='Dosage_doseAndRate_rate_Range', null=True, blank=True, on_delete=models.SET_NULL)
    rate_Quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='Dosage_doseAndRate_rate_Quantity', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_SP_Dosage_maxDosePerPeriod(FHIR_GP_Ratio):
    Dosage = models.ForeignKey(FHIR_SP_Dosage, related_name='Dosage_maxDosePerPeriod', null=False, on_delete=models.CASCADE)
