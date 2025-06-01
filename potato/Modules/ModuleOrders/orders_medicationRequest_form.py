from django import forms
from django.db import transaction
from potato.models_dir.FHIR_Resources.MedicationRequest import FHIR_MedicationRequest, FHIR_MedicationRequest_note
from potato.models_dir.FHIR_DataTypes.FHIR_generalpurpose import FHIR_GP_Coding
from datetime import datetime
from potato.Common.Widgets.InputSingleFromMany import InputSingleFromMany

class MedicationRequestForm(forms.ModelForm):
    class Meta:
        model = FHIR_MedicationRequest
        fields = ['medication_cc', 'status', 'priority']
        widgets = {
            'medication_cc': InputSingleFromMany(attrs={'class': 'form-input form-input-sm'}),
            'status': forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'priority': forms.Select(attrs={'class': 'form-select form-select-sm'}),
        }
        labels = {
            'medication_cc': 'Medication',
            'status': 'Status',
            'priority': 'Priority',
        }

class MedicationRequestNoteForm(forms.ModelForm):
    class Meta:
        model = FHIR_MedicationRequest_note
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control form-control-sm text-truncate w-100',
                'rows': '3'
            })
        }
        labels = {
            'text': 'Instructions'
        }

    def save(self, commit=True):
        # Don't save the form yet
        return super().save(commit=False)

def save_medication_request(med_request_form, note_form, patient_model=None, med_request_model=None):
    with transaction.atomic():
        if med_request_model is None:
            med_request = med_request_form.save(commit=False)
            if patient_model:
                med_request.subject_Patient = patient_model
        else:
            med_request = med_request_form.save(commit=False)
            med_request.id = med_request_model.id

        med_request.authoredOn = datetime.now()
        med_request.save()
        med_request_form.save_m2m()  # Save many-to-many relationships

        # Handle the note
        med_request.MedicationRequest_note.all().delete()
        note = note_form.save(commit=False)
        note.MedicationRequest = med_request
        note.save()

        return med_request