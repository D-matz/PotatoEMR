from django import forms
from django.db import transaction
from potato.models_dir.FHIR_Resources.MedicationAdministration import (
    FHIR_MedicationAdministration,
    FHIR_MedicationAdministration_note,
    FHIR_MedicationAdministration_dosage
)
from datetime import datetime
from potato.Common.Widgets.InputSingleFromMany import InputSingleFromMany

class MedicationAdministrationForm(forms.ModelForm):
    class Meta:
        model = FHIR_MedicationAdministration
        fields = [
            'medication_cc',
            'status',
            'occurrence_dateTime',
            'request',
        ]
        widgets = {
            'medication_cc': InputSingleFromMany(attrs={'class': 'form-input form-input-sm'}),
            'status': forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'occurrence_dateTime': forms.DateTimeInput(attrs={'class': 'form-input form-input-sm', 'type': 'datetime-local'}),
            'request': forms.Select(attrs={'class': 'form-select form-select-sm'}),
        }
        labels = {
            'medication_cc': 'Medication',
            'status': 'Status',
            'occurrence_dateTime': 'Administration Time',
            'request': 'Medication Request',
        }

class MedicationAdministrationNoteForm(forms.ModelForm):
    class Meta:
        model = FHIR_MedicationAdministration_note
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control form-control-sm text-truncate w-100',
                'rows': '3'
            })
        }
        labels = {
            'text': 'Notes'
        }

    def save(self, commit=True):
        return super().save(commit=False)

class MedicationAdministrationDosageForm(forms.ModelForm):
    class Meta:
        model = FHIR_MedicationAdministration_dosage
        fields = [
            'text',
            'site_cc',
            'route_cc',
            'method_cc',
        ]
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control form-control-sm',
                'rows': '2'
            }),
            'site_cc': InputSingleFromMany(attrs={'class': 'form-input form-input-sm'}),
            'route_cc': InputSingleFromMany(attrs={'class': 'form-input form-input-sm'}),
            'method_cc': InputSingleFromMany(attrs={'class': 'form-input form-input-sm'}),
        }
        labels = {
            'text': 'Dosage Instructions',
            'site_cc': 'Site',
            'route_cc': 'Route',
            'method_cc': 'Method',
        }

    def save(self, commit=True):
        return super().save(commit=False)

def save_medication_administration(med_admin_form, note_form, dosage_form, patient_model=None, med_admin_model=None):
    with transaction.atomic():
        if med_admin_model is None:
            med_admin = med_admin_form.save(commit=False)
            if patient_model:
                med_admin.subject_Patient = patient_model
        else:
            med_admin = med_admin_form.save(commit=False)
            med_admin.id = med_admin_model.id

        med_admin.occurrence_dateTime = datetime.now()
        med_admin.save()
        med_admin_form.save_m2m()

        med_admin.MedicationAdministration_note.all().delete()
        note = note_form.save(commit=False)
        note.MedicationAdministration = med_admin
        note.save()

        if dosage_form and dosage_form.is_valid():
            med_admin.MedicationAdministration_dosage.all().delete()
            dosage = dosage_form.save(commit=False)
            dosage.MedicationAdministration = med_admin
            dosage.save()
            dosage_form.save_m2m()

        return med_admin
