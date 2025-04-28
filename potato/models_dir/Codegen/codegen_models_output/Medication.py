#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Medication(models.Model):
    BINDING_code = "TODO"
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='Medication_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    class StatusChoices(models.TextChoices): ACTIVE = 'active', 'Active'; INACTIVE = 'inactive', 'Inactive'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    marketingAuthorizationHolder = models.ForeignKey("FHIR_Organization", related_name="Medication_marketingAuthorizationHolder", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_doseForm = "TODO"
    doseForm_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_doseForm}, related_name='Medication_doseForm', blank=True)
    doseForm_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    totalVolume = models.OneToOneField("FHIR_GP_Quantity", related_name='Medication_totalVolume', null=True, blank=True, on_delete=models.SET_NULL)
    definition = models.ForeignKey("FHIR_MedicationKnowledge", related_name="Medication_definition", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Medication_identifier(FHIR_GP_Identifier):
    Medication = models.ForeignKey(FHIR_Medication, related_name='Medication_identifier', null=False, on_delete=models.CASCADE)

class FHIR_Medication_ingredient(models.Model):
    Medication = models.ForeignKey(FHIR_Medication, related_name='Medication_ingredient', null=False, on_delete=models.CASCADE)
    BINDING_item = "TODO"
    item_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_item}, related_name='Medication_ingredient_item', blank=True)
    item_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    item_Substance_ref = models.ForeignKey("FHIR_Substance", related_name="Medication_ingredient_item_Substance", null=True, blank=True, on_delete=models.SET_NULL)
    item_Medication_ref = models.ForeignKey("FHIR_Medication", related_name="Medication_ingredient_item_Medication", null=True, blank=True, on_delete=models.SET_NULL)
    isActive = FHIR_primitive_BooleanField(null=True, blank=True, )
    strength_Ratio = models.OneToOneField("FHIR_GP_Ratio", related_name='Medication_ingredient_strength_Ratio', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_strength_CodeableConcept = "TODO"
    strength_CodeableConcept_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_strength_CodeableConcept}, related_name='Medication_ingredient_strength_CodeableConcept', blank=True)
    strength_CodeableConcept_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    strength_Quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='Medication_ingredient_strength_Quantity', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Medication_batch(models.Model):
    Medication = models.ForeignKey(FHIR_Medication, related_name='Medication_batch', null=False, on_delete=models.CASCADE)
    lotNumber = FHIR_primitive_StringField(null=True, blank=True, )
    expirationDate = FHIR_primitive_DateTimeField(null=True, blank=True, )
