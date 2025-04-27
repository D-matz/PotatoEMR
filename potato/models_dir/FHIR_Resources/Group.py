#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Group(models.Model):
    url = FHIR_primitive_URIField(null=True, blank=True, )
    version = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = models.OneToOneField("FHIR_GP_Coding", related_name='Group_versionAlgorithm', null=True, blank=True, on_delete=models.SET_NULL)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    title = FHIR_primitive_StringField(null=True, blank=True, )
    class StatusChoices(models.TextChoices): DRAFT = 'draft', 'Draft'; ACTIVE = 'active', 'Active'; RETIRED = 'retired', 'Retired'; UNKNOWN = 'unknown', 'Unknown'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    experimental = FHIR_primitive_BooleanField(null=True, blank=True, )
    date = FHIR_primitive_DateTimeField(null=True, blank=True, )
    publisher = FHIR_primitive_StringField(null=True, blank=True, )
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    purpose = FHIR_primitive_MarkdownField(null=True, blank=True, )
    copyright = FHIR_primitive_MarkdownField(null=True, blank=True, )
    copyrightLabel = FHIR_primitive_StringField(null=True, blank=True, )
    class TypeChoices(models.TextChoices): PERSON = 'person', 'Person'; ANIMAL = 'animal', 'Animal'; PRACTITIONER = 'practitioner', 'Practitioner'; DEVICE = 'device', 'Device'; CARETEAM = 'careteam', 'Careteam'; HEALTHCARESERVICE = 'healthcareservice', 'Healthcareservice'; LOCATION = 'location', 'Location'; ORGANIZATION = 'organization', 'Organization'; RELATEDPERSON = 'relatedperson', 'Relatedperson'; SPECIMEN = 'specimen', 'Specimen'; MEDICATION = 'medication', 'Medication'; SUBSTANCE = 'substance', 'Substance'; BIOLOGICALLYDERIVEDPRODUCT = 'biologicallyDerivedProduct', 'Biologicallyderivedproduct'; NUTRITIONPRODUCT = 'nutritionProduct', 'Nutritionproduct'; 
    type = FHIR_primitive_CodeField(choices=TypeChoices.choices, null=True, blank=True, )
    class MembershipChoices(models.TextChoices): DEFINITIONAL = 'definitional', 'Definitional'; CONCEPTUAL = 'conceptual', 'Conceptual'; ENUMERATED = 'enumerated', 'Enumerated'; 
    membership = FHIR_primitive_CodeField(choices=MembershipChoices.choices, null=True, blank=True, )
    BINDING_code = 'TODO'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='Group_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    quantity = FHIR_primitive_UnsignedIntField(null=True, blank=True, )
    managingEntity_Organization = models.ForeignKey("FHIR_Organization", related_name="Group_managingEntity", null=True, blank=True, on_delete=models.SET_NULL)
    managingEntity_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="Group_managingEntity", null=True, blank=True, on_delete=models.SET_NULL)
    managingEntity_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="Group_managingEntity", null=True, blank=True, on_delete=models.SET_NULL)
    managingEntity_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="Group_managingEntity", null=True, blank=True, on_delete=models.SET_NULL)
    class CombinationmethodChoices(models.TextChoices): ALL_OF = 'all-of', 'All-of'; ANY_OF = 'any-of', 'Any-of'; AT_LEAST = 'at-least', 'At-least'; AT_MOST = 'at-most', 'At-most'; EXCEPT_SUBSET = 'except-subset', 'Except-subset'; 
    combinationMethod = FHIR_primitive_CodeField(choices=CombinationmethodChoices.choices, null=True, blank=True, )
    combinationThreshold = FHIR_primitive_PositiveIntField(null=True, blank=True, )

class FHIR_Group_identifier(FHIR_GP_Identifier):
    Group = models.ForeignKey(FHIR_Group, related_name='Group_identifier', null=False, on_delete=models.CASCADE)

class FHIR_Group_characteristic(models.Model):
    Group = models.ForeignKey(FHIR_Group, related_name='Group_characteristic', null=False, on_delete=models.CASCADE)
    BINDING_code = 'TODO'
    code_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_code}, related_name='Group_characteristic_code', blank=True)
    code_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    BINDING_value = 'TODO'
    value_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_value}, related_name='Group_characteristic_value', blank=True)
    value_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    value = FHIR_primitive_BooleanField(null=True, blank=True, )
    value = models.OneToOneField("FHIR_GP_Quantity", related_name='Group_characteristic_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_Range", related_name='Group_characteristic_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = FHIR_primitive_URIField(null=True, blank=True, )
    exclude = FHIR_primitive_BooleanField(null=True, blank=True, )
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    determinedBy_Device = models.ForeignKey("FHIR_Device", related_name="Group_characteristic_determinedBy", null=True, blank=True, on_delete=models.SET_NULL)
    determinedBy_DeviceDefinition = models.ForeignKey("FHIR_DeviceDefinition", related_name="Group_characteristic_determinedBy", null=True, blank=True, on_delete=models.SET_NULL)
    determinedBy_DeviceMetric = models.ForeignKey("FHIR_DeviceMetric", related_name="Group_characteristic_determinedBy", null=True, blank=True, on_delete=models.SET_NULL)
    BINDING_offset = 'TODO'
    offset_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_offset}, related_name='Group_characteristic_offset', blank=True)
    offset_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    instances = FHIR_primitive_UnsignedIntField(null=True, blank=True, )
    instances = models.OneToOneField("FHIR_GP_Range", related_name='Group_characteristic_instances', null=True, blank=True, on_delete=models.SET_NULL)
    duration = models.OneToOneField("FHIR_GP_Quantity_Duration", related_name='Group_characteristic_duration', null=True, blank=True, on_delete=models.SET_NULL)
    duration = models.OneToOneField("FHIR_GP_Range", related_name='Group_characteristic_duration', null=True, blank=True, on_delete=models.SET_NULL)
    period = models.OneToOneField("FHIR_GP_Period", related_name='Group_characteristic_period', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Group_characteristic_method(models.Model):
    Group_characteristic = models.ForeignKey(FHIR_Group_characteristic, related_name='Group_characteristic_method', null=False, on_delete=models.CASCADE)
    BINDING_method = 'TODO'
    method_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_method}, related_name='Group_characteristic_method', blank=True)
    method_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Group_member(models.Model):
    Group = models.ForeignKey(FHIR_Group, related_name='Group_member', null=False, on_delete=models.CASCADE)
    entity_CareTeam = models.ForeignKey("FHIR_CareTeam", related_name="Group_member_entity", null=True, blank=True, on_delete=models.SET_NULL)
    entity_Device = models.ForeignKey("FHIR_Device", related_name="Group_member_entity", null=True, blank=True, on_delete=models.SET_NULL)
    entity_Group = models.ForeignKey("FHIR_Group", related_name="Group_member_entity", null=True, blank=True, on_delete=models.SET_NULL)
    entity_HealthcareService = models.ForeignKey("FHIR_HealthcareService", related_name="Group_member_entity", null=True, blank=True, on_delete=models.SET_NULL)
    entity_Location = models.ForeignKey("FHIR_Location", related_name="Group_member_entity", null=True, blank=True, on_delete=models.SET_NULL)
    entity_Organization = models.ForeignKey("FHIR_Organization", related_name="Group_member_entity", null=True, blank=True, on_delete=models.SET_NULL)
    entity_Patient = models.ForeignKey("FHIR_Patient", related_name="Group_member_entity", null=True, blank=True, on_delete=models.SET_NULL)
    entity_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="Group_member_entity", null=True, blank=True, on_delete=models.SET_NULL)
    entity_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="Group_member_entity", null=True, blank=True, on_delete=models.SET_NULL)
    entity_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="Group_member_entity", null=True, blank=True, on_delete=models.SET_NULL)
    entity_Specimen = models.ForeignKey("FHIR_Specimen", related_name="Group_member_entity", null=True, blank=True, on_delete=models.SET_NULL)
    entity_Medication = models.ForeignKey("FHIR_Medication", related_name="Group_member_entity", null=True, blank=True, on_delete=models.SET_NULL)
    entity_Substance = models.ForeignKey("FHIR_Substance", related_name="Group_member_entity", null=True, blank=True, on_delete=models.SET_NULL)
    entity_BiologicallyDerivedProduct = models.ForeignKey("FHIR_BiologicallyDerivedProduct", related_name="Group_member_entity", null=True, blank=True, on_delete=models.SET_NULL)
    entity_NutritionProduct = models.ForeignKey("FHIR_NutritionProduct", related_name="Group_member_entity", null=True, blank=True, on_delete=models.SET_NULL)
    period = models.OneToOneField("FHIR_GP_Period", related_name='Group_member_period', null=True, blank=True, on_delete=models.SET_NULL)
    inactive = FHIR_primitive_BooleanField(null=True, blank=True, )

class FHIR_Group_member_involvement(models.Model):
    Group_member = models.ForeignKey(FHIR_Group_member, related_name='Group_member_involvement', null=False, on_delete=models.CASCADE)
    BINDING_involvement = 'TODO'
    involvement_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_involvement}, related_name='Group_member_involvement', blank=True)
    involvement_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    