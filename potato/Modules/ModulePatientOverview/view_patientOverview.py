from django.shortcuts import render
from potato.models import (
    FHIR_Patient
)
from datetime import date
from dateutil.relativedelta import relativedelta

def patient_overview(request, id):
    patient_model = FHIR_Patient.objects.filter(id=id).first()
    if not patient_model:
        return render(request, '404.html', status=404)
    patientAge = relativedelta(date.today(), patient_model.birthDate)
    patientAgeStr =  f"{patientAge.years}y, {patientAge.months}m, {patientAge.days}d"
    return render(request, 'PatientOverview.html', {'patient': patient_model, 'patientAgeStr': patientAgeStr})

def patient_overview_partial(request, id):
    patient_model = FHIR_Patient.objects.filter(id=id).first()
    if not patient_model:
        return render(request, '404.html', status=404)
    patientAge = relativedelta(date.today(), patient_model.birthDate)
    patientAgeStr =  f"{patientAge.years}y, {patientAge.months}m, {patientAge.days}d"
    return render(request, 'PatientOverview_partial.html', {'patient': patient_model, 'patientAgeStr': patientAgeStr})
