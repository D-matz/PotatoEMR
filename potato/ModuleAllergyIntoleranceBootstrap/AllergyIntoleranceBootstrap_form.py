from django import forms
from django.forms.widgets import Select
from django.utils.safestring import mark_safe
from ..models_dir.FHIR_DataTypes.FHIR_generalpurpose import FHIR_GP_Coding
from potato.models_dir.FHIR_Resources.AllergyIntolerance import (
    FHIR_AllergyIntolerance,
    FHIR_AllergyIntolerance_reaction,
    FHIR_AllergyIntolerance_reaction_manifestation,
    FHIR_AllergyIntolerance_note
)
from django.db import transaction


class AllergyIntolerance_Combined_Form(forms.Form):
    code_cc = forms.ModelChoiceField(
        queryset=FHIR_GP_Coding.objects.filter(codings__binding_rule=FHIR_AllergyIntolerance.BINDING_code).order_by('display', 'code'),
        widget=forms.Select(attrs={
            'class': 'form-select tomselect',
            'data-plugins': 'remove_button',
            'autocomplete': 'off',
            'data-allow-empty': 'true'
        })
    )
    type_cc = forms.ModelChoiceField(
        required=False,
        queryset=FHIR_GP_Coding.objects.filter(codings__binding_rule=FHIR_AllergyIntolerance.BINDING_type).order_by('display', 'code'),
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

    severity = forms.ChoiceField(
        required=False,
        choices=FHIR_AllergyIntolerance_reaction.SeverityChoices.choices,
        widget=forms.Select(attrs={'class': 'form-select form-select-sm'})
    )

    manifestation_cc_1 = forms.ModelChoiceField(
        required=False,
        queryset=FHIR_GP_Coding.objects.filter(codings__binding_rule=FHIR_AllergyIntolerance_reaction_manifestation.BINDING_manifestation).order_by('display', 'code'),
        widget=forms.Select(attrs={'class': 'form-select tomselect', 'data-plugins': 'remove_button', 'autocomplete': 'off', 'data-allow-empty': 'true'})
    )
    manifestation_cc_2 = forms.ModelChoiceField(
        required=False,
        queryset=FHIR_GP_Coding.objects.filter(codings__binding_rule=FHIR_AllergyIntolerance_reaction_manifestation.BINDING_manifestation).order_by('display', 'code'),
        widget=forms.Select(attrs={'class': 'form-select tomselect', 'data-plugins': 'remove_button', 'autocomplete': 'off', 'data-allow-empty': 'true'})
    )
    manifestation_cc_3 = forms.ModelChoiceField(
        required=False,
        queryset=FHIR_GP_Coding.objects.filter(codings__binding_rule=FHIR_AllergyIntolerance_reaction_manifestation.BINDING_manifestation).order_by('display', 'code'),
        widget=forms.Select(attrs={'class': 'form-select tomselect', 'data-plugins': 'remove_button', 'autocomplete': 'off', 'data-allow-empty': 'true'})
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

    def save(self, allergy_model=None, patient_model=None, recorder_practitioner_model=None):
        if not self.is_valid():
            raise ValueError("Form is not valid, cannot save")

        cleaned_data = self.cleaned_data

        with transaction.atomic():
            if not allergy_model:
                allergy_model = FHIR_AllergyIntolerance()

            allergy_model.onset_dateTime=cleaned_data['onset_dateTime']
            allergy_model.recordedDate=cleaned_data['recordedDate']

            if patient_model:
                allergy_model.patient = patient_model

            if recorder_practitioner_model:
                allergy_model.recorder_practitioner = recorder_practitioner_model

            allergy_model.save()
            allergy_model.code_cc.set([cleaned_data['code_cc']])
            allergy_model.type_cc.set([cleaned_data['type_cc']])

            reaction_model, _ = FHIR_AllergyIntolerance_reaction.objects.get_or_create(AllergyIntolerance=allergy_model)
            reaction_model.severity=cleaned_data['severity']
            reaction_model.save()

            note_model, _ = FHIR_AllergyIntolerance_note.objects.get_or_create(AllergyIntolerance=allergy_model)
            note_model.text=cleaned_data['text']
            note_model.save()


            if reaction_model:
                FHIR_AllergyIntolerance_reaction_manifestation.objects.filter(AllergyIntolerance_reaction=reaction_model).delete()
                manifestation_cc_list = [
                    cleaned_data.get('manifestation_cc_1'),
                    cleaned_data.get('manifestation_cc_2'),
                    cleaned_data.get('manifestation_cc_3')
                ]
                for manifestation_cc in manifestation_cc_list:
                    if manifestation_cc:
                        manifestation_model = FHIR_AllergyIntolerance_reaction_manifestation(AllergyIntolerance_reaction=reaction_model)
                        manifestation_model.save()
                        manifestation_model.manifestation_cc.set([manifestation_cc])

        return allergy_model

    def __init__(self, *args, allergy_model=None, **kwargs):
        super().__init__(*args, **kwargs)
        if allergy_model:
            self.fields['code_cc'].initial = allergy_model.code_cc.first()
            self.fields['type_cc'].initial = allergy_model.type_cc.first()
            print(allergy_model.onset_dateTime, allergy_model.recordedDate)
            self.fields['onset_dateTime'].initial = allergy_model.onset_dateTime
            self.fields['recordedDate'].initial = allergy_model.recordedDate
            note_model = FHIR_AllergyIntolerance_note.objects.filter(AllergyIntolerance=allergy_model).first()
            if note_model:
                self.fields['text'].initial = note_model.text
            reaction_model = FHIR_AllergyIntolerance_reaction.objects.filter(AllergyIntolerance=allergy_model).first()
            if reaction_model:
                self.fields['severity'].initial = reaction_model.severity
                manifestation_model_list = FHIR_AllergyIntolerance_reaction_manifestation.objects.filter(AllergyIntolerance_reaction=reaction_model)[:3]
                for fieldnum, manifestation_model in zip(range(1, 4), manifestation_model_list):
                    self.fields['manifestation_cc_'+str(fieldnum)].initial = manifestation_model.manifestation_cc.first()
