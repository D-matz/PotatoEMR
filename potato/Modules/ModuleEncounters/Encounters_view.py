from django.shortcuts import render, get_object_or_404
from potato.models import FHIR_Encounter, FHIR_Patient, FHIR_DocumentReference
from .Encounters_form import (EncounterForm, 
    EncounterParticipantForm, DocumentReferenceForm, 
    DocumentReferenceContentForm, save_encounter)

def _encounter_get_patient_encounters(patient_id):
    """Get patient and encounters,
    and add the first note associated with each encounter"""
    patient = get_object_or_404(FHIR_Patient, id=patient_id)
    encounters = FHIR_Encounter.objects.filter(subject_Patient=patient)
    for encounter in encounters:
        encounter.note = ""
        if encounter.DocumentReference_context.count() > 0:
            if encounter.DocumentReference_context.first().DocumentReference_content.count() > 0:
                if encounter.DocumentReference_context.first().DocumentReference_content.first().attachment:
                    wholenote = str(encounter.DocumentReference_context.first().DocumentReference_content.first().attachment.data)
                    encounter.note = wholenote[:10]
                    if len(wholenote) > 10:
                        encounter.note += "..."
    return patient, encounters

def _encounter_create_formlist(encounter=None):
    """Create a list of encounter forms, which are used to display and save chosen fields.
    If encounter is provided, creates bound forms. Otherwise creates unbound forms."""
    DocumentReference_model = None
    DocumentReference_content_model = None
    DocumentReference_model_list = FHIR_DocumentReference.objects.filter(context_Encounter=encounter)
    if DocumentReference_model_list.count() > 0:
        DocumentReference_model = DocumentReference_model_list.first()
        DocumentReference_content_model_list = DocumentReference_model.DocumentReference_content.all()
        if DocumentReference_content_model_list.count() > 0:
            DocumentReference_content_model = DocumentReference_content_model_list.first()
    return [
        EncounterForm(instance=encounter if encounter else None),
        EncounterParticipantForm(instance=encounter.Encounter_participant.first() if encounter else None),
        DocumentReferenceForm(instance=DocumentReference_model),
        DocumentReferenceContentForm(instance=DocumentReference_content_model)
    ]

def _encounter_post_forms(patient, post_data, encounter=None):
    """Take POST data from new or existing encounter and try to save form
    Return if form valid, encounter model, and list of forms"""
    DocumentReference_model = None
    DocumentReference_content_model = None
    DocumentReference_model_list = FHIR_DocumentReference.objects.filter(context_Encounter=encounter)
    if DocumentReference_model_list.count() > 0:
        DocumentReference_model = DocumentReference_model_list.first()
        DocumentReference_content_model_list = DocumentReference_model.DocumentReference_content.all()
        if DocumentReference_content_model_list.count() > 0:
            DocumentReference_content_model = DocumentReference_content_model_list.first()
    forms = {
        'encounter_form': EncounterForm(post_data, instance=encounter),
        'participant_form': EncounterParticipantForm(post_data, instance=encounter.Encounter_participant.first() if encounter else None),
        'document_reference_form': DocumentReferenceForm(post_data, instance=DocumentReference_model),
        'document_reference_content_form': DocumentReferenceContentForm(post_data, instance=DocumentReference_content_model)
    }
    formlist = list(forms.values())
    print("post forms")
    if not all(form.is_valid() for form in formlist):
        print("form errors")
        for form in formlist:
            print(form.errors)
        print("end of form errors")
        return (False, encounter, formlist)
    else:
        encounter = save_encounter(
            encounter_form=forms['encounter_form'],
            participant_form=forms['participant_form'],
            document_reference_form=forms['document_reference_form'],
            document_reference_content_form=forms['document_reference_content_form'],
            patient_model=patient
        )
        return (True, encounter, formlist)

def encounters_table(request, patient_id):
    patient, encounters = _encounter_get_patient_encounters(patient_id)
    return render(request, 'Encounters_table.html', {
        'encounters': encounters,
        'patient': patient
    })

def encounters_new(request, patient_id):
    #these all replace whole table each time (rather than just the individual form)
    #point is to update table if encounter was added or edited
    #so it needs to pass list of patient encounter in
    #_encounter_post_forms can save encounter, so need to get list after that
    patient = get_object_or_404(FHIR_Patient, id=patient_id) #do need patient now though to post form on patient
    if request.method == 'GET':
        formlist = _encounter_create_formlist()
        patient, encounters = _encounter_get_patient_encounters(patient_id)
        return render(request, 'Encounters_table.html', {
            'encounters': encounters,
            'patient': patient,
            'formlist': formlist,
            'moreInfo_fragment': 'Encounters_edit_new'
        })
    
    elif request.method == 'POST':
        valid, encounter, formlist = _encounter_post_forms(patient, request.POST)
        patient, encounters = _encounter_get_patient_encounters(patient_id)
        if valid:
            return render(request, 'Encounters_table.html', {
                'encounters': encounters,
                'patient': patient,
                'encounter': encounter,
                'formlist': formlist,
                'moreInfo_fragment': 'Encounters_edit_existing'
            })
        else:
            return render(request, 'Encounters_table.html', {
                'encounters': encounters,
                'patient': patient,
                'formlist': formlist,
                'moreInfo_fragment': 'Encounters_edit_new'
            })

def encounters_existing_edit(request, patient_id, encounter_id):
    encounter = get_object_or_404(FHIR_Encounter, id=encounter_id)
    patient = get_object_or_404(FHIR_Patient, id=patient_id)
    
    if request.method == 'GET':
        formlist = _encounter_create_formlist(encounter)
        patient, encounters = _encounter_get_patient_encounters(patient_id)
        print(formlist)
        return render(request, 'Encounters_table.html', {
            'encounters': encounters,
            'formlist': formlist,
            'encounter': encounter,
            'patient': patient,
            'moreInfo_fragment': 'Encounters_edit_existing'
        })
    
    elif request.method == 'POST':
        valid, encounter, formlist = _encounter_post_forms(patient, request.POST, encounter)
        #get encounters again here because a new or edit encounter just posted
        patient, encounters = _encounter_get_patient_encounters(patient_id)
        if valid:
            return render(request, 'Encounters_table.html', {
                'encounters': encounters,
                'encounter': encounter,
                'patient': patient,
                'formlist': formlist,
                'moreInfo_fragment': 'Encounters_edit_existing'
            })
        else:
            return render(request, 'Encounters_table.html', {
                'encounters': encounters,
                'formlist': formlist,
                'encounter': encounter,
                'patient': patient,
                'moreInfo_fragment': 'Encounters_edit_existing'
            })
        
def encounters_existing_cancel(request, patient_id, encounter_id):
    patient, encounters = _encounter_get_patient_encounters(patient_id)
    encounter = get_object_or_404(FHIR_Encounter, id=encounter_id)
    formlist = _encounter_create_formlist(encounter)
    return render(request, 'Encounters_table.html', {
        'encounters': encounters,
        'encounter': encounter,
        'patient': patient,
        'formlist': formlist,
        'moreInfo_fragment': 'Encounters_edit_existing'
    })


