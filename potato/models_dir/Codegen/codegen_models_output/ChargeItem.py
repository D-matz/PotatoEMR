#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_ChargeItem(models.Model):
    class StatusChoices(models.TextChoices): PLANNED = 'planned', 'Planned'; BILLABLE = 'billable', 'Billable'; NOT_BILLABLE = 'not-billable', 'Not-billable'; ABORTED = 'aborted', 'Aborted'; BILLED = 'billed', 'Billed'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    partOf = models.ManyToManyField("FHIR_ChargeItem", related_name="ChargeItem_partOf", blank=True)
    BINDING_code = "TODO"
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='ChargeItem_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    subject_Patient = models.ForeignKey("FHIR_Patient", related_name="ChargeItem_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Group = models.ForeignKey("FHIR_Group", related_name="ChargeItem_subject", null=True, blank=True, on_delete=models.SET_NULL)
    encounter = models.ForeignKey("FHIR_Encounter", related_name="ChargeItem_encounter", null=True, blank=True, on_delete=models.SET_NULL)
    occurrence_dateTime = FHIR_primitive_DateTimeField(null=True, blank=True, )
    occurrence_Period = models.OneToOneField("FHIR_GP_Period", related_name='ChargeItem_occurrence_Period', null=True, blank=True, on_delete=models.SET_NULL)
    occurrence_Timing = models.OneToOneField("FHIR_GP_Timing", related_name='ChargeItem_occurrence_Timing', null=True, blank=True, on_delete=models.SET_NULL)
    performingOrganization = models.ForeignKey("FHIR_Organization", related_name="ChargeItem_performingOrganization", null=True, blank=True, on_delete=models.SET_NULL)
    requestingOrganization = models.ForeignKey("FHIR_Organization", related_name="ChargeItem_requestingOrganization", null=True, blank=True, on_delete=models.SET_NULL)
    costCenter = models.ForeignKey("FHIR_Organization", related_name="ChargeItem_costCenter", null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='ChargeItem_quantity', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_overrideReason = "TODO"
    overrideReason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_overrideReason}, related_name='ChargeItem_overrideReason', blank=True)
    overrideReason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    enterer_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="ChargeItem_enterer", null=True, blank=True, on_delete=models.SET_NULL)
    enterer_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="ChargeItem_enterer", null=True, blank=True, on_delete=models.SET_NULL)
    enterer_Organization = models.ForeignKey("FHIR_Organization", related_name="ChargeItem_enterer", null=True, blank=True, on_delete=models.SET_NULL)
    enterer_Patient = models.ForeignKey("FHIR_Patient", related_name="ChargeItem_enterer", null=True, blank=True, on_delete=models.SET_NULL)
    enterer_Device = models.ForeignKey("FHIR_Device", related_name="ChargeItem_enterer", null=True, blank=True, on_delete=models.SET_NULL)
    enterer_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="ChargeItem_enterer", null=True, blank=True, on_delete=models.SET_NULL)
    enteredDate = FHIR_primitive_DateTimeField(null=True, blank=True, )
    account = models.ManyToManyField("FHIR_Account", related_name="ChargeItem_account", blank=True)
                            #skipping Reference(Any) for field supportingInformation as ChargeItem supportingInformation not in referenceAny_targets

class FHIR_ChargeItem_identifier(FHIR_GP_Identifier):
    ChargeItem = models.ForeignKey(FHIR_ChargeItem, related_name='ChargeItem_identifier', null=False, on_delete=models.CASCADE)

class FHIR_ChargeItem_definitionUri(models.Model):
    ChargeItem = models.ForeignKey(FHIR_ChargeItem, related_name='ChargeItem_definitionUri', null=False, on_delete=models.CASCADE)
    
    definitionUri = FHIR_primitive_URIField(null=True, blank=True, )
    
class FHIR_ChargeItem_definitionCanonical(models.Model):
    ChargeItem = models.ForeignKey(FHIR_ChargeItem, related_name='ChargeItem_definitionCanonical', null=False, on_delete=models.CASCADE)
    
    definitionCanonical = FHIR_primitive_CanonicalField(null=True, blank=True, )
    
class FHIR_ChargeItem_performer(models.Model):
    ChargeItem = models.ForeignKey(FHIR_ChargeItem, related_name='ChargeItem_performer', null=False, on_delete=models.CASCADE)
    BINDING_function = "TODO"
    function_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_function}, related_name='ChargeItem_performer_function', blank=True)
    function_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    actor_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="ChargeItem_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="ChargeItem_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Organization = models.ForeignKey("FHIR_Organization", related_name="ChargeItem_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_HealthcareService = models.ForeignKey("FHIR_HealthcareService", related_name="ChargeItem_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_CareTeam = models.ForeignKey("FHIR_CareTeam", related_name="ChargeItem_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Patient = models.ForeignKey("FHIR_Patient", related_name="ChargeItem_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Device = models.ForeignKey("FHIR_Device", related_name="ChargeItem_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="ChargeItem_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ChargeItem_bodysite(models.Model):
    ChargeItem = models.ForeignKey(FHIR_ChargeItem, related_name='ChargeItem_bodysite', null=False, on_delete=models.CASCADE)
    BINDING_bodysite = "TODO"
    bodysite_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_bodysite}, related_name='ChargeItem_bodysite', blank=True)
    bodysite_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ChargeItem_reason(models.Model):
    ChargeItem = models.ForeignKey(FHIR_ChargeItem, related_name='ChargeItem_reason', null=False, on_delete=models.CASCADE)
    BINDING_reason = "TODO"
    reason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_reason}, related_name='ChargeItem_reason', blank=True)
    reason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    reason_Condition_ref = models.ForeignKey("FHIR_Condition", related_name="ChargeItem_reason_Condition", null=True, blank=True, on_delete=models.SET_NULL)
    reason_DiagnosticReport_ref = models.ForeignKey("FHIR_DiagnosticReport", related_name="ChargeItem_reason_DiagnosticReport", null=True, blank=True, on_delete=models.SET_NULL)
    reason_Observation_ref = models.ForeignKey("FHIR_Observation", related_name="ChargeItem_reason_Observation", null=True, blank=True, on_delete=models.SET_NULL)
    reason_ImmunizationRecommendation_ref = models.ForeignKey("FHIR_ImmunizationRecommendation", related_name="ChargeItem_reason_ImmunizationRecommendation", null=True, blank=True, on_delete=models.SET_NULL)
    reason_Procedure_ref = models.ForeignKey("FHIR_Procedure", related_name="ChargeItem_reason_Procedure", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ChargeItem_service(models.Model):
    ChargeItem = models.ForeignKey(FHIR_ChargeItem, related_name='ChargeItem_service', null=False, on_delete=models.CASCADE)
    BINDING_service = "TODO"
    service_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_service}, related_name='ChargeItem_service', blank=True)
    service_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    service_DiagnosticReport_ref = models.ForeignKey("FHIR_DiagnosticReport", related_name="ChargeItem_service_DiagnosticReport", null=True, blank=True, on_delete=models.SET_NULL)
    service_ImagingStudy_ref = models.ForeignKey("FHIR_ImagingStudy", related_name="ChargeItem_service_ImagingStudy", null=True, blank=True, on_delete=models.SET_NULL)
    service_Immunization_ref = models.ForeignKey("FHIR_Immunization", related_name="ChargeItem_service_Immunization", null=True, blank=True, on_delete=models.SET_NULL)
    service_MedicationAdministration_ref = models.ForeignKey("FHIR_MedicationAdministration", related_name="ChargeItem_service_MedicationAdministration", null=True, blank=True, on_delete=models.SET_NULL)
    service_MedicationDispense_ref = models.ForeignKey("FHIR_MedicationDispense", related_name="ChargeItem_service_MedicationDispense", null=True, blank=True, on_delete=models.SET_NULL)
    service_MedicationRequest_ref = models.ForeignKey("FHIR_MedicationRequest", related_name="ChargeItem_service_MedicationRequest", null=True, blank=True, on_delete=models.SET_NULL)
    service_Observation_ref = models.ForeignKey("FHIR_Observation", related_name="ChargeItem_service_Observation", null=True, blank=True, on_delete=models.SET_NULL)
    service_Procedure_ref = models.ForeignKey("FHIR_Procedure", related_name="ChargeItem_service_Procedure", null=True, blank=True, on_delete=models.SET_NULL)
    service_ServiceRequest_ref = models.ForeignKey("FHIR_ServiceRequest", related_name="ChargeItem_service_ServiceRequest", null=True, blank=True, on_delete=models.SET_NULL)
    service_SupplyDelivery_ref = models.ForeignKey("FHIR_SupplyDelivery", related_name="ChargeItem_service_SupplyDelivery", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ChargeItem_product(models.Model):
    ChargeItem = models.ForeignKey(FHIR_ChargeItem, related_name='ChargeItem_product', null=False, on_delete=models.CASCADE)
    BINDING_product = "TODO"
    product_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_product}, related_name='ChargeItem_product', blank=True)
    product_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    product_Device_ref = models.ForeignKey("FHIR_Device", related_name="ChargeItem_product_Device", null=True, blank=True, on_delete=models.SET_NULL)
    product_Medication_ref = models.ForeignKey("FHIR_Medication", related_name="ChargeItem_product_Medication", null=True, blank=True, on_delete=models.SET_NULL)
    product_Substance_ref = models.ForeignKey("FHIR_Substance", related_name="ChargeItem_product_Substance", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_ChargeItem_note(FHIR_GP_Annotation):
    ChargeItem = models.ForeignKey(FHIR_ChargeItem, related_name='ChargeItem_note', null=False, on_delete=models.CASCADE)
