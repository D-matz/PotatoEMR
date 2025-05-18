#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_MedicationDispense(models.Model):
    basedOn = models.ManyToManyField("FHIR_CarePlan", related_name="MedicationDispense_basedOn", blank=True)
    partOf_Procedure = models.ManyToManyField("FHIR_Procedure", related_name="MedicationDispense_partOf", blank=True)
    partOf_MedicationAdministration = models.ManyToManyField("FHIR_MedicationAdministration", related_name="MedicationDispense_partOf", blank=True)
    class StatusChoices(models.TextChoices): PREPARATION = 'preparation', 'Preparation'; IN_PROGRESS = 'in-progress', 'In-progress'; CANCELLED = 'cancelled', 'Cancelled'; ON_HOLD = 'on-hold', 'On-hold'; COMPLETED = 'completed', 'Completed'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; STOPPED = 'stopped', 'Stopped'; DECLINED = 'declined', 'Declined'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    BINDING_notPerformedReason = "TODO"
    notPerformedReason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_notPerformedReason}, related_name='MedicationDispense_notPerformedReason', blank=True)
    notPerformedReason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    notPerformedReason_DetectedIssue_ref = models.ForeignKey("FHIR_DetectedIssue", related_name="MedicationDispense_notPerformedReason_DetectedIssue", null=True, blank=True, on_delete=models.SET_NULL)
    statusChanged = FHIR_primitive_DateTimeField(null=True, blank=True, )
    BINDING_medication = "TODO"
    medication_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_medication}, related_name='MedicationDispense_medication', blank=True)
    medication_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    medication_Medication_ref = models.ForeignKey("FHIR_Medication", related_name="MedicationDispense_medication_Medication", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Patient = models.ForeignKey("FHIR_Patient", related_name="MedicationDispense_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Group = models.ForeignKey("FHIR_Group", related_name="MedicationDispense_subject", null=True, blank=True, on_delete=models.SET_NULL)
    encounter = models.ForeignKey("FHIR_Encounter", related_name="MedicationDispense_encounter", null=True, blank=True, on_delete=models.SET_NULL)
                            #skipping Reference(Any) for field supportingInformation as MedicationDispense supportingInformation not in referenceAny_targets
    location = models.ForeignKey("FHIR_Location", related_name="MedicationDispense_location", null=True, blank=True, on_delete=models.SET_NULL)
    authorizingPrescription = models.ManyToManyField("FHIR_MedicationRequest", related_name="MedicationDispense_authorizingPrescription", blank=True)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='MedicationDispense_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='MedicationDispense_quantity', null=True, blank=True, on_delete=models.SET_NULL)
    daysSupply = models.OneToOneField("FHIR_GP_Quantity", related_name='MedicationDispense_daysSupply', null=True, blank=True, on_delete=models.SET_NULL)
    fillNumber = FHIR_primitive_PositiveIntField(null=True, blank=True, )
    recorded = FHIR_primitive_DateTimeField(null=True, blank=True, )
    whenPrepared = FHIR_primitive_DateTimeField(null=True, blank=True, )
    whenHandedOver = FHIR_primitive_DateTimeField(null=True, blank=True, )
    destination = models.ForeignKey("FHIR_Location", related_name="MedicationDispense_destination", null=True, blank=True, on_delete=models.SET_NULL)
    receiver_Patient = models.ManyToManyField("FHIR_Patient", related_name="MedicationDispense_receiver", blank=True)
    receiver_Practitioner = models.ManyToManyField("FHIR_Practitioner", related_name="MedicationDispense_receiver", blank=True)
    receiver_RelatedPerson = models.ManyToManyField("FHIR_RelatedPerson", related_name="MedicationDispense_receiver", blank=True)
    receiver_Location = models.ManyToManyField("FHIR_Location", related_name="MedicationDispense_receiver", blank=True)
    receiver_PractitionerRole = models.ManyToManyField("FHIR_PractitionerRole", related_name="MedicationDispense_receiver", blank=True)
    receiver_Group = models.ManyToManyField("FHIR_Group", related_name="MedicationDispense_receiver", blank=True)
    renderedDosageInstruction = FHIR_primitive_MarkdownField(null=True, blank=True, )
    eventHistory = models.ManyToManyField("FHIR_Provenance", related_name="MedicationDispense_eventHistory", blank=True)

class FHIR_MedicationDispense_identifier(FHIR_GP_Identifier):
    MedicationDispense = models.ForeignKey(FHIR_MedicationDispense, related_name='MedicationDispense_identifier', null=False, on_delete=models.CASCADE)

class FHIR_MedicationDispense_category(models.Model):
    MedicationDispense = models.ForeignKey(FHIR_MedicationDispense, related_name='MedicationDispense_category', null=False, on_delete=models.CASCADE)
    BINDING_category = "TODO"
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='MedicationDispense_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_MedicationDispense_performer(models.Model):
    MedicationDispense = models.ForeignKey(FHIR_MedicationDispense, related_name='MedicationDispense_performer', null=False, on_delete=models.CASCADE)
    BINDING_function = "TODO"
    function_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_function}, related_name='MedicationDispense_performer_function', blank=True)
    function_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    actor_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="MedicationDispense_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="MedicationDispense_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Organization = models.ForeignKey("FHIR_Organization", related_name="MedicationDispense_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Patient = models.ForeignKey("FHIR_Patient", related_name="MedicationDispense_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Device = models.ForeignKey("FHIR_Device", related_name="MedicationDispense_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="MedicationDispense_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_CareTeam = models.ForeignKey("FHIR_CareTeam", related_name="MedicationDispense_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Group = models.ForeignKey("FHIR_Group", related_name="MedicationDispense_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_MedicationDispense_note(FHIR_GP_Annotation):
    MedicationDispense = models.ForeignKey(FHIR_MedicationDispense, related_name='MedicationDispense_note', null=False, on_delete=models.CASCADE)

class FHIR_MedicationDispense_dosageInstruction(FHIR_SP_Dosage):
    MedicationDispense = models.ForeignKey(FHIR_MedicationDispense, related_name='MedicationDispense_dosageInstruction', null=False, on_delete=models.CASCADE)

class FHIR_MedicationDispense_substitution(models.Model):
    MedicationDispense = models.ForeignKey(FHIR_MedicationDispense, related_name='MedicationDispense_substitution', null=False, on_delete=models.CASCADE)
    wasSubstituted = FHIR_primitive_BooleanField(null=True, blank=True, )
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='MedicationDispense_substitution_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    responsibleParty_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="MedicationDispense_substitution_responsibleParty", null=True, blank=True, on_delete=models.SET_NULL)
    responsibleParty_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="MedicationDispense_substitution_responsibleParty", null=True, blank=True, on_delete=models.SET_NULL)
    responsibleParty_Organization = models.ForeignKey("FHIR_Organization", related_name="MedicationDispense_substitution_responsibleParty", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_MedicationDispense_substitution_reason(models.Model):
    MedicationDispense_substitution = models.ForeignKey(FHIR_MedicationDispense_substitution, related_name='MedicationDispense_substitution_reason', null=False, on_delete=models.CASCADE)
    BINDING_reason = "TODO"
    reason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_reason}, related_name='MedicationDispense_substitution_reason', blank=True)
    reason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    