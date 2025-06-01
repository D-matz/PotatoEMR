from django.shortcuts import render, get_object_or_404
from potato.models import (
    FHIR_Patient,
    FHIR_ServiceRequest,
    FHIR_MedicationRequest,
    FHIR_DiagnosticReport
)
from .orders_medicationRequest_form import MedicationRequestForm, MedicationRequestNoteForm, save_medication_request

def orders_table(request, patient_id):
    patient = get_object_or_404(FHIR_Patient, id=patient_id)
    medication_requests = FHIR_MedicationRequest.objects.filter(subject_Patient=patient)
    return render(request, 'orders_table.html', {
        'medication_requests': medication_requests,
        'patient': patient
    })

def medicationRequest_new(request, patient_id):
    patient = get_object_or_404(FHIR_Patient, id=patient_id)
    
    if request.method == 'GET':
        med_request_form = MedicationRequestForm()
        note_form = MedicationRequestNoteForm()
        return render(request, 'orders_row_edit_new.html', {
            'med_request_form': med_request_form,
            'note_form': note_form,
            'patient': patient
        })
    
    elif request.method == 'POST':
        med_request_form = MedicationRequestForm(request.POST)
        note_form = MedicationRequestNoteForm(request.POST)
        if med_request_form.is_valid() and note_form.is_valid():
            med_request = save_medication_request(med_request_form, note_form, patient_model=patient)
            return render(request, 'orders_row_normal.html', {
                'med_request': med_request,
                'patient': patient
            })
        else:
            return render(request, 'orders_row_edit_new.html', {
                'med_request_form': med_request_form,
                'note_form': note_form,
                'patient': patient
            })

def medicationRequest_existing_edit(request, patient_id, med_request_id):
    patient = get_object_or_404(FHIR_Patient, id=patient_id)
    med_request = get_object_or_404(FHIR_MedicationRequest, id=med_request_id)
    
    if request.method == 'GET':
        med_request_form = MedicationRequestForm(instance=med_request)
        note_form = MedicationRequestNoteForm(instance=med_request.MedicationRequest_note.first())
        return render(request, 'orders_row_edit_existing.html', {
            'med_request_form': med_request_form,
            'note_form': note_form,
            'med_request': med_request,
            'patient': patient
        })
    
    elif request.method == 'POST':
        med_request_form = MedicationRequestForm(request.POST, instance=med_request)
        note_form = MedicationRequestNoteForm(request.POST)
        if med_request_form.is_valid() and note_form.is_valid():
            med_request = save_medication_request(med_request_form, note_form, med_request_model=med_request)
            return render(request, 'orders_row_normal.html', {
                'med_request': med_request,
                'patient': patient
            })
        else:
            return render(request, 'orders_row_edit_existing.html', {
                'med_request_form': med_request_form,
                'note_form': note_form,
                'med_request': med_request,
                'patient': patient
            })

def medicationRequest_existing_cancel(request, patient_id, med_request_id):
    patient = get_object_or_404(FHIR_Patient, id=patient_id)
    med_request = get_object_or_404(FHIR_MedicationRequest, id=med_request_id)
    return render(request, 'orders_row_normal.html', {
        'med_request': med_request,
        'patient': patient
    })
