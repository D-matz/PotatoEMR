#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Observation(models.Model):
    instantiates = FHIR_primitive_CanonicalField(null=True, blank=True, )
    instantiates = models.ForeignKey("FHIR_ObservationDefinition", related_name="Observation_instantiates", null=True, blank=True, on_delete=models.SET_NULL)
    basedOn_CarePlan = models.ManyToManyField("FHIR_CarePlan", related_name="Observation_basedOn", blank=True)
    basedOn_DeviceRequest = models.ManyToManyField("FHIR_DeviceRequest", related_name="Observation_basedOn", blank=True)
    basedOn_ImmunizationRecommendation = models.ManyToManyField("FHIR_ImmunizationRecommendation", related_name="Observation_basedOn", blank=True)
    basedOn_MedicationRequest = models.ManyToManyField("FHIR_MedicationRequest", related_name="Observation_basedOn", blank=True)
    basedOn_NutritionOrder = models.ManyToManyField("FHIR_NutritionOrder", related_name="Observation_basedOn", blank=True)
    basedOn_ServiceRequest = models.ManyToManyField("FHIR_ServiceRequest", related_name="Observation_basedOn", blank=True)
    partOf_MedicationAdministration = models.ManyToManyField("FHIR_MedicationAdministration", related_name="Observation_partOf", blank=True)
    partOf_MedicationDispense = models.ManyToManyField("FHIR_MedicationDispense", related_name="Observation_partOf", blank=True)
    partOf_MedicationStatement = models.ManyToManyField("FHIR_MedicationStatement", related_name="Observation_partOf", blank=True)
    partOf_Procedure = models.ManyToManyField("FHIR_Procedure", related_name="Observation_partOf", blank=True)
    partOf_Immunization = models.ManyToManyField("FHIR_Immunization", related_name="Observation_partOf", blank=True)
    partOf_ImagingStudy = models.ManyToManyField("FHIR_ImagingStudy", related_name="Observation_partOf", blank=True)
    partOf_GenomicStudy = models.ManyToManyField("FHIR_GenomicStudy", related_name="Observation_partOf", blank=True)
    class StatusChoices(models.TextChoices): REGISTERED = 'registered', 'Registered'; SPECIMEN_IN_PROCESS = 'specimen-in-process', 'Specimen-in-process'; PRELIMINARY = 'preliminary', 'Preliminary'; FINAL = 'final', 'Final'; AMENDED = 'amended', 'Amended'; CORRECTED = 'corrected', 'Corrected'; APPENDED = 'appended', 'Appended'; CANCELLED = 'cancelled', 'Cancelled'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; UNKNOWN = 'unknown', 'Unknown'; CANNOT_BE_OBTAINED = 'cannot-be-obtained', 'Cannot-be-obtained'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    BINDING_code = "TODO"
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='Observation_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    subject_Patient = models.ForeignKey("FHIR_Patient", related_name="Observation_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Group = models.ForeignKey("FHIR_Group", related_name="Observation_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Device = models.ForeignKey("FHIR_Device", related_name="Observation_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Location = models.ForeignKey("FHIR_Location", related_name="Observation_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Organization = models.ForeignKey("FHIR_Organization", related_name="Observation_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Procedure = models.ForeignKey("FHIR_Procedure", related_name="Observation_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="Observation_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Medication = models.ForeignKey("FHIR_Medication", related_name="Observation_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Substance = models.ForeignKey("FHIR_Substance", related_name="Observation_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_BiologicallyDerivedProduct = models.ForeignKey("FHIR_BiologicallyDerivedProduct", related_name="Observation_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_NutritionProduct = models.ForeignKey("FHIR_NutritionProduct", related_name="Observation_subject", null=True, blank=True, on_delete=models.SET_NULL)
    organizer = FHIR_primitive_BooleanField(null=True, blank=True, )
    encounter = models.ForeignKey("FHIR_Encounter", related_name="Observation_encounter", null=True, blank=True, on_delete=models.SET_NULL)
    effective = FHIR_primitive_DateTimeField(null=True, blank=True, )
    effective = models.OneToOneField("FHIR_GP_Period", related_name='Observation_effective', null=True, blank=True, on_delete=models.SET_NULL)
    effective = models.OneToOneField("FHIR_GP_Timing", related_name='Observation_effective', null=True, blank=True, on_delete=models.SET_NULL)
    effective = FHIR_primitive_InstantField(null=True, blank=True, )
    issued = FHIR_primitive_InstantField(null=True, blank=True, )
    performer_Practitioner = models.ManyToManyField("FHIR_Practitioner", related_name="Observation_performer", blank=True)
    performer_PractitionerRole = models.ManyToManyField("FHIR_PractitionerRole", related_name="Observation_performer", blank=True)
    performer_Organization = models.ManyToManyField("FHIR_Organization", related_name="Observation_performer", blank=True)
    performer_CareTeam = models.ManyToManyField("FHIR_CareTeam", related_name="Observation_performer", blank=True)
    performer_Patient = models.ManyToManyField("FHIR_Patient", related_name="Observation_performer", blank=True)
    performer_RelatedPerson = models.ManyToManyField("FHIR_RelatedPerson", related_name="Observation_performer", blank=True)
    performer_HealthcareService = models.ManyToManyField("FHIR_HealthcareService", related_name="Observation_performer", blank=True)
    value = models.OneToOneField("FHIR_GP_Quantity", related_name='Observation_value', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_value = "TODO"
    value_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_value}, related_name='Observation_value', blank=True)
    value_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value = FHIR_primitive_StringField(null=True, blank=True, )
    value = FHIR_primitive_BooleanField(null=True, blank=True, )
    value = models.OneToOneField("FHIR_GP_Range", related_name='Observation_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_Ratio", related_name='Observation_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_SampledData", related_name='Observation_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = FHIR_primitive_TimeField(null=True, blank=True, )
    value = FHIR_primitive_DateTimeField(null=True, blank=True, )
    value = models.OneToOneField("FHIR_GP_Period", related_name='Observation_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_Attachment", related_name='Observation_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.ForeignKey("FHIR_MolecularSequence", related_name="Observation_value", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_dataAbsentReason = "TODO"
    dataAbsentReason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_dataAbsentReason}, related_name='Observation_dataAbsentReason', blank=True)
    dataAbsentReason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_bodySite = "TODO"
    bodySite_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_bodySite}, related_name='Observation_bodySite', blank=True)
    bodySite_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    bodyStructure = models.ForeignKey("FHIR_BodyStructure", related_name="Observation_bodyStructure", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_method = "TODO"
    method_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_method}, related_name='Observation_method', blank=True)
    method_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    specimen_Specimen = models.ForeignKey("FHIR_Specimen", related_name="Observation_specimen", null=True, blank=True, on_delete=models.SET_NULL)
    specimen_Group = models.ForeignKey("FHIR_Group", related_name="Observation_specimen", null=True, blank=True, on_delete=models.SET_NULL)
    device_Device = models.ForeignKey("FHIR_Device", related_name="Observation_device", null=True, blank=True, on_delete=models.SET_NULL)
    device_DeviceMetric = models.ForeignKey("FHIR_DeviceMetric", related_name="Observation_device", null=True, blank=True, on_delete=models.SET_NULL)
    hasMember_Observation = models.ManyToManyField("FHIR_Observation", related_name="Observation_hasMember", blank=True)
    hasMember_QuestionnaireResponse = models.ManyToManyField("FHIR_QuestionnaireResponse", related_name="Observation_hasMember", blank=True)
    hasMember_MolecularSequence = models.ManyToManyField("FHIR_MolecularSequence", related_name="Observation_hasMember", blank=True)
    derivedFrom_DocumentReference = models.ManyToManyField("FHIR_DocumentReference", related_name="Observation_derivedFrom", blank=True)
    derivedFrom_ImagingStudy = models.ManyToManyField("FHIR_ImagingStudy", related_name="Observation_derivedFrom", blank=True)
    derivedFrom_ImagingSelection = models.ManyToManyField("FHIR_ImagingSelection", related_name="Observation_derivedFrom", blank=True)
    derivedFrom_QuestionnaireResponse = models.ManyToManyField("FHIR_QuestionnaireResponse", related_name="Observation_derivedFrom", blank=True)
    derivedFrom_Observation = models.ManyToManyField("FHIR_Observation", related_name="Observation_derivedFrom", blank=True)
    derivedFrom_MolecularSequence = models.ManyToManyField("FHIR_MolecularSequence", related_name="Observation_derivedFrom", blank=True)
    derivedFrom_GenomicStudy = models.ManyToManyField("FHIR_GenomicStudy", related_name="Observation_derivedFrom", blank=True)

class FHIR_Observation_identifier(FHIR_GP_Identifier):
    Observation = models.ForeignKey(FHIR_Observation, related_name='Observation_identifier', null=False, on_delete=models.CASCADE)

class FHIR_Observation_triggeredBy(models.Model):
    Observation = models.ForeignKey(FHIR_Observation, related_name='Observation_triggeredBy', null=False, on_delete=models.CASCADE)
    triggeredBy_observation = models.ForeignKey("FHIR_Observation", related_name="Observation_triggeredBy_observation", null=True, blank=True, on_delete=models.SET_NULL)
    class TypeChoices(models.TextChoices): REFLEX = 'reflex', 'Reflex'; REPEAT = 'repeat', 'Repeat'; RE_RUN = 're-run', 'Re-run'; 
    type = FHIR_primitive_CodeField(choices=TypeChoices.choices, null=True, blank=True, )
    reason = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_Observation_category(models.Model):
    Observation = models.ForeignKey(FHIR_Observation, related_name='Observation_category', null=False, on_delete=models.CASCADE)
    BINDING_category = "TODO"
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='Observation_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Observation_interpretation(models.Model):
    Observation = models.ForeignKey(FHIR_Observation, related_name='Observation_interpretation', null=False, on_delete=models.CASCADE)
    BINDING_interpretation = "TODO"
    interpretation_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_interpretation}, related_name='Observation_interpretation', blank=True)
    interpretation_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Observation_note(FHIR_GP_Annotation):
    Observation = models.ForeignKey(FHIR_Observation, related_name='Observation_note', null=False, on_delete=models.CASCADE)

class FHIR_Observation_referenceRange(models.Model):
    Observation = models.ForeignKey(FHIR_Observation, related_name='Observation_referenceRange', null=False, on_delete=models.CASCADE)
    low = models.OneToOneField("FHIR_GP_Quantity", related_name='Observation_referenceRange_low', null=True, blank=True, on_delete=models.SET_NULL)
    high = models.OneToOneField("FHIR_GP_Quantity", related_name='Observation_referenceRange_high', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_normalValue = "TODO"
    normalValue_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_normalValue}, related_name='Observation_referenceRange_normalValue', blank=True)
    normalValue_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='Observation_referenceRange_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    age = models.OneToOneField("FHIR_GP_Range", related_name='Observation_referenceRange_age', null=True, blank=True, on_delete=models.SET_NULL)
    text = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_Observation_referenceRange_appliesTo(models.Model):
    Observation_referenceRange = models.ForeignKey(FHIR_Observation_referenceRange, related_name='Observation_referenceRange_appliesTo', null=False, on_delete=models.CASCADE)
    BINDING_appliesTo = "TODO"
    appliesTo_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_appliesTo}, related_name='Observation_referenceRange_appliesTo', blank=True)
    appliesTo_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Observation_component(models.Model):
    Observation = models.ForeignKey(FHIR_Observation, related_name='Observation_component', null=False, on_delete=models.CASCADE)
    BINDING_code = "TODO"
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='Observation_component_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value = models.OneToOneField("FHIR_GP_Quantity", related_name='Observation_component_value', null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_value = "TODO"
    value_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_value}, related_name='Observation_component_value', blank=True)
    value_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value = FHIR_primitive_StringField(null=True, blank=True, )
    value = FHIR_primitive_BooleanField(null=True, blank=True, )
    value = models.OneToOneField("FHIR_GP_Range", related_name='Observation_component_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_Ratio", related_name='Observation_component_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_SampledData", related_name='Observation_component_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = FHIR_primitive_TimeField(null=True, blank=True, )
    value = FHIR_primitive_DateTimeField(null=True, blank=True, )
    value = models.OneToOneField("FHIR_GP_Period", related_name='Observation_component_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_Attachment", related_name='Observation_component_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.ForeignKey("FHIR_MolecularSequence", related_name="Observation_component_value", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_dataAbsentReason = "TODO"
    dataAbsentReason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_dataAbsentReason}, related_name='Observation_component_dataAbsentReason', blank=True)
    dataAbsentReason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_Observation_component_interpretation(models.Model):
    Observation_component = models.ForeignKey(FHIR_Observation_component, related_name='Observation_component_interpretation', null=False, on_delete=models.CASCADE)
    BINDING_interpretation = "TODO"
    interpretation_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_interpretation}, related_name='Observation_component_interpretation', blank=True)
    interpretation_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    