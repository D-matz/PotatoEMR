from django.shortcuts import render, redirect
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_Resources.Patient import FHIR_Patient
from ..FHIR_Resources.AllergyIntolerance import FHIR_AllergyIntolerance, FHIR_AllergyIntolerance_Note, FHIR_AllergyIntolerance_Reaction, FHIR_AllergyIntolerance_Reaction_Manifestation, FHIR_AllergyIntolerance_Reaction_Note
from django.http import HttpResponse
from django.urls import reverse
from .AllergyIntoleranceBootstrap_form import AllergyIntoleranceForm, AllergyIntoleranceReactionForm, AllergyIntoleranceReactionManifestationForm, AllergyIntoleranceNoteForm


def patient_allergies(request, patient_id, return_html):
    print("allergy_intolerance", patient_id)
    patient_model = FHIR_Patient.objects.filter(id=patient_id).first()
    if not patient_model:
        return HttpResponse("patient not found " + str(patient_id))

    for allergy in FHIR_AllergyIntolerance.objects.filter(patient=patient_model):
        if allergy.reactions.first():
            ms = allergy.reactions.first().manifestations.all()
            print("allergy", allergy.code_cc.first(), ms)
            for m in ms:
                print("m", m.manifestation_cc.first())
    return render(request, return_html, {
        'patient': patient_model,
        'allergy_list': FHIR_AllergyIntolerance.objects.filter(patient=patient_model),
    })

def allergy_intolerance_overview(request, patient_id):
    return patient_allergies(request, patient_id, 'AllergyIntoleranceBootstrap_overview.html')

def allergy_intolerance_table(request, patient_id):
    return patient_allergies(request, patient_id, 'AllergyIntoleranceBootstrap_table.html')


def allergy_intolerance_new(request, patient_id):
    form = AllergyIntoleranceForm()
    #todo
    return render(request, 'AllergyIntoleranceBootstrap_form.html', {'form': form})

def allergy_intolerance_existing(request, patient_id, allergy_id):
    print("allergy_intolerance_existing")
    allergy_model = FHIR_AllergyIntolerance.objects.filter(id=allergy_id).first()
    if not allergy_model:
        return HttpResponse("allergy not found " + str(allergy_id))

    context = {
        'allergy': allergy_model,
        'patient_id': patient_id,
        'allergy_id': allergy_id,
    }

    if request.method == 'GET':
        note_model = allergy_model.notes.first()
        if not note_model:
            note_model = allergy_model.notes.create()
        reaction_model = allergy_model.reactions.first()
        if not reaction_model:
            reaction_model = allergy_model.reactions.create()
        print("!!!", allergy_model.notes.first())

        context['save_result'] = "Existing"
        context['allergy_form'] = AllergyIntoleranceForm(instance=allergy_model)
        context['note_form'] = AllergyIntoleranceNoteForm(instance=note_model)
        context['reaction_form'] = AllergyIntoleranceReactionForm(instance=reaction_model)
        context['manifestation_forms'] = []
        manifestation_count = 0

        # Go through all reactions until we find at least 3 manifestations
        for reaction in allergy_model.reactions.all():
            for manifestation_model in reaction.manifestations.all():
                prefix = f"m{manifestation_count}"
                form = AllergyIntoleranceReactionManifestationForm(
                    instance=manifestation_model,
                    prefix=prefix
                )
                context['manifestation_forms'].append(form)
                manifestation_count += 1
                if manifestation_count >= 3:
                    break
            if manifestation_count >= 3:
                break

        while len(context['manifestation_forms']) < 3:
            prefix = f"m{manifestation_count}"
            form = AllergyIntoleranceReactionManifestationForm(prefix=prefix)
            context['manifestation_forms'].append(form)
            manifestation_count += 1

    elif request.method == 'POST':
        context['save_result'] = "Save_Success"
        print("POST")
        print(request.POST)
        allergy_form = AllergyIntoleranceForm(instance=allergy_model, data=request.POST)
        if allergy_form.is_valid():
            allergy_form.save()
        else:
            context['save_result'] = "Save_Failed"
            print("save failed 1")
        print("allergy_model saved", allergy_model, allergy_model.id, allergy_model.code_cc.all(), "type", allergy_model.type_cc.all())
        context['allergy_form'] = allergy_form
        print("save to???", allergy_model.notes.first())
        note_form = AllergyIntoleranceNoteForm(instance=allergy_model.notes.first(), data=request.POST)
        if note_form.is_valid():
            note_form.save()
        else:
            context['save_result'] = "Save_Failed"
            print("save failed 2")
        context['note_form'] = note_form
        reaction_form = AllergyIntoleranceReactionForm(instance=allergy_model.reactions.first(), data=request.POST)
        if reaction_form.is_valid():
            reaction_form.save()
        else:
            context['save_result'] = "Save_Failed"
            print("save failed 3", reaction_form.errors)
        context['reaction_form'] = reaction_form

        manifestation_forms = []
        if allergy_form.is_valid():
            reaction = allergy_model.reactions.first() or FHIR_AllergyIntolerance_Reaction.objects.create(allergy_intolerance=allergy_model)
            reaction.save()

            # Get existing manifestations or create new ones as needed
            manifestations = list(reaction.manifestations.all())
            while len(manifestations) < 3:
                manifestations.append(FHIR_AllergyIntolerance_Reaction_Manifestation(reaction=reaction))

            for i in range(3):
                manifestation_form = AllergyIntoleranceReactionManifestationForm(
                    prefix=f"m{i}",
                    instance=manifestations[i],
                    data=request.POST
                )
                if manifestation_form.is_valid():
                    manifestation_form.save()
                else:
                    context['save_result'] = "Save_Failed"
                    print("save failed 4")

                manifestation_forms.append(manifestation_form)
        context['manifestation_forms'] = manifestation_forms

    return render(request, 'AllergyIntoleranceBootstrap_form.html', context)
