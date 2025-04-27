#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_EncounterHistory(models.Model):
    encounter = models.ForeignKey("FHIR_Encounter", related_name="EncounterHistory_encounter", null=True, blank=True, on_delete=models.SET_NULL)
    class StatusChoices(models.TextChoices): PLANNED = 'planned', 'Planned'; IN_PROGRESS = 'in-progress', 'In-progress'; ON_HOLD = 'on-hold', 'On-hold'; DISCHARGED = 'discharged', 'Discharged'; COMPLETED = 'completed', 'Completed'; CANCELLED = 'cancelled', 'Cancelled'; DISCONTINUED = 'discontinued', 'Discontinued'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    BINDING_class = "TODO"
    class_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_class}, related_name='EncounterHistory_class', blank=True)
    class_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    subject_Patient = models.ForeignKey("FHIR_Patient", related_name="EncounterHistory_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Group = models.ForeignKey("FHIR_Group", related_name="EncounterHistory_subject", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_subjectStatus = "TODO"
    subjectStatus_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_subjectStatus}, related_name='EncounterHistory_subjectStatus', blank=True)
    subjectStatus_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    actualPeriod = models.OneToOneField("FHIR_GP_Period", related_name='EncounterHistory_actualPeriod', null=True, blank=True, on_delete=models.SET_NULL)
    plannedStartDate = FHIR_primitive_DateTimeField(null=True, blank=True, )
    plannedEndDate = FHIR_primitive_DateTimeField(null=True, blank=True, )
    length = models.OneToOneField("FHIR_GP_Quantity_Duration", related_name='EncounterHistory_length', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_EncounterHistory_identifier(FHIR_GP_Identifier):
    EncounterHistory = models.ForeignKey(FHIR_EncounterHistory, related_name='EncounterHistory_identifier', null=False, on_delete=models.CASCADE)

class FHIR_EncounterHistory_type(models.Model):
    EncounterHistory = models.ForeignKey(FHIR_EncounterHistory, related_name='EncounterHistory_type', null=False, on_delete=models.CASCADE)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='EncounterHistory_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_EncounterHistory_serviceType(models.Model):
    EncounterHistory = models.ForeignKey(FHIR_EncounterHistory, related_name='EncounterHistory_serviceType', null=False, on_delete=models.CASCADE)
    BINDING_serviceType = "TODO"
    serviceType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_serviceType}, related_name='EncounterHistory_serviceType', blank=True)
    serviceType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    serviceType_HealthcareService_ref = models.ForeignKey("FHIR_HealthcareService", related_name="EncounterHistory_serviceType_HealthcareService", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_EncounterHistory_location(models.Model):
    EncounterHistory = models.ForeignKey(FHIR_EncounterHistory, related_name='EncounterHistory_location', null=False, on_delete=models.CASCADE)
    location = models.ForeignKey("FHIR_Location", related_name="EncounterHistory_location_location", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_form = "TODO"
    form_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_form}, related_name='EncounterHistory_location_form', blank=True)
    form_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
