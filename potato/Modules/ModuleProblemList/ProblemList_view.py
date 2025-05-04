from django.shortcuts import render, get_object_or_404
from potato.models import (
    FHIR_Condition,
    FHIR_Patient
)
from .ProblemList_form import Condition_Combined_Form

def problem_list_overview(request, patient_id):
    patient_model = get_object_or_404(FHIR_Patient, id=patient_id)
    condition_model_list = FHIR_Condition.objects.filter(subject_Patient=patient_model)
    return render(request, 'ProblemList_overview.html', {'patient': patient_model, 'conditions': condition_model_list})

def problem_list_existing(request, patient_id, condition_id):
    condition_model = get_object_or_404(FHIR_Condition, id=condition_id)
    return render(request, 'ProblemList_existing.html', {'condition': condition_model})

def problem_list_existing(request, patient_id, condition_id):
    patient_model = get_object_or_404(FHIR_Patient, id=patient_id)
    existing_condition_model = get_object_or_404(FHIR_Condition, id=condition_id)
    context = {'patient_id': patient_id, 'condition_id': condition_id}
    if request.method == 'GET':
        context['condition_form'] = Condition_Combined_Form(condition_model=existing_condition_model)
    else:
        context['save_result'] = "Save_Failed"
        condition_form_bound = Condition_Combined_Form(request.POST)
        if condition_form_bound.is_valid():
            #TODO should probably set recorder practitioner model to user
            existing_condition_model = condition_form_bound.save(condition_model=existing_condition_model, patient_model=patient_model)
            #this save overwrites existing condition and other models
            context['save_result'] = "Save_Success"
        context['condition_form'] = condition_form_bound
    return render(request, 'ProblemList_form.html', context)


def problem_list_new(request, patient_id):
    patient_model = get_object_or_404(FHIR_Patient, id=patient_id)
    context = {'patient_id': patient_id}
    if request.method == 'GET':
        context['condition_form'] = Condition_Combined_Form()
    else:
        condition_form_bound = Condition_Combined_Form(request.POST)
        context['save_result'] = "Save_Failed"
        if condition_form_bound.is_valid():
            #TODO should probably set recorder practitioner model to user
            new_condition_model = condition_form_bound.save(patient_model=patient_model)
            #this save creates new condition and other models
            context['condition_id'] = new_condition_model.id
            #the template knows this is now an existing condition rather than new, because it has an condition is
            context['save_result'] = "Save_Success"
        context['condition_form'] = condition_form_bound

    return render(request, 'ProblemList_form.html', context)