from django.shortcuts import render, get_object_or_404
from potato.models import FHIR_Patient, FHIR_Observation
from datetime import datetime, time
from django.utils.timezone import make_aware, get_default_timezone
from .GrowthChart_percentileData import data_all_charts

def growth_chart_overview(request, patient_id):
    patient_model = get_object_or_404(FHIR_Patient, id=patient_id)
    patient_birthdate = make_aware(datetime.combine(patient_model.birthDate, time()), get_default_timezone())
    heightLOINC_list = ["3137-7", "3138-5", "8301-4", "8302-2", "8305-5", "8306-3", "8307-1", "8308-9", "92999-2"]
    weightLOINC_list = ["3141-9", "3142-7", "8350-1", "8351-9", "8352-7", "8353-5", "8354-3", "8355-0", "92998-4"]
    height_observation_model_list = FHIR_Observation.objects.filter(subject_Patient=patient_model, code_cc__system='http://loinc.org', code_cc__code__in=heightLOINC_list)
    weight_observation_model_list = FHIR_Observation.objects.filter(subject_Patient=patient_model, code_cc__system='http://loinc.org', code_cc__code__in=weightLOINC_list)
    bmiLOINC = "39156-5"
    bmi_observation_model_list = FHIR_Observation.objects.filter(subject_Patient=patient_model, code_cc__system='http://loinc.org', code_cc__code=bmiLOINC)
    headLOINC = "9843-3"
    head_observation_model_list = FHIR_Observation.objects.filter(subject_Patient=patient_model, code_cc__system='http://loinc.org', code_cc__code=headLOINC)

    head_point_list = []
    for head_observation_model in head_observation_model_list:
        obs_time = head_observation_model.get_effective_datetime()
        obs_value = head_observation_model.get_value_float()
        if obs_time and obs_value:
            age_in_weeks = (obs_time - patient_birthdate).days / 7
            head_point_list.append({
                'x': age_in_weeks,
                'y': obs_value,
                'date': obs_time.strftime('%Y-%m-%d')
            })
    head_point_list.sort(key=lambda x: x['x'])

    height_point_list = []
    for height_observation_model in height_observation_model_list:
        obs_time = height_observation_model.get_effective_datetime()
        obs_value = height_observation_model.get_value_float()
        if obs_time and obs_value:
            age_in_weeks = (obs_time - patient_birthdate).days / 7
            height_point_list.append({
                'x': age_in_weeks,
                'y': obs_value,
                'date': obs_time.strftime('%Y-%m-%d')
            })
    height_point_list.sort(key=lambda x: x['x'])

    weight_point_list = []
    for height_observation_model in height_observation_model_list:
        obs_time = height_observation_model.get_effective_datetime()
        obs_value = height_observation_model.get_value_float()
        if obs_time and obs_value:
            age_in_weeks = (obs_time - patient_birthdate).days / 7
            weight_point_list.append({
                'x': age_in_weeks,
                'y': obs_value,
                'date': obs_time.strftime('%Y-%m-%d')
            })
    weight_point_list.sort(key=lambda x: x['x'])
    
    bmi_point_list = []
    for bmi_observation_model in bmi_observation_model_list:
        obs_time = bmi_observation_model.get_effective_datetime()
        obs_value = bmi_observation_model.get_value_float()
        if obs_time and obs_value:
            age_in_weeks = (obs_time - patient_birthdate).days / 7
            bmi_point_list.append({
                'x': age_in_weeks,
                'y': obs_value,
                'date': obs_time.strftime('%Y-%m-%d')
            })
    bmi_point_list.sort(key=lambda x: x['x'])
    

    if patient_model.gender == 'male':
        name_list = [
            ['cdc_boys_bmi_age', bmi_point_list], 
            ['cdc_boys_head_age', head_point_list], 
            ['cdc_boys_length_age', height_point_list], 
            ['cdc_boys_stature_age', height_point_list], 
            ['cdc_boys_weight_age', weight_point_list], 
#            ['cdc_boys_weight_length', weight_length_observation_model_list], 
#            ['cdc_boys_weight_stature', weight_stature_observation_model_list]
        ]
    else:
        name_list = ['cdc_girls_bmi_age', 'cdc_girls_head_age', 'cdc_girls_length_age', 'cdc_girls_stature_age', 'cdc_girls_weight_age', 'cdc_girls_weight_length', 'cdc_girls_weight_stature']

    graph_list = []
    for name_and_patiendData in name_list:
        data = data_all_charts[name_and_patiendData[0]]
        data['patientData'] = name_and_patiendData[1]
        graph_list.append(data)

    return render(request, 'GrowthChart_overview.html', {
        'patient': patient_model,
        'graph_list': graph_list
    })
