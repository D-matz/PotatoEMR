#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_MolecularSequence(models.Model):
    class TypeChoices(models.TextChoices): AA = 'aa', 'Aa'; DNA = 'dna', 'Dna'; RNA = 'rna', 'Rna'; 
    type = FHIR_primitive_CodeField(choices=TypeChoices.choices, null=True, blank=True, )

class FHIR_MolecularSequence_identifier(FHIR_GP_Identifier):
    MolecularSequence = models.ForeignKey(FHIR_MolecularSequence, related_name='MolecularSequence_identifier', null=False, on_delete=models.CASCADE)

class FHIR_MolecularSequence_literal(models.Model):
    MolecularSequence = models.ForeignKey(FHIR_MolecularSequence, related_name='MolecularSequence_literal', null=False, on_delete=models.CASCADE)
    sequenceValue = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_MolecularSequence_file(FHIR_GP_Attachment):
    MolecularSequence = models.ForeignKey(FHIR_MolecularSequence, related_name='MolecularSequence_file', null=False, on_delete=models.CASCADE)

class FHIR_MolecularSequence_relative(models.Model):
    MolecularSequence = models.ForeignKey(FHIR_MolecularSequence, related_name='MolecularSequence_relative', null=False, on_delete=models.CASCADE)
    startingSequence = models.ForeignKey("FHIR_MolecularSequence", related_name="MolecularSequence_relative_startingSequence", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_MolecularSequence_relative_edit(models.Model):
    MolecularSequence_relative = models.ForeignKey(FHIR_MolecularSequence_relative, related_name='MolecularSequence_relative_edit', null=False, on_delete=models.CASCADE)
    BINDING_coordinateSystem = 'TODO'
    coordinateSystem_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_coordinateSystem}, related_name='MolecularSequence_relative_edit_coordinateSystem', blank=True)
    coordinateSystem_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    replacementSequence = models.ForeignKey("FHIR_MolecularSequence", related_name="MolecularSequence_relative_edit_replacementSequence", null=True, blank=True, on_delete=models.SET_NULL)
    replacedSequence = models.ForeignKey("FHIR_MolecularSequence", related_name="MolecularSequence_relative_edit_replacedSequence", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_MolecularSequence_extracted(models.Model):
    MolecularSequence = models.ForeignKey(FHIR_MolecularSequence, related_name='MolecularSequence_extracted', null=False, on_delete=models.CASCADE)
    startingSequence = models.ForeignKey("FHIR_MolecularSequence", related_name="MolecularSequence_extracted_startingSequence", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_coordinateSystem = 'TODO'
    coordinateSystem_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_coordinateSystem}, related_name='MolecularSequence_extracted_coordinateSystem', blank=True)
    coordinateSystem_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    reverseComplement = FHIR_primitive_BooleanField(null=True, blank=True, )

class FHIR_MolecularSequence_repeated(models.Model):
    MolecularSequence = models.ForeignKey(FHIR_MolecularSequence, related_name='MolecularSequence_repeated', null=False, on_delete=models.CASCADE)
    sequenceMotif = models.ForeignKey("FHIR_MolecularSequence", related_name="MolecularSequence_repeated_sequenceMotif", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_MolecularSequence_concatenated(models.Model):
    MolecularSequence = models.ForeignKey(FHIR_MolecularSequence, related_name='MolecularSequence_concatenated', null=False, on_delete=models.CASCADE)

class FHIR_MolecularSequence_concatenated_sequenceElement(models.Model):
    MolecularSequence_concatenated = models.ForeignKey(FHIR_MolecularSequence_concatenated, related_name='MolecularSequence_concatenated_sequenceElement', null=False, on_delete=models.CASCADE)
    sequence = models.ForeignKey("FHIR_MolecularSequence", related_name="MolecularSequence_concatenated_sequenceElement_sequence", null=True, blank=True, on_delete=models.SET_NULL)
