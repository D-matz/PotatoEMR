from django import forms
from ..models_dir.FHIR_DataTypes.FHIR_generalpurpose import FHIR_GP_Coding
from potato.models_dir.FHIR_Resources.Location import *
from potato.models_dir.FHIR_Resources.Practitioner import *
from potato.models_dir.FHIR_Resources.Appointment import *

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
            practitioner_roles__location=args[0].get('Location')
        ).distinct()

        self.fields['Practitioner'] = forms.ModelChoiceField(
            queryset=practitioners,
            widget=forms.Select(),
            empty_label=None,
        )
