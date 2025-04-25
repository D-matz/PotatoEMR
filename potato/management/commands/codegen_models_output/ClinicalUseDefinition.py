
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_ClinicalUseDefinition(models.Model):
    class TypeChoices(models.TextChoices): INDICATION = 'indication', 'Indication'; CONTRAINDICATION = 'contraindication', 'Contraindication'; INTERACTION = 'interaction', 'Interaction'; UNDESIRABLE_EFFECT = 'undesirable-effect', 'Undesirable-effect'; WARNING = 'warning', 'Warning'; 
    type = FHIR_primitive_CodeField(choices=TypeChoices.choices, null=True, blank=True, )
    subject_MedicinalProductDefinition = models.ManyToManyField("FHIR_MedicinalProductDefinition", related_name="ClinicalUseDefinition_subject", blank=True)
    subject_Medication = models.ManyToManyField("FHIR_Medication", related_name="ClinicalUseDefinition_subject", blank=True)
    subject_ActivityDefinition = models.ManyToManyField("FHIR_ActivityDefinition", related_name="ClinicalUseDefinition_subject", blank=True)
    subject_PlanDefinition = models.ManyToManyField("FHIR_PlanDefinition", related_name="ClinicalUseDefinition_subject", blank=True)
    subject_Device = models.ManyToManyField("FHIR_Device", related_name="ClinicalUseDefinition_subject", blank=True)
    subject_DeviceDefinition = models.ManyToManyField("FHIR_DeviceDefinition", related_name="ClinicalUseDefinition_subject", blank=True)
    subject_SubstanceDefinition = models.ManyToManyField("FHIR_SubstanceDefinition", related_name="ClinicalUseDefinition_subject", blank=True)
    subject_NutritionProduct = models.ManyToManyField("FHIR_NutritionProduct", related_name="ClinicalUseDefinition_subject", blank=True)
    subject_BiologicallyDerivedProduct = models.ManyToManyField("FHIR_BiologicallyDerivedProduct", related_name="ClinicalUseDefinition_subject", blank=True)
    BINDING_status = 'TODO'
    status_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_status}, related_name='ClinicalUseDefinition_status', blank=True)
    status_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    population = models.ManyToManyField("FHIR_Group", related_name="ClinicalUseDefinition_population", blank=True)

class FHIR_ClinicalUseDefinition_identifier(FHIR_GP_Identifier):
    ClinicalUseDefinition = models.ForeignKey(FHIR_ClinicalUseDefinition, related_name='ClinicalUseDefinition_identifier', null=False, on_delete=models.CASCADE)

class FHIR_ClinicalUseDefinition_category(models.Model):
    ClinicalUseDefinition = models.ForeignKey(FHIR_ClinicalUseDefinition, related_name='ClinicalUseDefinition_category', null=False, on_delete=models.CASCADE)
    BINDING_category = 'TODO'
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='ClinicalUseDefinition_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ClinicalUseDefinition_contraindication(models.Model):
    ClinicalUseDefinition = models.ForeignKey(FHIR_ClinicalUseDefinition, related_name='ClinicalUseDefinition_contraindication', null=False, on_delete=models.CASCADE)
    BINDING_diseaseSymptomProcedure = 'TODO'
    diseaseSymptomProcedure_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_diseaseSymptomProcedure}, related_name='ClinicalUseDefinition_contraindication_diseaseSymptomProcedure', blank=True)
    diseaseSymptomProcedure_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    diseaseSymptomProcedure_ObservationDefinition_ref = models.ForeignKey("FHIR_ObservationDefinition", related_name="ClinicalUseDefinition_contraindication_diseaseSymptomProcedure", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_diseaseStatus = 'TODO'
    diseaseStatus_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_diseaseStatus}, related_name='ClinicalUseDefinition_contraindication_diseaseStatus', blank=True)
    diseaseStatus_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    diseaseStatus_ObservationDefinition_ref = models.ForeignKey("FHIR_ObservationDefinition", related_name="ClinicalUseDefinition_contraindication_diseaseStatus", null=True, blank=True, on_delete=models.SET_NULL)
    indication = models.ManyToManyField("FHIR_ClinicalUseDefinition", related_name="ClinicalUseDefinition_contraindication_indication", blank=True)

class FHIR_ClinicalUseDefinition_contraindication_comorbidity(models.Model):
    ClinicalUseDefinition_contraindication = models.ForeignKey(FHIR_ClinicalUseDefinition_contraindication, related_name='ClinicalUseDefinition_contraindication_comorbidity', null=False, on_delete=models.CASCADE)
    BINDING_comorbidity = 'TODO'
    comorbidity_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_comorbidity}, related_name='ClinicalUseDefinition_contraindication_comorbidity', blank=True)
    comorbidity_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    comorbidity_ObservationDefinition_ref = models.ForeignKey("FHIR_ObservationDefinition", related_name="ClinicalUseDefinition_contraindication_comorbidity", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ClinicalUseDefinition_contraindication_otherTherapy(models.Model):
    ClinicalUseDefinition_contraindication = models.ForeignKey(FHIR_ClinicalUseDefinition_contraindication, related_name='ClinicalUseDefinition_contraindication_otherTherapy', null=False, on_delete=models.CASCADE)
    BINDING_relationshipType = 'TODO'
    relationshipType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_relationshipType}, related_name='ClinicalUseDefinition_contraindication_otherTherapy_relationshipType', blank=True)
    relationshipType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_treatment = 'TODO'
    treatment_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_treatment}, related_name='ClinicalUseDefinition_contraindication_otherTherapy_treatment', blank=True)
    treatment_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    treatment_MedicinalProductDefinition_ref = models.ForeignKey("FHIR_MedicinalProductDefinition", related_name="ClinicalUseDefinition_contraindication_otherTherapy_treatment", null=True, blank=True, on_delete=models.SET_NULL)
    treatment_Medication_ref = models.ForeignKey("FHIR_Medication", related_name="ClinicalUseDefinition_contraindication_otherTherapy_treatment", null=True, blank=True, on_delete=models.SET_NULL)
    treatment_SubstanceDefinition_ref = models.ForeignKey("FHIR_SubstanceDefinition", related_name="ClinicalUseDefinition_contraindication_otherTherapy_treatment", null=True, blank=True, on_delete=models.SET_NULL)
    treatment_NutritionProduct_ref = models.ForeignKey("FHIR_NutritionProduct", related_name="ClinicalUseDefinition_contraindication_otherTherapy_treatment", null=True, blank=True, on_delete=models.SET_NULL)
    treatment_BiologicallyDerivedProduct_ref = models.ForeignKey("FHIR_BiologicallyDerivedProduct", related_name="ClinicalUseDefinition_contraindication_otherTherapy_treatment", null=True, blank=True, on_delete=models.SET_NULL)
    treatment_ActivityDefinition_ref = models.ForeignKey("FHIR_ActivityDefinition", related_name="ClinicalUseDefinition_contraindication_otherTherapy_treatment", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ClinicalUseDefinition_indication(models.Model):
    ClinicalUseDefinition = models.ForeignKey(FHIR_ClinicalUseDefinition, related_name='ClinicalUseDefinition_indication', null=False, on_delete=models.CASCADE)
    BINDING_diseaseSymptomProcedure = 'TODO'
    diseaseSymptomProcedure_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_diseaseSymptomProcedure}, related_name='ClinicalUseDefinition_indication_diseaseSymptomProcedure', blank=True)
    diseaseSymptomProcedure_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    diseaseSymptomProcedure_ObservationDefinition_ref = models.ForeignKey("FHIR_ObservationDefinition", related_name="ClinicalUseDefinition_indication_diseaseSymptomProcedure", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_diseaseStatus = 'TODO'
    diseaseStatus_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_diseaseStatus}, related_name='ClinicalUseDefinition_indication_diseaseStatus', blank=True)
    diseaseStatus_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    diseaseStatus_ObservationDefinition_ref = models.ForeignKey("FHIR_ObservationDefinition", related_name="ClinicalUseDefinition_indication_diseaseStatus", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_intendedEffect = 'TODO'
    intendedEffect_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_intendedEffect}, related_name='ClinicalUseDefinition_indication_intendedEffect', blank=True)
    intendedEffect_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    intendedEffect_ObservationDefinition_ref = models.ForeignKey("FHIR_ObservationDefinition", related_name="ClinicalUseDefinition_indication_intendedEffect", null=True, blank=True, on_delete=models.SET_NULL)
    duration = models.OneToOneField("FHIR_GP_Range", related_name='ClinicalUseDefinition_indication_duration', null=True, blank=True, on_delete=models.SET_NULL)
    duration = FHIR_primitive_StringField(null=True, blank=True, )
    undesirableEffect = models.ManyToManyField("FHIR_ClinicalUseDefinition", related_name="ClinicalUseDefinition_indication_undesirableEffect", blank=True)

class FHIR_ClinicalUseDefinition_indication_comorbidity(models.Model):
    ClinicalUseDefinition_indication = models.ForeignKey(FHIR_ClinicalUseDefinition_indication, related_name='ClinicalUseDefinition_indication_comorbidity', null=False, on_delete=models.CASCADE)
    BINDING_comorbidity = 'TODO'
    comorbidity_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_comorbidity}, related_name='ClinicalUseDefinition_indication_comorbidity', blank=True)
    comorbidity_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    comorbidity_ObservationDefinition_ref = models.ForeignKey("FHIR_ObservationDefinition", related_name="ClinicalUseDefinition_indication_comorbidity", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ClinicalUseDefinition_interaction(models.Model):
    ClinicalUseDefinition = models.ForeignKey(FHIR_ClinicalUseDefinition, related_name='ClinicalUseDefinition_interaction', null=False, on_delete=models.CASCADE)
    BINDING_type = 'TODO'
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='ClinicalUseDefinition_interaction_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_effect = 'TODO'
    effect_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_effect}, related_name='ClinicalUseDefinition_interaction_effect', blank=True)
    effect_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    effect_ObservationDefinition_ref = models.ForeignKey("FHIR_ObservationDefinition", related_name="ClinicalUseDefinition_interaction_effect", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_incidence = 'TODO'
    incidence_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_incidence}, related_name='ClinicalUseDefinition_interaction_incidence', blank=True)
    incidence_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_ClinicalUseDefinition_interaction_interactant(models.Model):
    ClinicalUseDefinition_interaction = models.ForeignKey(FHIR_ClinicalUseDefinition_interaction, related_name='ClinicalUseDefinition_interaction_interactant', null=False, on_delete=models.CASCADE)
    item_MedicinalProductDefinition = models.ForeignKey("FHIR_MedicinalProductDefinition", related_name="ClinicalUseDefinition_interaction_interactant_item", null=True, blank=True, on_delete=models.SET_NULL)
    item_Medication = models.ForeignKey("FHIR_Medication", related_name="ClinicalUseDefinition_interaction_interactant_item", null=True, blank=True, on_delete=models.SET_NULL)
    item_SubstanceDefinition = models.ForeignKey("FHIR_SubstanceDefinition", related_name="ClinicalUseDefinition_interaction_interactant_item", null=True, blank=True, on_delete=models.SET_NULL)
    item_NutritionProduct = models.ForeignKey("FHIR_NutritionProduct", related_name="ClinicalUseDefinition_interaction_interactant_item", null=True, blank=True, on_delete=models.SET_NULL)
    item_BiologicallyDerivedProduct = models.ForeignKey("FHIR_BiologicallyDerivedProduct", related_name="ClinicalUseDefinition_interaction_interactant_item", null=True, blank=True, on_delete=models.SET_NULL)
    item_ObservationDefinition = models.ForeignKey("FHIR_ObservationDefinition", related_name="ClinicalUseDefinition_interaction_interactant_item", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_item = 'TODO'
    item_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_item}, related_name='ClinicalUseDefinition_interaction_interactant_item', blank=True)
    item_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_ClinicalUseDefinition_interaction_management(models.Model):
    ClinicalUseDefinition_interaction = models.ForeignKey(FHIR_ClinicalUseDefinition_interaction, related_name='ClinicalUseDefinition_interaction_management', null=False, on_delete=models.CASCADE)
    BINDING_management = 'TODO'
    management_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_management}, related_name='ClinicalUseDefinition_interaction_management', blank=True)
    management_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ClinicalUseDefinition_library(models.Model):
    ClinicalUseDefinition = models.ForeignKey(FHIR_ClinicalUseDefinition, related_name='ClinicalUseDefinition_library', null=False, on_delete=models.CASCADE)
    
    library = FHIR_primitive_CanonicalField(null=True, blank=True, )
    
class FHIR_ClinicalUseDefinition_undesirableEffect(models.Model):
    ClinicalUseDefinition = models.ForeignKey(FHIR_ClinicalUseDefinition, related_name='ClinicalUseDefinition_undesirableEffect', null=False, on_delete=models.CASCADE)
    BINDING_symptomConditionEffect = 'TODO'
    symptomConditionEffect_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_symptomConditionEffect}, related_name='ClinicalUseDefinition_undesirableEffect_symptomConditionEffect', blank=True)
    symptomConditionEffect_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    symptomConditionEffect_ObservationDefinition_ref = models.ForeignKey("FHIR_ObservationDefinition", related_name="ClinicalUseDefinition_undesirableEffect_symptomConditionEffect", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_classification = 'TODO'
    classification_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_classification}, related_name='ClinicalUseDefinition_undesirableEffect_classification', blank=True)
    classification_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_frequencyOfOccurrence = 'TODO'
    frequencyOfOccurrence_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_frequencyOfOccurrence}, related_name='ClinicalUseDefinition_undesirableEffect_frequencyOfOccurrence', blank=True)
    frequencyOfOccurrence_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_ClinicalUseDefinition_warning(models.Model):
    ClinicalUseDefinition = models.ForeignKey(FHIR_ClinicalUseDefinition, related_name='ClinicalUseDefinition_warning', null=False, on_delete=models.CASCADE)
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    BINDING_code = 'TODO'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='ClinicalUseDefinition_warning_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
