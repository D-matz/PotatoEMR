from django import forms
from potato.models import (
    FHIR_Condition,
    FHIR_Condition_note,
    FHIR_GP_Coding
)
from django.db import transaction


class Condition_Combined_Form(forms.Form):
    code_cc = forms.ModelChoiceField(
        queryset=FHIR_GP_Coding.objects.filter(codings__binding_rule=FHIR_Condition.BINDING_code).order_by('display', 'code'),
        widget=forms.Select(attrs={
            'class': 'form-select tomselect',
            'data-plugins': 'remove_button',
            'autocomplete': 'off',
            'data-allow-empty': 'true'
        })
    )
    
    clinicalStatus_cc = forms.ModelChoiceField(
        required=False,
        queryset=FHIR_GP_Coding.objects.filter(codings__binding_rule=FHIR_Condition.BINDING_clinicalStatus).order_by('display', 'code'),
        widget=forms.Select(attrs={'class': 'form-select form-select-sm'})
    )

    verificationStatus_cc = forms.ModelChoiceField(
        required=False,
        queryset=FHIR_GP_Coding.objects.filter(codings__binding_rule=FHIR_Condition.BINDING_verificationStatus).order_by('display', 'code'),
        widget=forms.Select(attrs={'class': 'form-select form-select-sm'})
    )

    severity_cc = forms.ModelChoiceField(
        required=False,
        queryset=FHIR_GP_Coding.objects.filter(codings__binding_rule=FHIR_Condition.BINDING_severity).order_by('display', 'code'),
        widget=forms.Select(attrs={'class': 'form-select form-select-sm'})
    )

    onset_dateTime = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control form-control-sm'})
    )

    recordedDate = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control form-control-sm'})
    )

    text = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 7,
            'class': 'form-control border-2'
        })
    )

    def is_valid(self):
        if not super().is_valid(): return False
        return True

    def save(self, condition_model=None, patient_model=None, recorder_practitioner_model=None):
        if not self.is_valid():
            raise ValueError("Form is not valid, cannot save")

        cleaned_data = self.cleaned_data

        with transaction.atomic():
            if not condition_model:
                condition_model = FHIR_Condition()

            condition_model.onset_dateTime = cleaned_data['onset_dateTime']
            condition_model.recordedDate = cleaned_data['recordedDate']

            if patient_model:
                condition_model.subject_Patient = patient_model

            if recorder_practitioner_model:
                condition_model.recorder_Practitioner = recorder_practitioner_model

            condition_model.save()
            condition_model.code_cc.set([cleaned_data['code_cc']])
            
            if cleaned_data['clinicalStatus_cc']:
                condition_model.clinicalStatus_cc.set([cleaned_data['clinicalStatus_cc']])
            
            if cleaned_data['verificationStatus_cc']:
                condition_model.verificationStatus_cc.set([cleaned_data['verificationStatus_cc']])
            
            if cleaned_data['severity_cc']:
                condition_model.severity_cc.set([cleaned_data['severity_cc']])

            if cleaned_data['text']:
                note_model, _ = FHIR_Condition_note.objects.get_or_create(Condition=condition_model)
                note_model.text = cleaned_data['text']
                note_model.save()

        return condition_model

    def __init__(self, *args, condition_model=None, **kwargs):
        super().__init__(*args, **kwargs)
        if condition_model:
            self.fields['code_cc'].initial = condition_model.code_cc.first()
            self.fields['clinicalStatus_cc'].initial = condition_model.clinicalStatus_cc.first()
            self.fields['verificationStatus_cc'].initial = condition_model.verificationStatus_cc.first()
            self.fields['severity_cc'].initial = condition_model.severity_cc.first()
            self.fields['onset_dateTime'].initial = condition_model.onset_dateTime
            self.fields['recordedDate'].initial = condition_model.recordedDate
            
            note_model = FHIR_Condition_note.objects.filter(Condition=condition_model).first()
            if note_model:
                self.fields['text'].initial = note_model.text
