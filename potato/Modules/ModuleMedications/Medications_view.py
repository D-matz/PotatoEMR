from django.shortcuts import render, get_object_or_404
from potato.models import (
    FHIR_Patient,
    FHIR_MedicationAdministration,
    FHIR_MedicationDispense
)
#funny thing about FHIR administration vs dispense is dosage is different:
#   administration has backbone element with its own fields
#   dispense has dosage element from the Dosage datatype
#another little difference is administration only has 1 MedicationRequest reference
#whereas dispense has many MedicationRequest references
from .Medications_dispense_form import (
    MedicationDispenseForm, MedicationDispenseNoteForm,
    MedicationDispenseDosageForm, MedicationDispenseQuantityForm,
    save_medication_dispense
)
from .Medications_administration_form import (
    MedicationAdministrationForm, MedicationAdministrationNoteForm,
    MedicationAdministrationDosageForm,
    save_medication_administration
)

def medication_table(request, patient_id):
    #defualt to medications adminstered tab, also have a dispense tab
    #kind of duplicated urls/views/forms/templates for both
    return medication_administration_table(request, patient_id)

def _medication_administration_create_formlist(med_admin=None):
    """Create a list of medication administration forms, which are used to display and save chosen fields.
    If med_admin is provided, creates bound forms. Otherwise creates unbound forms."""
    return [
        MedicationAdministrationForm(instance=med_admin if med_admin else None),
        MedicationAdministrationNoteForm(instance=med_admin.MedicationAdministration_note.first() if med_admin else None),
        MedicationAdministrationDosageForm(instance=med_admin.MedicationAdministration_dosage.first() if med_admin else None)
    ]

def _medication_administration_post_forms(patient, post_data, med_admin=None):
    """Take POST data from new or existing med admin and try to save form
    Return if form valid, med admin model, and list of forms"""
    forms = {
        'med_admin_form': MedicationAdministrationForm(post_data, instance=med_admin),
        'note_form': MedicationAdministrationNoteForm(post_data, instance=med_admin.MedicationAdministration_note.first() if med_admin else None),
        'dosage_form': MedicationAdministrationDosageForm(post_data, instance=med_admin.MedicationAdministration_dosage.first() if med_admin else None)
    }
    formlist = list(forms.values())
    if not all(form.is_valid() for form in formlist):
        return (False, med_admin, formlist)
    else:
        med_admin = save_medication_administration(
            med_admin_form=forms['med_admin_form'],
            note_form=forms['note_form'],
            dosage_form=forms['dosage_form'],
            patient_model=patient
        )
        return (True, med_admin, formlist)

def medication_administration_table(request, patient_id):
    patient = get_object_or_404(FHIR_Patient, id=patient_id)
    medicationAdministration_list = FHIR_MedicationAdministration.objects.filter(subject_Patient=patient)
    
    label_formlist = _medication_administration_create_formlist()
    formlist_list = [_medication_administration_create_formlist(med_admin) 
                     for med_admin in medicationAdministration_list]
    
    return render(request, 'medication_table_administration.html', {
        'medAdmin_and_form': zip(medicationAdministration_list, formlist_list),
        'patient': patient,
        'label_formlist': label_formlist
    })

def medicationAdministration_new(request, patient_id):
    patient = get_object_or_404(FHIR_Patient, id=patient_id)
    
    if request.method == 'GET':
        formlist = _medication_administration_create_formlist()
        return render(request, 'medication_table_administration_row_edit_new.html', {
            'formlist': formlist,
            'patient': patient
        })
    
    elif request.method == 'POST':
        valid, med_admin, formlist = _medication_administration_post_forms(patient, request.POST)
        if valid:
            return render(request, 'medication_table_administration_row_normal.html', {
                'med_admin': med_admin,
                'patient': patient,
                'formlist': formlist
            })
        else:
            return render(request, 'medication_table_administration_row_edit_new.html', {
                'formlist': formlist,
                'patient': patient
            })

def medicationAdministration_existing_edit(request, patient_id, med_admin_id):
    patient = get_object_or_404(FHIR_Patient, id=patient_id)
    med_admin = get_object_or_404(FHIR_MedicationAdministration, id=med_admin_id)
    
    if request.method == 'GET':
        formlist = _medication_administration_create_formlist(med_admin)
        return render(request, 'medication_table_administration_row_edit_existing.html', {
            'formlist': formlist,
            'med_admin': med_admin,
            'patient': patient
        })
    
    elif request.method == 'POST':
        valid, med_admin, formlist = _medication_administration_post_forms(patient, request.POST, med_admin)
        if valid:
            return render(request, 'medication_table_administration_row_normal.html', {
                'med_admin': med_admin,
                'patient': patient,
                'formlist': formlist
            })
        else:
            return render(request, 'medication_table_administration_row_edit_existing.html', {
                'formlist': formlist,
                'med_admin': med_admin,
                'patient': patient
            })

def medicationAdministration_existing_cancel(request, patient_id, med_admin_id):
    patient = get_object_or_404(FHIR_Patient, id=patient_id)
    med_admin = get_object_or_404(FHIR_MedicationAdministration, id=med_admin_id)
    formlist = _medication_administration_create_formlist(med_admin)
    return render(request, 'medication_table_administration_row_normal.html', {
        'med_admin': med_admin,
        'patient': patient,
        'formlist': formlist
    })

# a lot of commonality between medicationDispense and medicationAdministration
# but just duplicating everything for now
# probably bad, means duplicate forms, urls, views, templates

def _medication_dispense_create_formlist(med_dispense=None):
    """Create a list of medication dispense forms, which are used to display and save chosen fields.
    If med_dispense is provided, creates bound forms. Otherwise creates unbound forms."""
    return [
        MedicationDispenseForm(instance=med_dispense if med_dispense else None),
        MedicationDispenseQuantityForm(instance=med_dispense.quantity if med_dispense else None),
        MedicationDispenseNoteForm(instance=med_dispense.MedicationDispense_note.first() if med_dispense else None),
        MedicationDispenseDosageForm(instance=med_dispense.MedicationDispense_dosageInstruction.first() if med_dispense else None)
    ]

def _medication_dispense_post_forms(patient, post_data, med_dispense=None):
    """Take POST data from new or existing med dispense and try to save form
    Return if form valid, med dispense model, and list of forms"""
    forms = {
        'med_dispense_form': MedicationDispenseForm(post_data, instance=med_dispense),
        'quantity_form': MedicationDispenseQuantityForm(post_data, instance=med_dispense.quantity if med_dispense else None),
        'note_form': MedicationDispenseNoteForm(post_data, instance=med_dispense.MedicationDispense_note.first() if med_dispense else None),
        'dosage_form': MedicationDispenseDosageForm(post_data, instance=med_dispense.MedicationDispense_dosageInstruction.first() if med_dispense else None)
    }
    formlist = list(forms.values())
    if not all(form.is_valid() for form in formlist):
        return (False, med_dispense, formlist)
    else:
        med_dispense = save_medication_dispense(
            med_dispense_form=forms['med_dispense_form'],
            quantity_form=forms['quantity_form'],
            note_form=forms['note_form'],
            dosage_form=forms['dosage_form'],
            patient_model=patient
        )
        return (True, med_dispense, formlist)

def medication_dispense_table(request, patient_id):
    patient = get_object_or_404(FHIR_Patient, id=patient_id)
    medicationDispsense_list = FHIR_MedicationDispense.objects.filter(subject_Patient=patient)
    
    label_formlist = _medication_dispense_create_formlist()
    formlist_list = [_medication_dispense_create_formlist(med_dispense) 
                     for med_dispense in medicationDispsense_list]

    return render(request, 'medication_table_dispense.html', {
        'medDispense_and_form': zip(medicationDispsense_list, formlist_list),
        'patient': patient,
        'label_formlist': label_formlist
    })

def medicationDispense_new(request, patient_id):
    patient = get_object_or_404(FHIR_Patient, id=patient_id)
    
    if request.method == 'GET':
        formlist = _medication_dispense_create_formlist()
        return render(request, 'medication_table_dispense_row_edit_new.html', {
            'formlist': formlist,
            'patient': patient
        })
    
    elif request.method == 'POST':
        valid, med_dispense, formlist = _medication_dispense_post_forms(patient, request.POST)
        if valid:
            return render(request, 'medication_table_dispense_row_normal.html', {
                'med_dispense': med_dispense,
                'patient': patient,
                'formlist': formlist
            })
        else:
            return render(request, 'medication_table_dispense_row_edit_new.html', {
                'formlist': formlist,
                'patient': patient
            })

def medicationDispense_existing_edit(request, patient_id, med_dispense_id):
    patient = get_object_or_404(FHIR_Patient, id=patient_id)
    med_dispense = get_object_or_404(FHIR_MedicationDispense, id=med_dispense_id)
    
    if request.method == 'GET':
        formlist = _medication_dispense_create_formlist(med_dispense)
        return render(request, 'medication_table_dispense_row_edit_existing.html', {
            'formlist': formlist,
            'med_dispense': med_dispense,
            'patient': patient
        })
    
    elif request.method == 'POST':
        valid, med_dispense, formlist = _medication_dispense_post_forms(patient, request.POST, med_dispense)
        if valid:
            return render(request, 'medication_table_dispense_row_normal.html', {
                'med_dispense': med_dispense,
                'patient': patient,
                'formlist': formlist
            })
        else:
            return render(request, 'medication_table_dispense_row_edit_existing.html', {
                'formlist': formlist,
                'med_dispense': med_dispense,
                'patient': patient
            })

def medicationDispense_existing_cancel(request, patient_id, med_dispense_id):
    patient = get_object_or_404(FHIR_Patient, id=patient_id)
    med_dispense = get_object_or_404(FHIR_MedicationDispense, id=med_dispense_id)
    formlist = _medication_dispense_create_formlist(med_dispense)
    return render(request, 'medication_table_dispense_row_normal.html', {
        'med_dispense': med_dispense,
        'patient': patient,
        'formlist': formlist
    })

