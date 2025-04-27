#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_List(models.Model):
    class StatusChoices(models.TextChoices): CURRENT = 'current', 'Current'; RETIRED = 'retired', 'Retired'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    class ModeChoices(models.TextChoices): WORKING = 'working', 'Working'; SNAPSHOT = 'snapshot', 'Snapshot'; CHANGES = 'changes', 'Changes'; 
    mode = FHIR_primitive_CodeField(choices=ModeChoices.choices, null=True, blank=True, )
    title = FHIR_primitive_StringField(null=True, blank=True, )
    BINDING_code = 'TODO'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='List_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    encounter = models.ForeignKey("FHIR_Encounter", related_name="List_encounter", null=True, blank=True, on_delete=models.SET_NULL)
    date = FHIR_primitive_DateTimeField(null=True, blank=True, )
    source_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="List_source", null=True, blank=True, on_delete=models.SET_NULL)
    source_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="List_source", null=True, blank=True, on_delete=models.SET_NULL)
    source_Patient = models.ForeignKey("FHIR_Patient", related_name="List_source", null=True, blank=True, on_delete=models.SET_NULL)
    source_Device = models.ForeignKey("FHIR_Device", related_name="List_source", null=True, blank=True, on_delete=models.SET_NULL)
    source_Organization = models.ForeignKey("FHIR_Organization", related_name="List_source", null=True, blank=True, on_delete=models.SET_NULL)
    source_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="List_source", null=True, blank=True, on_delete=models.SET_NULL)
    source_CareTeam = models.ForeignKey("FHIR_CareTeam", related_name="List_source", null=True, blank=True, on_delete=models.SET_NULL)
    source_Group = models.ForeignKey("FHIR_Group", related_name="List_source", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_orderedBy = 'TODO'
    orderedBy_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_orderedBy}, related_name='List_orderedBy', blank=True)
    orderedBy_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_emptyReason = 'TODO'
    emptyReason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_emptyReason}, related_name='List_emptyReason', blank=True)
    emptyReason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_List_identifier(FHIR_GP_Identifier):
    List = models.ForeignKey(FHIR_List, related_name='List_identifier', null=False, on_delete=models.CASCADE)

class FHIR_List_note(FHIR_GP_Annotation):
    List = models.ForeignKey(FHIR_List, related_name='List_note', null=False, on_delete=models.CASCADE)

class FHIR_List_entry(models.Model):
    List = models.ForeignKey(FHIR_List, related_name='List_entry', null=False, on_delete=models.CASCADE)
    BINDING_flag = 'TODO'
    flag_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_flag}, related_name='List_entry_flag', blank=True)
    flag_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    deleted = FHIR_primitive_BooleanField(null=True, blank=True, )
    date = FHIR_primitive_DateTimeField(null=True, blank=True, )
