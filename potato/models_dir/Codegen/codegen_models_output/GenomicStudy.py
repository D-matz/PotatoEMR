#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_GenomicStudy(models.Model):
    class StatusChoices(models.TextChoices): REGISTERED = 'registered', 'Registered'; AVAILABLE = 'available', 'Available'; CANCELLED = 'cancelled', 'Cancelled'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    subject_Patient = models.ForeignKey("FHIR_Patient", related_name="GenomicStudy_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Group = models.ForeignKey("FHIR_Group", related_name="GenomicStudy_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_Substance = models.ForeignKey("FHIR_Substance", related_name="GenomicStudy_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_BiologicallyDerivedProduct = models.ForeignKey("FHIR_BiologicallyDerivedProduct", related_name="GenomicStudy_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_NutritionProduct = models.ForeignKey("FHIR_NutritionProduct", related_name="GenomicStudy_subject", null=True, blank=True, on_delete=models.SET_NULL)
    encounter = models.ForeignKey("FHIR_Encounter", related_name="GenomicStudy_encounter", null=True, blank=True, on_delete=models.SET_NULL)
    startDate = FHIR_primitive_DateTimeField(null=True, blank=True, )
    basedOn_ServiceRequest = models.ManyToManyField("FHIR_ServiceRequest", related_name="GenomicStudy_basedOn", blank=True)
    basedOn_Task = models.ManyToManyField("FHIR_Task", related_name="GenomicStudy_basedOn", blank=True)
    referrer_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="GenomicStudy_referrer", null=True, blank=True, on_delete=models.SET_NULL)
    referrer_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="GenomicStudy_referrer", null=True, blank=True, on_delete=models.SET_NULL)
    interpreter_Practitioner = models.ManyToManyField("FHIR_Practitioner", related_name="GenomicStudy_interpreter", blank=True)
    interpreter_PractitionerRole = models.ManyToManyField("FHIR_PractitionerRole", related_name="GenomicStudy_interpreter", blank=True)
    instantiatesCanonical = FHIR_primitive_CanonicalField(null=True, blank=True, )
    instantiatesUri = FHIR_primitive_URIField(null=True, blank=True, )
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_GenomicStudy_identifier(FHIR_GP_Identifier):
    GenomicStudy = models.ForeignKey(FHIR_GenomicStudy, related_name='GenomicStudy_identifier', null=False, on_delete=models.CASCADE)

class FHIR_GenomicStudy_type(models.Model):
    GenomicStudy = models.ForeignKey(FHIR_GenomicStudy, related_name='GenomicStudy_type', null=False, on_delete=models.CASCADE)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='GenomicStudy_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_GenomicStudy_reason(models.Model):
    GenomicStudy = models.ForeignKey(FHIR_GenomicStudy, related_name='GenomicStudy_reason', null=False, on_delete=models.CASCADE)
    BINDING_reason = "TODO"
    reason_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_reason}, related_name='GenomicStudy_reason', blank=True)
    reason_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    reason_Condition_ref = models.ForeignKey("FHIR_Condition", related_name="GenomicStudy_reason_Condition", null=True, blank=True, on_delete=models.SET_NULL)
    reason_Observation_ref = models.ForeignKey("FHIR_Observation", related_name="GenomicStudy_reason_Observation", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_GenomicStudy_note(FHIR_GP_Annotation):
    GenomicStudy = models.ForeignKey(FHIR_GenomicStudy, related_name='GenomicStudy_note', null=False, on_delete=models.CASCADE)

class FHIR_GenomicStudy_analysis(models.Model):
    GenomicStudy = models.ForeignKey(FHIR_GenomicStudy, related_name='GenomicStudy_analysis', null=False, on_delete=models.CASCADE)
    BINDING_genomeBuild = "TODO"
    genomeBuild_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_genomeBuild}, related_name='GenomicStudy_analysis_genomeBuild', blank=True)
    genomeBuild_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    instantiatesCanonical = FHIR_primitive_CanonicalField(null=True, blank=True, )
    instantiatesUri = FHIR_primitive_URIField(null=True, blank=True, )
    title = FHIR_primitive_StringField(null=True, blank=True, )
    specimen = models.ManyToManyField("FHIR_Specimen", related_name="GenomicStudy_analysis_specimen", blank=True)
    date = FHIR_primitive_DateTimeField(null=True, blank=True, )
    protocolPerformed_Procedure = models.ForeignKey("FHIR_Procedure", related_name="GenomicStudy_analysis_protocolPerformed", null=True, blank=True, on_delete=models.SET_NULL)
    protocolPerformed_Task = models.ForeignKey("FHIR_Task", related_name="GenomicStudy_analysis_protocolPerformed", null=True, blank=True, on_delete=models.SET_NULL)
    regionsStudied_DocumentReference = models.ManyToManyField("FHIR_DocumentReference", related_name="GenomicStudy_analysis_regionsStudied", blank=True)
    regionsStudied_Observation = models.ManyToManyField("FHIR_Observation", related_name="GenomicStudy_analysis_regionsStudied", blank=True)
    regionsCalled_DocumentReference = models.ManyToManyField("FHIR_DocumentReference", related_name="GenomicStudy_analysis_regionsCalled", blank=True)
    regionsCalled_Observation = models.ManyToManyField("FHIR_Observation", related_name="GenomicStudy_analysis_regionsCalled", blank=True)

class FHIR_GenomicStudy_analysis_identifier(FHIR_GP_Identifier):
    GenomicStudy_analysis = models.ForeignKey(FHIR_GenomicStudy_analysis, related_name='GenomicStudy_analysis_identifier', null=False, on_delete=models.CASCADE)

class FHIR_GenomicStudy_analysis_methodType(models.Model):
    GenomicStudy_analysis = models.ForeignKey(FHIR_GenomicStudy_analysis, related_name='GenomicStudy_analysis_methodType', null=False, on_delete=models.CASCADE)
    BINDING_methodType = "TODO"
    methodType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_methodType}, related_name='GenomicStudy_analysis_methodType', blank=True)
    methodType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_GenomicStudy_analysis_changeType(models.Model):
    GenomicStudy_analysis = models.ForeignKey(FHIR_GenomicStudy_analysis, related_name='GenomicStudy_analysis_changeType', null=False, on_delete=models.CASCADE)
    BINDING_changeType = "TODO"
    changeType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_changeType}, related_name='GenomicStudy_analysis_changeType', blank=True)
    changeType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_GenomicStudy_analysis_note(FHIR_GP_Annotation):
    GenomicStudy_analysis = models.ForeignKey(FHIR_GenomicStudy_analysis, related_name='GenomicStudy_analysis_note', null=False, on_delete=models.CASCADE)

class FHIR_GenomicStudy_analysis_input(models.Model):
    GenomicStudy_analysis = models.ForeignKey(FHIR_GenomicStudy_analysis, related_name='GenomicStudy_analysis_input', null=False, on_delete=models.CASCADE)
    file = models.ForeignKey("FHIR_DocumentReference", related_name="GenomicStudy_analysis_input_file", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='GenomicStudy_analysis_input_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    generatedBy_Identifier = models.OneToOneField("FHIR_GP_Identifier", related_name='GenomicStudy_analysis_input_generatedBy_Identifier', null=True, blank=True, on_delete=models.SET_NULL)
    generatedBy_Reference = models.ForeignKey("FHIR_GenomicStudy", related_name="GenomicStudy_analysis_input_generatedBy_Reference", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_GenomicStudy_analysis_output(models.Model):
    GenomicStudy_analysis = models.ForeignKey(FHIR_GenomicStudy_analysis, related_name='GenomicStudy_analysis_output', null=False, on_delete=models.CASCADE)
    file = models.ForeignKey("FHIR_DocumentReference", related_name="GenomicStudy_analysis_output_file", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='GenomicStudy_analysis_output_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_GenomicStudy_analysis_performer(models.Model):
    GenomicStudy_analysis = models.ForeignKey(FHIR_GenomicStudy_analysis, related_name='GenomicStudy_analysis_performer', null=False, on_delete=models.CASCADE)
    actor_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="GenomicStudy_analysis_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="GenomicStudy_analysis_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Organization = models.ForeignKey("FHIR_Organization", related_name="GenomicStudy_analysis_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    actor_Device = models.ForeignKey("FHIR_Device", related_name="GenomicStudy_analysis_performer_actor", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_role = "TODO"
    role_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_role}, related_name='GenomicStudy_analysis_performer_role', blank=True)
    role_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_GenomicStudy_analysis_device(models.Model):
    GenomicStudy_analysis = models.ForeignKey(FHIR_GenomicStudy_analysis, related_name='GenomicStudy_analysis_device', null=False, on_delete=models.CASCADE)
    device = models.ForeignKey("FHIR_Device", related_name="GenomicStudy_analysis_device_device", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_function = "TODO"
    function_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_function}, related_name='GenomicStudy_analysis_device_function', blank=True)
    function_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
