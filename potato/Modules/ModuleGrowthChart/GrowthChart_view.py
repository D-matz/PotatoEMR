from django.shortcuts import render, get_object_or_404
from potato.models import (
    FHIR_Patient,
    FHIR_Observation
)
from datetime import datetime, time
from django.utils.timezone import make_aware, get_default_timezone
from .GrowthChart_percentileData import (
  cdc_boys_bmi_age, cdc_boys_head_age, cdc_boys_length_age, cdc_boys_stature_age, cdc_boys_weight_age, 
  cdc_boys_weight_age_24_240, cdc_boys_weight_length, cdc_boys_weight_stature, cdc_girls_bmi_age, 
  cdc_girls_head_age, cdc_girls_length_age, cdc_girls_stature_age, cdc_girls_weight_age, 
  cdc_girls_weight_age_24_240, cdc_girls_weight_length, cdc_girls_weight_stature, who_boys_circumference_age, 
  who_boys_length_age, who_boys_weight_age, who_boys_weight_length, who_girls_circumference_age, 
  who_girls_length_age, who_girls_weight_age, who_girls_weight_length, 
)

days_per_month = 365/12

def obsList_to_PointList(observation_model_list, patient_birthdate, age_divider=1):
    point_list = []
    for observation_model in observation_model_list:
        obs_time = observation_model.get_effective_datetime()
        obs_value = observation_model.get_value_float()
        if obs_time and obs_value:
            age_days = (obs_time - patient_birthdate).days / age_divider
            point_list.append({
                'x': age_days,
                'y': obs_value,
                'date': obs_time.strftime('%Y-%m-%d')
            })
    point_list.sort(key=lambda x: x['x'])
    return point_list

def GrowthChart_overview(request, patient_id):
    patient_model = get_object_or_404(FHIR_Patient, id=patient_id)
    if patient_model.birthDate is None:
        return render(request, 'common_error_patient.html', {'patient': patient_model, 'error_message': "Patient has no birth date at GrowthChart_overview in GrowthChart_view.py"})
    patient_birthdate = make_aware(datetime.combine(patient_model.birthDate, time.min), get_default_timezone())
    heightLOINC_list = ["3137-7", "3138-5", "8301-4", "8302-2", "8305-5", "8306-3", "8307-1", "8308-9", "92999-2"]
    height_observation_model_list = FHIR_Observation.objects.filter(subject_Patient=patient_model, code_cc__system='http://loinc.org', code_cc__code__in=heightLOINC_list)
    weightLOINC = "29463-7"
    weight_observation_model_list = FHIR_Observation.objects.filter(subject_Patient=patient_model, code_cc__system='http://loinc.org', code_cc__code=weightLOINC)
    bmiLOINC = "39156-5"
    bmi_observation_model_list = FHIR_Observation.objects.filter(subject_Patient=patient_model, code_cc__system='http://loinc.org', code_cc__code=bmiLOINC)
    headLOINC = "9843-4"
    head_observation_model_list = FHIR_Observation.objects.filter(subject_Patient=patient_model, code_cc__system='http://loinc.org', code_cc__code=headLOINC)

    head_point_list = obsList_to_PointList(head_observation_model_list, patient_birthdate, 7)
    height_point_list = obsList_to_PointList(height_observation_model_list, patient_birthdate, 7)
    weight_point_list = obsList_to_PointList(weight_observation_model_list, patient_birthdate, 7)
    bmi_point_list = obsList_to_PointList(bmi_observation_model_list, patient_birthdate, days_per_month)
    

    patient_age_months = (datetime.now() - datetime.combine(patient_model.birthDate, time.min)).days / days_per_month
    #choose which graphs depending on patient gender and age
    #merge percentile data (from CDC, WHO, etc.) with patient data (list of points from observations)
    if patient_model.gender == 'male':        
        if patient_age_months > 20:
            graph_list = [
                cdc_boys_bmi_age | {'patientData': bmi_point_list},
                cdc_boys_stature_age | {'patientData': height_point_list}
            ]
        if patient_age_months < 40:
            graph_list = [
                cdc_boys_head_age | {'patientData': head_point_list},
                cdc_boys_length_age | {'patientData': height_point_list},
                cdc_boys_weight_age | {'patientData': weight_point_list}
            ]
    else:
        percentiles_vs_patientData_list = ['cdc_girls_bmi_age', 'cdc_girls_head_age', 'cdc_girls_length_age', 'cdc_girls_stature_age', 'cdc_girls_weight_age', 'cdc_girls_weight_length', 'cdc_girls_weight_stature']

    print(graph_list)

    return render(request, 'GrowthChart_overview.html', {
        'patient': patient_model,
        'graph_list': graph_list
    })
