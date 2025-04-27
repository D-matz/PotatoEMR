#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_PersonalRelationship(models.Model):
    source_Patient = models.ForeignKey("FHIR_Patient", related_name="PersonalRelationship_source", null=True, blank=True, on_delete=models.SET_NULL)
    source_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="PersonalRelationship_source", null=True, blank=True, on_delete=models.SET_NULL)
    source_Person = models.ForeignKey("FHIR_Person", related_name="PersonalRelationship_source", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_relationshipType = "TODO"
    relationshipType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_relationshipType}, related_name='PersonalRelationship_relationshipType', blank=True)
    relationshipType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    target_Patient = models.ForeignKey("FHIR_Patient", related_name="PersonalRelationship_target", null=True, blank=True, on_delete=models.SET_NULL)
    target_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="PersonalRelationship_target", null=True, blank=True, on_delete=models.SET_NULL)
    target_Person = models.ForeignKey("FHIR_Person", related_name="PersonalRelationship_target", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_confidence = "TODO"
    confidence_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_confidence}, related_name='PersonalRelationship_confidence', blank=True)
    confidence_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    asserter_Patient = models.ForeignKey("FHIR_Patient", related_name="PersonalRelationship_asserter", null=True, blank=True, on_delete=models.SET_NULL)
    asserter_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="PersonalRelationship_asserter", null=True, blank=True, on_delete=models.SET_NULL)
    asserter_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="PersonalRelationship_asserter", null=True, blank=True, on_delete=models.SET_NULL)
    asserter_Organization = models.ForeignKey("FHIR_Organization", related_name="PersonalRelationship_asserter", null=True, blank=True, on_delete=models.SET_NULL)
    group = models.ManyToManyField("FHIR_Group", related_name="PersonalRelationship_group", blank=True)

class FHIR_PersonalRelationship_period(FHIR_GP_Period):
    PersonalRelationship = models.ForeignKey(FHIR_PersonalRelationship, related_name='PersonalRelationship_period', null=False, on_delete=models.CASCADE)
