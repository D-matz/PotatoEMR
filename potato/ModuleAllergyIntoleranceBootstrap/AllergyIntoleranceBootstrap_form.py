from django import forms
from django.forms.widgets import Select
from django.utils.safestring import mark_safe
from ..FHIR_DataTypes.FHIR_generalpurpose import FHIR_GP_Coding
from potato.FHIR_Resources.AllergyIntolerance import (
    FHIR_AllergyIntolerance,
    FHIR_AllergyIntolerance_Reaction,
    FHIR_AllergyIntolerance_Reaction_Manifestation,
    FHIR_AllergyIntolerance_Note
)


class AllergyIntoleranceForm(forms.ModelForm):
    code_cc = forms.ModelChoiceField(
        queryset=FHIR_GP_Coding.objects.filter(binding__binding_rule=FHIR_AllergyIntolerance.BINDING_RULE_CODE).order_by('display', 'code'),
        widget=forms.Select(attrs={
            'class': 'form-select tomselect',
            'data-plugins': 'remove_button',
            'autocomplete': 'off',
            'data-allow-empty': 'true'
        })
    )
    type_cc = forms.ModelChoiceField(
        queryset=FHIR_GP_Coding.objects.filter(binding__binding_rule=FHIR_AllergyIntolerance.BINDING_RULE_TYPE).order_by('display', 'code'),
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'})
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)        
        if self.instance:
            first_code = self.instance.code_cc.first()
            if first_code:
                self.initial['code_cc'] = first_code.pk
            first_type = self.instance.type_cc.first()
            if first_type:
                self.initial['type_cc'] = first_type.pk

    class Meta:
        model = FHIR_AllergyIntolerance
        fields = ['code_cc', 'type_cc', 'onset_dateTime', 'recordedDate']
        widgets = {
            'onset_dateTime': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control form-control-sm'}),
            'recordedDate': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control form-control-sm'}),
        }
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            instance.code_cc.clear()
            instance.type_cc.clear()
            instance.code_cc.add(self.cleaned_data['code_cc'])
            instance.type_cc.add(self.cleaned_data['type_cc'])
        return instance

class AllergyIntoleranceReactionForm(forms.ModelForm):
    class Meta:
        model = FHIR_AllergyIntolerance_Reaction
        fields = ['severity']
        widgets = {
            'severity': forms.Select(attrs={'class': 'form-control form-control-sm'}),
        }

class AllergyIntoleranceReactionManifestationForm(forms.ModelForm):
    manifestation_cc = forms.ModelChoiceField(
        required=False,
        queryset=FHIR_GP_Coding.objects.filter(binding__binding_rule=FHIR_AllergyIntolerance_Reaction_Manifestation.BINDING_RULE_MANIFESTATION).order_by('display', 'code'),
        widget=forms.Select(attrs={'class': 'form-select tomselect', 'data-plugins': 'remove_button', 'autocomplete': 'off', 'data-allow-empty': 'true'})
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            first_manifestation = self.instance.manifestation_cc.first()
            if first_manifestation:
                self.initial['manifestation_cc'] = first_manifestation.pk

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            instance.manifestation_cc.clear()
            instance.manifestation_cc.add(self.cleaned_data['manifestation_cc'])
        return instance
    
    class Meta:
        model = FHIR_AllergyIntolerance_Reaction_Manifestation
        fields = ['manifestation_cc']


class AllergyIntoleranceNoteForm(forms.ModelForm):
    class Meta:
        model = FHIR_AllergyIntolerance_Note
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3, 'class': 'form-control border-2'}),
        }