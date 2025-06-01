from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .LabResults_form import (
    DiagnosticReportForm, DiagnosticReportNoteForm,
    DiagnosticReportMediaForm, DiagnosticReportConclusionCodeForm,
    save_diagnostic_report
)
from potato.models import FHIR_Patient, FHIR_DiagnosticReport
# a lot of duplicate views/forms/templates/urls with Medications
# could probably pull it out into common view

def _diagnostic_report_create_formlist(report=None):
    """Create a list of diagnostic report forms, which are used to display and save chosen fields.
    If report is provided, creates bound forms. Otherwise creates unbound forms."""
    return [
        DiagnosticReportForm(instance=report if report else None),
        DiagnosticReportNoteForm(instance=report.DiagnosticReport_note.first() if report else None),
        DiagnosticReportMediaForm(instance=report.DiagnosticReport_media.first() if report else None),
        DiagnosticReportConclusionCodeForm(instance=report.DiagnosticReport_conclusionCode.first() if report else None)
    ]

def _diagnostic_report_post_forms(patient, post_data, report=None):
    """Take POST data from new or existing report and try to save form
    Return if form valid, report model, and list of forms"""
    forms = {
        'report_form': DiagnosticReportForm(post_data, instance=report),
        'note_form': DiagnosticReportNoteForm(post_data, instance=report.DiagnosticReport_note.first() if report else None),
        'media_form': DiagnosticReportMediaForm(post_data, instance=report.DiagnosticReport_media.first() if report else None),
        'conclusion_form': DiagnosticReportConclusionCodeForm(post_data, instance=report.DiagnosticReport_conclusionCode.first() if report else None)
    }
    formlist = list(forms.values())
    if not all(form.is_valid() for form in formlist):
        return (False, report, formlist)
    else:
        report = save_diagnostic_report(
            report_form=forms['report_form'],
            note_form=forms['note_form'],
            media_form=forms['media_form'],
            conclusion_form=forms['conclusion_form'],
            patient_model=patient
        )
        return (True, report, formlist)

def labResults_table(request, patient_id):
    patient = get_object_or_404(FHIR_Patient, id=patient_id)
    diagnosticReport_list = FHIR_DiagnosticReport.objects.filter(subject_Patient=patient)
    
    label_formlist = _diagnostic_report_create_formlist()
    formlist_list = [_diagnostic_report_create_formlist(report) 
                     for report in diagnosticReport_list]
    
    return render(request, 'LabResults_table.html', {
        'report_and_form': zip(diagnosticReport_list, formlist_list),
        'patient': patient,
        'label_formlist': label_formlist
    })

def labResults_new(request, patient_id):
    patient = get_object_or_404(FHIR_Patient, id=patient_id)
    
    if request.method == 'GET':
        formlist = _diagnostic_report_create_formlist()
        return render(request, 'LabResults_table_row_edit_new.html', {
            'formlist': formlist,
            'patient': patient
        })
    
    elif request.method == 'POST':
        valid, report, formlist = _diagnostic_report_post_forms(patient, request.POST)
        if valid:
            return render(request, 'LabResults_table_row_normal.html', {
                'report': report,
                'patient': patient,
                'formlist': formlist
            })
        else:
            return render(request, 'LabResults_table_row_edit_new.html', {
                'formlist': formlist,
                'patient': patient
            })

def labResults_existing_edit(request, patient_id, diagnosticReport_id):
    patient = get_object_or_404(FHIR_Patient, id=patient_id)
    report = get_object_or_404(FHIR_DiagnosticReport, id=diagnosticReport_id)
    if request.method == 'GET':
        formlist = _diagnostic_report_create_formlist(report)
        return render(request, 'LabResults_table_row_edit_existing.html', {
            'formlist': formlist,
            'report': report,
            'patient': patient
        })
    
    elif request.method == 'POST':
        valid, report, formlist = _diagnostic_report_post_forms(patient, request.POST, report)
        if valid:
            return render(request, 'LabResults_table_row_normal.html', {
                'report': report,
                'patient': patient,
                'formlist': formlist
            })
        else:
            return render(request, 'LabResults_table_row_edit_existing.html', {
                'formlist': formlist,
                'report': report,
                'patient': patient
            })

def labResults_existing_cancel(request, patient_id, diagnosticReport_id):
    patient = get_object_or_404(FHIR_Patient, id=patient_id)
    report = get_object_or_404(FHIR_DiagnosticReport, id=diagnosticReport_id)
    formlist = _diagnostic_report_create_formlist(report)
    return render(request, 'LabResults_table_row_normal.html', {
        'report': report,
        'patient': patient,
        'formlist': formlist
    })
