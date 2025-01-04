from django.shortcuts import render
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_Resources.Patient import FHIR_Patient
from datetime import date
from dateutil.relativedelta import relativedelta

def patient_overview(request, id):
    patient_model = FHIR_Patient.objects.filter(id=id).first()
    if not patient_model:
        return render(request, '404.html', status=404)
    patientAge = relativedelta(date.today(), patient_model.birthDate_date)
    patientAgeStr =  f"{patientAge.years}y, {patientAge.months}m, {patientAge.days}d"
    return render(request, 'Patient.html', {'patient': patient_model, 'patientAgeStr': patientAgeStr})
