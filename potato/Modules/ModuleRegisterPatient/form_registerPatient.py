from django import forms
from potato.models import (
    FHIR_Patient,
    FHIR_GP_HumanName,
    FHIR_GP_Address,
    FHIR_GP_ContactPoint
)
class RegisterPatientForm(forms.Form):
    #patient's demographics
    prefix = forms.CharField(max_length=255, required=False, label="Title")
    given_name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'First'}))
    middle_name = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'placeholder': 'Middle'}))
    family_name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'Last'}))
    suffix = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'placeholder': 'suffix'}))
    nickname = forms.CharField(max_length=255, required=False)
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
