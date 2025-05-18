#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Immunization(models.Model):
    basedOn_CarePlan = models.ManyToManyField("FHIR_CarePlan", related_name="Immunization_basedOn", blank=True)
    basedOn_MedicationRequest = models.ManyToManyField("FHIR_MedicationRequest", related_name="Immunization_basedOn", blank=True)
    basedOn_ServiceRequest = models.ManyToManyField("FHIR_ServiceRequest", related_name="Immunization_basedOn", blank=True)
    basedOn_ImmunizationRecommendation = models.ManyToManyField("FHIR_ImmunizationRecommendation", related_name="Immunization_basedOn", blank=True)
    class StatusChoices(models.TextChoices): COMPLETED = 'completed', 'Completed'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; NOT_DONE = 'not-done', 'Not-done'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    BINDING_statusReason = "TODO"
    statusReason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_statusReason}, related_name='Immunization_statusReason', blank=True)
    statusReason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_vaccineCode = "TODO"
    vaccineCode_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_vaccineCode}, related_name='Immunization_vaccineCode', blank=True)
    vaccineCode_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_administeredProduct = "TODO"
    administeredProduct_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_administeredProduct}, related_name='Immunization_administeredProduct', blank=True)
    administeredProduct_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    administeredProduct_Medication_ref = models.ForeignKey("FHIR_Medication", related_name="Immunization_administeredProduct_Medication", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_manufacturer = "TODO"
    manufacturer_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_manufacturer}, related_name='Immunization_manufacturer', blank=True)
    manufacturer_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    manufacturer_Organization_ref = models.ForeignKey("FHIR_Organization", related_name="Immunization_manufacturer_Organization", null=True, blank=True, on_delete=models.SET_NULL)
    lotNumber = FHIR_primitive_StringField(null=True, blank=True, )
    expirationDate = FHIR_primitive_DateField(null=True, blank=True, )
    patient = models.ForeignKey("FHIR_Patient", related_name="Immunization_patient", null=True, blank=True, on_delete=models.SET_NULL)
    encounter = models.ForeignKey("FHIR_Encounter", related_name="Immunization_encounter", null=True, blank=True, on_delete=models.SET_NULL)
                            #skipping Reference(Any) for field supportingInformation as Immunization supportingInformation not in referenceAny_targets
    occurrence_dateTime = FHIR_primitive_DateTimeField(null=True, blank=True, )
    occurrence_string = FHIR_primitive_StringField(null=True, blank=True, )
    primarySource = FHIR_primitive_BooleanField(null=True, blank=True, )
    BINDING_informationSource = "TODO"
    informationSource_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_informationSource}, related_name='Immunization_informationSource', blank=True)
    informationSource_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    informationSource_Patient_ref = models.ForeignKey("FHIR_Patient", related_name="Immunization_informationSource_Patient", null=True, blank=True, on_delete=models.SET_NULL)
    informationSource_Practitioner_ref = models.ForeignKey("FHIR_Practitioner", related_name="Immunization_informationSource_Practitioner", null=True, blank=True, on_delete=models.SET_NULL)
    informationSource_PractitionerRole_ref = models.ForeignKey("FHIR_PractitionerRole", related_name="Immunization_informationSource_PractitionerRole", null=True, blank=True, on_delete=models.SET_NULL)
    informationSource_RelatedPerson_ref = models.ForeignKey("FHIR_RelatedPerson", related_name="Immunization_informationSource_RelatedPerson", null=True, blank=True, on_delete=models.SET_NULL)
    informationSource_Organization_ref = models.ForeignKey("FHIR_Organization", related_name="Immunization_informationSource_Organization", null=True, blank=True, on_delete=models.SET_NULL)
    location = models.ForeignKey("FHIR_Location", related_name="Immunization_location", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_site = "TODO"
    site_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_site}, related_name='Immunization_site', blank=True)
    site_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_route = "TODO"
    route_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_route}, related_name='Immunization_route', blank=True)
    route_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    doseQuantity = models.OneToOneField("FHIR_GP_Quantity", related_name='Immunization_doseQuantity', null=True, blank=True, on_delete=models.SET_NULL)
    isSubpotent = FHIR_primitive_BooleanField(null=True, blank=True, )
    BINDING_fundingSource = "TODO"
    fundingSource_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_fundingSource}, related_name='Immunization_fundingSource', blank=True)
    fundingSource_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_Immunization_identifier(FHIR_GP_Identifier):
    Immunization = models.ForeignKey(FHIR_Immunization, related_name='Immunization_identifier', null=False, on_delete=models.CASCADE)

class FHIR_Immunization_performer(models.Model):
    Immunization = models.ForeignKey(FHIR_Immunization, related_name='Immunization_performer', null=False, on_delete=models.CASCADE)
    BINDING_function = "TODO"
    function_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_function}, related_name='Immunization_performer_function', blank=True)
    function_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    actor_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="Immunization_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="Immunization_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Organization = models.ForeignKey("FHIR_Organization", related_name="Immunization_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Patient = models.ForeignKey("FHIR_Patient", related_name="Immunization_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="Immunization_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Immunization_note(FHIR_GP_Annotation):
    Immunization = models.ForeignKey(FHIR_Immunization, related_name='Immunization_note', null=False, on_delete=models.CASCADE)

class FHIR_Immunization_reason(models.Model):
    Immunization = models.ForeignKey(FHIR_Immunization, related_name='Immunization_reason', null=False, on_delete=models.CASCADE)
    BINDING_reason = "TODO"
    reason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_reason}, related_name='Immunization_reason', blank=True)
    reason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    reason_Condition_ref = models.ForeignKey("FHIR_Condition", related_name="Immunization_reason_Condition", null=True, blank=True, on_delete=models.SET_NULL)
    reason_Observation_ref = models.ForeignKey("FHIR_Observation", related_name="Immunization_reason_Observation", null=True, blank=True, on_delete=models.SET_NULL)
    reason_DiagnosticReport_ref = models.ForeignKey("FHIR_DiagnosticReport", related_name="Immunization_reason_DiagnosticReport", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Immunization_subpotentReason(models.Model):
    Immunization = models.ForeignKey(FHIR_Immunization, related_name='Immunization_subpotentReason', null=False, on_delete=models.CASCADE)
    BINDING_subpotentReason = "TODO"
    subpotentReason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_subpotentReason}, related_name='Immunization_subpotentReason', blank=True)
    subpotentReason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Immunization_programEligibility(models.Model):
    Immunization = models.ForeignKey(FHIR_Immunization, related_name='Immunization_programEligibility', null=False, on_delete=models.CASCADE)
    BINDING_program = "TODO"
    program_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_program}, related_name='Immunization_programEligibility_program', blank=True)
    program_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_programStatus = "TODO"
    programStatus_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_programStatus}, related_name='Immunization_programEligibility_programStatus', blank=True)
    programStatus_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_Immunization_reaction(models.Model):
    Immunization = models.ForeignKey(FHIR_Immunization, related_name='Immunization_reaction', null=False, on_delete=models.CASCADE)
    date = FHIR_primitive_DateTimeField(null=True, blank=True, )
    BINDING_manifestation = "TODO"
    manifestation_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_manifestation}, related_name='Immunization_reaction_manifestation', blank=True)
    manifestation_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    manifestation_Observation_ref = models.ForeignKey("FHIR_Observation", related_name="Immunization_reaction_manifestation_Observation", null=True, blank=True, on_delete=models.SET_NULL)
    reported = FHIR_primitive_BooleanField(null=True, blank=True, )

class FHIR_Immunization_protocolApplied(models.Model):
    Immunization = models.ForeignKey(FHIR_Immunization, related_name='Immunization_protocolApplied', null=False, on_delete=models.CASCADE)
    series = FHIR_primitive_StringField(null=True, blank=True, )
    authority = models.ForeignKey("FHIR_Organization", related_name="Immunization_protocolApplied_authority", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_doseNumber = "TODO"
    doseNumber_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_doseNumber}, related_name='Immunization_protocolApplied_doseNumber', blank=True)
    doseNumber_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_seriesDoses = "TODO"
    seriesDoses_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_seriesDoses}, related_name='Immunization_protocolApplied_seriesDoses', blank=True)
    seriesDoses_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_Immunization_protocolApplied_targetDisease(models.Model):
    Immunization_protocolApplied = models.ForeignKey(FHIR_Immunization_protocolApplied, related_name='Immunization_protocolApplied_targetDisease', null=False, on_delete=models.CASCADE)
    BINDING_targetDisease = "TODO"
    targetDisease_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_targetDisease}, related_name='Immunization_protocolApplied_targetDisease', blank=True)
    targetDisease_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    