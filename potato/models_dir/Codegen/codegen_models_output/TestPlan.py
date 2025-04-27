#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_TestPlan(models.Model):
    url = FHIR_primitive_URIField(null=True, blank=True, )
    version = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = models.OneToOneField("FHIR_GP_Coding", related_name='TestPlan_versionAlgorithm', null=True, blank=True, on_delete=models.SET_NULL)
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
    testTools = FHIR_primitive_MarkdownField(null=True, blank=True, )
    exitCriteria = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_TestPlan_identifier(FHIR_GP_Identifier):
    TestPlan = models.ForeignKey(FHIR_TestPlan, related_name='TestPlan_identifier', null=False, on_delete=models.CASCADE)

class FHIR_TestPlan_jurisdiction(models.Model):
    TestPlan = models.ForeignKey(FHIR_TestPlan, related_name='TestPlan_jurisdiction', null=False, on_delete=models.CASCADE)
    BINDING_jurisdiction = "TODO"
    jurisdiction_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_jurisdiction}, related_name='TestPlan_jurisdiction', blank=True)
    jurisdiction_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_TestPlan_category(models.Model):
    TestPlan = models.ForeignKey(FHIR_TestPlan, related_name='TestPlan_category', null=False, on_delete=models.CASCADE)
    BINDING_category = "TODO"
    category_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_category}, related_name='TestPlan_category', blank=True)
    category_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_TestPlan_scope(models.Model):
    TestPlan = models.ForeignKey(FHIR_TestPlan, related_name='TestPlan_scope', null=False, on_delete=models.CASCADE)
    artifact = FHIR_primitive_CanonicalField(null=True, blank=True, )
    artifact = FHIR_primitive_MarkdownField(null=True, blank=True, )
    artifact = FHIR_primitive_URIField(null=True, blank=True, )

class FHIR_TestPlan_dependency(models.Model):
    TestPlan = models.ForeignKey(FHIR_TestPlan, related_name='TestPlan_dependency', null=False, on_delete=models.CASCADE)
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    predecessor = models.ForeignKey("FHIR_TestPlan", related_name="TestPlan_dependency_predecessor", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_TestPlan_testCase(models.Model):
    TestPlan = models.ForeignKey(FHIR_TestPlan, related_name='TestPlan_testCase', null=False, on_delete=models.CASCADE)
    key = FHIR_primitive_IdField(null=True, blank=True, )
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_TestPlan_testCase_scope(models.Model):
    TestPlan_testCase = models.ForeignKey(FHIR_TestPlan_testCase, related_name='TestPlan_testCase_scope', null=False, on_delete=models.CASCADE)
    artifact = FHIR_primitive_CanonicalField(null=True, blank=True, )
    artifact = FHIR_primitive_MarkdownField(null=True, blank=True, )
    artifact = FHIR_primitive_URIField(null=True, blank=True, )

class FHIR_TestPlan_testCase_requirement(models.Model):
    TestPlan_testCase = models.ForeignKey(FHIR_TestPlan_testCase, related_name='TestPlan_testCase_requirement', null=False, on_delete=models.CASCADE)
    reference = FHIR_primitive_CanonicalField(null=True, blank=True, )
    key = FHIR_primitive_IdField(null=True, blank=True, )

class FHIR_TestPlan_testCase_dependency(models.Model):
    TestPlan_testCase = models.ForeignKey(FHIR_TestPlan_testCase, related_name='TestPlan_testCase_dependency', null=False, on_delete=models.CASCADE)
    description = FHIR_primitive_MarkdownField(null=True, blank=True, )
    reference = FHIR_primitive_CanonicalField(null=True, blank=True, )
    key = FHIR_primitive_IdField(null=True, blank=True, )

class FHIR_TestPlan_testCase_testRun(models.Model):
    TestPlan_testCase = models.ForeignKey(FHIR_TestPlan_testCase, related_name='TestPlan_testCase_testRun', null=False, on_delete=models.CASCADE)
    narrative = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_TestPlan_testCase_testRun_script(models.Model):
    TestPlan_testCase_testRun = models.ForeignKey(FHIR_TestPlan_testCase_testRun, related_name='TestPlan_testCase_testRun_script', null=False, on_delete=models.CASCADE)
    BINDING_language = "TODO"
    language_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_language}, related_name='TestPlan_testCase_testRun_script_language', blank=True)
    language_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    source = FHIR_primitive_StringField(null=True, blank=True, )
    source = models.OneToOneField("FHIR_GP_Attachment", related_name='TestPlan_testCase_testRun_script_source', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_TestPlan_testCase_testData(models.Model):
    TestPlan_testCase = models.ForeignKey(FHIR_TestPlan_testCase, related_name='TestPlan_testCase_testData', null=False, on_delete=models.CASCADE)
    type = models.OneToOneField("FHIR_GP_Coding", related_name='TestPlan_testCase_testData_type', null=True, blank=True, on_delete=models.SET_NULL)
    source = FHIR_primitive_StringField(null=True, blank=True, )
    source = FHIR_primitive_URIField(null=True, blank=True, )

class FHIR_TestPlan_testCase_assertion(models.Model):
    TestPlan_testCase = models.ForeignKey(FHIR_TestPlan_testCase, related_name='TestPlan_testCase_assertion', null=False, on_delete=models.CASCADE)

class FHIR_TestPlan_testCase_assertion_type(models.Model):
    TestPlan_testCase_assertion = models.ForeignKey(FHIR_TestPlan_testCase_assertion, related_name='TestPlan_testCase_assertion_type', null=False, on_delete=models.CASCADE)
    BINDING_type = "TODO"
    type_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_type}, related_name='TestPlan_testCase_assertion_type', blank=True)
    type_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_TestPlan_testCase_assertion_object(models.Model):
    TestPlan_testCase_assertion = models.ForeignKey(FHIR_TestPlan_testCase_assertion, related_name='TestPlan_testCase_assertion_object', null=False, on_delete=models.CASCADE)
    BINDING_object = "TODO"
    object_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_object}, related_name='TestPlan_testCase_assertion_object', blank=True)
    object_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_TestPlan_testCase_assertion_result(models.Model):
    TestPlan_testCase_assertion = models.ForeignKey(FHIR_TestPlan_testCase_assertion, related_name='TestPlan_testCase_assertion_result', null=False, on_delete=models.CASCADE)
    BINDING_result = "TODO"
    result_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_result}, related_name='TestPlan_testCase_assertion_result', blank=True)
    result_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
