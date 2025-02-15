from django.shortcuts import render
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_Resources.Patient import FHIR_Patient
from ..FHIR_Resources.AllergyIntolerance import FHIR_AllergyIntolerance, FHIR_AllergyIntolerance_Note, FHIR_AllergyIntolerance_Reaction, FHIR_AllergyIntolerance_Reaction_Manifestation, FHIR_AllergyIntolerance_Reaction_Note
from .form_addAllergyIntolerance import AllergyIntoleranceForm, NoteForm, ReactionForm, Reaction_NoteForm, ManifestationForm
from django.http import HttpResponse
from django.urls import reverse

#base page -> get list of old allergies, also button to get new allergy
#get new allergy -> empty forms, no specific allergy in database
#post new allergy -> (if saved) form for this specific allergy; (if not valid/saved, same forms with errors)
#get old allergy -> bound forms, hidden input for id
#post old allergy -> (if saved) form for this specific allergy; (if not valid/saved, same form with errors)

def allergy_intolerance(request, id):
    patient_model = FHIR_Patient.objects.filter(id=id).first()
    if not patient_model:
        return HttpResponse("patient not found " + str(id))
    
    context = {
        'patient': patient_model,
        'allergy_list': FHIR_AllergyIntolerance.objects.filter(patient=patient_model),
    }

    if request.method == 'GET':
        return render(request, 'allergy_overview.html', context)

def allergy_form_allergy_row(request, allergy_id):
    allergy = FHIR_AllergyIntolerance.objects.get(id=allergy_id)
    return render(request, 'allergy_table_row.html', {'allergy': allergy})

def allergy_form_get_new(request, patient_id):
    patient_model = FHIR_Patient.objects.filter(id=patient_id).first()
    if not patient_model:
        return HttpResponse("patient not found " + str(patient_id))
    allergy_form = AllergyIntoleranceForm()
    note_form = NoteForm()
    manifestation_form1 = ManifestationForm(prefix="manifestation1")
    manifestation_form2 = ManifestationForm(prefix="manifestation2")
    manifestation_form3 = ManifestationForm(prefix="manifestation3")

    return render(request, 'allergy_form.html', {
        'patient_id': patient_id,
        'allergy_form': allergy_form,
        'note_form': note_form,
        'allergy_name': "New Allergy/Intolerance",
        'manifestation_form1': manifestation_form1,
        'manifestation_form2': manifestation_form2,
        'manifestation_form3': manifestation_form3,
    })

def allergy_form_save_new(request, patient_id):
    if request.method == 'POST':
        # Create new instances
        allergy_model = FHIR_AllergyIntolerance.objects.create(patient_id=patient_id)
        reaction_model = FHIR_AllergyIntolerance_Reaction.objects.create(allergy_intolerance=allergy_model)
        note_model = FHIR_AllergyIntolerance_Note.objects.create(allergy_intolerance=allergy_model)
        
        manifestations = [
            FHIR_AllergyIntolerance_Reaction_Manifestation.objects.create(reaction=reaction_model)
            for _ in range(3)
        ]
        
        # Create forms with POST data
        allergy_form = AllergyIntoleranceForm(request.POST, instance=allergy_model)
        note_form = NoteForm(request.POST, instance=note_model)
        manifestation_forms = [
            ManifestationForm(request.POST, instance=manifestation, prefix=f'manifestation{i + 1}')
            for i, manifestation in enumerate(manifestations)
        ]
        
        all_valid = True
        fading_resp = f'''text-white font-semibold p-2 m-2 rounded w-64" hx-get="{reverse('empty')}" hx-trigger="load" hx-swap="outerHTML swap:5s'''
        saveResult = f'''<p class="fade-me-out bg-green-600 {fading_resp}">Allergy created successfully</p>'''
        for form in [allergy_form, note_form] + manifestation_forms:
            if not form.is_valid():
                all_valid = False
                saveResult = f'''<p class="fade-me-out bg-red-600 {fading_resp}">Error on form, not saved</p>'''        
        
        allergy_name = "New Allergy/Intolerance"
        if all_valid:
            allergy_model = allergy_form.save()
            allergy_name = str(allergy_model)
            note_form.save()
            for manifestation_form in manifestation_forms:
                manifestation_form.save()

            allergy_form = AllergyIntoleranceForm(instance=allergy_model)
        
        return render(request, 'allergy_form.html', {
            'saveResult': saveResult,
            'allergy_id': allergy_model.id,
            'allergy_name': allergy_name,
            'allergy_form': allergy_form,
            'note_form': note_form,
            'manifestation_form1': manifestation_forms[0],
            'manifestation_form2': manifestation_forms[1],
            'manifestation_form3': manifestation_forms[2],
        })


def allergy_form_get_existing(request, allergy_id):
    allergy_model = FHIR_AllergyIntolerance.objects.get(id=allergy_id)
    reaction_model = allergy_model.reactions.first()
    note_model = allergy_model.notes.first()
    manifestations = []
    if reaction_model:
        manifestations = reaction_model.manifestations.all()[:3]
    print(allergy_id, allergy_model.id, allergy_model.code_cc.all())
    allergy_form = AllergyIntoleranceForm(instance=allergy_model)
    note_form = NoteForm(instance=note_model)
    manifestation_form1 = ManifestationForm(instance=manifestations[0] if len(manifestations) > 0 else None, prefix="manifestation1")
    manifestation_form2 = ManifestationForm(instance=manifestations[1] if len(manifestations) > 1 else None, prefix="manifestation2")
    manifestation_form3 = ManifestationForm(instance=manifestations[2] if len(manifestations) > 2 else None, prefix="manifestation3")

    return render(request, 'allergy_form.html', {
        'allergy_id': allergy_id,
        'allergy_form': allergy_form,
        'allergy_name': str(allergy_model),
        'note_form': note_form,
        'manifestation_form1': manifestation_form1,
        'manifestation_form2': manifestation_form2,
        'manifestation_form3': manifestation_form3,
    })

def allergy_form_save_existing(request, allergy_id):
    if request.method == 'POST':
        print(request.POST)
        allergy_model = FHIR_AllergyIntolerance.objects.get(id=allergy_id)
        if not allergy_model.reactions.exists():
            reaction_model = FHIR_AllergyIntolerance_Reaction.objects.create(allergy_intolerance=allergy_model)
        else:
            reaction_model = allergy_model.reactions.first()
        note_model = allergy_model.notes.first() if allergy_model.notes.exists() else None

        # Create the forms with the POST data
        allergy_form = AllergyIntoleranceForm(request.POST, instance=allergy_model)
        #reaction_form = ReactionForm(request.POST, instance=reaction_model)
        note_form = NoteForm(request.POST, instance=note_model)

        while reaction_model.manifestations.count() < 3:
            FHIR_AllergyIntolerance_Reaction_Manifestation.objects.create(reaction=reaction_model)

        manifestation_models = reaction_model.manifestations.all()
        manifestation_forms = [
            ManifestationForm(request.POST, instance=manifestation_model, prefix=f'manifestation{i + 1}')
            for i, manifestation_model in enumerate(manifestation_models[:3])
        ]
        
        all_valid = True
        fading_resp = f'''text-white font-semibold p-2 m-2 rounded w-64" hx-get="{reverse('empty')}" hx-trigger="load" hx-swap="outerHTML swap:5s'''
        saveResult = f'''<p class="fade-me-out bg-green-600 {fading_resp}">Allergy updated successfully</p>'''
        for form in [allergy_form, note_form] + manifestation_forms:
            if not form.is_valid():
                all_valid = False
                saveResult = f'''<p class="fade-me-out bg-red-600 {fading_resp}">Error on form, not saved</p>'''
        if all_valid:
            allergy_model = allergy_form.save()
            note_form.save()
            for manifestation_form in manifestation_forms:
                manifestation_form.save()

            allergy_form = AllergyIntoleranceForm(instance=allergy_model)

        return render(request, 'allergy_form.html', {
            'saveResult': saveResult,
            'allergy_id': allergy_id,
            'allergy_name': str(allergy_model),
            'allergy_form': allergy_form,
            'note_form': note_form,
            'manifestation_form1': manifestation_forms[0],
            'manifestation_form2': manifestation_forms[1],
            'manifestation_form3': manifestation_forms[2],
        })


def allergy_activeSearch_code_cc(request):
    query = "e"
    results = FHIR_GP_Coding.objects.filter(
        binding__binding_rule=FHIR_AllergyIntolerance.BINDING_RULE_CODE,
        display__icontains=query,
        code__icontains=query
    )
    return render(request, 'allergy_datalist.html', {'results': results})