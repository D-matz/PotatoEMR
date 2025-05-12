from django.shortcuts import render, redirect
from django.http import HttpResponse
from potato.models import FHIR_Patient, FHIR_Condition, FHIR_Practitioner

def lists(request):
    patients = FHIR_Patient.objects.all()
    
    data_list = []
    for patient in patients:
        conditions = FHIR_Condition.objects.filter(subject_Patient=patient)
        print("conditions: ", conditions)
        data_list.append({
            "patient": patient,
            "conditions": conditions
        })
    return render(request, "PatientLists.html", {"data_list": data_list})

def lists_practitioner(request, practitioner_name):
        
    practitioner = FHIR_Practitioner.objects.filter(Practitioner_name__text__contains=practitioner_name).first()
    if practitioner:
        patients = FHIR_Patient.objects.filter(generalPractitioner_Practitioner=practitioner)
    else:
        return HttpResponse("Practitioner not found")

    data_list = []
    for patient in patients:
        conditions = FHIR_Condition.objects.filter(subject_Patient=patient)
        print("conditions: ", conditions)
        data_list.append({
            "patient": patient,
            "conditions": conditions
        })
    return render(request, "PatientLists.html", {"data_list": data_list})
