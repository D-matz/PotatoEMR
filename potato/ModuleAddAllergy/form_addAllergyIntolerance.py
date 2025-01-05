from django import forms
from ..FHIR_Codings import terminology_hl7_org_CodeSystem_allergyintolerance_clinical

class AddAllergyIntoleranceForm(forms.Form):
    clinical_status = forms.ChoiceField(choices=[(c['code'], c['display']) for c in terminology_hl7_org_CodeSystem_allergyintolerance_clinical.coding])
    

    category = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple())
    code = forms.CharField()
    onset_dateTime = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))