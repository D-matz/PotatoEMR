
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_SubstanceReferenceInformation(models.Model):
    comment = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_SubstanceReferenceInformation_gene(models.Model):
    SubstanceReferenceInformation = models.ForeignKey(FHIR_SubstanceReferenceInformation, related_name='SubstanceReferenceInformation_gene', null=False, on_delete=models.CASCADE)
    BINDING_geneSequenceOrigin = 'TODO'
    geneSequenceOrigin_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_geneSequenceOrigin}, related_name='SubstanceReferenceInformation_gene_geneSequenceOrigin', blank=True)
    geneSequenceOrigin_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_gene = 'TODO'
    gene_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_gene}, related_name='SubstanceReferenceInformation_gene_gene', blank=True)
    gene_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    source = models.ManyToManyField("FHIR_DocumentReference", related_name="SubstanceReferenceInformation_gene_source", blank=True)

class FHIR_SubstanceReferenceInformation_geneElement(models.Model):
    SubstanceReferenceInformation = models.ForeignKey(FHIR_SubstanceReferenceInformation, related_name='SubstanceReferenceInformation_geneElement', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='SubstanceReferenceInformation_geneElement_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    element = models.OneToOneField("FHIR_GP_Identifier", related_name='SubstanceReferenceInformation_geneElement_element', null=True, blank=True, on_delete=models.SET_NULL)
    source = models.ManyToManyField("FHIR_DocumentReference", related_name="SubstanceReferenceInformation_geneElement_source", blank=True)

class FHIR_SubstanceReferenceInformation_target(models.Model):
    SubstanceReferenceInformation = models.ForeignKey(FHIR_SubstanceReferenceInformation, related_name='SubstanceReferenceInformation_target', null=False, on_delete=models.CASCADE)
    target = models.OneToOneField("FHIR_GP_Identifier", related_name='SubstanceReferenceInformation_target_target', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='SubstanceReferenceInformation_target_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_interaction = 'TODO'
    interaction_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_interaction}, related_name='SubstanceReferenceInformation_target_interaction', blank=True)
    interaction_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_organism = 'TODO'
    organism_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_organism}, related_name='SubstanceReferenceInformation_target_organism', blank=True)
    organism_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_organismType = 'TODO'
    organismType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_organismType}, related_name='SubstanceReferenceInformation_target_organismType', blank=True)
    organismType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    amount = models.OneToOneField("FHIR_GP_Quantity", related_name='SubstanceReferenceInformation_target_amount', null=True, blank=True, on_delete=models.SET_NULL)
    amount = models.OneToOneField("FHIR_GP_Range", related_name='SubstanceReferenceInformation_target_amount', null=True, blank=True, on_delete=models.SET_NULL)
    amount = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_amountType = 'TODO'
    amountType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_amountType}, related_name='SubstanceReferenceInformation_target_amountType', blank=True)
    amountType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    source = models.ManyToManyField("FHIR_DocumentReference", related_name="SubstanceReferenceInformation_target_source", blank=True)
