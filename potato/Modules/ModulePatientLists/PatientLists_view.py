from django.shortcuts import render, redirect
from potato.models import FHIR_Patient
def lists(request):
    patients = FHIR_Patient.objects.all()
    return render(request, "PatientLists.html", {"patients": patients})
