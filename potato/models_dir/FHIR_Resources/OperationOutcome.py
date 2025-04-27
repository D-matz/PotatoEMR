#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_OperationOutcome(models.Model):pass

class FHIR_OperationOutcome_issue(models.Model):
    OperationOutcome = models.ForeignKey(FHIR_OperationOutcome, related_name='OperationOutcome_issue', null=False, on_delete=models.CASCADE)
    class SeverityChoices(models.TextChoices): FATAL = 'fatal', 'Fatal'; ERROR = 'error', 'Error'; WARNING = 'warning', 'Warning'; INFORMATION = 'information', 'Information'; SUCCESS = 'success', 'Success'; 
    severity = FHIR_primitive_CodeField(choices=SeverityChoices.choices, null=True, blank=True, )
    class CodeChoices(models.TextChoices): TODO = 'TODO', 'Todo'; 
    code = FHIR_primitive_CodeField(choices=CodeChoices.choices, null=True, blank=True, )
    BINDING_details = 'TODO'
    details_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_details}, related_name='OperationOutcome_issue_details', blank=True)
    details_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    diagnostics = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_OperationOutcome_issue_location(models.Model):
    OperationOutcome_issue = models.ForeignKey(FHIR_OperationOutcome_issue, related_name='OperationOutcome_issue_location', null=False, on_delete=models.CASCADE)
    
    location = FHIR_primitive_StringField(null=True, blank=True, )
    
class FHIR_OperationOutcome_issue_expression(models.Model):
    OperationOutcome_issue = models.ForeignKey(FHIR_OperationOutcome_issue, related_name='OperationOutcome_issue_expression', null=False, on_delete=models.CASCADE)
    
    expression = FHIR_primitive_StringField(null=True, blank=True, )
    