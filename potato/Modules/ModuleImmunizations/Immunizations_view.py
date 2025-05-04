from django.shortcuts import render, get_object_or_404
from potato.models import (
    FHIR_Immunization,
    FHIR_Patient
)
from .Immunizations_form import Immunization_Combined_Form

def immunization_overview(request, patient_id):
    patient_model = get_object_or_404(FHIR_Patient, id=patient_id)
    immunization_model_list = FHIR_Immunization.objects.filter(patient=patient_model)
    return render(request, 'Immunizations_overview.html', {'patient': patient_model, 'immunizations': immunization_model_list})

def immunization_existing(request, patient_id, immunization_id):
    patient_model = get_object_or_404(FHIR_Patient, id=patient_id)
    existing_immunization_model = get_object_or_404(FHIR_Immunization, id=immunization_id)
    context = {'patient_id': patient_id, 'immunization_id': immunization_id}
    
    if request.method == 'GET':
        context['immunization_form'] = Immunization_Combined_Form(immunization_model=existing_immunization_model)
    else:
        context['save_result'] = "Save_Failed"
        immunization_form_bound = Immunization_Combined_Form(request.POST)
        if immunization_form_bound.is_valid():
            existing_immunization_model = immunization_form_bound.save(
                immunization_model=existing_immunization_model,
                patient_model=patient_model
            )
            context['save_result'] = "Save_Success"
        context['immunization_form'] = immunization_form_bound
    return render(request, 'Immunizations_form.html', context)

def immunization_new(request, patient_id):
    patient_model = get_object_or_404(FHIR_Patient, id=patient_id)
    context = {'patient_id': patient_id}
    
    if request.method == 'GET':
        context['immunization_form'] = Immunization_Combined_Form()
    else:
        immunization_form_bound = Immunization_Combined_Form(request.POST)
        context['save_result'] = "Save_Failed"
        if immunization_form_bound.is_valid():
            new_immunization_model = immunization_form_bound.save(patient_model=patient_model)
            context['immunization_id'] = new_immunization_model.id
            context['save_result'] = "Save_Success"
        context['immunization_form'] = immunization_form_bound

    return render(request, 'Immunizations_form.html', context)