from django.shortcuts import render, redirect
from potato.models import (
    FHIR_Patient,
    FHIR_AllergyIntolerance
)
from django.shortcuts import get_object_or_404
from .AllergyIntoleranceBootstrap_form import AllergyIntolerance_Combined_Form

def patient_allergies(request, patient_id, return_html):
    patient_model = get_object_or_404(FHIR_Patient, id=patient_id)
    return render(request, return_html, {
        'patient': patient_model,
        'allergy_list': FHIR_AllergyIntolerance.objects.filter(patient=patient_model),
    })

def allergy_intolerance_overview(request, patient_id):
    return patient_allergies(request, patient_id, 'AllergyIntoleranceBootstrap_overview.html')

def allergy_intolerance_new(request, patient_id):
    patient_model = get_object_or_404(FHIR_Patient, id=patient_id)
    context = {'patient_id': patient_id}
    if request.method == 'GET':
        context['allergy_form'] = AllergyIntolerance_Combined_Form()
    else:
        allergy_form_bound = AllergyIntolerance_Combined_Form(request.POST)
        context['save_result'] = "Save_Failed"
        if allergy_form_bound.is_valid():
            #TODO should probably set recorder practitioner model to user
            new_allergy_model = allergy_form_bound.save(patient_model=patient_model)
            #this save creates new allergy and other models
            context['allergy_id'] = new_allergy_model.id
            #the template knows this is now an existing allergy rather than new, because it has an allergy is
            context['save_result'] = "Save_Success"
        context['allergy_form'] = allergy_form_bound

    return render(request, 'AllergyIntoleranceBootstrap_form.html', context)

def allergy_intolerance_existing(request, patient_id, allergy_id):
    patient_model = get_object_or_404(FHIR_Patient, id=patient_id)
    existing_allergy_model = get_object_or_404(FHIR_AllergyIntolerance, id=allergy_id)
    context = {'patient_id': patient_id, 'allergy_id': allergy_id}
    if request.method == 'GET':
        context['allergy_form'] = AllergyIntolerance_Combined_Form(allergy_model=existing_allergy_model)
    else:
        context['save_result'] = "Save_Failed"
        allergy_form_bound = AllergyIntolerance_Combined_Form(request.POST)
        if allergy_form_bound.is_valid():
            #TODO should probably set recorder practitioner model to user
            existing_allergy_model = allergy_form_bound.save(allergy_model=existing_allergy_model, patient_model=patient_model)
            #this save overwrites existing allergy and other models
            context['save_result'] = "Save_Success"
        context['allergy_form'] = allergy_form_bound
    return render(request, 'AllergyIntoleranceBootstrap_form.html', context)
