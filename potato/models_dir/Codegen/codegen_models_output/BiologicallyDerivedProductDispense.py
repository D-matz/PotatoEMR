#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_BiologicallyDerivedProductDispense(models.Model):
    basedOn = models.ManyToManyField("FHIR_ServiceRequest", related_name="BiologicallyDerivedProductDispense_basedOn", blank=True)
    partOf = models.ManyToManyField("FHIR_BiologicallyDerivedProductDispense", related_name="BiologicallyDerivedProductDispense_partOf", blank=True)
    class StatusChoices(models.TextChoices): PREPARATION = 'preparation', 'Preparation'; IN_PROGRESS = 'in-progress', 'In-progress'; ALLOCATED = 'allocated', 'Allocated'; ISSUED = 'issued', 'Issued'; UNFULFILLED = 'unfulfilled', 'Unfulfilled'; RETURNED = 'returned', 'Returned'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    BINDING_originRelationshipType = "TODO"
    originRelationshipType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_originRelationshipType}, related_name='BiologicallyDerivedProductDispense_originRelationshipType', blank=True)
    originRelationshipType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    product = models.ForeignKey("FHIR_BiologicallyDerivedProduct", related_name="BiologicallyDerivedProductDispense_product", null=True, blank=True, on_delete=models.SET_NULL)
    patient = models.ForeignKey("FHIR_Patient", related_name="BiologicallyDerivedProductDispense_patient", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_matchStatus = "TODO"
    matchStatus_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_matchStatus}, related_name='BiologicallyDerivedProductDispense_matchStatus', blank=True)
    matchStatus_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    location = models.ForeignKey("FHIR_Location", related_name="BiologicallyDerivedProductDispense_location", null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='BiologicallyDerivedProductDispense_quantity', null=True, blank=True, on_delete=models.SET_NULL)
    preparedDate = FHIR_primitive_DateTimeField(null=True, blank=True, )
    whenHandedOver = FHIR_primitive_DateTimeField(null=True, blank=True, )
    destination = models.ForeignKey("FHIR_Location", related_name="BiologicallyDerivedProductDispense_destination", null=True, blank=True, on_delete=models.SET_NULL)
    usageInstruction = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_BiologicallyDerivedProductDispense_identifier(FHIR_GP_Identifier):
    BiologicallyDerivedProductDispense = models.ForeignKey(FHIR_BiologicallyDerivedProductDispense, related_name='BiologicallyDerivedProductDispense_identifier', null=False, on_delete=models.CASCADE)

class FHIR_BiologicallyDerivedProductDispense_performer(models.Model):
    BiologicallyDerivedProductDispense = models.ForeignKey(FHIR_BiologicallyDerivedProductDispense, related_name='BiologicallyDerivedProductDispense_performer', null=False, on_delete=models.CASCADE)
    BINDING_function = "TODO"
    function_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_function}, related_name='BiologicallyDerivedProductDispense_performer_function', blank=True)
    function_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    actor = models.ForeignKey("FHIR_Practitioner", related_name="BiologicallyDerivedProductDispense_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_BiologicallyDerivedProductDispense_note(FHIR_GP_Annotation):
    BiologicallyDerivedProductDispense = models.ForeignKey(FHIR_BiologicallyDerivedProductDispense, related_name='BiologicallyDerivedProductDispense_note', null=False, on_delete=models.CASCADE)
