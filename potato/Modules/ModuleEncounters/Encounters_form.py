from django import forms
from django.db import transaction
from potato.models import (FHIR_Encounter, 
    FHIR_Encounter_participant, 
    FHIR_DocumentReference,
    FHIR_DocumentReference_content
)
from potato.models_dir.FHIR_DataTypes.FHIR_generalpurpose import FHIR_GP_Attachment
from potato.Common.Widgets.InputSingleFromMany import InputSingleFromMany
import base64
import hashlib

# Form for both the encounter and the associated note

class EncounterForm(forms.ModelForm):
    class Meta:
        model = FHIR_Encounter
        fields = ['status', 'priority_cc', 'subjectStatus_cc', 
                  #'episodeOfCare', 'partOf', 'serviceProvider',
                  'appointment', 'plannedStartDate',
                  'plannedEndDate'
                  #'account', 'length'
                  ]
        widgets = {
            'status': forms.Select(attrs={'class': 'form-select'}),
            'priority_cc': InputSingleFromMany(attrs={'class': 'form-select'}),
            'subjectStatus_cc': InputSingleFromMany(attrs={'class': 'form-select'}),
            #'episodeOfCare': InputSingleFromMany(attrs={'class': 'form-select'},),
            #'careTeam': InputSingleFromMany(attrs={'class': 'form-select'}),
            #'partOf': forms.Select(attrs={'class': 'form-select'}),
            #'serviceProvider': InputSingleFromMany(attrs={'class': 'form-select'}),
            'appointment': InputSingleFromMany(attrs={'class': 'form-select'}),
            'plannedStartDate': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'plannedEndDate': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            #'account': InputSingleFromMany(attrs={'class': 'form-select'}),
        }

class EncounterParticipantForm(forms.ModelForm):
    class Meta:
        model = FHIR_Encounter_participant
        fields = ['actor_Practitioner']
        widgets = {
            'actor_Practitioner': forms.Select(attrs={'class': 'form-select'}),
        }

class DocumentReferenceForm(forms.ModelForm):
    class Meta:
        model = FHIR_DocumentReference
        fields = [
            'date',
            'author_Practitioner'
        ]
        widgets = {
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'author_Practitioner': InputSingleFromMany(attrs={'class': 'form-select'}),
        }
        labels = {
            'date': 'Note Date',
            'author_Practitioner': 'Note Author',
        }

class DocumentReferenceContentForm(forms.ModelForm):
    # Add a custom text field for the note content
    note_text = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control', 
            'rows': 10,
            'placeholder': 'Enter note content here...'
        }),
        label='Note Content',
        required=False
    )
    
    class Meta:
        model = FHIR_DocumentReference_content
        fields = []  # We'll handle attachment creation manually
        labels = {
            'note_text': 'Note Content',
        }

def save_encounter(encounter_form, participant_form, document_reference_form, document_reference_content_form, patient_model=None, encounter_model=None):
    with transaction.atomic():
        if encounter_model is None:
            encounter = encounter_form.save(commit=False)
            if patient_model:
                encounter.subject_Patient = patient_model
        else:
            encounter = encounter_form.save(commit=False)
            encounter.id = encounter_model.id

        encounter.save()
        encounter_form.save_m2m()

        if participant_form and participant_form.is_valid():
            encounter.Encounter_participant.all().delete()
            participant = participant_form.save(commit=False)
            participant.Encounter = encounter
            participant.save()

        if document_reference_form and document_reference_form.is_valid():
            print(f"Document Reference Form author_practitioner: {document_reference_form.cleaned_data.get('author_Practitioner')}")
            docmentReference_model = document_reference_form.save(commit=False)
            docmentReference_model.save()
            docmentReference_model.context_Encounter.set([encounter])
        else:
            print(document_reference_form.errors)

        if document_reference_content_form and document_reference_content_form.is_valid():
            documentReference_content_model = document_reference_content_form.save(commit=False)
            documentReference_content_model.DocumentReference = docmentReference_model
            
            # Handle the note text by creating a FHIR_GP_Attachment
            note_text = document_reference_content_form.cleaned_data.get('note_text')
            if note_text:                
                attachment = FHIR_GP_Attachment.objects.create(
                    title="Clinical Note",
                    contentType="text/plain; charset=utf-8",
                    language="en",
                    data=note_text,
                    url="",
                    size=len(note_text),
                    hash=hashlib.sha1(note_text.encode('utf-8')).digest(),
                    upload_to=""
                )
                documentReference_content_model.attachment = attachment
            
            documentReference_content_model.save()

        return encounter
