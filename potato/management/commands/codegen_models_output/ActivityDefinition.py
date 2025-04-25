
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_ActivityDefinition(models.Model):
    url = FHIR_primitive_URIField(null=True, blank=True, )
    version = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = models.OneToOneField("FHIR_GP_Coding", related_name='ActivityDefinition_versionAlgorithm', null=True, blank=True, on_delete=models.SET_NULL)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    title = FHIR_primitive_StringField(null=True, blank=True, )
    subtitle = FHIR_primitive_StringField(null=True, blank=True, )
    class StatusChoices(models.TextChoices): DRAFT = 'draft', 'Draft'; ACTIVE = 'active', 'Active'; RETIRED = 'retired', 'Retired'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    experimental = FHIR_primitive_BooleanField(null=True, blank=True, )
    BINDING_subject = 'TODO'
    subject_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_subject}, related_name='ActivityDefinition_subject', blank=True)
    subject_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    subject_Group = models.ForeignKey("FHIR_Group", related_name="ActivityDefinition_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_MedicinalProductDefinition = models.ForeignKey("FHIR_MedicinalProductDefinition", related_name="ActivityDefinition_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_SubstanceDefinition = models.ForeignKey("FHIR_SubstanceDefinition", related_name="ActivityDefinition_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_AdministrableProductDefinition = models.ForeignKey("FHIR_AdministrableProductDefinition", related_name="ActivityDefinition_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_ManufacturedItemDefinition = models.ForeignKey("FHIR_ManufacturedItemDefinition", related_name="ActivityDefinition_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject_PackagedProductDefinition = models.ForeignKey("FHIR_PackagedProductDefinition", related_name="ActivityDefinition_subject", null=True, blank=True, on_delete=models.SET_NULL)
    subject = FHIR_primitive_CanonicalField(null=True, blank=True, )
    date = FHIR_primitive_DateTimeField(null=True, blank=True, )
    publisher = FHIR_primitive_StringField(null=True, blank=True, )
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    purpose = FHIR_primitive_MarkdownField(null=True, blank=True, )
    usage = FHIR_primitive_MarkdownField(null=True, blank=True, )
    copyright = FHIR_primitive_MarkdownField(null=True, blank=True, )
    copyrightLabel = FHIR_primitive_StringField(null=True, blank=True, )
    approvalDate = FHIR_primitive_DateField(null=True, blank=True, )
    lastReviewDate = FHIR_primitive_DateField(null=True, blank=True, )
    effectivePeriod = models.OneToOneField("FHIR_GP_Period", related_name='ActivityDefinition_effectivePeriod', null=True, blank=True, on_delete=models.SET_NULL)
    class KindChoices(models.TextChoices): KIND_OF_RESOURCE = 'Kind of resource', 'Kind of resource'; 
    kind = FHIR_primitive_CodeField(choices=KindChoices.choices, null=True, blank=True, )
    profile = FHIR_primitive_CanonicalField(null=True, blank=True, )
    BINDING_code = 'TODO'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='ActivityDefinition_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    class IntentChoices(models.TextChoices): PROPOSAL = 'proposal', 'Proposal'; PLAN = 'plan', 'Plan'; DIRECTIVE = 'directive', 'Directive'; ORDER = 'order', 'Order'; ORIGINAL_ORDER = 'original-order', 'Original-order'; REFLEX_ORDER = 'reflex-order', 'Reflex-order'; FILLER_ORDER = 'filler-order', 'Filler-order'; INSTANCE_ORDER = 'instance-order', 'Instance-order'; OPTION = 'option', 'Option'; 
    intent = FHIR_primitive_CodeField(choices=IntentChoices.choices, null=True, blank=True, )
    class PriorityChoices(models.TextChoices): ROUTINE = 'routine', 'Routine'; URGENT = 'urgent', 'Urgent'; ASAP = 'asap', 'Asap'; STAT = 'stat', 'Stat'; 
    priority = FHIR_primitive_CodeField(choices=PriorityChoices.choices, null=True, blank=True, )
    doNotPerform = FHIR_primitive_BooleanField(null=True, blank=True, )
    timing = models.OneToOneField("FHIR_GP_Timing", related_name='ActivityDefinition_timing', null=True, blank=True, on_delete=models.SET_NULL)
    timing = models.OneToOneField("FHIR_GP_Quantity_Age", related_name='ActivityDefinition_timing', null=True, blank=True, on_delete=models.SET_NULL)
    timing = models.OneToOneField("FHIR_GP_Range", related_name='ActivityDefinition_timing', null=True, blank=True, on_delete=models.SET_NULL)
    timing = models.OneToOneField("FHIR_GP_Quantity_Duration", related_name='ActivityDefinition_timing', null=True, blank=True, on_delete=models.SET_NULL)
    asNeeded = FHIR_primitive_BooleanField(null=True, blank=True, )
    BINDING_asNeeded = 'TODO'
    asNeeded_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_asNeeded}, related_name='ActivityDefinition_asNeeded', blank=True)
    asNeeded_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_location = 'TODO'
    location_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_location}, related_name='ActivityDefinition_location', blank=True)
    location_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    location_Location_ref = models.ForeignKey("FHIR_Location", related_name="ActivityDefinition_location", null=True, blank=True, on_delete=models.SET_NULL)
    product_Medication = models.ForeignKey("FHIR_Medication", related_name="ActivityDefinition_product", null=True, blank=True, on_delete=models.SET_NULL)
    product_Ingredient = models.ForeignKey("FHIR_Ingredient", related_name="ActivityDefinition_product", null=True, blank=True, on_delete=models.SET_NULL)
    product_SubstanceDefinition = models.ForeignKey("FHIR_SubstanceDefinition", related_name="ActivityDefinition_product", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_product = 'TODO'
    product_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_product}, related_name='ActivityDefinition_product', blank=True)
    product_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    quantity = models.OneToOneField("FHIR_GP_Quantity", related_name='ActivityDefinition_quantity', null=True, blank=True, on_delete=models.SET_NULL)
    transform = FHIR_primitive_CanonicalField(null=True, blank=True, )

class FHIR_ActivityDefinition_identifier(FHIR_GP_Identifier):
    ActivityDefinition = models.ForeignKey(FHIR_ActivityDefinition, related_name='ActivityDefinition_identifier', null=False, on_delete=models.CASCADE)

class FHIR_ActivityDefinition_jurisdiction(models.Model):
    ActivityDefinition = models.ForeignKey(FHIR_ActivityDefinition, related_name='ActivityDefinition_jurisdiction', null=False, on_delete=models.CASCADE)
    BINDING_jurisdiction = 'TODO'
    jurisdiction_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_jurisdiction}, related_name='ActivityDefinition_jurisdiction', blank=True)
    jurisdiction_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ActivityDefinition_topic(models.Model):
    ActivityDefinition = models.ForeignKey(FHIR_ActivityDefinition, related_name='ActivityDefinition_topic', null=False, on_delete=models.CASCADE)
    BINDING_topic = 'TODO'
    topic_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_topic}, related_name='ActivityDefinition_topic', blank=True)
    topic_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ActivityDefinition_library(models.Model):
    ActivityDefinition = models.ForeignKey(FHIR_ActivityDefinition, related_name='ActivityDefinition_library', null=False, on_delete=models.CASCADE)
    
    library = FHIR_primitive_CanonicalField(null=True, blank=True, )
    
class FHIR_ActivityDefinition_participant(models.Model):
    ActivityDefinition = models.ForeignKey(FHIR_ActivityDefinition, related_name='ActivityDefinition_participant', null=False, on_delete=models.CASCADE)
    class TypeChoices(models.TextChoices): CARETEAM = 'careteam', 'Careteam'; DEVICE = 'device', 'Device'; GROUP = 'group', 'Group'; HEALTHCARESERVICE = 'healthcareservice', 'Healthcareservice'; LOCATION = 'location', 'Location'; ORGANIZATION = 'organization', 'Organization'; PATIENT = 'patient', 'Patient'; PRACTITIONER = 'practitioner', 'Practitioner'; PRACTITIONERROLE = 'practitionerrole', 'Practitionerrole'; RELATEDPERSON = 'relatedperson', 'Relatedperson'; 
    type = FHIR_primitive_CodeField(choices=TypeChoices.choices, null=True, blank=True, )
    typeCanonical = FHIR_primitive_CanonicalField(null=True, blank=True, )
    typeReference_BiologicallyDerivedProduct = models.ForeignKey("FHIR_BiologicallyDerivedProduct", related_name="ActivityDefinition_participant_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_CareTeam = models.ForeignKey("FHIR_CareTeam", related_name="ActivityDefinition_participant_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_Device = models.ForeignKey("FHIR_Device", related_name="ActivityDefinition_participant_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_DeviceDefinition = models.ForeignKey("FHIR_DeviceDefinition", related_name="ActivityDefinition_participant_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_Endpoint = models.ForeignKey("FHIR_Endpoint", related_name="ActivityDefinition_participant_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_Group = models.ForeignKey("FHIR_Group", related_name="ActivityDefinition_participant_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_HealthcareService = models.ForeignKey("FHIR_HealthcareService", related_name="ActivityDefinition_participant_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_Location = models.ForeignKey("FHIR_Location", related_name="ActivityDefinition_participant_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_Medication = models.ForeignKey("FHIR_Medication", related_name="ActivityDefinition_participant_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_Organization = models.ForeignKey("FHIR_Organization", related_name="ActivityDefinition_participant_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_Patient = models.ForeignKey("FHIR_Patient", related_name="ActivityDefinition_participant_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="ActivityDefinition_participant_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="ActivityDefinition_participant_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="ActivityDefinition_participant_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_Specimen = models.ForeignKey("FHIR_Specimen", related_name="ActivityDefinition_participant_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    typeReference_Substance = models.ForeignKey("FHIR_Substance", related_name="ActivityDefinition_participant_typeReference", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_role = 'TODO'
    role_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_role}, related_name='ActivityDefinition_participant_role', blank=True)
    role_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_function = 'TODO'
    function_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_function}, related_name='ActivityDefinition_participant_function', blank=True)
    function_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_ActivityDefinition_dosage(FHIR_SP_Dosage):
    ActivityDefinition = models.ForeignKey(FHIR_ActivityDefinition, related_name='ActivityDefinition_dosage', null=False, on_delete=models.CASCADE)

class FHIR_ActivityDefinition_bodySite(models.Model):
    ActivityDefinition = models.ForeignKey(FHIR_ActivityDefinition, related_name='ActivityDefinition_bodySite', null=False, on_delete=models.CASCADE)
    BINDING_bodySite = 'TODO'
    bodySite_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_bodySite}, related_name='ActivityDefinition_bodySite', blank=True)
    bodySite_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_ActivityDefinition_specimenRequirement(models.Model):
    ActivityDefinition = models.ForeignKey(FHIR_ActivityDefinition, related_name='ActivityDefinition_specimenRequirement', null=False, on_delete=models.CASCADE)
    
    specimenRequirement = FHIR_primitive_CanonicalField(null=True, blank=True, )
    
class FHIR_ActivityDefinition_observationRequirement(models.Model):
    ActivityDefinition = models.ForeignKey(FHIR_ActivityDefinition, related_name='ActivityDefinition_observationRequirement', null=False, on_delete=models.CASCADE)
    
    observationRequirement = FHIR_primitive_CanonicalField(null=True, blank=True, )
    
class FHIR_ActivityDefinition_observationResultRequirement(models.Model):
    ActivityDefinition = models.ForeignKey(FHIR_ActivityDefinition, related_name='ActivityDefinition_observationResultRequirement', null=False, on_delete=models.CASCADE)
    
    observationResultRequirement = FHIR_primitive_CanonicalField(null=True, blank=True, )
    
class FHIR_ActivityDefinition_dynamicValue(models.Model):
    ActivityDefinition = models.ForeignKey(FHIR_ActivityDefinition, related_name='ActivityDefinition_dynamicValue', null=False, on_delete=models.CASCADE)
    path = FHIR_primitive_StringField(null=True, blank=True, )
