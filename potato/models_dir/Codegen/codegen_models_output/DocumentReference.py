#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_DocumentReference(models.Model):
    version = FHIR_primitive_StringField(null=True, blank=True, )
    basedOn_Appointment = models.ManyToManyField("FHIR_Appointment", related_name="DocumentReference_basedOn", blank=True)
    basedOn_AppointmentResponse = models.ManyToManyField("FHIR_AppointmentResponse", related_name="DocumentReference_basedOn", blank=True)
    basedOn_CarePlan = models.ManyToManyField("FHIR_CarePlan", related_name="DocumentReference_basedOn", blank=True)
    basedOn_Claim = models.ManyToManyField("FHIR_Claim", related_name="DocumentReference_basedOn", blank=True)
    basedOn_CommunicationRequest = models.ManyToManyField("FHIR_CommunicationRequest", related_name="DocumentReference_basedOn", blank=True)
    basedOn_Contract = models.ManyToManyField("FHIR_Contract", related_name="DocumentReference_basedOn", blank=True)
    basedOn_CoverageEligibilityRequest = models.ManyToManyField("FHIR_CoverageEligibilityRequest", related_name="DocumentReference_basedOn", blank=True)
    basedOn_DeviceRequest = models.ManyToManyField("FHIR_DeviceRequest", related_name="DocumentReference_basedOn", blank=True)
    basedOn_EnrollmentRequest = models.ManyToManyField("FHIR_EnrollmentRequest", related_name="DocumentReference_basedOn", blank=True)
    basedOn_ImmunizationRecommendation = models.ManyToManyField("FHIR_ImmunizationRecommendation", related_name="DocumentReference_basedOn", blank=True)
    basedOn_MedicationRequest = models.ManyToManyField("FHIR_MedicationRequest", related_name="DocumentReference_basedOn", blank=True)
    basedOn_NutritionOrder = models.ManyToManyField("FHIR_NutritionOrder", related_name="DocumentReference_basedOn", blank=True)
    basedOn_RequestOrchestration = models.ManyToManyField("FHIR_RequestOrchestration", related_name="DocumentReference_basedOn", blank=True)
    basedOn_ServiceRequest = models.ManyToManyField("FHIR_ServiceRequest", related_name="DocumentReference_basedOn", blank=True)
    basedOn_SupplyRequest = models.ManyToManyField("FHIR_SupplyRequest", related_name="DocumentReference_basedOn", blank=True)
    basedOn_VisionPrescription = models.ManyToManyField("FHIR_VisionPrescription", related_name="DocumentReference_basedOn", blank=True)
    class StatusChoices(models.TextChoices): CURRENT = 'current', 'Current'; SUPERSEDED = 'superseded', 'Superseded'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    class DocstatusChoices(models.TextChoices): REGISTERED = 'registered', 'Registered'; PARTIAL = 'partial', 'Partial'; PRELIMINARY = 'preliminary', 'Preliminary'; FINAL = 'final', 'Final'; AMENDED = 'amended', 'Amended'; CORRECTED = 'corrected', 'Corrected'; APPENDED = 'appended', 'Appended'; CANCELLED = 'cancelled', 'Cancelled'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; DEPRECATED = 'deprecated', 'Deprecated'; UNKNOWN = 'unknown', 'Unknown'; 
    docStatus = FHIR_primitive_CodeField(choices=DocstatusChoices.choices, null=True, blank=True, )
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='DocumentReference_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    context_Appointment = models.ManyToManyField("FHIR_Appointment", related_name="DocumentReference_context", blank=True)
    context_Encounter = models.ManyToManyField("FHIR_Encounter", related_name="DocumentReference_context", blank=True)
    context_EpisodeOfCare = models.ManyToManyField("FHIR_EpisodeOfCare", related_name="DocumentReference_context", blank=True)
    BINDING_facilityType = "TODO"
    facilityType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_facilityType}, related_name='DocumentReference_facilityType', blank=True)
    facilityType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_practiceSetting = "TODO"
    practiceSetting_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_practiceSetting}, related_name='DocumentReference_practiceSetting', blank=True)
    practiceSetting_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    period = models.OneToOneField("FHIR_GP_Period", related_name='DocumentReference_period', null=True, blank=True, on_delete=models.SET_NULL)
    date = FHIR_primitive_DateTimeField(null=True, blank=True, )
    author_Practitioner = models.ManyToManyField("FHIR_Practitioner", related_name="DocumentReference_author", blank=True)
    author_PractitionerRole = models.ManyToManyField("FHIR_PractitionerRole", related_name="DocumentReference_author", blank=True)
    author_Organization = models.ManyToManyField("FHIR_Organization", related_name="DocumentReference_author", blank=True)
    author_Device = models.ManyToManyField("FHIR_Device", related_name="DocumentReference_author", blank=True)
    author_Patient = models.ManyToManyField("FHIR_Patient", related_name="DocumentReference_author", blank=True)
    author_RelatedPerson = models.ManyToManyField("FHIR_RelatedPerson", related_name="DocumentReference_author", blank=True)
    author_CareTeam = models.ManyToManyField("FHIR_CareTeam", related_name="DocumentReference_author", blank=True)
    author_Group = models.ManyToManyField("FHIR_Group", related_name="DocumentReference_author", blank=True)
    custodian = models.ForeignKey("FHIR_Organization", related_name="DocumentReference_custodian", null=True, blank=True, on_delete=models.SET_NULL)
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_DocumentReference_identifier(FHIR_GP_Identifier):
    DocumentReference = models.ForeignKey(FHIR_DocumentReference, related_name='DocumentReference_identifier', null=False, on_delete=models.CASCADE)

class FHIR_DocumentReference_modality(models.Model):
    DocumentReference = models.ForeignKey(FHIR_DocumentReference, related_name='DocumentReference_modality', null=False, on_delete=models.CASCADE)
    BINDING_modality = "TODO"
    modality_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_modality}, related_name='DocumentReference_modality', blank=True)
    modality_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_DocumentReference_category(models.Model):
    DocumentReference = models.ForeignKey(FHIR_DocumentReference, related_name='DocumentReference_category', null=False, on_delete=models.CASCADE)
    BINDING_category = "TODO"
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='DocumentReference_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_DocumentReference_event(models.Model):
    DocumentReference = models.ForeignKey(FHIR_DocumentReference, related_name='DocumentReference_event', null=False, on_delete=models.CASCADE)
    BINDING_event = "TODO"
    event_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_event}, related_name='DocumentReference_event', blank=True)
    event_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_DocumentReference_bodySite(models.Model):
    DocumentReference = models.ForeignKey(FHIR_DocumentReference, related_name='DocumentReference_bodySite', null=False, on_delete=models.CASCADE)
    BINDING_bodySite = "TODO"
    bodySite_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_bodySite}, related_name='DocumentReference_bodySite', blank=True)
    bodySite_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    bodySite_BodyStructure_ref = models.ForeignKey("FHIR_BodyStructure", related_name="DocumentReference_bodySite_BodyStructure", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_DocumentReference_attester(models.Model):
    DocumentReference = models.ForeignKey(FHIR_DocumentReference, related_name='DocumentReference_attester', null=False, on_delete=models.CASCADE)
    BINDING_mode = "TODO"
    mode_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_mode}, related_name='DocumentReference_attester_mode', blank=True)
    mode_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    time = FHIR_primitive_DateTimeField(null=True, blank=True, )
    party_Patient = models.ForeignKey("FHIR_Patient", related_name="DocumentReference_attester_party", null=True, blank=True, on_delete=models.SET_NULL)
    party_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="DocumentReference_attester_party", null=True, blank=True, on_delete=models.SET_NULL)
    party_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="DocumentReference_attester_party", null=True, blank=True, on_delete=models.SET_NULL)
    party_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="DocumentReference_attester_party", null=True, blank=True, on_delete=models.SET_NULL)
    party_Organization = models.ForeignKey("FHIR_Organization", related_name="DocumentReference_attester_party", null=True, blank=True, on_delete=models.SET_NULL)
    party_Group = models.ForeignKey("FHIR_Group", related_name="DocumentReference_attester_party", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_DocumentReference_relatesTo(models.Model):
    DocumentReference = models.ForeignKey(FHIR_DocumentReference, related_name='DocumentReference_relatesTo', null=False, on_delete=models.CASCADE)
    BINDING_code = "TODO"
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='DocumentReference_relatesTo_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    target = models.ForeignKey("FHIR_DocumentReference", related_name="DocumentReference_relatesTo_target", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_DocumentReference_securityLabel(models.Model):
    DocumentReference = models.ForeignKey(FHIR_DocumentReference, related_name='DocumentReference_securityLabel', null=False, on_delete=models.CASCADE)
    BINDING_securityLabel = "TODO"
    securityLabel_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_securityLabel}, related_name='DocumentReference_securityLabel', blank=True)
    securityLabel_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_DocumentReference_content(models.Model):
    DocumentReference = models.ForeignKey(FHIR_DocumentReference, related_name='DocumentReference_content', null=False, on_delete=models.CASCADE)
    attachment = models.OneToOneField("FHIR_GP_Attachment", related_name='DocumentReference_content_attachment', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_DocumentReference_content_profile(models.Model):
    DocumentReference_content = models.ForeignKey(FHIR_DocumentReference_content, related_name='DocumentReference_content_profile', null=False, on_delete=models.CASCADE)
    value_Coding = models.OneToOneField("FHIR_GP_Coding", related_name='DocumentReference_content_profile_value_Coding', null=True, blank=True, on_delete=models.SET_NULL)
    value_uri = FHIR_primitive_URIField(null=True, blank=True, )
    value_canonical = FHIR_primitive_CanonicalField(null=True, blank=True, )
