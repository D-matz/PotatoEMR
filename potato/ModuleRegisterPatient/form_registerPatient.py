from django import forms
from ..models import FHIR_Patient
from ..FHIR_DataTypes.FHIR_generalpurpose import *

class RegisterPatientForm(forms.Form):
    #patient's demographics
    given_name = forms.CharField(max_length=255, required=False, label="Given Name")
    family_name = forms.CharField(max_length=255, required=True, label="Family Name")
    prefix = forms.CharField(max_length=255, required=False, label="Prefix")
    suffix = forms.CharField(max_length=255, required=False, label="Suffix")
    name_use = forms.ChoiceField(choices=FHIR_GP_HumanName.NameUseChoices.choices, required=False, label="Name Type", initial=FHIR_GP_HumanName.NameUseChoices.OFFICIAL)
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True, label="Date of Birth")
    gender = forms.ChoiceField(choices=FHIR_Patient.GenderChoices.choices, required=True, label="Gender")

    #patient's address
    address_use = forms.ChoiceField(choices=FHIR_GP_Address.AddressUse.choices, required=False, label="Address Type", initial=FHIR_GP_Address.AddressUse.HOME)
    address = forms.CharField(max_length=255, required=True, label="Address")
    city = forms.CharField(max_length=255, required=True, label="City")
    state = forms.CharField(max_length=255, required=True, label="State")
    zip_code = forms.CharField(max_length=20, required=True, label="Zip")

    #patient's contact info
    email_addr = forms.CharField(max_length=255, required=False, label="Email")
    phone_use = forms.ChoiceField(choices=FHIR_GP_ContactPoint.Use.choices, required=False, label="Contact Use", initial=FHIR_GP_ContactPoint.Use.MOBILE)
    phone_number = forms.CharField(max_length=255, required=False, label="Phone Number")
