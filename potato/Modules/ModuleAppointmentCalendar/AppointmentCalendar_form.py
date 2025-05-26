from django import forms
from potato.models import (
    FHIR_Location,
    FHIR_Practitioner,
)

class ApptClndrForm(forms.Form):
    Date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    Location = forms.ModelChoiceField(
        queryset=FHIR_Location.objects.all(),
        widget=forms.Select(),
        empty_label=None,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #practitioner list depends on the chosen location
        practitioners = FHIR_Practitioner.objects.filter(
            PractitionerRole_practitioner__location=args[0].get('Location')
        ).distinct()
        
        if practitioners.exists():
            self.fields['Practitioner'] = forms.ModelChoiceField(
                queryset=practitioners,
                widget=forms.Select(),
                empty_label=None,
            )
        else:
            self.add_error('Location', f'No practitioners working at this location')