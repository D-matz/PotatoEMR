from django import forms
from potato.models import (
    FHIR_Location,
    FHIR_Practitioner,
)

class PatientSearchForm(forms.Form):
    Name = forms.CharField(required=False)
    Phone = forms.CharField(required=False)
    Email = forms.EmailField(required=False)
    fuzzy = forms.BooleanField(required=False,
                            label="Fuzzy search",
                            widget=forms.CheckboxInput(attrs={'title': 'Allow typos in text, eg "harrypoter" finds "harry potter"',
                                                              'font-size': '0.9rem',
                                                              'class': 'form-check-input border-2 border-danger'}))
