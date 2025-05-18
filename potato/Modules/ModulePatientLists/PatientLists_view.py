from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from potato.models import (
    FHIR_Patient, FHIR_Condition, FHIR_Practitioner,
    FHIR_List, FHIR_List_entry
)
from potato.Common.PatientSearch.CommonPatientSearch_form import PatientSearchForm
#simplest list is just a list of patients
#title, and each entry has an item_Patient
#user chooses arbitrary patients to add, which only affects the list

#altrnatively, list defined by relation
#in which case add/remove affects database

def render_patient_list(request, list_model, editing=False):
    data_list = []
    if list_model:
        patients_list = list_model.get_patients()
        for patient in patients_list:
            conditions = FHIR_Condition.objects.filter(subject_Patient=patient)
            data_list.append({
                "patient": patient,
                "conditions": conditions
            })
    return render(request, "PatientLists.html", {
        "data_list": data_list,
        "list_model": list_model,
        "sidebar_lists": FHIR_List.objects.all(),
        "editing": editing
    })

def create_patient_list(request):
    test = FHIR_List.objects.create()
    return render_patient_list(request, test)

def get_patient_list(request, list_id):
    test = get_object_or_404(FHIR_List, id=list_id)    
    return render_patient_list(request, test)

def lists(request):
    if FHIR_List.objects.count() == 0: 
        return render_patient_list(request, None)
    return get_patient_list(request, FHIR_List.objects.first().id)

def edit_title(request, list_id):
    if request.method == "POST":
        return saved_title(request, list_id)
    list_model = get_object_or_404(FHIR_List, id=list_id)
    return render_patient_list(request, list_model, editing=True)

def saved_title(request, list_id):
    list_model = get_object_or_404(FHIR_List, id=list_id)
    list_model.title = request.POST.get("title")
    list_model.save()
    return render_patient_list(request, list_model)

def delete_list(request, list_id):
    list_model = get_object_or_404(FHIR_List, id=list_id)
    list_model.delete()
    return lists(request)

def searchModal(request, list_id):
    list_model = get_object_or_404(FHIR_List, id=list_id)
    return render(request, "PatientLists_searchModal.html", {
        "list_model": list_model,
        "form": PatientSearchForm()
    })

def remove_patient(request, list_id, patient_id):
    list_model = get_object_or_404(FHIR_List, id=list_id)
    FHIR_List_entry.objects.filter(List=list_model, item_Patient=patient_id).delete()
    return render_patient_list(request, list_model)

def add_patient(request, list_id, patient_id):
    list_model = get_object_or_404(FHIR_List, id=list_id)
    patient = get_object_or_404(FHIR_Patient, id=patient_id)
    if not FHIR_List_entry.objects.filter(List=list_model, item_Patient=patient).exists():
        FHIR_List_entry.objects.create(
            List=list_model,
            item_Patient=patient
        )
    return render_patient_list(request, list_model)
