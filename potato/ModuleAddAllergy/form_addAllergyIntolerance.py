from django import forms
from django.forms import inlineformset_factory
from ..FHIR_Resources.AllergyIntolerance import FHIR_AllergyIntolerance, FHIR_AllergyIntolerance_Reaction, FHIR_AllergyIntolerance_Reaction_Manifestation, FHIR_AllergyIntolerance_Note, FHIR_AllergyIntolerance_Reaction_Note

class AddAllergyIntoleranceForm(forms.ModelForm):
    class Meta:
        model = FHIR_AllergyIntolerance
        fields = [
            'clinical_status_cc',
            'verification_status_cc', 
            'type_cc',
            'category_codes',
            'criticality_code',
            'code_cc',
            'onset_dateTime',
            'recordedDate',
            'lastOccurrence',
        ]
        #leaving participant alone for now, needs reference to practitioner, org, etc models

class NoteForm(forms.ModelForm):
    class Meta:
        model = FHIR_AllergyIntolerance_Note
        fields = [
            'text',
        ]

# Create an inline formset for notes
NoteFormSet = inlineformset_factory(
    FHIR_AllergyIntolerance,
    FHIR_AllergyIntolerance_Note,
    form=NoteForm,
    extra=4,  # Number of empty forms to display
)

class ReactionForm(forms.ModelForm):
    class Meta:
        model = FHIR_AllergyIntolerance_Reaction
        fields = [
            'substance_cc',
            'description',
            'onset',
            'severity',
            'exposureRoute_cc',
        ]

class ReactionNoteForm(forms.ModelForm):
    class Meta:
        model = FHIR_AllergyIntolerance_Reaction_Note
        fields = [
            'text',
        ]

class ManifestationForm(forms.ModelForm):
    class Meta:
        model = FHIR_AllergyIntolerance_Reaction_Manifestation
        fields = [
            'manifestation_cc',
        ]
