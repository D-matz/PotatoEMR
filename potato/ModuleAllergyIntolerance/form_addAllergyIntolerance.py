from django import forms
from ..FHIR_Resources.AllergyIntolerance import FHIR_AllergyIntolerance, FHIR_AllergyIntolerance_Reaction, FHIR_AllergyIntolerance_Reaction_Manifestation, FHIR_AllergyIntolerance_Note, FHIR_AllergyIntolerance_Reaction_Note
from ..FHIR_DataTypes.FHIR_generalpurpose import FHIR_GP_Coding
from datetime import datetime
from django.utils.safestring import mark_safe

common_widget_attrs = {
    'class': 'w-32 m-1 bg-gray-100 border border-gray-300 rounded-md p-2'
}
longer_widget_attrs = {
    'class': 'w-48 m-1 bg-gray-100 border border-gray-300 rounded-md p-2'
}
datetime_widget_attrs = {
    'class': 'w-40 m-1 bg-gray-100 border border-gray-300 rounded-md p-2',  # Same as select
    'type': 'datetime-local',  # Ensures that the input is a datetime-local input type
}

input_widget_attrs = common_widget_attrs
input_widget_attrs['maxlength'] = '10000'

from django.template.loader import render_to_string
class AlpineSelectWidget(forms.Widget):
    def __init__(self, choice_values=['no values provided for this field'], field_width='w-full', attrs=None):
        super().__init__(attrs)
        self.choice_values = choice_values
        self.field_width = field_width
    
    def render(self, name, value, attrs=None, renderer=None):
        #could also passs in template name as argument but seems like giving you rope to hang yourself with
        return mark_safe(render_to_string('common_alpine_select.html', {
            'choice_values': self.choice_values,
            'initial_value': self.initial_value,
            'field_width': self.field_width
        }))




class AllergyIntoleranceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        super().__init__(*args, **kwargs)
        self.fields['code_cc'].widget.initial_value = ''
        if instance:
            if instance.code_cc.exists():
                self.fields['code_cc'].widget.initial_value = instance.code_cc.first().display        
        self.initial['code_cc'] = ''
        self.initial['criticality_code'] = ''
        if instance:
            if instance.code_cc.exists():
                self.initial['code_cc'] = instance.code_cc.first()
            self.initial['criticality_code'] = instance.criticality_code

    code_cc = forms.ModelChoiceField(
        label='Agent',
        queryset=FHIR_GP_Coding.objects.filter(binding__binding_rule=FHIR_AllergyIntolerance.BINDING_RULE_CODE).order_by('display', 'code'),
        widget=AlpineSelectWidget(field_width="w-80", choice_values=list(
            FHIR_GP_Coding.objects.filter(binding__binding_rule=FHIR_AllergyIntolerance.BINDING_RULE_CODE).order_by('display').values_list('display', flat=True))),
        required=False,
        to_field_name='display'
    )


    onset_dateTime = forms.DateTimeField(
        label='Onset',
        widget=forms.DateTimeInput(attrs={'class': 'w-full max-w-full', 'type': 'datetime-local'}),
        required=False
    )
    
    criticality_code = forms.ModelChoiceField(
        label='Severity',
        queryset=FHIR_GP_Coding.objects.filter(binding__binding_rule=FHIR_AllergyIntolerance.BINDING_RULE_CRITICALITY),
        widget=forms.Select(attrs={'class': 'w-full max-w-full'}),
        required=False,
    )


    type_cc = forms.ModelMultipleChoiceField(
        label='Reaction Type',
        queryset=FHIR_GP_Coding.objects.filter(binding__binding_rule=FHIR_AllergyIntolerance.BINDING_RULE_TYPE),
        widget=forms.SelectMultiple(attrs={'class': 'w-full max-w-full'}),
        required=False
    )

    class Meta:
        model = FHIR_AllergyIntolerance
        fields = [
            'code_cc', 'category_codes', 'type_cc', 
            'verification_status_cc', 'clinical_status_cc', 
            'criticality_code', 'onset_dateTime', 'lastOccurrence', 'recordedDate'
        ]

    def save(self):
        allergy = super().save(commit=False)
        allergy.code_cc.clear()
        allergy.recordedDate = datetime.now()
        if self.cleaned_data.get('code_cc'):
            coding = FHIR_GP_Coding.objects.filter(
                binding__binding_rule=FHIR_AllergyIntolerance.BINDING_RULE_CODE,
                display=self.cleaned_data['code_cc']
            ).first()
            print("coding is", coding)
            if coding:
                allergy.code_cc.set([coding])
        allergy.save()
        return allergy


class NoteForm(forms.ModelForm):
    text = forms.CharField(
        label='Comments',
        widget=forms.Textarea(attrs={'class': 'w-full h-40'})
    )    
    class Meta:
        model = FHIR_AllergyIntolerance_Note
        fields = ['text']

class ReactionForm(forms.ModelForm):
    class Meta:
        model = FHIR_AllergyIntolerance_Reaction
        fields = '__all__'

class ManifestationForm(forms.ModelForm):
    manifestation_cc = forms.ModelChoiceField(
        queryset=FHIR_GP_Coding.objects.filter(binding__binding_rule='https://www.hl7.org/fhir/valueset-clinical-findings.html'),
        required=False,
        to_field_name='code',
        widget=forms.Select()
    )



    class Meta:
        model = FHIR_AllergyIntolerance_Reaction_Manifestation
        fields = ['manifestation_cc']

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        super().__init__(*args, **kwargs)
        self.initial['manifestation_cc'] = ''
        if instance and instance.manifestation_cc.exists():
            self.initial['manifestation_cc'] = instance.manifestation_cc.first()

    def save(self):
        manifestation = super().save(commit=False)
        manifestation.save()
        manifestation.manifestation_cc.clear()
        if self.cleaned_data.get('manifestation_cc'):
            manifestation.manifestation_cc.set([self.cleaned_data['manifestation_cc']])
        return manifestation


class Reaction_NoteForm(forms.ModelForm):
    class Meta:
        model = FHIR_AllergyIntolerance_Reaction_Note
        fields = '__all__'
        