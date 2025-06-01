from django import forms
from django.db import transaction
from potato.models_dir.FHIR_Resources.MedicationDispense import (
    FHIR_MedicationDispense,
    FHIR_MedicationDispense_note,
    FHIR_MedicationDispense_dosageInstruction
)
from potato.models_dir.FHIR_DataTypes.FHIR_generalpurpose import FHIR_GP_Quantity
from datetime import datetime
from potato.Common.Widgets.InputSingleFromMany import InputSingleFromMany

class MedicationDispenseForm(forms.ModelForm):
    class Meta:
        model = FHIR_MedicationDispense
        fields = [
            'medication_cc',
            'status',
            'whenHandedOver',
            'authorizingPrescription',
        ]
        widgets = {
            'medication_cc': InputSingleFromMany(attrs={'class': 'form-input form-input-sm'}),
            'status': forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'whenHandedOver': forms.DateTimeInput(attrs={'class': 'form-input form-input-sm', 'type': 'datetime-local'}),
            'authorizingPrescription': InputSingleFromMany(attrs={'class': 'form-input form-input-sm'}),
        }
        labels = {
            'medication_cc': 'Medication',
            'status': 'Status',
            'whenHandedOver': 'Handed Over Time',
            'authorizingPrescription': 'Authorizing Prescription',
        }

class MedicationDispenseQuantityForm(forms.ModelForm):
    class Meta:
        model = FHIR_GP_Quantity
        fields = ['value', 'unit']
        widgets = {
            'value': forms.NumberInput(attrs={'class': 'form-input form-input-sm'}),
            'unit': forms.TextInput(attrs={'class': 'form-input form-input-sm'}),
        }
        labels = {
            'value': 'Quantity',
            'unit': 'Unit',
        }

    def clean(self):
        cleaned_data = super().clean()
        #save not working because needs system before save to pass clean (if unit presnt, needs system)
        #could also have a system field in form to choose system manually
        self.instance.system = "http://unitsofmeasure.org"
        return cleaned_data

class MedicationDispenseNoteForm(forms.ModelForm):
    class Meta:
        model = FHIR_MedicationDispense_note
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

class MedicationDispenseDosageForm(forms.ModelForm):
    class Meta:
        model = FHIR_MedicationDispense_dosageInstruction
        fields = [
            'patientInstruction',
            'asNeeded',
            'route_cc',
            'method_cc',
        ]
        widgets = {
            'patientInstruction': forms.Textarea(attrs={
                'class': 'form-control form-control-sm',
                'rows': '2'
            }),
            'asNeeded': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'route_cc': InputSingleFromMany(attrs={'class': 'form-input form-input-sm'}),
            'method_cc': InputSingleFromMany(attrs={'class': 'form-input form-input-sm'}),
        }
        labels = {
            'patientInstruction': 'Patient Instructions',
            'asNeeded': 'As Needed',
            'route_cc': 'Route',
            'method_cc': 'Method',
        }

    def save(self, commit=True):
        return super().save(commit=False)

def save_medication_dispense(med_dispense_form, quantity_form, note_form, dosage_form, patient_model=None, med_dispense_model=None):
    with transaction.atomic():
        if med_dispense_model is None:
            med_dispense = med_dispense_form.save(commit=False)
            if patient_model:
                med_dispense.subject_Patient = patient_model
        else:
            med_dispense = med_dispense_form.save(commit=False)
            med_dispense.id = med_dispense_model.id

        # quantity, note, dosage are individual modelforms
        # so they get submitted together but saved individually

        med_dispense.whenHandedOver = datetime.now()
        med_dispense.save()
        med_dispense_form.save_m2m()

        quantity = quantity_form.save()
        med_dispense.quantity = quantity
        med_dispense.save()

        med_dispense.MedicationDispense_note.all().delete()
        note = note_form.save(commit=False)
        note.MedicationDispense = med_dispense
        note.save()

        if dosage_form and dosage_form.is_valid():
            med_dispense.MedicationDispense_dosageInstruction.all().delete()
            dosage = dosage_form.save(commit=False)
            dosage.MedicationDispense = med_dispense
            dosage.save()
            dosage_form.save_m2m()

        return med_dispense
