
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_MolecularDefinition(models.Model):
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    BINDING_moleculeType = 'TODO'
    moleculeType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_moleculeType}, related_name='MolecularDefinition_moleculeType', blank=True)
    moleculeType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    member = models.ManyToManyField("FHIR_MolecularDefinition", related_name="MolecularDefinition_member", blank=True)

class FHIR_MolecularDefinition_identifier(FHIR_GP_Identifier):
    MolecularDefinition = models.ForeignKey(FHIR_MolecularDefinition, related_name='MolecularDefinition_identifier', null=False, on_delete=models.CASCADE)

class FHIR_MolecularDefinition_type(models.Model):
    MolecularDefinition = models.ForeignKey(FHIR_MolecularDefinition, related_name='MolecularDefinition_type', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='MolecularDefinition_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_MolecularDefinition_topology(models.Model):
    MolecularDefinition = models.ForeignKey(FHIR_MolecularDefinition, related_name='MolecularDefinition_topology', null=False, on_delete=models.CASCADE)
    BINDING_topology = 'TODO'
    topology_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_topology}, related_name='MolecularDefinition_topology', blank=True)
    topology_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_MolecularDefinition_location(models.Model):
    MolecularDefinition = models.ForeignKey(FHIR_MolecularDefinition, related_name='MolecularDefinition_location', null=False, on_delete=models.CASCADE)

class FHIR_MolecularDefinition_location_sequenceLocation(models.Model):
    MolecularDefinition_location = models.ForeignKey(FHIR_MolecularDefinition_location, related_name='MolecularDefinition_location_sequenceLocation', null=False, on_delete=models.CASCADE)
    sequenceContext = models.ForeignKey("FHIR_MolecularDefinition", related_name="MolecularDefinition_location_sequenceLocation_sequenceContext", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_strand = 'TODO'
    strand_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_strand}, related_name='MolecularDefinition_location_sequenceLocation_strand', blank=True)
    strand_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_MolecularDefinition_location_sequenceLocation_coordinateInterval(models.Model):
    MolecularDefinition_location_sequenceLocation = models.ForeignKey(FHIR_MolecularDefinition_location_sequenceLocation, related_name='MolecularDefinition_location_sequenceLocation_coordinateInterval', null=False, on_delete=models.CASCADE)
    start = models.OneToOneField("FHIR_GP_Quantity", related_name='MolecularDefinition_location_sequenceLocation_coordinateInterval_start', null=True, blank=True, on_delete=models.SET_NULL)
    start = models.OneToOneField("FHIR_GP_Range", related_name='MolecularDefinition_location_sequenceLocation_coordinateInterval_start', null=True, blank=True, on_delete=models.SET_NULL)
    end = models.OneToOneField("FHIR_GP_Quantity", related_name='MolecularDefinition_location_sequenceLocation_coordinateInterval_end', null=True, blank=True, on_delete=models.SET_NULL)
    end = models.OneToOneField("FHIR_GP_Range", related_name='MolecularDefinition_location_sequenceLocation_coordinateInterval_end', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_MolecularDefinition_location_sequenceLocation_coordinateInterval_coordinateSystem(models.Model):
    MolecularDefinition_location_sequenceLocation_coordinateInterval = models.ForeignKey(FHIR_MolecularDefinition_location_sequenceLocation_coordinateInterval, related_name='MolecularDefinition_location_sequenceLocation_coordinateInterval_coordinateSystem', null=False, on_delete=models.CASCADE)
    BINDING_system = 'TODO'
    system_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_system}, related_name='MolecularDefinition_location_sequenceLocation_coordinateInterval_coordinateSystem_system', blank=True)
    system_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_origin = 'TODO'
    origin_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_origin}, related_name='MolecularDefinition_location_sequenceLocation_coordinateInterval_coordinateSystem_origin', blank=True)
    origin_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_normalizationMethod = 'TODO'
    normalizationMethod_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_normalizationMethod}, related_name='MolecularDefinition_location_sequenceLocation_coordinateInterval_coordinateSystem_normalizationMethod', blank=True)
    normalizationMethod_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_MolecularDefinition_location_cytobandLocation(models.Model):
    MolecularDefinition_location = models.ForeignKey(FHIR_MolecularDefinition_location, related_name='MolecularDefinition_location_cytobandLocation', null=False, on_delete=models.CASCADE)

class FHIR_MolecularDefinition_location_cytobandLocation_genomeAssembly(models.Model):
    MolecularDefinition_location_cytobandLocation = models.ForeignKey(FHIR_MolecularDefinition_location_cytobandLocation, related_name='MolecularDefinition_location_cytobandLocation_genomeAssembly', null=False, on_delete=models.CASCADE)
    BINDING_organism = 'TODO'
    organism_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_organism}, related_name='MolecularDefinition_location_cytobandLocation_genomeAssembly_organism', blank=True)
    organism_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_build = 'TODO'
    build_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_build}, related_name='MolecularDefinition_location_cytobandLocation_genomeAssembly_build', blank=True)
    build_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_accession = 'TODO'
    accession_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_accession}, related_name='MolecularDefinition_location_cytobandLocation_genomeAssembly_accession', blank=True)
    accession_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    description = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_MolecularDefinition_location_cytobandLocation_cytobandInterval(models.Model):
    MolecularDefinition_location_cytobandLocation = models.ForeignKey(FHIR_MolecularDefinition_location_cytobandLocation, related_name='MolecularDefinition_location_cytobandLocation_cytobandInterval', null=False, on_delete=models.CASCADE)
    BINDING_chromosome = 'TODO'
    chromosome_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_chromosome}, related_name='MolecularDefinition_location_cytobandLocation_cytobandInterval_chromosome', blank=True)
    chromosome_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_MolecularDefinition_location_cytobandLocation_cytobandInterval_startCytoband(models.Model):
    MolecularDefinition_location_cytobandLocation_cytobandInterval = models.ForeignKey(FHIR_MolecularDefinition_location_cytobandLocation_cytobandInterval, related_name='MolecularDefinition_location_cytobandLocation_cytobandInterval_startCytoband', null=False, on_delete=models.CASCADE)
    class ArmChoices(models.TextChoices): ARM = 'Arm', 'Arm'; 
    arm = FHIR_primitive_CodeField(choices=ArmChoices.choices, null=True, blank=True, )
    arm = FHIR_primitive_StringField(null=True, blank=True, )
    class RegionChoices(models.TextChoices): REGION = 'Region', 'Region'; 
    region = FHIR_primitive_CodeField(choices=RegionChoices.choices, null=True, blank=True, )
    region = FHIR_primitive_StringField(null=True, blank=True, )
    class BandChoices(models.TextChoices): BAND = 'Band', 'Band'; 
    band = FHIR_primitive_CodeField(choices=BandChoices.choices, null=True, blank=True, )
    band = FHIR_primitive_StringField(null=True, blank=True, )
    class SubbandChoices(models.TextChoices): SUB_BAND = 'Sub-band', 'Sub-band'; 
    subBand = FHIR_primitive_CodeField(choices=SubbandChoices.choices, null=True, blank=True, )
    subBand = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_MolecularDefinition_location_cytobandLocation_cytobandInterval_endCytoband(models.Model):
    MolecularDefinition_location_cytobandLocation_cytobandInterval = models.ForeignKey(FHIR_MolecularDefinition_location_cytobandLocation_cytobandInterval, related_name='MolecularDefinition_location_cytobandLocation_cytobandInterval_endCytoband', null=False, on_delete=models.CASCADE)
    class ArmChoices(models.TextChoices): ARM = 'Arm', 'Arm'; 
    arm = FHIR_primitive_CodeField(choices=ArmChoices.choices, null=True, blank=True, )
    arm = FHIR_primitive_StringField(null=True, blank=True, )
    class RegionChoices(models.TextChoices): REGION = 'Region', 'Region'; 
    region = FHIR_primitive_CodeField(choices=RegionChoices.choices, null=True, blank=True, )
    region = FHIR_primitive_StringField(null=True, blank=True, )
    class BandChoices(models.TextChoices): BAND = 'Band', 'Band'; 
    band = FHIR_primitive_CodeField(choices=BandChoices.choices, null=True, blank=True, )
    band = FHIR_primitive_StringField(null=True, blank=True, )
    class SubbandChoices(models.TextChoices): SUBAND = 'SuBand', 'Suband'; 
    subBand = FHIR_primitive_CodeField(choices=SubbandChoices.choices, null=True, blank=True, )
    subBand = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_MolecularDefinition_representation(models.Model):
    MolecularDefinition = models.ForeignKey(FHIR_MolecularDefinition, related_name='MolecularDefinition_representation', null=False, on_delete=models.CASCADE)
    BINDING_focus = 'TODO'
    focus_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_focus}, related_name='MolecularDefinition_representation_focus', blank=True)
    focus_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    resolvable = models.ForeignKey("FHIR_DocumentReference", related_name="MolecularDefinition_representation_resolvable", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_MolecularDefinition_representation_code(models.Model):
    MolecularDefinition_representation = models.ForeignKey(FHIR_MolecularDefinition_representation, related_name='MolecularDefinition_representation_code', null=False, on_delete=models.CASCADE)
    BINDING_code = 'TODO'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='MolecularDefinition_representation_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_MolecularDefinition_representation_literal(models.Model):
    MolecularDefinition_representation = models.ForeignKey(FHIR_MolecularDefinition_representation, related_name='MolecularDefinition_representation_literal', null=False, on_delete=models.CASCADE)
    BINDING_encoding = 'TODO'
    encoding_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_encoding}, related_name='MolecularDefinition_representation_literal_encoding', blank=True)
    encoding_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_MolecularDefinition_representation_extracted(models.Model):
    MolecularDefinition_representation = models.ForeignKey(FHIR_MolecularDefinition_representation, related_name='MolecularDefinition_representation_extracted', null=False, on_delete=models.CASCADE)
    startingMolecule = models.ForeignKey("FHIR_MolecularDefinition", related_name="MolecularDefinition_representation_extracted_startingMolecule", null=True, blank=True, on_delete=models.SET_NULL)
    reverseComplement = FHIR_primitive_BooleanField(null=True, blank=True, )

class FHIR_MolecularDefinition_representation_extracted_coordinateInterval(models.Model):
    MolecularDefinition_representation_extracted = models.ForeignKey(FHIR_MolecularDefinition_representation_extracted, related_name='MolecularDefinition_representation_extracted_coordinateInterval', null=False, on_delete=models.CASCADE)
    start = models.OneToOneField("FHIR_GP_Quantity", related_name='MolecularDefinition_representation_extracted_coordinateInterval_start', null=True, blank=True, on_delete=models.SET_NULL)
    start = models.OneToOneField("FHIR_GP_Range", related_name='MolecularDefinition_representation_extracted_coordinateInterval_start', null=True, blank=True, on_delete=models.SET_NULL)
    end = models.OneToOneField("FHIR_GP_Quantity", related_name='MolecularDefinition_representation_extracted_coordinateInterval_end', null=True, blank=True, on_delete=models.SET_NULL)
    end = models.OneToOneField("FHIR_GP_Range", related_name='MolecularDefinition_representation_extracted_coordinateInterval_end', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_MolecularDefinition_representation_extracted_coordinateInterval_coordinateSystem(models.Model):
    MolecularDefinition_representation_extracted_coordinateInterval = models.ForeignKey(FHIR_MolecularDefinition_representation_extracted_coordinateInterval, related_name='MolecularDefinition_representation_extracted_coordinateInterval_coordinateSystem', null=False, on_delete=models.CASCADE)
    BINDING_system = 'TODO'
    system_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_system}, related_name='MolecularDefinition_representation_extracted_coordinateInterval_coordinateSystem_system', blank=True)
    system_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_origin = 'TODO'
    origin_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_origin}, related_name='MolecularDefinition_representation_extracted_coordinateInterval_coordinateSystem_origin', blank=True)
    origin_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_normalizationMethod = 'TODO'
    normalizationMethod_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_normalizationMethod}, related_name='MolecularDefinition_representation_extracted_coordinateInterval_coordinateSystem_normalizationMethod', blank=True)
    normalizationMethod_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_MolecularDefinition_representation_repeated(models.Model):
    MolecularDefinition_representation = models.ForeignKey(FHIR_MolecularDefinition_representation, related_name='MolecularDefinition_representation_repeated', null=False, on_delete=models.CASCADE)
    sequenceMotif = models.ForeignKey("FHIR_MolecularDefinition", related_name="MolecularDefinition_representation_repeated_sequenceMotif", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_MolecularDefinition_representation_concatenated(models.Model):
    MolecularDefinition_representation = models.ForeignKey(FHIR_MolecularDefinition_representation, related_name='MolecularDefinition_representation_concatenated', null=False, on_delete=models.CASCADE)

class FHIR_MolecularDefinition_representation_concatenated_sequenceElement(models.Model):
    MolecularDefinition_representation_concatenated = models.ForeignKey(FHIR_MolecularDefinition_representation_concatenated, related_name='MolecularDefinition_representation_concatenated_sequenceElement', null=False, on_delete=models.CASCADE)
    sequence = models.ForeignKey("FHIR_MolecularDefinition", related_name="MolecularDefinition_representation_concatenated_sequenceElement_sequence", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_MolecularDefinition_representation_relative(models.Model):
    MolecularDefinition_representation = models.ForeignKey(FHIR_MolecularDefinition_representation, related_name='MolecularDefinition_representation_relative', null=False, on_delete=models.CASCADE)
    startingMolecule = models.ForeignKey("FHIR_MolecularDefinition", related_name="MolecularDefinition_representation_relative_startingMolecule", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_MolecularDefinition_representation_relative_edit(models.Model):
    MolecularDefinition_representation_relative = models.ForeignKey(FHIR_MolecularDefinition_representation_relative, related_name='MolecularDefinition_representation_relative_edit', null=False, on_delete=models.CASCADE)
    replacementMolecule = models.ForeignKey("FHIR_MolecularDefinition", related_name="MolecularDefinition_representation_relative_edit_replacementMolecule", null=True, blank=True, on_delete=models.SET_NULL)
    replacedMolecule = models.ForeignKey("FHIR_MolecularDefinition", related_name="MolecularDefinition_representation_relative_edit_replacedMolecule", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_MolecularDefinition_representation_relative_edit_coordinateInterval(models.Model):
    MolecularDefinition_representation_relative_edit = models.ForeignKey(FHIR_MolecularDefinition_representation_relative_edit, related_name='MolecularDefinition_representation_relative_edit_coordinateInterval', null=False, on_delete=models.CASCADE)
    start = models.OneToOneField("FHIR_GP_Quantity", related_name='MolecularDefinition_representation_relative_edit_coordinateInterval_start', null=True, blank=True, on_delete=models.SET_NULL)
    start = models.OneToOneField("FHIR_GP_Range", related_name='MolecularDefinition_representation_relative_edit_coordinateInterval_start', null=True, blank=True, on_delete=models.SET_NULL)
    end = models.OneToOneField("FHIR_GP_Quantity", related_name='MolecularDefinition_representation_relative_edit_coordinateInterval_end', null=True, blank=True, on_delete=models.SET_NULL)
    end = models.OneToOneField("FHIR_GP_Range", related_name='MolecularDefinition_representation_relative_edit_coordinateInterval_end', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_MolecularDefinition_representation_relative_edit_coordinateInterval_coordinateSystem(models.Model):
    MolecularDefinition_representation_relative_edit_coordinateInterval = models.ForeignKey(FHIR_MolecularDefinition_representation_relative_edit_coordinateInterval, related_name='MolecularDefinition_representation_relative_edit_coordinateInterval_coordinateSystem', null=False, on_delete=models.CASCADE)
    BINDING_system = 'TODO'
    system_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_system}, related_name='MolecularDefinition_representation_relative_edit_coordinateInterval_coordinateSystem_system', blank=True)
    system_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_origin = 'TODO'
    origin_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_origin}, related_name='MolecularDefinition_representation_relative_edit_coordinateInterval_coordinateSystem_origin', blank=True)
    origin_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_normalizationMethod = 'TODO'
    normalizationMethod_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_normalizationMethod}, related_name='MolecularDefinition_representation_relative_edit_coordinateInterval_coordinateSystem_normalizationMethod', blank=True)
    normalizationMethod_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
