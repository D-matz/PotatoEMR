
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_Bundle(models.Model):
    identifier = models.OneToOneField("FHIR_GP_Identifier", related_name='Bundle_identifier', null=True, blank=True, on_delete=models.SET_NULL)
    class TypeChoices(models.TextChoices): DOCUMENT = 'document', 'Document'; MESSAGE = 'message', 'Message'; TRANSACTION = 'transaction', 'Transaction'; TRANSACTION_RESPONSE = 'transaction-response', 'Transaction-response'; BATCH = 'batch', 'Batch'; BATCH_RESPONSE = 'batch-response', 'Batch-response'; HISTORY = 'history', 'History'; SEARCHSET = 'searchset', 'Searchset'; COLLECTION = 'collection', 'Collection'; SUBSCRIPTION_NOTIFICATION = 'subscription-notification', 'Subscription-notification'; 
    type = FHIR_primitive_CodeField(choices=TypeChoices.choices, null=True, blank=True, )
    timestamp = FHIR_primitive_InstantField(null=True, blank=True, )
    total = FHIR_primitive_UnsignedIntField(null=True, blank=True, )
    signature = models.OneToOneField("FHIR_GP_Signature", related_name='Bundle_signature', null=True, blank=True, on_delete=models.SET_NULL)

class FHIR_Bundle_link(models.Model):
    Bundle = models.ForeignKey(FHIR_Bundle, related_name='Bundle_link', null=False, on_delete=models.CASCADE)
    class RelationChoices(models.TextChoices): SEE_HTTP://WWW.IANA.ORG/ASSIGNMENTS/LINK_RELATIONS/LINK_RELATIONS.XHTML#LINK_RELATIONS_1 = 'See http://www.iana.org/assignments/link-relations/link-relations.xhtml#link-relations-1', 'See http://www.iana.org/assignments/link-relations/link-relations.xhtml#link-relations-1'; 
    relation = FHIR_primitive_CodeField(choices=RelationChoices.choices, null=True, blank=True, )
    url = FHIR_primitive_URIField(null=True, blank=True, )

class FHIR_Bundle_entry(models.Model):
    Bundle = models.ForeignKey(FHIR_Bundle, related_name='Bundle_entry', null=False, on_delete=models.CASCADE)
    fullUrl = FHIR_primitive_URIField(null=True, blank=True, )

class FHIR_Bundle_entry_search(models.Model):
    Bundle_entry = models.ForeignKey(FHIR_Bundle_entry, related_name='Bundle_entry_search', null=False, on_delete=models.CASCADE)
    class ModeChoices(models.TextChoices): MATCH = 'match', 'Match'; INCLUDE___WHY_THIS_IS_IN_THE_RESULT_SET = 'include - why this is in the result set', 'Include - why this is in the result set'; 
    mode = FHIR_primitive_CodeField(choices=ModeChoices.choices, null=True, blank=True, )
    score = FHIR_primitive_DecimalField(null=True, blank=True, )

class FHIR_Bundle_entry_request(models.Model):
    Bundle_entry = models.ForeignKey(FHIR_Bundle_entry, related_name='Bundle_entry_request', null=False, on_delete=models.CASCADE)
    class MethodChoices(models.TextChoices): GET = 'GET', 'Get'; HEAD = 'HEAD', 'Head'; POST = 'POST', 'Post'; PUT = 'PUT', 'Put'; DELETE = 'DELETE', 'Delete'; PATCH = 'PATCH', 'Patch'; 
    method = FHIR_primitive_CodeField(choices=MethodChoices.choices, null=True, blank=True, )
    url = FHIR_primitive_URIField(null=True, blank=True, )
    ifNoneMatch = FHIR_primitive_StringField(null=True, blank=True, )
    ifModifiedSince = FHIR_primitive_InstantField(null=True, blank=True, )
    ifMatch = FHIR_primitive_StringField(null=True, blank=True, )
    ifNoneExist = FHIR_primitive_StringField(null=True, blank=True, )

class FHIR_Bundle_entry_response(models.Model):
    Bundle_entry = models.ForeignKey(FHIR_Bundle_entry, related_name='Bundle_entry_response', null=False, on_delete=models.CASCADE)
    status = FHIR_primitive_StringField(null=True, blank=True, )
    location = FHIR_primitive_URIField(null=True, blank=True, )
    etag = FHIR_primitive_StringField(null=True, blank=True, )
    lastModified = FHIR_primitive_InstantField(null=True, blank=True, )
