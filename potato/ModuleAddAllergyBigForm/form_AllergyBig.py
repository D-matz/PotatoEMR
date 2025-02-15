from django import forms
from ..FHIR_Resources.AllergyIntolerance import FHIR_AllergyIntolerance, FHIR_AllergyIntolerance_Reaction, FHIR_AllergyIntolerance_Reaction_Manifestation, FHIR_AllergyIntolerance_Note, FHIR_AllergyIntolerance_Reaction_Note
from ..FHIR_DataTypes.FHIR_generalpurpose import FHIR_GP_Coding
from datetime import datetime

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

class AllergyIntoleranceForm(forms.ModelForm):
    class Meta:
        model = FHIR_AllergyIntolerance
        fields = [
            'code_cc', 'category_codes', 'type_cc', 
            'verification_status_cc', 'clinical_status_cc', 
            'criticality_code', 'onset_dateTime', 'lastOccurrence'
        ]
        widgets = {
            'code_cc': forms.Select(attrs=common_widget_attrs),
            'category_codes': forms.Select(attrs=common_widget_attrs),
            'type_cc': forms.Select(attrs=common_widget_attrs),
            'verification_status_cc': forms.Select(attrs=common_widget_attrs),
            'clinical_status_cc': forms.Select(attrs=common_widget_attrs),
            'criticality_code': forms.Select(attrs=common_widget_attrs),
            'onset_dateTime': forms.DateTimeInput(attrs=datetime_widget_attrs),
            'lastOccurrence': forms.DateTimeInput(attrs=datetime_widget_attrs),
        }
    code_cc = forms.ModelChoiceField(
        queryset=FHIR_GP_Coding.objects.filter(binding__binding_rule='https://www.hl7.org/fhir/valueset-allergyintolerance-code.html'),
        required=True,
        label="Code",
        widget=forms.Select(attrs=longer_widget_attrs),
    )
    category_codes = forms.ModelChoiceField(
        queryset=FHIR_GP_Coding.objects.filter(binding__binding_rule='https://www.hl7.org/fhir/valueset-allergy-intolerance-category.html'),
        required=False,
        label="Category",
        widget=forms.Select(attrs=common_widget_attrs),
    )
    type_cc = forms.ModelChoiceField(
        queryset=FHIR_GP_Coding.objects.filter(binding__binding_rule='https://www.hl7.org/fhir/valueset-allergy-intolerance-type.html'),
        required=False,
        label="Allergy/Intolerance",
        widget=forms.Select(attrs=common_widget_attrs),
    )
    verification_status_cc = forms.ModelChoiceField(
        queryset=FHIR_GP_Coding.objects.filter(binding__binding_rule='https://www.hl7.org/fhir/valueset-allergyintolerance-verification.html'),
        required=False,
        label="Verification",
        widget=forms.Select(attrs=common_widget_attrs),
    )
    clinical_status_cc = forms.ModelChoiceField(
        queryset=FHIR_GP_Coding.objects.filter(binding__binding_rule='https://www.hl7.org/fhir/valueset-allergyintolerance-clinical.html'),
        required=False,
        label="Clinical Status",
        widget=forms.Select(attrs=common_widget_attrs),
    )
    criticality_code = forms.ModelChoiceField(
        queryset=FHIR_GP_Coding.objects.filter(binding__binding_rule='https://www.hl7.org/fhir/valueset-allergy-intolerance-criticality.html'),
        required=False,
        label="Criticality",
        widget=forms.Select(attrs=common_widget_attrs),
    )

    onset_dateTime = forms.DateTimeField(
        required=False,
        label="Onset",
        widget=forms.DateTimeInput(attrs=datetime_widget_attrs),
    )
    lastOccurrence = forms.DateTimeField(
        required=False,
        label="Last Occurrence",
        widget=forms.DateTimeInput(attrs=datetime_widget_attrs),
    )
        #leaving participant alone for now, needs reference to practitioner, org, etc models
    def is_valid(self):
        print("valid?")
        ret = super().is_valid()
        verification_result = self.cleaned_data.get('verification_status_cc')
        if verification_result == None:
            self.add_error('verification_status_cc', 'Error: Verification must be Confirmed')
            ret = False
        elif verification_result.display != "Confirmed":
            self.add_error('verification_status_cc', 'Error: Verification must be Confirmed')
            ret = False
        return ret
    def save(self, parent):
        allergy_model = super().save(commit=False)
        allergy_model.patient = parent
        allergy_model.save()
        allergy_model.verification_status_cc.add(self.cleaned_data.get('verification_status_cc'))
        allergy_model.type_cc.add(self.cleaned_data.get('type_cc'))
        allergy_model.category_codes.add(self.cleaned_data.get('category_codes'))
        allergy_model.code_cc.add(self.cleaned_data.get('code_cc'))
        allergy_model.clinical_status_cc.add(self.cleaned_data.get('clinical_status'))
        allergy_model.criticality_code.add(self.cleaned_data.get('criticality_code'))
        allergy_model.save()
        return allergy_model

class NoteForm(forms.ModelForm):
    class Meta:
        model = FHIR_AllergyIntolerance_Note
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'rows': 4,
                'style': 'resize: both;',
                'placeholder': 'This note must start with "zzz"'
            }),
        }
    def is_valid(self):
        valid = super().is_valid()
        text = self.cleaned_data.get('text', '')
        if not text.startswith('zzz'):
            self.add_error('text', 'Error: Text must start with "zzz"')
            return False
        return valid
    
    def save(self, parent):
        print("save note")
        note = super().save(commit=False)
        note.allergy_intolerance = parent
        note.save()
        self.save_m2m()
        return note

    
class ReactionForm(forms.ModelForm):
    substance_cc = forms.ModelChoiceField(
        queryset=FHIR_GP_Coding.objects.filter(binding__binding_rule='https://www.hl7.org/fhir/valueset-substance-code.html'),
        required=False,
        label="Substance",
        widget=forms.Select(attrs=common_widget_attrs),
    )
    severity = forms.ModelChoiceField(
        queryset=FHIR_GP_Coding.objects.filter(binding__binding_rule='https://www.hl7.org/fhir/valueset-reaction-event-severity.html'),
        required=False,
        label="Severity",
        widget=forms.Select(attrs=common_widget_attrs),
    )
    exposureRoute_cc = forms.ModelChoiceField(
        queryset=FHIR_GP_Coding.objects.filter(binding__binding_rule='https://www.hl7.org/fhir/valueset-route-codes.html'),
        required=False,
        label="Exposure Route",
        widget=forms.Select(attrs=common_widget_attrs),
    )
    onset = forms.DateTimeField(
        required=False,
        label="Onset",
        widget=forms.DateTimeInput(attrs=datetime_widget_attrs),
    )
    description = forms.CharField(
        required=False,
        label="Description",
        widget=forms.TextInput(attrs=input_widget_attrs)
    )
    class Meta:
        model = FHIR_AllergyIntolerance_Reaction
        fields = [
            'substance_cc',
            'description',
            'onset',
            'severity',
            'exposureRoute_cc',
        ]
    def save(self, parent):
        reaction = super().save(commit=False)
        reaction.allergy_intolerance = parent
        reaction.save()
        reaction.substance_cc.add(self.cleaned_data.get('substance_cc'))
        reaction.exposureRoute_cc.add(self.cleaned_data.get('exposureRoute_cc'))
        reaction.save()
        return reaction
    
class ReactionNoteForm(forms.ModelForm):
    class Meta:
        model = FHIR_AllergyIntolerance_Reaction_Note
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'rows': 4,
                'style': 'resize: both;',
                'placeholder': "This note must include the name of at least one manifestation of this reaction"
            }),
        }
    def save(self, parent):
        reactionForm = super().save(commit=False)
        reactionForm.reaction = parent
        reactionForm.save()
        self.save_m2m()
        return reactionForm
    
class ManifestationForm(forms.ModelForm):
    manifestation_cc = forms.ModelChoiceField(
        queryset=FHIR_GP_Coding.objects.filter(binding__binding_rule='https://www.hl7.org/fhir/valueset-clinical-findings.html'),
        required=False,
        label="Clinical Finding",
        widget=forms.Select(attrs=longer_widget_attrs),
    )
    class Meta:
        model = FHIR_AllergyIntolerance_Reaction_Manifestation
        fields = [
            'manifestation_cc',
        ]
    def save(self, parent):
        manifestation = super().save(commit=False)
        print("HELLO", self.cleaned_data.get('manifestation_cc'))
        manifestation.reaction = parent
        manifestation.save()
        if self.cleaned_data.get('manifestation_cc'):
            manifestation.manifestation_cc.set([self.cleaned_data['manifestation_cc']])
        return manifestation
