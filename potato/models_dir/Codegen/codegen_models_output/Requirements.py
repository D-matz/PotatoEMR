#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Requirements(models.Model):
    url = FHIR_primitive_URIField(null=True, blank=True, )
    version = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = FHIR_primitive_StringField(null=True, blank=True, )
    versionAlgorithm = models.OneToOneField("FHIR_GP_Coding", related_name='Requirements_versionAlgorithm', null=True, blank=True, on_delete=models.SET_NULL)
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

class FHIR_Requirements_identifier(FHIR_GP_Identifier):
    Requirements = models.ForeignKey(FHIR_Requirements, related_name='Requirements_identifier', null=False, on_delete=models.CASCADE)

class FHIR_Requirements_jurisdiction(models.Model):
    Requirements = models.ForeignKey(FHIR_Requirements, related_name='Requirements_jurisdiction', null=False, on_delete=models.CASCADE)
    BINDING_jurisdiction = "TODO"
    jurisdiction_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_jurisdiction}, related_name='Requirements_jurisdiction', blank=True)
    jurisdiction_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)
    
class FHIR_Requirements_derivedFrom(models.Model):
    Requirements = models.ForeignKey(FHIR_Requirements, related_name='Requirements_derivedFrom', null=False, on_delete=models.CASCADE)
    
    derivedFrom = FHIR_primitive_CanonicalField(null=True, blank=True, )
    
class FHIR_Requirements_imports(models.Model):
    Requirements = models.ForeignKey(FHIR_Requirements, related_name='Requirements_imports', null=False, on_delete=models.CASCADE)
    reference = FHIR_primitive_CanonicalField(null=True, blank=True, )

class FHIR_Requirements_imports_key(models.Model):
    Requirements_imports = models.ForeignKey(FHIR_Requirements_imports, related_name='Requirements_imports_key', null=False, on_delete=models.CASCADE)
    
    key = FHIR_primitive_IdField(null=True, blank=True, )
    
class FHIR_Requirements_reference(models.Model):
    Requirements = models.ForeignKey(FHIR_Requirements, related_name='Requirements_reference', null=False, on_delete=models.CASCADE)
    
    reference = FHIR_primitive_URLField(null=True, blank=True, )
    
class FHIR_Requirements_actor(models.Model):
    Requirements = models.ForeignKey(FHIR_Requirements, related_name='Requirements_actor', null=False, on_delete=models.CASCADE)
    reference = FHIR_primitive_CanonicalField(null=True, blank=True, )
    key = FHIR_primitive_IdField(null=True, blank=True, )

class FHIR_Requirements_statement(models.Model):
    Requirements = models.ForeignKey(FHIR_Requirements, related_name='Requirements_statement', null=False, on_delete=models.CASCADE)
    key = FHIR_primitive_IdField(null=True, blank=True, )
    label = FHIR_primitive_StringField(null=True, blank=True, )
    conditionality = FHIR_primitive_BooleanField(null=True, blank=True, )
    requirement = FHIR_primitive_MarkdownField(null=True, blank=True, )
    source_CareTeam = models.ManyToManyField("FHIR_CareTeam", related_name="Requirements_statement_source", blank=True)
    source_Device = models.ManyToManyField("FHIR_Device", related_name="Requirements_statement_source", blank=True)
    source_Group = models.ManyToManyField("FHIR_Group", related_name="Requirements_statement_source", blank=True)
    source_HealthcareService = models.ManyToManyField("FHIR_HealthcareService", related_name="Requirements_statement_source", blank=True)
    source_Organization = models.ManyToManyField("FHIR_Organization", related_name="Requirements_statement_source", blank=True)
    source_Patient = models.ManyToManyField("FHIR_Patient", related_name="Requirements_statement_source", blank=True)
    source_Practitioner = models.ManyToManyField("FHIR_Practitioner", related_name="Requirements_statement_source", blank=True)
    source_PractitionerRole = models.ManyToManyField("FHIR_PractitionerRole", related_name="Requirements_statement_source", blank=True)
    source_RelatedPerson = models.ManyToManyField("FHIR_RelatedPerson", related_name="Requirements_statement_source", blank=True)

class FHIR_Requirements_statement_conformance(models.Model):
    Requirements_statement = models.ForeignKey(FHIR_Requirements_statement, related_name='Requirements_statement_conformance', null=False, on_delete=models.CASCADE)
    
    class ConformanceChoices(models.TextChoices): SHALL = 'SHALL', 'Shall'; SHOULD = 'SHOULD', 'Should'; MAY = 'MAY', 'May'; SHOULD_NOT = 'SHOULD-NOT', 'Should-not'; SHALL_NOT = 'SHALL-NOT', 'Shall-not'; 
    conformance = FHIR_primitive_CodeField(choices=ConformanceChoices.choices, null=True, blank=True, )
    
class FHIR_Requirements_statement_derivedFrom(models.Model):
    Requirements_statement = models.ForeignKey(FHIR_Requirements_statement, related_name='Requirements_statement_derivedFrom', null=False, on_delete=models.CASCADE)
    reference = FHIR_primitive_CanonicalField(null=True, blank=True, )
    key = FHIR_primitive_IdField(null=True, blank=True, )

class FHIR_Requirements_statement_partOf(models.Model):
    Requirements_statement = models.ForeignKey(FHIR_Requirements_statement, related_name='Requirements_statement_partOf', null=False, on_delete=models.CASCADE)
    reference = FHIR_primitive_CanonicalField(null=True, blank=True, )
    key = FHIR_primitive_IdField(null=True, blank=True, )

class FHIR_Requirements_statement_satisfiedBy(models.Model):
    Requirements_statement = models.ForeignKey(FHIR_Requirements_statement, related_name='Requirements_statement_satisfiedBy', null=False, on_delete=models.CASCADE)
    
    satisfiedBy = FHIR_primitive_URLField(null=True, blank=True, )
    
class FHIR_Requirements_statement_reference(models.Model):
    Requirements_statement = models.ForeignKey(FHIR_Requirements_statement, related_name='Requirements_statement_reference', null=False, on_delete=models.CASCADE)
    
    reference = FHIR_primitive_URLField(null=True, blank=True, )
    
class FHIR_Requirements_statement_actor(models.Model):
    Requirements_statement = models.ForeignKey(FHIR_Requirements_statement, related_name='Requirements_statement_actor', null=False, on_delete=models.CASCADE)
    
    actor = FHIR_primitive_IdField(null=True, blank=True, )
    