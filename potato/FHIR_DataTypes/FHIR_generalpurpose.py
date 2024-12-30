#https://www.hl7.org/fhir/datatypes.html#complex
#FHIR_primitive_CodeField etc from FHIR_primitive.py
#FHIR_SP_Reference etc from FHIR_specialpurpose.py

from .FHIR_primitive import *
from .FHIR_specialpurpose import *
from ..FHIR_Resources.Organization import FHIR_Organization

class FHIR_GP_Attachment(models.Model):
    contentType = FHIR_primitive_CodeField(max_length=256)  # Mime type of the content, with charset etc.
    language = FHIR_primitive_CodeField(max_length=10)  # Human language of the content (BCP-47)
    data = FHIR_primitive_Base64BinaryField()  # Data inline, base64-encoded
    url = FHIR_primitive_URLField(max_length=1024)  # URI where the data can be found
    size = FHIR_primitive_SignedInt64Field()  # Number of bytes of content (if URL is provided)
    hash = FHIR_primitive_Base64BinaryField()  # Hash of the data (SHA-1, base64-encoded)
    title = FHIR_primitive_StringField(max_length=256)  # Label to display in place of the data
    creation = FHIR_primitive_DateTimeField()  # Date the attachment was first created
    height = FHIR_primitive_PositiveIntField(null=True, blank=True)  # Height of the image in pixels (photo/video)
    width = FHIR_primitive_PositiveIntField(null=True, blank=True)  # Width of the image in pixels (photo/video)
    frames = FHIR_primitive_PositiveIntField(null=True, blank=True)  # Number of frames if > 1 (photo)
    duration = FHIR_primitive_DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Length in seconds (audio/video)
    pages = FHIR_primitive_PositiveIntField(null=True, blank=True)  # Number of printed pages
    def clean(self):
        if self.data and not self.contentType:
            raise ValidationError("If data is provided, contentType must be defined.")
    def __str__(self):
        if self.title:
            return self.title
        else:
            return "unknown_file" + str(self.id)

class FHIR_GP_Coding(models.Model):
    system = FHIR_primitive_URIField(max_length=1024)  # Identity of the terminology system (URI)
    version = FHIR_primitive_StringField(max_length=256, null=True, blank=True)  # Version of the system (optional)
    code = FHIR_primitive_CodeField(max_length=256, null=True, blank=True)  # Symbol in syntax defined by the system
    display = FHIR_primitive_StringField(max_length=256, null=True, blank=True)  # Representation defined by the system (optional)
    userSelected = FHIR_primitive_BooleanField()  # If this coding was chosen directly by the user

class FHIR_GP_CodeableConcept(models.Model):
    coding = models.ManyToManyField(FHIR_GP_Coding, blank=True)  # Code(s) defined by a terminology system
    text = FHIR_primitive_StringField(max_length=1024, null=True, blank=True)  # Plain text representation(s) of the concept
    def __str__(self):
        return self.text

class FHIR_GP_Quantity(models.Model):
    class Comparator(models.TextChoices):
        LESS_THAN = '<', 'Less than'
        LESS_THAN_OR_EQUAL = '<=', 'Less than or equal to'
        GREATER_THAN_OR_EQUAL = '>=', 'Greater than or equal to'
        GREATER_THAN = '>', 'Greater than'
    value = FHIR_primitive_DecimalField(max_digits=18, decimal_places=17)  # Numerical value
    comparator = FHIR_primitive_CodeField(max_length=2, choices=Comparator.choices, blank=True, null=True)  # Optional comparator
    unit = FHIR_primitive_StringField(max_length=64)  # Unit representation
    system = FHIR_primitive_URIField(max_length=255, blank=True, null=True)  # URI for the unit system
    code = FHIR_primitive_CodeField(max_length=64, blank=True, null=True)  # Coded form of the unit
    def clean(self):
        if self.unit and not self.system:
            raise ValidationError("If a code for the unit is present, the system must also be present	")
    def __str__(self):
        return f"{self.value} {self.unit} {self.get_comparator_display() if self.comparator else ''}"

class FHIR_GP_Quantity_Distance(FHIR_GP_Quantity):
    def clean(self):
        super().clean()
        if self.value is not None and not self.code:
            raise ValidationError("A code must exist if there is a value, and the code should be an expression of length")
        if self.system and self.system.lower() != 'http://unitsofmeasure.org':
            raise ValidationError("If a system is present, it must be UCUM (http://unitsofmeasure.org).")

class FHIR_GP_Quantity_Count(FHIR_GP_Quantity):
    def clean(self):
        super().clean()
        if self.value is not None:
            if not self.code or self.code != '1':
                raise ValidationError("A code with the value '1' must exist if there is a value.")
        if self.system and self.system.lower() != 'http://unitsofmeasure.org':
            raise ValidationError("If a system is present, it must be UCUM (http://unitsofmeasure.org).")
        if self.value is not None and self.value % 1 != 0:
                raise ValidationError("If present, the value must be a whole number.")

class FHIR_GP_Quantity_Duration(FHIR_GP_Quantity):
    def clean(self):
        super().clean()
        if self.value is not None and not self.code:
            raise ValidationError("A code must exist if there is a value, and it must be an expression of time.")
        if self.system and self.system.lower() != 'http://unitsofmeasure.org':
            raise ValidationError("If a system is present, it must be UCUM (http://unitsofmeasure.org).")

class FHIR_GP_Quantity_Simple(FHIR_GP_Quantity):
    def clean(self):
        super().clean()
        if self.comparator:
            raise ValidationError("SimpleQuantity must not have a comparator.")

#note money is its own data type, which is *not* a quantity
#quantity_money is for when money needs to represent a ratio using quantity
class FHIR_GP_Quantity_Money(FHIR_GP_Quantity):
    def clean(self):
        super().clean()
        if self.value is not None and not self.code:
            raise ValidationError("A code must exist if there is a value, and it must represent a currency.")
        if self.system and self.system != 'urn:iso:std:iso:4217':
            raise ValidationError("If a system is present, it must be ISO 4217 (urn:iso:std:iso:4217).")

class FHIR_GP_Money(models.Model):
    value = FHIR_primitive_DecimalField(null=True, blank=True)
    currency = FHIR_primitive_CodeField(
        max_length=3,
        blank=True,
        null=True,
        help_text="ISO 4217 currency code (e.g., USD, EUR)."
    )

class FHIR_GP_Range(models.Model):
    low = models.OneToOneField(FHIR_GP_Quantity_Simple, on_delete=models.CASCADE, related_name="range_low", null=True, blank=True)
    high = models.OneToOneField(FHIR_GP_Quantity_Simple, on_delete=models.CASCADE, related_name="range_high", null=True, blank=True)
    def clean(self):
        if self.low and self.high:
            if self.high.value < self.low.value:
                raise ValidationError("Range high value must be greater than low value.")
    def __str__(self):
        return f"{self.low} to {self.high}"

class FHIR_GP_Ratio(models.Model):
    numerator = models.OneToOneField(FHIR_GP_Quantity, on_delete=models.CASCADE, related_name="ratio_numerator", null=True, blank=True)
    denominator = models.OneToOneField(FHIR_GP_Quantity_Simple, on_delete=models.CASCADE, related_name="ratio_denominator", null=True, blank=True)
    def clean(self):
        if self.numerator and not self.denominator:
            raise ValidationError("Numerator exists but denominator doesn't - numerator and denominator must both be present.")
        if self.denominator and not self.numerator:
            raise ValidationError("Denominator exists but numerator doesn't - numerator and denominator must both be present.")
    def str(self):
        return self.numerator + "/" + self.denominator

class FHIR_GP_RatioRange(models.Model):
    numerator_high = models.OneToOneField(FHIR_GP_Quantity_Simple, on_delete=models.CASCADE, related_name="ratio_range_numerator_high", null=True, blank=True)
    numerator_low = models.OneToOneField(FHIR_GP_Quantity_Simple, on_delete=models.CASCADE, related_name="ratio_range_numerator_low", null=True, blank=True)
    denominator = models.OneToOneField(FHIR_GP_Quantity_Simple, on_delete=models.CASCADE, related_name="ratio_range_denominator", null=True, blank=True)
    def clean(self):
        if (self.numerator_low or self.numerator_high) and not self.denominator:
            raise ValidationError("Numerator high or low exists but denominator doesn't - numerator and denominator must both be present.")
        if self.numerator_low and self.numerator_high:
            if self.numerator_high < self.numerator_low:
                raise ValidationError("Ratio range high numerator must be greater than low numerator.")
    def __str__(self):
        return "(" + self.numerator + " to " + self.denominator + ")/" + self.denominator

class FHIR_GP_Period(models.Model):
    start = models.OneToOneField(FHIR_primitive_DateTimeField, on_delete=models.CASCADE, related_name="period_start", null=True, blank=True)
    end = models.OneToOneField(FHIR_primitive_DateTimeField, on_delete=models.CASCADE, related_name="period_end", null=True, blank=True)
    def clean(self):
        if self.start and self.end:
            if self.start.datetime and self.end.datetime:
                if self.start.datetime > self.end.datetime:
                    raise ValidationError("Start time must be before or equal to end time.")
    def __str__(self):
        if self.start and self.end:
            return f"Period: {self.start.datetime} to {self.end.datetime}"
        elif self.start:
            return f"Period starts at {self.start.datetime}"
        elif self.end:
            return f"Period ends at {self.end.datetime}"
        else:
            return "Period not specified"

#A SampledData provides a concise way to handle the data produced by devices that sample a particular physical state at a high frequency.
#A typical use for this is for the output of an ECG or EKG device.
#The datatype includes a series of raw decimal values (which are mostly simple integers) or codes, along with adjustments for scale and factor.
#These are interpreted such that:
#original measured value[i] = SampledData.data[i] * SampledData.factor + SampledData.origin.value
class FHIR_GP_SampledData(models.Model):
    origin = models.OneToOneField(FHIR_GP_Quantity_Simple, on_delete=models.CASCADE, related_name="sampleddata_origin")  # Zero value and units
    interval = FHIR_primitive_DecimalField(null=True, blank=True)  # Number of intervalUnits between samples
    intervalUnit = FHIR_primitive_CodeField(max_length=64)  # The measurement unit of the interval between samples
    factor = FHIR_primitive_DecimalField(null=True, blank=True)  # Multiply data by this before adding to origin
    lowerLimit = FHIR_primitive_DecimalField(null=True, blank=True)  # Lower limit of detection
    upperLimit = FHIR_primitive_DecimalField(null=True, blank=True)  # Upper limit of detection
    dimensions = FHIR_primitive_PositiveIntField()  # Number of sample points at each time point
    codeMap = FHIR_primitive_CanonicalField(max_length=256, null=True, blank=True)  # Defines the codes used in the data
    offsets = FHIR_primitive_StringField(max_length=1024, null=True, blank=True)  # Offsets at which data values were taken
    data = FHIR_primitive_StringField(max_length=1024, null=True, blank=True)  # Decimal values or another code
    def __str__(self):
        return f"SampledData with origin: {self.origin}, dimensions: {self.dimensions}"


class FHIR_GP_Identifier(models.Model):
    class IdentifierUse(models.TextChoices): USUAL = "usual", "Usual"; OFFICIAL = "official", "Official"; TEMP = "temp", "Temporary"; SECONDARY = "secondary", "Secondary"; OLD = "old", "Old"
    use = FHIR_primitive_CodeField(max_length=16, choices=IdentifierUse.choices, null=True, blank=True)
    type = models.OneToOneField(FHIR_GP_CodeableConcept, on_delete=models.CASCADE, related_name="identifier_type", null=True, blank=True)
    system = FHIR_primitive_URIField(max_length=1024, null=True, blank=True)
    value = FHIR_primitive_StringField(max_length=1024, null=True, blank=True)
    period = models.OneToOneField(FHIR_GP_Period, on_delete=models.CASCADE, related_name="identifier_period", null=True, blank=True)
    assigner_reference = models.OneToOneField(FHIR_SP_Reference, on_delete=models.CASCADE, null=True, blank=True)
    assigner_foreignKey = models.ForeignKey(FHIR_Organization, on_delete=models.CASCADE, related_name="identifier_assigner")
    def clean(self):
        if not self.value:
            raise ValidationError("Value must exist.")
    def __str__(self):
        return f"Identifier: {self.value}"



class FHIR_GP_HumanName(models.Model):
    class NameUseChoices(models.TextChoices): USUAL = 'usual', 'Usual'; OFFICIAL = 'official', 'Official'; TEMP = 'temp', 'Temporary'; NICKNAME = 'nickname', 'Nickname'; ANONYMOUS = 'anonymous', 'Anonymous'; OLD = 'old', 'Old'; MAIDEN = 'maiden', 'Maiden'
    use = models.CharField(max_length=20, choices=NameUseChoices.choices, null=True, blank=True)
    text = FHIR_primitive_StringField(max_length=255, null=True, blank=True)
    family = FHIR_primitive_StringField(max_length=255, null=True, blank=True)
    period = models.OneToOneField(FHIR_GP_Period, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.text}"
    #given, prefix, suffix - can have 0 to many, so defined separately with foreign keys
class FHIR_GP_HumanName_Given(models.Model):
    value = FHIR_primitive_StringField(max_length=255)
    human_name = models.ForeignKey(FHIR_GP_HumanName, related_name="given_names", on_delete=models.CASCADE)
class FHIR_GP_HumanName_Prefix(models.Model):
    value = FHIR_primitive_StringField(max_length=255)
    human_name = models.ForeignKey(FHIR_GP_HumanName, related_name="prefixes", on_delete=models.CASCADE)
class FHIR_GP_HumanName_Suffix(models.Model):
    value = FHIR_primitive_StringField(max_length=255)
    human_name = models.ForeignKey(FHIR_GP_HumanName, related_name="suffixes", on_delete=models.CASCADE)


class FHIR_GP_Address(models.Model):
    class AddressUse(models.TextChoices): HOME = 'home', 'Home'; WORK = 'work', 'Work'; TEMP = 'temp', 'Temporary'; OLD = 'old', 'Old'; BILLING = 'billing', 'Billing'
    class AddressType(models.TextChoices): POSTAL = 'postal', 'Postal'; PHYSICAL = 'physical', 'Physical'; BOTH = 'both', 'Both'
    use = FHIR_primitive_CodeField(max_length=20, null=True, blank=True, choices=AddressUse.choices)  # home | work | temp | old | billing - purpose of this address
    type = FHIR_primitive_CodeField(max_length=20, null=True, blank=True, choices=AddressType.choices)  # postal | physical | both
    text = FHIR_primitive_StringField(max_length=255, null=True, blank=True)  # Text representation of the address
    city = FHIR_primitive_StringField(max_length=255, null=True, blank=True)  # Name of city, town etc.
    district = FHIR_primitive_StringField(max_length=255, null=True, blank=True)  # District name (aka county)
    state = FHIR_primitive_StringField(max_length=255, null=True, blank=True)  # Sub-unit of country (abbreviations ok)
    postalCode = FHIR_primitive_StringField(max_length=20, null=True, blank=True)  # Postal code for area
    country = FHIR_primitive_StringField(max_length=3, null=True, blank=True)  # Country (e.g. may be ISO 3166 2 or 3 letter code)
    period = models.OneToOneField(FHIR_GP_Period, null=True, blank=True, on_delete=models.CASCADE)  # Time period when address was/is in use
    def __str__(self):
        return f"{self.text}"
class FHIR_GP_AddressLine(models.Model):
    value = FHIR_primitive_StringField(max_length=255)  # Street name, number, direction & P.O. Box etc.
    #This repeating element order: The order in which lines should appear in an address label
    address = models.ForeignKey(FHIR_GP_Address, related_name="lines", on_delete=models.CASCADE)

class FHIR_GP_ContactPoint(models.Model):
    class System(models.TextChoices): PHONE = 'phone', 'Phone'; FAX = 'fax', 'Fax'; EMAIL = 'email', 'Email'; PAGER = 'pager', 'Pager'; URL = 'url', 'URL'; SMS = 'sms', 'SMS'; OTHER = 'other', 'Other'
    class Use(models.TextChoices): HOME = 'home', 'Home'; WORK = 'work', 'Work'; TEMP = 'temp', 'Temporary'; OLD = 'old', 'Old'; MOBILE = 'mobile', 'Mobile'
    system = FHIR_primitive_CodeField(max_length=20, choices=System.choices, null=True, blank=True)
    value = FHIR_primitive_StringField(max_length=255, null=True, blank=True)
    use = FHIR_primitive_CodeField(max_length=20, choices=Use.choices, null=True, blank=True)
    rank = models.PositiveIntegerField(null=True, blank=True)
    period = models.OneToOneField(FHIR_GP_Period, null=True, blank=True, on_delete=models.CASCADE)
    def clean(self):
        if self.value and not self.system:
            raise ValidationError("A 'system' is required if a 'value' is provided.")
    def __str__(self):
        return f"{self.value}"


class FHIR_GP_Event(models.Model):
    class DurationUnitChoices(models.TextChoices): SECONDS = 's', 'Seconds'; MINUTES = 'min', 'Minutes'; HOURS = 'h', 'Hours'; DAYS = 'd', 'Days'; WEEKS = 'wk', 'Weeks'; MONTHS = 'mo', 'Months'; YEARS = 'a', 'Years'  # I s | min | h | d | wk | mo | a - unit of time (UCUM)
    class PeriodUnitChoices(models.TextChoices): SECONDS = 's', 'Seconds'; MINUTES = 'min', 'Minutes'; HOURS = 'h', 'Hours'; DAYS = 'd', 'Days'; WEEKS = 'wk', 'Weeks'; MONTHS = 'mo', 'Months'; YEARS = 'a', 'Years'  # I s | min | h | d | wk | mo | a - unit of time (UCUM)
    class DayOfWeekChoices(models.TextChoices): MON = 'mon', 'Monday'; TUE = 'tue', 'Tuesday'; WED = 'wed', 'Wednesday'; THU = 'thu', 'Thursday'; FRI = 'fri', 'Friday'; SAT = 'sat', 'Saturday'; SUN = 'sun', 'Sunday'  # mon | tue | wed | thu | fri | sat | sun
    event = models.JSONField(null=True, blank=True)  # When the event occurs
    boundsDuration = models.OneToOneField(FHIR_GP_Quantity_Duration, null=True, blank=True, on_delete=models.CASCADE)  # Length/Range of lengths
    boundsRange = models.OneToOneField(FHIR_GP_Range, null=True, blank=True, on_delete=models.CASCADE)  # Start and/or end limits
    boundsPeriod = models.OneToOneField(FHIR_GP_Period, null=True, blank=True, on_delete=models.CASCADE)  # Start and/or end limits
    count = models.PositiveIntegerField(null=True, blank=True)  # I Number of times to repeat
    countMax = models.PositiveIntegerField(null=True, blank=True)  # I Maximum number of times to repeat
    duration = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # I How long when it happens
    durationMax = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # I How long when it happens (Max)
    durationUnit = models.CharField(max_length=10, choices=DurationUnitChoices.choices, null=True, blank=True)  # I s | min | h | d | wk | mo | a - unit of time (UCUM)
    frequency = models.PositiveIntegerField(null=True, blank=True)  # Indicates the number of repetitions that should occur within a period. I.e., Event occurs frequency times per period
    frequencyMax = models.PositiveIntegerField(null=True, blank=True)  # Event occurs up to frequencyMax times per period
    period = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # I The duration to which the frequency applies. I.e., Event occurs frequency times per period
    periodMax = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # I Upper limit of period (3-4 hours)
    periodUnit = models.CharField(max_length=10, choices=PeriodUnitChoices.choices, null=True, blank=True)  # I s | min | h | d | wk | mo | a - unit of time (UCUM)
    dayOfWeek = models.CharField(max_length=10, choices=DayOfWeekChoices.choices, null=True, blank=True)  # mon | tue | wed | thu | fri | sat | sun
    timeOfDay = models.JSONField(null=True, blank=True)  # I Time of day for action
    when = models.JSONField(null=True, blank=True)  # I Code for time period of occurrence
    offset = models.PositiveIntegerField(null=True, blank=True)  # I Minutes from event (before or after)
    code = models.OneToOneField(FHIR_GP_CodeableConcept, null=True, blank=True, on_delete=models.CASCADE)  # C | BID | TID | QID | AM | PM | QD | QOD | +
    def __str__(self):
        return f"FHIR_GP_Event: {self.event}"
    def clean(self):
        raise ValidationError("idk todo")

class FHIR_GP_Signature(models.Model):
    type = models.ManyToManyField(FHIR_GP_Coding, related_name="types", blank=True)
    when = FHIR_primitive_InstantField(max_length=99999, null=True, blank=True)  # When the signature was created
    #who reference and ForeignKey to Practitioner | PractitionerRole | RelatedPerson | Patient | Device | Organization
    who_reference = models.OneToOneField(FHIR_SP_Reference, on_delete=models.CASCADE, null=True, blank=True, related_name="who_reference")
    who_practitioner_foreignKey = models.ForeignKey('FHIR_Practitioner', null=True, on_delete=models.SET_NULL, related_name="who_practitioner")
    who_relatedPerson_foreignKey = models.ForeignKey('FHIR_RelatedPerson', null=True, on_delete=models.SET_NULL, related_name="who_relatedPerson")
    who_patient_foreignKey = models.ForeignKey('FHIR_Patient', null=True, on_delete=models.SET_NULL, related_name="who_patient")
    who_device_foreignKey = models.ForeignKey('FHIR_Device', null=True, on_delete=models.SET_NULL, related_name="who_device")
    who_organization_foreignKey = models.ForeignKey('FHIR_Organization', null=True, on_delete=models.SET_NULL, related_name="who_organization")
    #onBehalfOf reference and ForeignKey to Practitioner | PractitionerRole | RelatedPerson | Patient | Device | Organization)
    onBehalfOf_reference = models.OneToOneField(FHIR_SP_Reference, on_delete=models.CASCADE, null=True, blank=True, related_name="onBehalfOf_reference")
    onBehalfOf_practitioner_foreignKey = models.ForeignKey('FHIR_Practitioner', null=True, on_delete=models.SET_NULL, related_name="onBehalfOf_practitioner")
    onBehalfOf_relatedPerson_foreignKey = models.ForeignKey('FHIR_RelatedPerson', null=True, on_delete=models.SET_NULL, related_name="onBehalfOf_relatedPerson")
    onBehalfOf_patient_foreignKey = models.ForeignKey('FHIR_Patient', null=True, on_delete=models.SET_NULL, related_name="onBehalfOf_patient")
    onBehalfOf_device_foreignKey = models.ForeignKey('FHIR_Device', null=True, on_delete=models.SET_NULL, related_name="onBehalfOf_device")
    onBehalfOf_organization_foreignKey = models.ForeignKey('FHIR_Organization', null=True, on_delete=models.SET_NULL, related_name="onBehalfOf_organization")
    targetFormat = FHIR_primitive_CodeField(max_length=255, null=True, blank=True)  # The technical format of the signed resources
    sigFormat = FHIR_primitive_CodeField(max_length=255, null=True, blank=True)  # The technical format of the signature
    data = FHIR_primitive_Base64BinaryField(null=True, blank=True)  # The actual signature content (XML DigSig, JWS, picture, etc.)

    def __str__(self):
        return "idk todo"


class FHIR_GP_Annotation(models.Model):
    author_reference = models.ForeignKey(FHIR_SP_Reference, null=True, blank=True, on_delete=models.SET_NULL, related_name="author_reference")
    author_practitioner_foreignKey = models.ForeignKey('FHIR_Practitioner', null=True, on_delete=models.SET_NULL, related_name="author_practitioner")
    author_practitionerRole_foreignKey = models.ForeignKey('FHIR_PractitionerRole', null=True, on_delete=models.SET_NULL, related_name="author_practitionerRole")
    author_patient_foreignKey = models.ForeignKey('FHIR_Patient', null=True, on_delete=models.SET_NULL, related_name="author_patient")
    author_relatedPerson_foreignKey = models.ForeignKey('FHIR_RelatedPerson', null=True, on_delete=models.SET_NULL, related_name="author_relatedPerson")
    author_organization_foreignKey = models.ForeignKey('FHIR_Organization', null=True, on_delete=models.SET_NULL, related_name="author_organization")
    author_string = FHIR_primitive_StringField(max_length=255, null=True, blank=True)
    time = FHIR_primitive_DateTimeField()
    text = FHIR_primitive_MarkdownField(max_length=99999)
    class AuthorType(models.TextChoices): REFERENCE = "authorReference", "Reference"; STRING = "authorString", "String"
    author_type = FHIR_primitive_CodeField(max_length=20, choices=AuthorType.choices, null=True, blank=True)