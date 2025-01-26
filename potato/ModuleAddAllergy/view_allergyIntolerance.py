from django.shortcuts import render, redirect
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_Resources.Patient import FHIR_Patient
from ..FHIR_Resources.AllergyIntolerance import FHIR_AllergyIntolerance, FHIR_AllergyIntolerance_Reaction, FHIR_AllergyIntolerance_Reaction_Manifestation, FHIR_AllergyIntolerance_Reaction_Note
from .form_addAllergyIntolerance import AllergyIntoleranceForm, ReactionForm, ManifestationForm, NoteForm, ReactionNoteForm
from django.http import HttpResponse
from django.db import transaction
from django.utils import timezone
from django.forms import inlineformset_factory
import json
from django.http import QueryDict

def listToQueryDict(input_list):
    qdict = QueryDict(mutable=True)
    for input in input_list:
        for name, value in input.items():
            if isinstance(value, list):
                #select can have multiple options selected
                #this is needed to avoid qdict being double bracket [[1, 2, 3]]
                for item in value:
                    qdict.appendlist(name, item)
            else:
                qdict[name] = value
    return qdict

def jsonToForms(formTypes, formData):
    thisFormName = formData["leaf"]["formName"]
    thisFormData = formData["leaf"]["formFields"]
    thisForm = formTypes[thisFormName](listToQueryDict(thisFormData)) #making a form from data, which django wants in queryset
    returnBoundFormAndChildren = {
        "leafBoundForm": thisForm,
        "valid": thisForm.is_valid(),
        "children": []
    }
    if "children" in formData:
        for child in formData["children"]:
            childRet = jsonToForms(formTypes, child)
            returnBoundFormAndChildren["children"].append(childRet)
            if not childRet["valid"]: returnBoundFormAndChildren["valid"] = False
    return returnBoundFormAndChildren

def saveAllModels(boundFormAndChildren, parent_model):
    thisModel = boundFormAndChildren["leafBoundForm"].save(parent=parent_model)
    returnAllSavedModels = {
        "leafSavedModel": thisModel,
        "children": []
    }
    for child in boundFormAndChildren["children"]:
        returnAllSavedModels["children"].append(saveAllModels(child, thisModel))
    return returnAllSavedModels


def formatForTemplate(boundFormAndChildren, thisFormType, formTypes):
    thisForm = boundFormAndChildren["leafBoundForm"]
    return_BoundFormAndChildren = {thisFormType + "_form" : thisForm}
    for child in boundFormAndChildren["children"]:
        childType = None
        for typeString, formClass in formTypes.items():
            if isinstance(child["leafBoundForm"], formClass):
                childType = typeString
                break
        if childType is None:
            print(child["leafBoundForm"] + " form type not in " + formTypes)

        child_BoundFormAndChildren = formatForTemplate(child, childType, formTypes)
        #we have a list of each child form type, add child to the right one
        childListName = childType + "_list"
        if childListName in return_BoundFormAndChildren:
            return_BoundFormAndChildren[childListName].append(child_BoundFormAndChildren)
        else:
            return_BoundFormAndChildren[childListName] = [child_BoundFormAndChildren]
    return return_BoundFormAndChildren

def allergy_intolerance(request, id):
    patient_model = FHIR_Patient.objects.filter(id=id).first()
    if not patient_model:
        return HttpResponse("patient not found " + id)

    #example with one form each
    #populates template starting data on get
    #also always used for template examples that must have forms, with no data in them

    #nested object more complicated then just passing each form into flat context
    #but it means we can use the same template+allergyFormAndChildren data structure
    #here and when we send back a POST form with errors
    example_allergyFormAndChildren = {
        "allergy_form": AllergyIntoleranceForm(),
        "note_list": [{"note_form": NoteForm()}],
        "reaction_list": [
            {
                "reaction_form": ReactionForm(),
                "manifestation_list": [{"manifestation_form": ManifestationForm()}],
                "reactionNote_list": [{"reactionNote_form": ReactionNoteForm()}]
            }
        ]
    }

    context = {
        'patient': patient_model,
        'allergy_list': FHIR_AllergyIntolerance.objects.filter(patient=patient_model),
        'allergyFormAndChildren': example_allergyFormAndChildren, #for GET we populate form with example, but for POST replace it with invalid submitted form
        'example_allergyFormAndChildren': example_allergyFormAndChildren,
    }


    #GET request just looks up patient allergy page
    if request.method == 'GET':
        return render(request, 'allergy_overview.html', context)
    else:
        #POST
        #to respond to POST send just page allergy_overview_content, don't need to refresh nav bar as well
        #the form is either populated with errors if invalid or set back to example form if submitted 

        allergyPostJSON = json.loads(request.body.decode('utf-8'))

        allergyFormTypes = {
            "allergy": AllergyIntoleranceForm,
            "note": NoteForm,
            "reaction": ReactionForm,
            "reactionNote": ReactionNoteForm,
            "manifestation": ManifestationForm,
        }

        #allergyFormTypes are the fieldset name/formtype pairs in this form, eg <fieldset data-nested:"reaction">
        #allergyPostJSON has structured form data
        #idk parent form maybe needed for validation
        #returns leafBoundForm, valid, children
        boundFormAndChildren = jsonToForms(formTypes=allergyFormTypes, formData=allergyPostJSON)
        boundFormsTemplateFormat = formatForTemplate(boundFormAndChildren=boundFormAndChildren, thisFormType="allergy", formTypes=allergyFormTypes)
        is_valid = boundFormAndChildren["valid"]
        
        allergy_codes = [boundFormsTemplateFormat['allergy_form'].cleaned_data.get('code_cc')] #[] because manyToMany field but single select form input
        if FHIR_AllergyIntolerance.objects.filter(
            patient=patient_model,
            code_cc__in=allergy_codes
        ).exists():
            is_valid = False
            boundFormsTemplateFormat['allergy_form'].add_error('code_cc', "Error: Allergy " + allergy_codes[0].display + " already exists for " + str(patient_model))

        for reaction in boundFormsTemplateFormat["reaction_list"]:
            manifestation_displays = []
            for manifestation in reaction['manifestation_list']:
                manifestation_cc = manifestation['manifestation_form'].cleaned_data.get('manifestation_cc')
                if manifestation_cc != None:
                    manifestation_displays.append(manifestation_cc.display)
            for reaction_note in reaction['reactionNote_list']:
                reaction_note_text =  reaction_note['reactionNote_form'].cleaned_data.get('text')
                text_contains_manifestation = False
                for md_ns in manifestation_displays:
                    if md_ns.lower().replace(" ", "") in reaction_note_text.lower().replace(" ", ""):
                        text_contains_manifestation = True
                        break
                if text_contains_manifestation == False:
                    is_valid = False
                    if len(manifestation_displays) == 0:
                        reaction_note['reactionNote_form'].add_error('text', "Error: The reaction note must mention a manifestation from this reaction. This reaction currently has no manifestations selected.")
                    else:
                        reaction_note['reactionNote_form'].add_error('text', "Error: The reaction note must mention a manifestation from this reaction: " + str(manifestation_displays))
        if not is_valid:
            #return bound form with errors
            context["allergyFormAndChildren"] = boundFormsTemplateFormat
            return render(request, 'allergy_overview_content.html', context)

        #form validated, save models and return page with new allergy
        saved_models = saveAllModels(boundFormAndChildren, patient_model)
        #actually seems like we don't need to get objects again for new allergy object, maybe since evaluated lazily, but here for clarity
        context["allergy_list"] = FHIR_AllergyIntolerance.objects.filter(patient=patient_model)
        return render(request, 'allergy_overview_content.html', context)
    
def allergy_intolerance_reactionDetail(request, allergy_id):
    allergy = FHIR_AllergyIntolerance.objects.get(id=allergy_id)
    print("allergy", allergy)
    return render(request, 'allergy_listItem_reactionInfo.html', {'allergy': allergy})