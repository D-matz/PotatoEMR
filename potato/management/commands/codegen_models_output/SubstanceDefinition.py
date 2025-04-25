
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_SubstanceDefinition(models.Model):
    version = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_status = 'TODO'
    status_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_status}, related_name='SubstanceDefinition_status', blank=True)
    status_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_domain = 'TODO'
    domain_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_domain}, related_name='SubstanceDefinition_domain', blank=True)
    domain_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    informationSource = models.ManyToManyField("FHIR_Citation", related_name="SubstanceDefinition_informationSource", blank=True)
    manufacturer = models.ManyToManyField("FHIR_Organization", related_name="SubstanceDefinition_manufacturer", blank=True)
    supplier = models.ManyToManyField("FHIR_Organization", related_name="SubstanceDefinition_supplier", blank=True)
    referenceInformation = models.ForeignKey("FHIR_SubstanceReferenceInformation", related_name="SubstanceDefinition_referenceInformation", null=True, blank=True, on_delete=models.SET_NULL)
    nucleicAcid = models.ForeignKey("FHIR_SubstanceNucleicAcid", related_name="SubstanceDefinition_nucleicAcid", null=True, blank=True, on_delete=models.SET_NULL)
    polymer = models.ForeignKey("FHIR_SubstancePolymer", related_name="SubstanceDefinition_polymer", null=True, blank=True, on_delete=models.SET_NULL)
    protein = models.ForeignKey("FHIR_SubstanceProtein", related_name="SubstanceDefinition_protein", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_SubstanceDefinition_identifier(FHIR_GP_Identifier):
    SubstanceDefinition = models.ForeignKey(FHIR_SubstanceDefinition, related_name='SubstanceDefinition_identifier', null=False, on_delete=models.CASCADE)

class FHIR_SubstanceDefinition_classification(models.Model):
    SubstanceDefinition = models.ForeignKey(FHIR_SubstanceDefinition, related_name='SubstanceDefinition_classification', null=False, on_delete=models.CASCADE)
    BINDING_classification = 'TODO'
    classification_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_classification}, related_name='SubstanceDefinition_classification', blank=True)
    classification_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_SubstanceDefinition_grade(models.Model):
    SubstanceDefinition = models.ForeignKey(FHIR_SubstanceDefinition, related_name='SubstanceDefinition_grade', null=False, on_delete=models.CASCADE)
    BINDING_grade = 'TODO'
    grade_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_grade}, related_name='SubstanceDefinition_grade', blank=True)
    grade_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_SubstanceDefinition_note(FHIR_GP_Annotation):
    SubstanceDefinition = models.ForeignKey(FHIR_SubstanceDefinition, related_name='SubstanceDefinition_note', null=False, on_delete=models.CASCADE)

class FHIR_SubstanceDefinition_moiety(models.Model):
    SubstanceDefinition = models.ForeignKey(FHIR_SubstanceDefinition, related_name='SubstanceDefinition_moiety', null=False, on_delete=models.CASCADE)
    BINDING_role = 'TODO'
    role_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_role}, related_name='SubstanceDefinition_moiety_role', blank=True)
    role_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    identifier = models.OneToOneField("FHIR_GP_Identifier", related_name='SubstanceDefinition_moiety_identifier', null=True, blank=True, on_delete=models.SET_NULL)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_stereochemistry = 'TODO'
    stereochemistry_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_stereochemistry}, related_name='SubstanceDefinition_moiety_stereochemistry', blank=True)
    stereochemistry_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_opticalActivity = 'TODO'
    opticalActivity_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_opticalActivity}, related_name='SubstanceDefinition_moiety_opticalActivity', blank=True)
    opticalActivity_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    molecularFormula = FHIR_primitive_StringField(null=True, blank=True, )
    amount = models.OneToOneField("FHIR_GP_Quantity", related_name='SubstanceDefinition_moiety_amount', null=True, blank=True, on_delete=models.SET_NULL)
    amount = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_measurementType = 'TODO'
    measurementType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_measurementType}, related_name='SubstanceDefinition_moiety_measurementType', blank=True)
    measurementType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_SubstanceDefinition_characterization(models.Model):
    SubstanceDefinition = models.ForeignKey(FHIR_SubstanceDefinition, related_name='SubstanceDefinition_characterization', null=False, on_delete=models.CASCADE)
    BINDING_technique = 'TODO'
    technique_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_technique}, related_name='SubstanceDefinition_characterization_technique', blank=True)
    technique_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_form = 'TODO'
    form_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_form}, related_name='SubstanceDefinition_characterization_form', blank=True)
    form_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_SubstanceDefinition_characterization_file(FHIR_GP_Attachment):
    SubstanceDefinition_characterization = models.ForeignKey(FHIR_SubstanceDefinition_characterization, related_name='SubstanceDefinition_characterization_file', null=False, on_delete=models.CASCADE)

class FHIR_SubstanceDefinition_property(models.Model):
    SubstanceDefinition = models.ForeignKey(FHIR_SubstanceDefinition, related_name='SubstanceDefinition_property', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='SubstanceDefinition_property_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_value = 'TODO'
    value_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_value}, related_name='SubstanceDefinition_property_value', blank=True)
    value_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value = models.OneToOneField("FHIR_GP_Quantity", related_name='SubstanceDefinition_property_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = FHIR_primitive_DateField(null=True, blank=True, )
    value = FHIR_primitive_BooleanField(null=True, blank=True, )
    value = models.OneToOneField("FHIR_GP_Attachment", related_name='SubstanceDefinition_property_value', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_SubstanceDefinition_molecularWeight(models.Model):
    SubstanceDefinition = models.ForeignKey(FHIR_SubstanceDefinition, related_name='SubstanceDefinition_molecularWeight', null=False, on_delete=models.CASCADE)
    BINDING_method = 'TODO'
    method_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_method}, related_name='SubstanceDefinition_molecularWeight_method', blank=True)
    method_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='SubstanceDefinition_molecularWeight_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    amount = models.OneToOneField("FHIR_GP_Quantity", related_name='SubstanceDefinition_molecularWeight_amount', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_SubstanceDefinition_structure(models.Model):
    SubstanceDefinition = models.ForeignKey(FHIR_SubstanceDefinition, related_name='SubstanceDefinition_structure', null=False, on_delete=models.CASCADE)
    BINDING_stereochemistry = 'TODO'
    stereochemistry_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_stereochemistry}, related_name='SubstanceDefinition_structure_stereochemistry', blank=True)
    stereochemistry_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_opticalActivity = 'TODO'
    opticalActivity_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_opticalActivity}, related_name='SubstanceDefinition_structure_opticalActivity', blank=True)
    opticalActivity_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    molecularFormula = FHIR_primitive_StringField(null=True, blank=True, )
    molecularFormulaByMoiety = FHIR_primitive_StringField(null=True, blank=True, )
    sourceDocument = models.ManyToManyField("FHIR_DocumentReference", related_name="SubstanceDefinition_structure_sourceDocument", blank=True)

class FHIR_SubstanceDefinition_structure_technique(models.Model):
    SubstanceDefinition_structure = models.ForeignKey(FHIR_SubstanceDefinition_structure, related_name='SubstanceDefinition_structure_technique', null=False, on_delete=models.CASCADE)
    BINDING_technique = 'TODO'
    technique_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_technique}, related_name='SubstanceDefinition_structure_technique', blank=True)
    technique_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_SubstanceDefinition_structure_representation(models.Model):
    SubstanceDefinition_structure = models.ForeignKey(FHIR_SubstanceDefinition_structure, related_name='SubstanceDefinition_structure_representation', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='SubstanceDefinition_structure_representation_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    representation = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_format = 'TODO'
    format_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_format}, related_name='SubstanceDefinition_structure_representation_format', blank=True)
    format_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    document = models.ForeignKey("FHIR_DocumentReference", related_name="SubstanceDefinition_structure_representation_document", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_SubstanceDefinition_code(models.Model):
    SubstanceDefinition = models.ForeignKey(FHIR_SubstanceDefinition, related_name='SubstanceDefinition_code', null=False, on_delete=models.CASCADE)
    BINDING_code = 'TODO'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='SubstanceDefinition_code_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_status = 'TODO'
    status_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_status}, related_name='SubstanceDefinition_code_status', blank=True)
    status_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    statusDate = FHIR_primitive_DateTimeField(null=True, blank=True, )
    source = models.ManyToManyField("FHIR_DocumentReference", related_name="SubstanceDefinition_code_source", blank=True)

class FHIR_SubstanceDefinition_code_note(FHIR_GP_Annotation):
    SubstanceDefinition_code = models.ForeignKey(FHIR_SubstanceDefinition_code, related_name='SubstanceDefinition_code_note', null=False, on_delete=models.CASCADE)

class FHIR_SubstanceDefinition_name(models.Model):
    SubstanceDefinition = models.ForeignKey(FHIR_SubstanceDefinition, related_name='SubstanceDefinition_name', null=False, on_delete=models.CASCADE)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='SubstanceDefinition_name_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_status = 'TODO'
    status_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_status}, related_name='SubstanceDefinition_name_status', blank=True)
    status_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    preferred = FHIR_primitive_BooleanField(null=True, blank=True, )
    source = models.ManyToManyField("FHIR_DocumentReference", related_name="SubstanceDefinition_name_source", blank=True)

class FHIR_SubstanceDefinition_name_language(models.Model):
    SubstanceDefinition_name = models.ForeignKey(FHIR_SubstanceDefinition_name, related_name='SubstanceDefinition_name_language', null=False, on_delete=models.CASCADE)
    BINDING_language = 'TODO'
    language_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_language}, related_name='SubstanceDefinition_name_language', blank=True)
    language_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_SubstanceDefinition_name_domain(models.Model):
    SubstanceDefinition_name = models.ForeignKey(FHIR_SubstanceDefinition_name, related_name='SubstanceDefinition_name_domain', null=False, on_delete=models.CASCADE)
    BINDING_domain = 'TODO'
    domain_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_domain}, related_name='SubstanceDefinition_name_domain', blank=True)
    domain_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_SubstanceDefinition_name_jurisdiction(models.Model):
    SubstanceDefinition_name = models.ForeignKey(FHIR_SubstanceDefinition_name, related_name='SubstanceDefinition_name_jurisdiction', null=False, on_delete=models.CASCADE)
    BINDING_jurisdiction = 'TODO'
    jurisdiction_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_jurisdiction}, related_name='SubstanceDefinition_name_jurisdiction', blank=True)
    jurisdiction_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_SubstanceDefinition_name_official(models.Model):
    SubstanceDefinition_name = models.ForeignKey(FHIR_SubstanceDefinition_name, related_name='SubstanceDefinition_name_official', null=False, on_delete=models.CASCADE)
    BINDING_authority = 'TODO'
    authority_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_authority}, related_name='SubstanceDefinition_name_official_authority', blank=True)
    authority_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_status = 'TODO'
    status_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_status}, related_name='SubstanceDefinition_name_official_status', blank=True)
    status_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    date = FHIR_primitive_DateTimeField(null=True, blank=True, )

class FHIR_SubstanceDefinition_relationship(models.Model):
    SubstanceDefinition = models.ForeignKey(FHIR_SubstanceDefinition, related_name='SubstanceDefinition_relationship', null=False, on_delete=models.CASCADE)
    substanceDefinition = models.ForeignKey("FHIR_SubstanceDefinition", related_name="SubstanceDefinition_relationship_substanceDefinition", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_substanceDefinition = 'TODO'
    substanceDefinition_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_substanceDefinition}, related_name='SubstanceDefinition_relationship_substanceDefinition', blank=True)
    substanceDefinition_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='SubstanceDefinition_relationship_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    isDefining = FHIR_primitive_BooleanField(null=True, blank=True, )
    amount = models.OneToOneField("FHIR_GP_Quantity", related_name='SubstanceDefinition_relationship_amount', null=True, blank=True, on_delete=models.SET_NULL)
    amount = models.OneToOneField("FHIR_GP_Ratio", related_name='SubstanceDefinition_relationship_amount', null=True, blank=True, on_delete=models.SET_NULL)
    amount = FHIR_primitive_StringField(null=True, blank=True, )
    ratioHighLimitAmount = models.OneToOneField("FHIR_GP_Ratio", related_name='SubstanceDefinition_relationship_ratioHighLimitAmount', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_comparator = 'TODO'
    comparator_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_comparator}, related_name='SubstanceDefinition_relationship_comparator', blank=True)
    comparator_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    source = models.ManyToManyField("FHIR_DocumentReference", related_name="SubstanceDefinition_relationship_source", blank=True)

class FHIR_SubstanceDefinition_sourceMaterial(models.Model):
    SubstanceDefinition = models.ForeignKey(FHIR_SubstanceDefinition, related_name='SubstanceDefinition_sourceMaterial', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='SubstanceDefinition_sourceMaterial_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_genus = 'TODO'
    genus_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_genus}, related_name='SubstanceDefinition_sourceMaterial_genus', blank=True)
    genus_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_species = 'TODO'
    species_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_species}, related_name='SubstanceDefinition_sourceMaterial_species', blank=True)
    species_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_part = 'TODO'
    part_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_part}, related_name='SubstanceDefinition_sourceMaterial_part', blank=True)
    part_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_SubstanceDefinition_sourceMaterial_countryOfOrigin(models.Model):
    SubstanceDefinition_sourceMaterial = models.ForeignKey(FHIR_SubstanceDefinition_sourceMaterial, related_name='SubstanceDefinition_sourceMaterial_countryOfOrigin', null=False, on_delete=models.CASCADE)
    BINDING_countryOfOrigin = 'TODO'
    countryOfOrigin_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_countryOfOrigin}, related_name='SubstanceDefinition_sourceMaterial_countryOfOrigin', blank=True)
    countryOfOrigin_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    