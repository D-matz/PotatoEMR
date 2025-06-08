from django.shortcuts import render, get_object_or_404
from potato.models import FHIR_DocumentReference, FHIR_Patient
from .Notes_form import (DocumentReferenceForm, 
    DocumentReferenceContentForm, save_document_reference)

def _notes_get_patient_notes(patient_id):
    """Get patient and their document references (notes)"""
    patient = get_object_or_404(FHIR_Patient, id=patient_id)
    # Link notes to patient through context_Encounter which has subject_Patient
    # This will get notes that are associated with encounters for this patient
    notes = FHIR_DocumentReference.objects.filter(context_Encounter__subject_Patient=patient).distinct()
    for note in notes:
        note.content_preview = ""
        if note.DocumentReference_content.count() > 0:
            if note.DocumentReference_content.first().attachment:
                wholenote = str(note.DocumentReference_content.first().attachment.data)
                note.content_preview = wholenote[:100]
                if len(wholenote) > 100:
                    note.content_preview += "..."
    return patient, notes

def _notes_create_formlist(note=None):
    """Create a list of note forms"""
    content_model = None
    if note:
        content_model_list = note.DocumentReference_content.all()
        if content_model_list.count() > 0:
            content_model = content_model_list.first()
    return [
        DocumentReferenceForm(instance=note if note else None),
        DocumentReferenceContentForm(instance=content_model)
    ]

def _notes_post_forms(patient, post_data, note=None):
    """Take POST data from new or existing note and try to save form"""
    content_model = None
    if note:
        content_model_list = note.DocumentReference_content.all()
        if content_model_list.count() > 0:
            content_model = content_model_list.first()
    
    forms = {
        'document_reference_form': DocumentReferenceForm(post_data, instance=note),
        'document_reference_content_form': DocumentReferenceContentForm(post_data, instance=content_model)
    }
    formlist = list(forms.values())
    
    if not all(form.is_valid() for form in formlist):
        print("form errors")
        for form in formlist:
            print(form.errors)
        return (False, note, formlist)
    else:
        note = save_document_reference(
            document_reference_form=forms['document_reference_form'],
            document_reference_content_form=forms['document_reference_content_form'],
            patient_model=patient
        )
        return (True, note, formlist)

def notes_table(request, patient_id):
    patient, notes = _notes_get_patient_notes(patient_id)
    return render(request, 'Notes_table.html', {
        'notes': notes,
        'patient': patient
    })

def notes_new(request, patient_id):
    patient = get_object_or_404(FHIR_Patient, id=patient_id)
    if request.method == 'GET':
        formlist = _notes_create_formlist()
        patient, notes = _notes_get_patient_notes(patient_id)
        return render(request, 'Notes_table.html', {
            'notes': notes,
            'patient': patient,
            'formlist': formlist,
            'moreInfo_fragment': 'Notes_edit_new'
        })
    
    elif request.method == 'POST':
        valid, note, formlist = _notes_post_forms(patient, request.POST)
        patient, notes = _notes_get_patient_notes(patient_id)
        if valid:
            return render(request, 'Notes_table.html', {
                'notes': notes,
                'patient': patient,
                'note': note,
                'formlist': formlist,
                'moreInfo_fragment': 'Notes_edit_existing'
            })
        else:
            return render(request, 'Notes_table.html', {
                'notes': notes,
                'patient': patient,
                'formlist': formlist,
                'moreInfo_fragment': 'Notes_edit_new'
            })

def notes_existing_edit(request, patient_id, note_id):
    note = get_object_or_404(FHIR_DocumentReference, id=note_id)
    patient = get_object_or_404(FHIR_Patient, id=patient_id)
    
    if request.method == 'GET':
        formlist = _notes_create_formlist(note)
        patient, notes = _notes_get_patient_notes(patient_id)
        return render(request, 'Notes_table.html', {
            'notes': notes,
            'formlist': formlist,
            'note': note,
            'patient': patient,
            'moreInfo_fragment': 'Notes_edit_existing'
        })
    
    elif request.method == 'POST':
        valid, note, formlist = _notes_post_forms(patient, request.POST, note)
        patient, notes = _notes_get_patient_notes(patient_id)
        if valid:
            return render(request, 'Notes_table.html', {
                'notes': notes,
                'note': note,
                'patient': patient,
                'formlist': formlist,
                'moreInfo_fragment': 'Notes_edit_existing'
            })
        else:
            return render(request, 'Notes_table.html', {
                'notes': notes,
                'formlist': formlist,
                'note': note,
                'patient': patient,
                'moreInfo_fragment': 'Notes_edit_existing'
            })

def notes_existing_cancel(request, patient_id, note_id):
    patient, notes = _notes_get_patient_notes(patient_id)
    note = get_object_or_404(FHIR_DocumentReference, id=note_id)
    formlist = _notes_create_formlist(note)
    return render(request, 'Notes_table.html', {
        'notes': notes,
        'note': note,
        'patient': patient,
        'formlist': formlist,
        'moreInfo_fragment': 'Notes_edit_existing'
    }) 