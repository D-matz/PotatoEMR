#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_MedicationKnowledge(models.Model):
    BINDING_code = 'TODO'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='MedicationKnowledge_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    class StatusChoices(models.TextChoices): DRAFT = 'draft', 'Draft'; ACTIVE = 'active', 'Active'; RETIRED = 'retired', 'Retired'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    name = FHIR_primitive_StringField(null=True, blank=True, )
    associatedMedication = models.ManyToManyField("FHIR_Medication", related_name="MedicationKnowledge_associatedMedication", blank=True)
    preparationInstruction = FHIR_primitive_MarkdownField(null=True, blank=True, )
    clinicalUseIssue = models.ManyToManyField("FHIR_ClinicalUseDefinition", related_name="MedicationKnowledge_clinicalUseIssue", blank=True)

class FHIR_MedicationKnowledge_identifier(FHIR_GP_Identifier):
    MedicationKnowledge = models.ForeignKey(FHIR_MedicationKnowledge, related_name='MedicationKnowledge_identifier', null=False, on_delete=models.CASCADE)

class FHIR_MedicationKnowledge_jurisdiction(models.Model):
    MedicationKnowledge = models.ForeignKey(FHIR_MedicationKnowledge, related_name='MedicationKnowledge_jurisdiction', null=False, on_delete=models.CASCADE)
    BINDING_jurisdiction = 'TODO'
    jurisdiction_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_jurisdiction}, related_name='MedicationKnowledge_jurisdiction', blank=True)
    jurisdiction_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_MedicationKnowledge_relatedMedicationKnowledge(models.Model):
    MedicationKnowledge = models.ForeignKey(FHIR_MedicationKnowledge, related_name='MedicationKnowledge_relatedMedicationKnowledge', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='MedicationKnowledge_relatedMedicationKnowledge_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    reference = models.ManyToManyField("FHIR_MedicationKnowledge", related_name="MedicationKnowledge_relatedMedicationKnowledge_reference", blank=True)

class FHIR_MedicationKnowledge_productType(models.Model):
    MedicationKnowledge = models.ForeignKey(FHIR_MedicationKnowledge, related_name='MedicationKnowledge_productType', null=False, on_delete=models.CASCADE)
    BINDING_productType = 'TODO'
    productType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_productType}, related_name='MedicationKnowledge_productType', blank=True)
    productType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_MedicationKnowledge_monograph(models.Model):
    MedicationKnowledge = models.ForeignKey(FHIR_MedicationKnowledge, related_name='MedicationKnowledge_monograph', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='MedicationKnowledge_monograph_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    source = models.ForeignKey("FHIR_DocumentReference", related_name="MedicationKnowledge_monograph_source", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_MedicationKnowledge_cost(models.Model):
    MedicationKnowledge = models.ForeignKey(FHIR_MedicationKnowledge, related_name='MedicationKnowledge_cost', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='MedicationKnowledge_cost_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    source = FHIR_primitive_StringField(null=True, blank=True, )
    cost = models.OneToOneField("FHIR_GP_Quantity_Money", related_name='MedicationKnowledge_cost_cost', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_cost = 'TODO'
    cost_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_cost}, related_name='MedicationKnowledge_cost_cost', blank=True)
    cost_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_MedicationKnowledge_cost_effectiveDate(FHIR_GP_Period):
    MedicationKnowledge_cost = models.ForeignKey(FHIR_MedicationKnowledge_cost, related_name='MedicationKnowledge_cost_effectiveDate', null=False, on_delete=models.CASCADE)

class FHIR_MedicationKnowledge_monitoringProgram(models.Model):
    MedicationKnowledge = models.ForeignKey(FHIR_MedicationKnowledge, related_name='MedicationKnowledge_monitoringProgram', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='MedicationKnowledge_monitoringProgram_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    name = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_MedicationKnowledge_indicationGuideline(models.Model):
    MedicationKnowledge = models.ForeignKey(FHIR_MedicationKnowledge, related_name='MedicationKnowledge_indicationGuideline', null=False, on_delete=models.CASCADE)

class FHIR_MedicationKnowledge_indicationGuideline_indication(models.Model):
    MedicationKnowledge_indicationGuideline = models.ForeignKey(FHIR_MedicationKnowledge_indicationGuideline, related_name='MedicationKnowledge_indicationGuideline_indication', null=False, on_delete=models.CASCADE)
    BINDING_indication = 'TODO'
    indication_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_indication}, related_name='MedicationKnowledge_indicationGuideline_indication', blank=True)
    indication_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    indication_ClinicalUseDefinition_ref = models.ForeignKey("FHIR_ClinicalUseDefinition", related_name="MedicationKnowledge_indicationGuideline_indication_ClinicalUseDefinition", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_MedicationKnowledge_indicationGuideline_dosingGuideline(models.Model):
    MedicationKnowledge_indicationGuideline = models.ForeignKey(FHIR_MedicationKnowledge_indicationGuideline, related_name='MedicationKnowledge_indicationGuideline_dosingGuideline', null=False, on_delete=models.CASCADE)
    BINDING_treatmentIntent = 'TODO'
    treatmentIntent_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_treatmentIntent}, related_name='MedicationKnowledge_indicationGuideline_dosingGuideline_treatmentIntent', blank=True)
    treatmentIntent_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_administrationTreatment = 'TODO'
    administrationTreatment_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_administrationTreatment}, related_name='MedicationKnowledge_indicationGuideline_dosingGuideline_administrationTreatment', blank=True)
    administrationTreatment_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_MedicationKnowledge_indicationGuideline_dosingGuideline_dosage(models.Model):
    MedicationKnowledge_indicationGuideline_dosingGuideline = models.ForeignKey(FHIR_MedicationKnowledge_indicationGuideline_dosingGuideline, related_name='MedicationKnowledge_indicationGuideline_dosingGuideline_dosage', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='MedicationKnowledge_indicationGuideline_dosingGuideline_dosage_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_MedicationKnowledge_indicationGuideline_dosingGuideline_dosage_dosage(FHIR_SP_Dosage):
    MedicationKnowledge_indicationGuideline_dosingGuideline_dosage = models.ForeignKey(FHIR_MedicationKnowledge_indicationGuideline_dosingGuideline_dosage, related_name='MedicationKnowledge_indicationGuideline_dosingGuideline_dosage_dosage', null=False, on_delete=models.CASCADE)

class FHIR_MedicationKnowledge_indicationGuideline_dosingGuideline_patientCharacteristic(models.Model):
    MedicationKnowledge_indicationGuideline_dosingGuideline = models.ForeignKey(FHIR_MedicationKnowledge_indicationGuideline_dosingGuideline, related_name='MedicationKnowledge_indicationGuideline_dosingGuideline_patientCharacteristic', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='MedicationKnowledge_indicationGuideline_dosingGuideline_patientCharacteristic_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_value = 'TODO'
    value_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_value}, related_name='MedicationKnowledge_indicationGuideline_dosingGuideline_patientCharacteristic_value', blank=True)
    value_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value = models.OneToOneField("FHIR_GP_Quantity", related_name='MedicationKnowledge_indicationGuideline_dosingGuideline_patientCharacteristic_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_Range", related_name='MedicationKnowledge_indicationGuideline_dosingGuideline_patientCharacteristic_value', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_MedicationKnowledge_medicineClassification(models.Model):
    MedicationKnowledge = models.ForeignKey(FHIR_MedicationKnowledge, related_name='MedicationKnowledge_medicineClassification', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='MedicationKnowledge_medicineClassification_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    source = FHIR_primitive_StringField(null=True, blank=True, )
    source = FHIR_primitive_URIField(null=True, blank=True, )

class FHIR_MedicationKnowledge_medicineClassification_classification(models.Model):
    MedicationKnowledge_medicineClassification = models.ForeignKey(FHIR_MedicationKnowledge_medicineClassification, related_name='MedicationKnowledge_medicineClassification_classification', null=False, on_delete=models.CASCADE)
    BINDING_classification = 'TODO'
    classification_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_classification}, related_name='MedicationKnowledge_medicineClassification_classification', blank=True)
    classification_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_MedicationKnowledge_packaging(models.Model):
    MedicationKnowledge = models.ForeignKey(FHIR_MedicationKnowledge, related_name='MedicationKnowledge_packaging', null=False, on_delete=models.CASCADE)
    packagedProduct = models.ForeignKey("FHIR_PackagedProductDefinition", related_name="MedicationKnowledge_packaging_packagedProduct", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_MedicationKnowledge_storageGuideline(models.Model):
    MedicationKnowledge = models.ForeignKey(FHIR_MedicationKnowledge, related_name='MedicationKnowledge_storageGuideline', null=False, on_delete=models.CASCADE)
    reference = FHIR_primitive_URIField(null=True, blank=True, )
    stabilityDuration = models.OneToOneField("FHIR_GP_Quantity_Duration", related_name='MedicationKnowledge_storageGuideline_stabilityDuration', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_MedicationKnowledge_storageGuideline_note(FHIR_GP_Annotation):
    MedicationKnowledge_storageGuideline = models.ForeignKey(FHIR_MedicationKnowledge_storageGuideline, related_name='MedicationKnowledge_storageGuideline_note', null=False, on_delete=models.CASCADE)

class FHIR_MedicationKnowledge_storageGuideline_environmentalSetting(models.Model):
    MedicationKnowledge_storageGuideline = models.ForeignKey(FHIR_MedicationKnowledge_storageGuideline, related_name='MedicationKnowledge_storageGuideline_environmentalSetting', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='MedicationKnowledge_storageGuideline_environmentalSetting_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value = models.OneToOneField("FHIR_GP_Quantity", related_name='MedicationKnowledge_storageGuideline_environmentalSetting_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_Range", related_name='MedicationKnowledge_storageGuideline_environmentalSetting_value', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_value = 'TODO'
    value_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_value}, related_name='MedicationKnowledge_storageGuideline_environmentalSetting_value', blank=True)
    value_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_MedicationKnowledge_regulatory(models.Model):
    MedicationKnowledge = models.ForeignKey(FHIR_MedicationKnowledge, related_name='MedicationKnowledge_regulatory', null=False, on_delete=models.CASCADE)
    regulatoryAuthority = models.ForeignKey("FHIR_Organization", related_name="MedicationKnowledge_regulatory_regulatoryAuthority", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_MedicationKnowledge_regulatory_substitution(models.Model):
    MedicationKnowledge_regulatory = models.ForeignKey(FHIR_MedicationKnowledge_regulatory, related_name='MedicationKnowledge_regulatory_substitution', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='MedicationKnowledge_regulatory_substitution_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    allowed = FHIR_primitive_BooleanField(null=True, blank=True, )

class FHIR_MedicationKnowledge_regulatory_schedule(models.Model):
    MedicationKnowledge_regulatory = models.ForeignKey(FHIR_MedicationKnowledge_regulatory, related_name='MedicationKnowledge_regulatory_schedule', null=False, on_delete=models.CASCADE)
    BINDING_schedule = 'TODO'
    schedule_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_schedule}, related_name='MedicationKnowledge_regulatory_schedule', blank=True)
    schedule_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_MedicationKnowledge_regulatory_maxDispense(models.Model):
    MedicationKnowledge_regulatory = models.ForeignKey(FHIR_MedicationKnowledge_regulatory, related_name='MedicationKnowledge_regulatory_maxDispense', null=False, on_delete=models.CASCADE)
    quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='MedicationKnowledge_regulatory_maxDispense_quantity', null=True, blank=True, on_delete=models.SET_NULL)
    period = models.OneToOneField("FHIR_GP_Quantity_Duration", related_name='MedicationKnowledge_regulatory_maxDispense_period', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_MedicationKnowledge_definitional(models.Model):
    MedicationKnowledge = models.ForeignKey(FHIR_MedicationKnowledge, related_name='MedicationKnowledge_definitional', null=False, on_delete=models.CASCADE)
    definition = models.ManyToManyField("FHIR_MedicinalProductDefinition", related_name="MedicationKnowledge_definitional_definition", blank=True)
    BINDING_doseForm = 'TODO'
    doseForm_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_doseForm}, related_name='MedicationKnowledge_definitional_doseForm', blank=True)
    doseForm_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_MedicationKnowledge_definitional_intendedRoute(models.Model):
    MedicationKnowledge_definitional = models.ForeignKey(FHIR_MedicationKnowledge_definitional, related_name='MedicationKnowledge_definitional_intendedRoute', null=False, on_delete=models.CASCADE)
    BINDING_intendedRoute = 'TODO'
    intendedRoute_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_intendedRoute}, related_name='MedicationKnowledge_definitional_intendedRoute', blank=True)
    intendedRoute_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_MedicationKnowledge_definitional_ingredient(models.Model):
    MedicationKnowledge_definitional = models.ForeignKey(FHIR_MedicationKnowledge_definitional, related_name='MedicationKnowledge_definitional_ingredient', null=False, on_delete=models.CASCADE)
    BINDING_item = 'TODO'
    item_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_item}, related_name='MedicationKnowledge_definitional_ingredient_item', blank=True)
    item_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    item_Substance_ref = models.ForeignKey("FHIR_Substance", related_name="MedicationKnowledge_definitional_ingredient_item_Substance", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='MedicationKnowledge_definitional_ingredient_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    strength = models.OneToOneField("FHIR_GP_Ratio", related_name='MedicationKnowledge_definitional_ingredient_strength', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_strength = 'TODO'
    strength_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_strength}, related_name='MedicationKnowledge_definitional_ingredient_strength', blank=True)
    strength_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    strength = models.OneToOneField("FHIR_GP_Quantity", related_name='MedicationKnowledge_definitional_ingredient_strength', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_MedicationKnowledge_definitional_drugCharacteristic(models.Model):
    MedicationKnowledge_definitional = models.ForeignKey(FHIR_MedicationKnowledge_definitional, related_name='MedicationKnowledge_definitional_drugCharacteristic', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='MedicationKnowledge_definitional_drugCharacteristic_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_value = 'TODO'
    value_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_value}, related_name='MedicationKnowledge_definitional_drugCharacteristic_value', blank=True)
    value_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value = FHIR_primitive_StringField(null=True, blank=True, )
    value = models.OneToOneField("FHIR_GP_Quantity", related_name='MedicationKnowledge_definitional_drugCharacteristic_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = FHIR_primitive_Base64BinaryField(null=True, blank=True, )
    value = models.OneToOneField("FHIR_GP_Attachment", related_name='MedicationKnowledge_definitional_drugCharacteristic_value', null=True, blank=True, on_delete=models.SET_NULL)
