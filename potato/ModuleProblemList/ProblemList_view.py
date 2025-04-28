from django.shortcuts import render, get_object_or_404
from ..models_dir.FHIR_DataTypes.FHIR_generalpurpose import *
from potato.models import *

def problem_list(request, patient_id):
    patient_model = get_object_or_404(FHIR_Patient, id=patient_id)
    condition_model_list = FHIR_Condition.objects.filter(subject_Patient=patient_model)
    return render(request, 'ProblemList_overview.html', {'patient': patient_model, 'conditions': condition_model_list})
