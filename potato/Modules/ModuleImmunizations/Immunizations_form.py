from django import forms
from potato.models import (
    FHIR_Immunization,
    FHIR_Immunization_note,
    FHIR_Immunization_performer,
    FHIR_GP_Coding
)
from django.db import transaction


class Immunization_Combined_Form(forms.Form):
    vaccineCode_cc = forms.ModelChoiceField(
        queryset=FHIR_GP_Coding.objects.filter(codings__binding_rule=FHIR_Immunization.BINDING_vaccineCode).order_by('display', 'code'),
        widget=forms.Select(attrs={
            'class': 'form-select tomselect',
            'data-plugins': 'remove_button',
            'autocomplete': 'off',
            'data-allow-empty': 'true'
        })
    )
    
    status = forms.ChoiceField(
        choices=FHIR_Immunization.StatusChoices.choices,
        widget=forms.Select(attrs={'class': 'form-select form-select-sm'})
    )

    occurrence_dateTime = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control form-control-sm'})
    )

    route_cc = forms.ModelChoiceField(
        required=False,
        queryset=FHIR_GP_Coding.objects.filter(codings__binding_rule=FHIR_Immunization.BINDING_route).order_by('display', 'code'),
        widget=forms.Select(attrs={'class': 'form-select form-select-sm'})
    )

    site_cc = forms.ModelChoiceField(
        required=False,
        queryset=FHIR_GP_Coding.objects.filter(codings__binding_rule=FHIR_Immunization.BINDING_site).order_by('display', 'code'),
        widget=forms.Select(attrs={'class': 'form-select form-select-sm'})
    )

    text = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'rows': 7,
            'class': 'form-control border-2'
        })
    )

    def is_valid(self):
        if not super().is_valid(): return False
        return True

    def save(self, immunization_model=None, patient_model=None, performer_practitioner_model=None):
        if not self.is_valid():
            raise ValueError("Form is not valid, cannot save")

        cleaned_data = self.cleaned_data

        with transaction.atomic():
            if not immunization_model:
                immunization_model = FHIR_Immunization()

            immunization_model.occurrence_dateTime = cleaned_data['occurrence_dateTime']
            immunization_model.status = cleaned_data['status']

            if patient_model:
                immunization_model.patient = patient_model

            immunization_model.save()
            immunization_model.vaccineCode_cc.set([cleaned_data['vaccineCode_cc']])
            
            if performer_practitioner_model:
                performer, _ = FHIR_Immunization_performer.objects.get_or_create(
                    Immunization=immunization_model
                )
                performer.actor_Practitioner = performer_practitioner_model
                performer.save()
            
            if cleaned_data['route_cc']:
                immunization_model.route_cc.set([cleaned_data['route_cc']])
            
            if cleaned_data['site_cc']:
                immunization_model.site_cc.set([cleaned_data['site_cc']])

            if cleaned_data['text']:
                note_model, _ = FHIR_Immunization_note.objects.get_or_create(
                    Immunization=immunization_model
                )
                note_model.text = cleaned_data['text']
                note_model.save()

        return immunization_model

    def __init__(self, *args, immunization_model=None, **kwargs):
        super().__init__(*args, **kwargs)
        if immunization_model:
            self.fields['vaccineCode_cc'].initial = immunization_model.vaccineCode_cc.first()
            self.fields['status'].initial = immunization_model.status
            self.fields['route_cc'].initial = immunization_model.route_cc.first()
            self.fields['site_cc'].initial = immunization_model.site_cc.first()
            self.fields['occurrence_dateTime'].initial = immunization_model.occurrence_dateTime
            
            note_model = FHIR_Immunization_note.objects.filter(Immunization=immunization_model).first()
            if note_model:
                self.fields['text'].initial = note_model.text
