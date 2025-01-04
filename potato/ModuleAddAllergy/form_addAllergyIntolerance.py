from django import forms
from ..FHIR_Resources.AllergyIntolerance import *

class AllergyIntoleranceForm(forms.ModelForm):
    class Meta:
        model = FHIR_AllergyIntolerance
        fields = [
            'clinical_status',
            'verification_status',
            'type',
            'category',
            'criticality',
            'code',
            'onset_dateTime',
            'onset_string',
            'recorded_date',
        ]
        widgets = {
            'onset_dateTime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'recorded_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        labels = {
            'clinical_status': 'Clinical Status',
            'verification_status': 'Verification Status',
            'type': 'Type',
            'category': 'Category',
            'criticality': 'Criticality',
            'code': 'Allergy/Intolerance Code',
            'onset_dateTime': 'Onset Date',
            'onset_string': 'Onset Description',
            'recorded_date': 'Record Date',
        }

class AllergyIntoleranceReactionForm(forms.ModelForm):
    class Meta:
        model = FHIR_AllergyIntolerance_Reaction
        fields = [
            'substance',
            'description',
            'onset',
            'severity',
            'exposure_route',
        ]
        widgets = {
            'onset': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'substance': 'Substance',
            'description': 'Reaction Description',
            'onset': 'Reaction Onset',
            'severity': 'Severity',
            'exposure_route': 'Exposure Route',
        }

class AllergyIntoleranceNoteForm(forms.ModelForm):
    class Meta:
        model = FHIR_AllergyIntolerance_Note
        fields = ['text', 'time_datetime']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3}),
            'time_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        labels = {
            'text': 'Note',
            'time_datetime': 'Note Date/Time',
        }
