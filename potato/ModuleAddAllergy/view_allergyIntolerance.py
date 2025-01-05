from django.shortcuts import render, redirect
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_Resources.Patient import FHIR_Patient
from .form_addAllergyIntolerance import AddAllergyIntoleranceForm

def allergy_intolerance(request, id):
    patient_model = FHIR_Patient.objects.filter(id=id).first()
    if not patient_model:
        return render(request, '404.html', status=404)

    if request.method == 'POST':
        allergy_form = AddAllergyIntoleranceForm(request.POST)    
        return redirect('patient_overview', id=id)
    else:
        allergy_form = AddAllergyIntoleranceForm()
    
    context = {
        'patient': patient_model,
        'allergy_form': allergy_form,
    }
    
    return render(request, 'form_addAllergyIntolerance.html', context)
