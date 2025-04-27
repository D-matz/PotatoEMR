#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_TestReport(models.Model):
    identifier = models.OneToOneField("FHIR_GP_Identifier", related_name='TestReport_identifier', null=True, blank=True, on_delete=models.SET_NULL)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    class StatusChoices(models.TextChoices): COMPLETED = 'completed', 'Completed'; IN_PROGRESS = 'in-progress', 'In-progress'; WAITING = 'waiting', 'Waiting'; STOPPED = 'stopped', 'Stopped'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    testScript = FHIR_primitive_CanonicalField(null=True, blank=True, )
    class ResultChoices(models.TextChoices): PASS = 'pass', 'Pass'; FAIL = 'fail', 'Fail'; PENDING = 'pending', 'Pending'; 
    result = FHIR_primitive_CodeField(choices=ResultChoices.choices, null=True, blank=True, )
    score = FHIR_primitive_DecimalField(null=True, blank=True, )
    tester = FHIR_primitive_StringField(null=True, blank=True, )
    issued = FHIR_primitive_DateTimeField(null=True, blank=True, )
    presentedForm = models.OneToOneField("FHIR_GP_Attachment", related_name='TestReport_presentedForm', null=True, blank=True, on_delete=models.SET_NULL)
    log = models.OneToOneField("FHIR_GP_Attachment", related_name='TestReport_log', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_TestReport_participant(models.Model):
    TestReport = models.ForeignKey(FHIR_TestReport, related_name='TestReport_participant', null=False, on_delete=models.CASCADE)
    class TypeChoices(models.TextChoices): TEST_ENGINE = 'test-engine', 'Test-engine'; CLIENT = 'client', 'Client'; SERVER = 'server', 'Server'; 
    type = FHIR_primitive_CodeField(choices=TypeChoices.choices, null=True, blank=True, )
    uri = FHIR_primitive_URIField(null=True, blank=True, )
    version = FHIR_primitive_URIField(null=True, blank=True, )
    display = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_TestReport_parameter(models.Model):
    TestReport = models.ForeignKey(FHIR_TestReport, related_name='TestReport_parameter', null=False, on_delete=models.CASCADE)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    documentation = FHIR_primitive_MarkdownField(null=True, blank=True, )

class FHIR_TestReport_setup(models.Model):
    TestReport = models.ForeignKey(FHIR_TestReport, related_name='TestReport_setup', null=False, on_delete=models.CASCADE)

class FHIR_TestReport_setup_action(models.Model):
    TestReport_setup = models.ForeignKey(FHIR_TestReport_setup, related_name='TestReport_setup_action', null=False, on_delete=models.CASCADE)

class FHIR_TestReport_setup_action_operation(models.Model):
    TestReport_setup_action = models.ForeignKey(FHIR_TestReport_setup_action, related_name='TestReport_setup_action_operation', null=False, on_delete=models.CASCADE)
    class ResultChoices(models.TextChoices): PASS = 'pass', 'Pass'; SKIP = 'skip', 'Skip'; FAIL = 'fail', 'Fail'; WARNING = 'warning', 'Warning'; ERROR = 'error', 'Error'; 
    result = FHIR_primitive_CodeField(choices=ResultChoices.choices, null=True, blank=True, )
    message = FHIR_primitive_MarkdownField(null=True, blank=True, )
    detail = FHIR_primitive_URIField(null=True, blank=True, )

class FHIR_TestReport_setup_action_assert(models.Model):
    TestReport_setup_action = models.ForeignKey(FHIR_TestReport_setup_action, related_name='TestReport_setup_action_assert', null=False, on_delete=models.CASCADE)
    class ResultChoices(models.TextChoices): PASS = 'pass', 'Pass'; SKIP = 'skip', 'Skip'; FAIL = 'fail', 'Fail'; WARNING = 'warning', 'Warning'; ERROR = 'error', 'Error'; 
    result = FHIR_primitive_CodeField(choices=ResultChoices.choices, null=True, blank=True, )
    message = FHIR_primitive_MarkdownField(null=True, blank=True, )
    detail = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_TestReport_setup_action_assert_requirement(models.Model):
    TestReport_setup_action_assert = models.ForeignKey(FHIR_TestReport_setup_action_assert, related_name='TestReport_setup_action_assert_requirement', null=False, on_delete=models.CASCADE)
    link_uri = FHIR_primitive_URIField(null=True, blank=True, )
    link_canonical = FHIR_primitive_CanonicalField(null=True, blank=True, )

class FHIR_TestReport_test(models.Model):
    TestReport = models.ForeignKey(FHIR_TestReport, related_name='TestReport_test', null=False, on_delete=models.CASCADE)
    name = FHIR_primitive_StringField(null=True, blank=True, )
    description = FHIR_primitive_StringField(null=True, blank=True, )
    class ResultChoices(models.TextChoices): PASS = 'pass', 'Pass'; SKIP = 'skip', 'Skip'; FAIL = 'fail', 'Fail'; WARNING = 'warning', 'Warning'; ERROR = 'error', 'Error'; 
    result = FHIR_primitive_CodeField(choices=ResultChoices.choices, null=True, blank=True, )
    period = models.OneToOneField("FHIR_GP_Period", related_name='TestReport_test_period', null=True, blank=True, on_delete=models.SET_NULL)
    log = models.OneToOneField("FHIR_GP_Attachment", related_name='TestReport_test_log', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_TestReport_test_action(models.Model):
    TestReport_test = models.ForeignKey(FHIR_TestReport_test, related_name='TestReport_test_action', null=False, on_delete=models.CASCADE)

class FHIR_TestReport_teardown(models.Model):
    TestReport = models.ForeignKey(FHIR_TestReport, related_name='TestReport_teardown', null=False, on_delete=models.CASCADE)

class FHIR_TestReport_teardown_action(models.Model):
    TestReport_teardown = models.ForeignKey(FHIR_TestReport_teardown, related_name='TestReport_teardown_action', null=False, on_delete=models.CASCADE)
