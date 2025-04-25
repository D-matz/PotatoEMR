
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_QuestionnaireResponse(models.Model):
    basedOn_CarePlan = models.ManyToManyField("FHIR_CarePlan", related_name="QuestionnaireResponse_basedOn", blank=True)
    basedOn_ServiceRequest = models.ManyToManyField("FHIR_ServiceRequest", related_name="QuestionnaireResponse_basedOn", blank=True)
    partOf_Observation = models.ManyToManyField("FHIR_Observation", related_name="QuestionnaireResponse_partOf", blank=True)
    partOf_Procedure = models.ManyToManyField("FHIR_Procedure", related_name="QuestionnaireResponse_partOf", blank=True)
    questionnaire = FHIR_primitive_CanonicalField(null=True, blank=True, )
    class StatusChoices(models.TextChoices): IN_PROGRESS = 'in-progress', 'In-progress'; COMPLETED = 'completed', 'Completed'; AMENDED = 'amended', 'Amended'; ENTERED_IN_ERROR = 'entered-in-error', 'Entered-in-error'; STOPPED = 'stopped', 'Stopped'; 
    status = FHIR_primitive_CodeField(choices=StatusChoices.choices, null=True, blank=True, )
    encounter = models.ForeignKey("FHIR_Encounter", related_name="QuestionnaireResponse_encounter", null=True, blank=True, on_delete=models.SET_NULL)
    authored = FHIR_primitive_DateTimeField(null=True, blank=True, )
    author_Device = models.ForeignKey("FHIR_Device", related_name="QuestionnaireResponse_author", null=True, blank=True, on_delete=models.SET_NULL)
    author_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="QuestionnaireResponse_author", null=True, blank=True, on_delete=models.SET_NULL)
    author_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="QuestionnaireResponse_author", null=True, blank=True, on_delete=models.SET_NULL)
    author_Patient = models.ForeignKey("FHIR_Patient", related_name="QuestionnaireResponse_author", null=True, blank=True, on_delete=models.SET_NULL)
    author_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="QuestionnaireResponse_author", null=True, blank=True, on_delete=models.SET_NULL)
    author_Organization = models.ForeignKey("FHIR_Organization", related_name="QuestionnaireResponse_author", null=True, blank=True, on_delete=models.SET_NULL)
    author_Group = models.ForeignKey("FHIR_Group", related_name="QuestionnaireResponse_author", null=True, blank=True, on_delete=models.SET_NULL)
    source_Device = models.ForeignKey("FHIR_Device", related_name="QuestionnaireResponse_source", null=True, blank=True, on_delete=models.SET_NULL)
    source_Organization = models.ForeignKey("FHIR_Organization", related_name="QuestionnaireResponse_source", null=True, blank=True, on_delete=models.SET_NULL)
    source_Patient = models.ForeignKey("FHIR_Patient", related_name="QuestionnaireResponse_source", null=True, blank=True, on_delete=models.SET_NULL)
    source_Practitioner = models.ForeignKey("FHIR_Practitioner", related_name="QuestionnaireResponse_source", null=True, blank=True, on_delete=models.SET_NULL)
    source_PractitionerRole = models.ForeignKey("FHIR_PractitionerRole", related_name="QuestionnaireResponse_source", null=True, blank=True, on_delete=models.SET_NULL)
    source_RelatedPerson = models.ForeignKey("FHIR_RelatedPerson", related_name="QuestionnaireResponse_source", null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_QuestionnaireResponse_identifier(FHIR_GP_Identifier):
    QuestionnaireResponse = models.ForeignKey(FHIR_QuestionnaireResponse, related_name='QuestionnaireResponse_identifier', null=False, on_delete=models.CASCADE)

class FHIR_QuestionnaireResponse_item(models.Model):
    QuestionnaireResponse = models.ForeignKey(FHIR_QuestionnaireResponse, related_name='QuestionnaireResponse_item', null=False, on_delete=models.CASCADE)
    linkId = FHIR_primitive_StringField(null=True, blank=True, )
    text = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_QuestionnaireResponse_item_definition(models.Model):
    QuestionnaireResponse_item = models.ForeignKey(FHIR_QuestionnaireResponse_item, related_name='QuestionnaireResponse_item_definition', null=False, on_delete=models.CASCADE)
    
    definition = FHIR_primitive_URIField(null=True, blank=True, )
    
class FHIR_QuestionnaireResponse_item_answer(models.Model):
    QuestionnaireResponse_item = models.ForeignKey(FHIR_QuestionnaireResponse_item, related_name='QuestionnaireResponse_item_answer', null=False, on_delete=models.CASCADE)
    value = FHIR_primitive_BooleanField(null=True, blank=True, )
    value = FHIR_primitive_DecimalField(null=True, blank=True, )
    value = FHIR_primitive_DateField(null=True, blank=True, )
    value = FHIR_primitive_DateTimeField(null=True, blank=True, )
    value = FHIR_primitive_TimeField(null=True, blank=True, )
    value = FHIR_primitive_StringField(null=True, blank=True, )
    value = FHIR_primitive_URIField(null=True, blank=True, )
    value = models.OneToOneField("FHIR_GP_Attachment", related_name='QuestionnaireResponse_item_answer_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_Coding", related_name='QuestionnaireResponse_item_answer_value', null=True, blank=True, on_delete=models.SET_NULL)
    value = models.OneToOneField("FHIR_GP_Quantity", related_name='QuestionnaireResponse_item_answer_value', null=True, blank=True, on_delete=models.SET_NULL)
