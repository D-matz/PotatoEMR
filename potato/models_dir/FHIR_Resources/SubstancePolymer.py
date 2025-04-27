#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_SubstancePolymer(models.Model):
    identifier = models.OneToOneField("FHIR_GP_Identifier", related_name='SubstancePolymer_identifier', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_class = 'TODO'
    class_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_class}, related_name='SubstancePolymer_class', blank=True)
    class_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_geometry = 'TODO'
    geometry_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_geometry}, related_name='SubstancePolymer_geometry', blank=True)
    geometry_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    modification = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_SubstancePolymer_copolymerConnectivity(models.Model):
    SubstancePolymer = models.ForeignKey(FHIR_SubstancePolymer, related_name='SubstancePolymer_copolymerConnectivity', null=False, on_delete=models.CASCADE)
    BINDING_copolymerConnectivity = 'TODO'
    copolymerConnectivity_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_copolymerConnectivity}, related_name='SubstancePolymer_copolymerConnectivity', blank=True)
    copolymerConnectivity_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_SubstancePolymer_monomerSet(models.Model):
    SubstancePolymer = models.ForeignKey(FHIR_SubstancePolymer, related_name='SubstancePolymer_monomerSet', null=False, on_delete=models.CASCADE)
    BINDING_ratioType = 'TODO'
    ratioType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_ratioType}, related_name='SubstancePolymer_monomerSet_ratioType', blank=True)
    ratioType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_SubstancePolymer_monomerSet_startingMaterial(models.Model):
    SubstancePolymer_monomerSet = models.ForeignKey(FHIR_SubstancePolymer_monomerSet, related_name='SubstancePolymer_monomerSet_startingMaterial', null=False, on_delete=models.CASCADE)
    BINDING_code = 'TODO'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='SubstancePolymer_monomerSet_startingMaterial_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_category = 'TODO'
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='SubstancePolymer_monomerSet_startingMaterial_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    isDefining = FHIR_primitive_BooleanField(null=True, blank=True, )
    amount = models.OneToOneField("FHIR_GP_Quantity", related_name='SubstancePolymer_monomerSet_startingMaterial_amount', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_SubstancePolymer_repeat(models.Model):
    SubstancePolymer = models.ForeignKey(FHIR_SubstancePolymer, related_name='SubstancePolymer_repeat', null=False, on_delete=models.CASCADE)
    averageMolecularFormula = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_repeatUnitAmountType = 'TODO'
    repeatUnitAmountType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_repeatUnitAmountType}, related_name='SubstancePolymer_repeat_repeatUnitAmountType', blank=True)
    repeatUnitAmountType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_SubstancePolymer_repeat_repeatUnit(models.Model):
    SubstancePolymer_repeat = models.ForeignKey(FHIR_SubstancePolymer_repeat, related_name='SubstancePolymer_repeat_repeatUnit', null=False, on_delete=models.CASCADE)
    unit = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_orientation = 'TODO'
    orientation_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_orientation}, related_name='SubstancePolymer_repeat_repeatUnit_orientation', blank=True)
    orientation_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_SubstancePolymer_repeat_repeatUnit_degreeOfPolymerisation(models.Model):
    SubstancePolymer_repeat_repeatUnit = models.ForeignKey(FHIR_SubstancePolymer_repeat_repeatUnit, related_name='SubstancePolymer_repeat_repeatUnit_degreeOfPolymerisation', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='SubstancePolymer_repeat_repeatUnit_degreeOfPolymerisation_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_SubstancePolymer_repeat_repeatUnit_structuralRepresentation(models.Model):
    SubstancePolymer_repeat_repeatUnit = models.ForeignKey(FHIR_SubstancePolymer_repeat_repeatUnit, related_name='SubstancePolymer_repeat_repeatUnit_structuralRepresentation', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='SubstancePolymer_repeat_repeatUnit_structuralRepresentation_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    representation = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_format = 'TODO'
    format_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_format}, related_name='SubstancePolymer_repeat_repeatUnit_structuralRepresentation_format', blank=True)
    format_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    attachment = models.OneToOneField("FHIR_GP_Attachment", related_name='SubstancePolymer_repeat_repeatUnit_structuralRepresentation_attachment', null=True, blank=True, on_delete=models.SET_NULL)
