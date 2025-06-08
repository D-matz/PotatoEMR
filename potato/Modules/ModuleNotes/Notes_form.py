from django import forms
from django.db import transaction
from potato.models import (
    FHIR_DocumentReference,
    FHIR_DocumentReference_content
)
from potato.models_dir.FHIR_DataTypes.FHIR_generalpurpose import FHIR_GP_Attachment
from potato.Common.Widgets.InputSingleFromMany import InputSingleFromMany
import hashlib

class DocumentReferenceForm(forms.ModelForm):
    class Meta:
        model = FHIR_DocumentReference
        fields = [
            'date',
            'author_Practitioner',
            'description'
        ]
        widgets = {
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'author_Practitioner': InputSingleFromMany(attrs={'class': 'form-select'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Brief description or title'})
        }
        labels = {
            'date': 'Note Date',
            'author_Practitioner': 'Note Author',
            'description': 'Title/Description'
        }

class DocumentReferenceContentForm(forms.ModelForm):
    # Add a custom text field for the note content
    note_text = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control', 
            'rows': 15,
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

def save_document_reference(document_reference_form, document_reference_content_form, patient_model=None):
    with transaction.atomic():
        # Save the DocumentReference
        document_reference = document_reference_form.save(commit=False)
        document_reference.save()
        document_reference_form.save_m2m()
        
        # If we have a patient, we need to associate this note with an encounter
        # Create a simple encounter for this note if needed
        if patient_model:
            from potato.models import FHIR_Encounter
            from datetime import datetime
            
            # Create a simple encounter for this note
            encounter = FHIR_Encounter.objects.create(
                subject_Patient=patient_model,
                status='finished',  # Use finished status for note encounters
                plannedStartDate=datetime.now(),
                plannedEndDate=datetime.now()
            )
            document_reference.context_Encounter.add(encounter)

        # Save the DocumentReference content
        if document_reference_content_form and document_reference_content_form.is_valid():
            # Get or create the content model
            content_model_list = document_reference.DocumentReference_content.all()
            if content_model_list.count() > 0:
                document_reference_content = content_model_list.first()
            else:
                document_reference_content = FHIR_DocumentReference_content.objects.create(
                    DocumentReference=document_reference
                )
            
            # Handle the note text by creating a FHIR_GP_Attachment
            note_text = document_reference_content_form.cleaned_data.get('note_text')
            if note_text:
                # Delete existing attachment if it exists
                if document_reference_content.attachment:
                    document_reference_content.attachment.delete()
                
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
                document_reference_content.attachment = attachment
                document_reference_content.save()

        return document_reference 