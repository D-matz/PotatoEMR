from django import forms
from django.db import transaction
from potato.models_dir.FHIR_Resources.DiagnosticReport import (
    FHIR_DiagnosticReport,
    FHIR_DiagnosticReport_note,
    FHIR_DiagnosticReport_media,
    FHIR_DiagnosticReport_conclusionCode
)
from datetime import datetime
from potato.Common.Widgets.InputSingleFromMany import InputSingleFromMany

#why is issued an instant vs effective_dateTime is a datetime?
class DiagnosticReportForm(forms.ModelForm):
    class Meta:
        model = FHIR_DiagnosticReport
        fields = [
            'code_cc',
            'status',
            'effective_dateTime',
            'issued',
            'conclusion',
            'result'
        ]
        widgets = {
            'code_cc': InputSingleFromMany(attrs={'class': 'form-input form-input-sm'}),
            'status': forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'effective_dateTime': forms.DateTimeInput(attrs={'class': 'form-input form-input-sm', 'type': 'datetime-local'}),
            'issued': forms.DateTimeInput(attrs={'class': 'form-input form-input-sm', 'type': 'datetime-local'}),
            'conclusion': forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': '3'}),
            'result': InputSingleFromMany(attrs={'class': 'form-input form-input-sm'})
        }
        labels = {
            'code_cc': 'Report Type',
            'status': 'Status',
            'effective_dateTime': 'Effective Time',
            'issued': 'Issue Time',
            'conclusion': 'Conclusion',
            'result': 'Results'
        }

class DiagnosticReportNoteForm(forms.ModelForm):
    class Meta:
        model = FHIR_DiagnosticReport_note
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control form-control-sm',
                'rows': '3'
            })
        }
        labels = {
            'text': 'Notes'
        }

    def save(self, commit=True):
        return super().save(commit=False)

class DiagnosticReportMediaForm(forms.ModelForm):
    class Meta:
        model = FHIR_DiagnosticReport_media
        fields = [
            'comment',
            'link'
        ]
        widgets = {
            'comment': forms.TextInput(attrs={'class': 'form-input form-input-sm'}),
            'link': forms.Select(attrs={'class': 'form-select form-select-sm'})
        }
        labels = {
            'comment': 'Media Comment',
            'link': 'Document Reference'
        }

    def save(self, commit=True):
        return super().save(commit=False)

class DiagnosticReportConclusionCodeForm(forms.ModelForm):
    class Meta:
        model = FHIR_DiagnosticReport_conclusionCode
        fields = [
            'conclusionCode_cc',
        ]
        widgets = {
            'conclusionCode_cc': InputSingleFromMany(attrs={'class': 'form-input form-input-sm'}),
        }
        labels = {
            'conclusionCode_cc': 'Conclusion Code',
        }

    def save(self, commit=True):
        return super().save(commit=False)

def save_diagnostic_report(report_form, note_form, media_form, conclusion_form, patient_model=None, report_model=None):
    with transaction.atomic():
        if report_model is None:
            report = report_form.save(commit=False)
            if patient_model:
                report.subject_Patient = patient_model
        else:
            report = report_form.save(commit=False)
            report.id = report_model.id

        report.save()
        report_form.save_m2m() #saves m2m fields in diagnosticReport like code_cc

        if note_form and note_form.is_valid():
            report.DiagnosticReport_note.all().delete()
            note = note_form.save(commit=False)
            note.DiagnosticReport = report
            note.save()

        if media_form and media_form.is_valid():
            report.DiagnosticReport_media.all().delete()
            media = media_form.save(commit=False)
            media.DiagnosticReport = report
            media.save()

        if conclusion_form and conclusion_form.is_valid():
            report.DiagnosticReport_conclusionCode.all().delete()
            conclusion = conclusion_form.save(commit=False)
            conclusion.DiagnosticReport = report
            conclusion.save()
            conclusion_form.save_m2m()

        return report
