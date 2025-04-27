#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_SubstanceNucleicAcid(models.Model):
    BINDING_sequenceType = 'TODO'
    sequenceType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_sequenceType}, related_name='SubstanceNucleicAcid_sequenceType', blank=True)
    sequenceType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    areaOfHybridisation = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_oligoNucleotideType = 'TODO'
    oligoNucleotideType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_oligoNucleotideType}, related_name='SubstanceNucleicAcid_oligoNucleotideType', blank=True)
    oligoNucleotideType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_SubstanceNucleicAcid_subunit(models.Model):
    SubstanceNucleicAcid = models.ForeignKey(FHIR_SubstanceNucleicAcid, related_name='SubstanceNucleicAcid_subunit', null=False, on_delete=models.CASCADE)
    sequence = FHIR_primitive_StringField(null=True, blank=True, )
    sequenceAttachment = models.OneToOneField("FHIR_GP_Attachment", related_name='SubstanceNucleicAcid_subunit_sequenceAttachment', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_fivePrime = 'TODO'
    fivePrime_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_fivePrime}, related_name='SubstanceNucleicAcid_subunit_fivePrime', blank=True)
    fivePrime_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_threePrime = 'TODO'
    threePrime_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_threePrime}, related_name='SubstanceNucleicAcid_subunit_threePrime', blank=True)
    threePrime_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_SubstanceNucleicAcid_subunit_linkage(models.Model):
    SubstanceNucleicAcid_subunit = models.ForeignKey(FHIR_SubstanceNucleicAcid_subunit, related_name='SubstanceNucleicAcid_subunit_linkage', null=False, on_delete=models.CASCADE)
    connectivity = FHIR_primitive_StringField(null=True, blank=True, )
    identifier = models.OneToOneField("FHIR_GP_Identifier", related_name='SubstanceNucleicAcid_subunit_linkage_identifier', null=True, blank=True, on_delete=models.SET_NULL)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    residueSite = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_SubstanceNucleicAcid_subunit_sugar(models.Model):
    SubstanceNucleicAcid_subunit = models.ForeignKey(FHIR_SubstanceNucleicAcid_subunit, related_name='SubstanceNucleicAcid_subunit_sugar', null=False, on_delete=models.CASCADE)
    identifier = models.OneToOneField("FHIR_GP_Identifier", related_name='SubstanceNucleicAcid_subunit_sugar_identifier', null=True, blank=True, on_delete=models.SET_NULL)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    residueSite = FHIR_primitive_StringField(null=True, blank=True, )
