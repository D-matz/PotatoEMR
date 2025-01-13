from django.shortcuts import render, redirect
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_Resources.Patient import FHIR_Patient
from .form_addAllergyIntolerance import AddAllergyIntoleranceForm, ReactionForm, ManifestationForm, NoteForm, ReactionNoteForm, NoteFormSet
from django.http import HttpResponse
from django.db import transaction

def allergy_intolerance(request, id):
    patient_model = FHIR_Patient.objects.filter(id=id).first()
    if not patient_model:
        return HttpResponse("patient not found " + id)

    if request.method == 'POST':
        allergy_form = AddAllergyIntoleranceForm(request.POST, prefix='allergy')
        reaction_form = ReactionForm(request.POST, prefix='reaction')
        manifestation_form = ManifestationForm(request.POST, prefix='manifestation')
        note_form = NoteForm(request.POST, prefix='note')
        reaction_note_form = ReactionNoteForm(request.POST, prefix='reaction_note')
        note_formset = NoteFormSet(request.POST, instance=allergy_form.instance)
        print("note formset", note_formset)
        print("form errors?",allergy_form.errors)
        if allergy_form.is_valid() and reaction_form.is_valid() and manifestation_form.is_valid() and note_form.is_valid() and reaction_note_form.is_valid():
            print("valid form",allergy_form.cleaned_data)
            print("patient", patient_model)
            with transaction.atomic():
                allergy = allergy_form.save(commit=False)
                allergy.patient = patient_model
                allergy.save()
                note = note_form.save(commit=False)
                note.allergy_intolerance = allergy
                note.save()
                print("normal?", note)
                reaction = reaction_form.save(commit=False)
                reaction.allergy_intolerance = allergy
                reaction.save()
                manifestation = manifestation_form.save(commit=False)
                manifestation.reaction = reaction
                manifestation.save()
                reaction_note = reaction_note_form.save(commit=False)
                reaction_note.reaction = reaction
                reaction_note.save()
                print("reaction?", reaction_note)
            return redirect('patient_overview', id=patient_model.id)
        context = {
            'patient': patient_model,
            'allergy_form': allergy_form,
            'reaction_form': reaction_form,
            'manifestation_form': manifestation_form,
            'note_form': note_form,
            'reaction_note_form': reaction_note_form,
            'errors': allergy_form.errors,
        }
        return render(request, 'form_addAllergyIntolerance.html', context)
    else:
        allergy_form = AddAllergyIntoleranceForm(prefix='allergy')
        reaction_form = ReactionForm(prefix='reaction')
        manifestation_form = ManifestationForm(prefix='manifestation')
        note_form = NoteForm(prefix='note')
        reaction_note_form = ReactionNoteForm(prefix='reaction_note')
        note_formset = NoteFormSet(prefix='note_formset')
        context = {
            'patient': patient_model,
            'allergy_form': allergy_form,
            'reaction_form': reaction_form,
            'manifestation_form': manifestation_form,
            'note_form': note_form,
            'reaction_note_form': reaction_note_form,
            'note_formset': note_formset,
        }
        
        return render(request, 'form_addAllergyIntolerance.html', context)

