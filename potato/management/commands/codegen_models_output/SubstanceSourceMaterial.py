
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_SubstanceSourceMaterial(models.Model):
    BINDING_sourceMaterialClass = 'TODO'
    sourceMaterialClass_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_sourceMaterialClass}, related_name='SubstanceSourceMaterial_sourceMaterialClass', blank=True)
    sourceMaterialClass_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_sourceMaterialType = 'TODO'
    sourceMaterialType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_sourceMaterialType}, related_name='SubstanceSourceMaterial_sourceMaterialType', blank=True)
    sourceMaterialType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_sourceMaterialState = 'TODO'
    sourceMaterialState_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_sourceMaterialState}, related_name='SubstanceSourceMaterial_sourceMaterialState', blank=True)
    sourceMaterialState_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    organismId = models.OneToOneField("FHIR_GP_Identifier", related_name='SubstanceSourceMaterial_organismId', null=True, blank=True, on_delete=models.SET_NULL)
    organismName = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_developmentStage = 'TODO'
    developmentStage_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_developmentStage}, related_name='SubstanceSourceMaterial_developmentStage', blank=True)
    developmentStage_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_SubstanceSourceMaterial_parentSubstanceId(FHIR_GP_Identifier):
    SubstanceSourceMaterial = models.ForeignKey(FHIR_SubstanceSourceMaterial, related_name='SubstanceSourceMaterial_parentSubstanceId', null=False, on_delete=models.CASCADE)

class FHIR_SubstanceSourceMaterial_parentSubstanceName(models.Model):
    SubstanceSourceMaterial = models.ForeignKey(FHIR_SubstanceSourceMaterial, related_name='SubstanceSourceMaterial_parentSubstanceName', null=False, on_delete=models.CASCADE)
    
    parentSubstanceName = FHIR_primitive_StringField(null=True, blank=True, )
    
class FHIR_SubstanceSourceMaterial_countryOfOrigin(models.Model):
    SubstanceSourceMaterial = models.ForeignKey(FHIR_SubstanceSourceMaterial, related_name='SubstanceSourceMaterial_countryOfOrigin', null=False, on_delete=models.CASCADE)
    BINDING_countryOfOrigin = 'TODO'
    countryOfOrigin_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_countryOfOrigin}, related_name='SubstanceSourceMaterial_countryOfOrigin', blank=True)
    countryOfOrigin_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_SubstanceSourceMaterial_geographicalLocation(models.Model):
    SubstanceSourceMaterial = models.ForeignKey(FHIR_SubstanceSourceMaterial, related_name='SubstanceSourceMaterial_geographicalLocation', null=False, on_delete=models.CASCADE)
    
    geographicalLocation = FHIR_primitive_StringField(null=True, blank=True, )
    
class FHIR_SubstanceSourceMaterial_fractionDescription(models.Model):
    SubstanceSourceMaterial = models.ForeignKey(FHIR_SubstanceSourceMaterial, related_name='SubstanceSourceMaterial_fractionDescription', null=False, on_delete=models.CASCADE)
    fraction = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_materialType = 'TODO'
    materialType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_materialType}, related_name='SubstanceSourceMaterial_fractionDescription_materialType', blank=True)
    materialType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_SubstanceSourceMaterial_organism(models.Model):
    SubstanceSourceMaterial = models.ForeignKey(FHIR_SubstanceSourceMaterial, related_name='SubstanceSourceMaterial_organism', null=False, on_delete=models.CASCADE)
    BINDING_family = 'TODO'
    family_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_family}, related_name='SubstanceSourceMaterial_organism_family', blank=True)
    family_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_genus = 'TODO'
    genus_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_genus}, related_name='SubstanceSourceMaterial_organism_genus', blank=True)
    genus_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_species = 'TODO'
    species_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_species}, related_name='SubstanceSourceMaterial_organism_species', blank=True)
    species_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_intraspecificType = 'TODO'
    intraspecificType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_intraspecificType}, related_name='SubstanceSourceMaterial_organism_intraspecificType', blank=True)
    intraspecificType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    intraspecificDescription = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_SubstanceSourceMaterial_organism_author(models.Model):
    SubstanceSourceMaterial_organism = models.ForeignKey(FHIR_SubstanceSourceMaterial_organism, related_name='SubstanceSourceMaterial_organism_author', null=False, on_delete=models.CASCADE)
    BINDING_authorType = 'TODO'
    authorType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_authorType}, related_name='SubstanceSourceMaterial_organism_author_authorType', blank=True)
    authorType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    authorDescription = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_SubstanceSourceMaterial_organism_hybrid(models.Model):
    SubstanceSourceMaterial_organism = models.ForeignKey(FHIR_SubstanceSourceMaterial_organism, related_name='SubstanceSourceMaterial_organism_hybrid', null=False, on_delete=models.CASCADE)
    maternalOrganismId = FHIR_primitive_StringField(null=True, blank=True, )
    maternalOrganismName = FHIR_primitive_StringField(null=True, blank=True, )
    paternalOrganismId = FHIR_primitive_StringField(null=True, blank=True, )
    paternalOrganismName = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_hybridType = 'TODO'
    hybridType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_hybridType}, related_name='SubstanceSourceMaterial_organism_hybrid_hybridType', blank=True)
    hybridType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_SubstanceSourceMaterial_organism_organismGeneral(models.Model):
    SubstanceSourceMaterial_organism = models.ForeignKey(FHIR_SubstanceSourceMaterial_organism, related_name='SubstanceSourceMaterial_organism_organismGeneral', null=False, on_delete=models.CASCADE)
    BINDING_kingdom = 'TODO'
    kingdom_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_kingdom}, related_name='SubstanceSourceMaterial_organism_organismGeneral_kingdom', blank=True)
    kingdom_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_phylum = 'TODO'
    phylum_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_phylum}, related_name='SubstanceSourceMaterial_organism_organismGeneral_phylum', blank=True)
    phylum_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_class = 'TODO'
    class_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_class}, related_name='SubstanceSourceMaterial_organism_organismGeneral_class', blank=True)
    class_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_order = 'TODO'
    order_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_order}, related_name='SubstanceSourceMaterial_organism_organismGeneral_order', blank=True)
    order_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_SubstanceSourceMaterial_partDescription(models.Model):
    SubstanceSourceMaterial = models.ForeignKey(FHIR_SubstanceSourceMaterial, related_name='SubstanceSourceMaterial_partDescription', null=False, on_delete=models.CASCADE)
    BINDING_part = 'TODO'
    part_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_part}, related_name='SubstanceSourceMaterial_partDescription_part', blank=True)
    part_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_partLocation = 'TODO'
    partLocation_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_partLocation}, related_name='SubstanceSourceMaterial_partDescription_partLocation', blank=True)
    partLocation_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
