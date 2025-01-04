from django.shortcuts import render, redirect
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_Resources.Patient import FHIR_Patient
from .form_addAllergyIntolerance import AllergyIntoleranceForm, AllergyIntoleranceReactionForm, AllergyIntoleranceNoteForm

def allergy_intolerance(request, id):
    patient_model = FHIR_Patient.objects.filter(id=id).first()
    if not patient_model:
        return render(request, '404.html', status=404)

    if request.method == 'POST':
        allergy_form = AllergyIntoleranceForm(request.POST)
        reaction_form = AllergyIntoleranceReactionForm(request.POST)
        note_form = AllergyIntoleranceNoteForm(request.POST)
        
        if all([allergy_form.is_valid(), reaction_form.is_valid(), note_form.is_valid()]):
            allergy = allergy_form.save(commit=False)
            allergy.patient = patient_model
            allergy.save()
            
            if reaction_form.has_changed():
                reaction = reaction_form.save(commit=False)
                reaction.allergy_intolerance = allergy
                reaction.save()
                
            if note_form.has_changed():
                note = note_form.save(commit=False)
                note.allergy_intolerance = allergy
                note.save()
                
            return redirect('patient_overview', id=id)
    else:
        allergy_form = AllergyIntoleranceForm()
        reaction_form = AllergyIntoleranceReactionForm()
        note_form = AllergyIntoleranceNoteForm()
    
    context = {
        'patient': patient_model,
        'allergy_form': allergy_form,
        'reaction_form': reaction_form,
        'note_form': note_form,
    }
    
    return render(request, 'form_addAllergyIntolerance.html', context)
