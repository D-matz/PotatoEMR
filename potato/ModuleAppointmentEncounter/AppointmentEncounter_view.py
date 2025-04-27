from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from potato.models import FHIR_Patient, FHIR_Encounter, FHIR_Encounter_participant

def overview(request, patient_id, encounter_id):
    patient_model = get_object_or_404(FHIR_Patient, id=patient_id)
    encounter_model = get_object_or_404(FHIR_Encounter, id=encounter_id)
    enc_pract_participant_model = FHIR_Encounter_participant.objects.filter(Encounter=encounter_model, actor_Practitioner__isnull=False).first()
    if enc_pract_participant_model:
        practitioner_model = enc_pract_participant_model.actor_Practitioner
    else:
        practitioner_model = None
    return render(request, "AppointmentEncounter_overview.html", {"patient": patient_model, "encounter": encounter_model, "practitioner": practitioner_model})
