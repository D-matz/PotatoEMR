#https://www.hl7.org/fhir/datatypes.html#primitive
#used in other FHIR data types, see FHIR_generalpurpose.py

import re
from django.core.exceptions import ValidationError
from django.db import models
from decimal import Decimal, ROUND_HALF_UP




def apply_regex(value, regex, error_msg):
    if value and not re.match(regex, value):
        raise ValidationError(error_msg)
    return value

BASE64_REGEX = r'^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$'
BASE64_ERROR = "Invalid base64Binary content."
class FHIR_primitive_Base64BinaryField(models.TextField):
    def clean(self, value, model_instance):
        value = ''.join(value.split())
        return apply_regex(value, BASE64_REGEX, BASE64_ERROR)

class FHIR_primitive_BooleanField(models.BooleanField):
    pass


CANONICAL_REGEX = r'^\S*(\|[^\s]*)?(#[^\s]*)?$'
CANONICAL_ERROR = "Invalid canonical URI format."
class FHIR_primitive_CanonicalField(models.CharField):
    def clean(self, value, model_instance): return apply_regex(value, CANONICAL_REGEX, CANONICAL_ERROR)

CODE_REGEX = r'^[^\s]+( [^\s]+)*$'
CODE_ERROR = "Invalid token format. It must have no leading/trailing whitespace and words separated by single spaces."
class FHIR_primitive_CodeField(models.CharField):
    def clean(self, value, model_instance): return apply_regex(value, CODE_REGEX, CODE_ERROR)

class FHIR_primitive_DateField(models.DateField):
    pass

class FHIR_primitive_DateField_Precision(models.CharField):
    class Precision(models.TextChoices):
        YEAR = 'year', 'Year'
        MONTH = 'month', 'Month'
        DAY = 'day', 'Day'
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = self.Precision.choices
        kwargs['max_length'] = 5
        super().__init__(*args, **kwargs)

class FHIR_primitive_DateTimeField(models.DateTimeField):
    pass

class FHIR_primitive_DateTimeField_Precision(models.CharField):
    class Precision(models.TextChoices):
        YEAR = 'year', 'Year'
        MONTH = 'month', 'Month'
        DAY = 'day', 'Day'
        SECONDS = 'seconds', 'Seconds'
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = self.Precision.choices
        kwargs['max_length'] = 7
        super().__init__(*args, **kwargs)


class FHIR_primitive_DecimalField(models.DecimalField):
    def __init__(self, *args, **kwargs):
        kwargs['max_digits'] = kwargs.get('max_digits', 18)
        kwargs['decimal_places'] = kwargs.get('decimal_places', 17)
        super().__init__(*args, **kwargs)

ID_REGEX = r'^[A-Za-z0-9\-\.]{1,64}$'
ID_ERROR = "Invalid id format. Must only contain letters, numbers, hyphens, and periods, and be no longer than 64 characters."
class FHIR_primitive_IdField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 64  # Set max_length to 64
        super().__init__(*args, **kwargs)
    def clean(self, value, model_instance): return apply_regex(value, ID_REGEX, ID_ERROR)

INSTANT_REGEX = r'^([0-9]{4})(-(0[1-9]|1[0-2]))?(-(0[1-9]|[12][0-9]|3[01]))T([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9]|60)(\.[0-9]{1,9})?(Z|([+-])((0[0-9]|1[0-3]):[0-5][0-9]|14:00))$'
INSTANT_ERROR = "Invalid instant format. Must match the format: YYYY-MM-DDThh:mm:ss.sss+zz:zz or Z."
class FHIR_primitive_InstantField(models.CharField):
    def clean(self, value, model_instance): return apply_regex(value, INSTANT_REGEX, INSTANT_ERROR)

class FHIR_primitive_SignedIntField(models.IntegerField):
    pass

class FHIR_primitive_SignedInt64Field(models.BigIntegerField):
    pass

MARKDOWN_REGEX = r'^[\s\S]+$'
MARKDOWN_ERROR = "Invalid markdown: string must not be empty."
class FHIR_primitive_MarkdownField(models.CharField):
    def clean(self, value, model_instance): return apply_regex(value, MARKDOWN_REGEX, MARKDOWN_ERROR)

OID_REGEX = r'urn:oid:[0-2](\.(0|[1-9][0-9]*))+'
OID_ERROR = "urn:oid:numbers incorrect"
class FHIR_primitive_OID_Field(models.CharField):
    def clean(self, value, model_instance): return apply_regex(value, OID_REGEX, OID_ERROR)

STRING_REGEX = r'^[\s\S]+$'
STRING_ERROR = "Invalid markdown: string must not be empty."
class FHIR_primitive_StringField(models.CharField):
    def clean(self, value, model_instance): return apply_regex(value, STRING_REGEX, STRING_ERROR)

class FHIR_primitive_PositiveIntField(models.IntegerField):
    def clean(self, value, model_instance):
        if value < 1: raise ValidationError("Positive int must be greater than 0")

class FHIR_primitive_TimeField(models.TimeField):
    def clean(self, value, model_instance):
        if value >= time(24, 0, 0):
            raise ValidationError("Time must be less than 24:00:00.")
        return value

class FHIR_primitive_UnsignedIntField(models.IntegerField):
    def clean(self, value, model_instance):
        if value < 0: raise ValidationError("Positive int must be greater than 0")

URI_REGEX = r'\S*'
URI_ERROR = "URI must not have spaces and not be empty"
class FHIR_primitive_URIField(models.CharField):
    def clean(self, value, model_instance): return apply_regex(value, URI_REGEX, URI_ERROR)

URL_REGEX = r'\S*'
URL_ERROR = "URL must not have spaces and not be empty"
class FHIR_primitive_URLField(models.CharField):
    def clean(self, value, model_instance): return apply_regex(value, URL_REGEX, URL_ERROR)

UUID_REGEX = r'^([0-9]{4})(-(0[1-9]|1[0-2]))?(-(0[1-9]|[12][0-9]|3[01]))T([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9]|60)(\.[0-9]{1,9})?(Z|([+-])((0[0-9]|1[0-3]):[0-5][0-9]|14:00))$'
UUID_ERROR = "Invalid UUID format, see https://www.ietf.org/rfc/rfc4122.txt"
class FHIR_primitive_UUIDField(models.CharField):
    def clean(self, value, model_instance): return apply_regex(value, UUID_REGEX, UUID_ERROR)
