from django.shortcuts import render
from potato.models import (
    FHIR_Patient,
    FHIR_Observation
)
from datetime import date
from dateutil.relativedelta import relativedelta
from django.db import models
from django.apps import apps

def patient_overview(request, patient_id):
    patient_model = FHIR_Patient.objects.filter(id=patient_id).first()
    if not patient_model:
        return render(request, '404.html', status=404)
    
    #card - patient info
    patientAge = relativedelta(date.today(), patient_model.birthDate)
    patientAgeStr =  f"{patientAge.years}y, {patientAge.months}m, {patientAge.days}d"

    #card - explorer
    related_objects = get_all_related_objects(patient_model)

    #card - vital signs
    #kind of duplicating GrowthChart overview code, should maybe pull out into common vitals
    heightLOINC_list = ["3137-7", "3138-5", "8301-4", "8302-2", "8305-5", "8306-3", "8307-1", "8308-9", "92999-2"]
    height_observation_model_list = FHIR_Observation.objects.filter(subject_Patient=patient_model, code_cc__system='http://loinc.org', code_cc__code__in=heightLOINC_list)
    weightLOINC = "29463-7"
    weight_observation_model_list = FHIR_Observation.objects.filter(subject_Patient=patient_model, code_cc__system='http://loinc.org', code_cc__code=weightLOINC)
    bmiLOINC = "39156-5"
    bmi_observation_model_list = FHIR_Observation.objects.filter(subject_Patient=patient_model, code_cc__system='http://loinc.org', code_cc__code=bmiLOINC)
    headLOINC = "9843-4"
    head_observation_model_list = FHIR_Observation.objects.filter(subject_Patient=patient_model, code_cc__system='http://loinc.org', code_cc__code=headLOINC)
    
    # Add additional vital signs
    respiratoryRateLOINC = "9279-1"
    respiratory_rate_observation_model_list = FHIR_Observation.objects.filter(subject_Patient=patient_model, code_cc__system='http://loinc.org', code_cc__code=respiratoryRateLOINC)
    
    heartRateLOINC = "8867-4"
    heart_rate_observation_model_list = FHIR_Observation.objects.filter(subject_Patient=patient_model, code_cc__system='http://loinc.org', code_cc__code=heartRateLOINC)
    
    oxygenSaturationLOINC_list = ["2708-6", "59408-5"]
    oxygen_saturation_observation_model_list = FHIR_Observation.objects.filter(subject_Patient=patient_model, code_cc__system='http://loinc.org', code_cc__code__in=oxygenSaturationLOINC_list)
    
    temperatureLOINC = "8310-5"
    temperature_observation_model_list = FHIR_Observation.objects.filter(subject_Patient=patient_model, code_cc__system='http://loinc.org', code_cc__code=temperatureLOINC)
    
    bloodPressureLOINC = "85354-9"
    blood_pressure_observation_model_list = FHIR_Observation.objects.filter(subject_Patient=patient_model, code_cc__system='http://loinc.org', code_cc__code=bloodPressureLOINC)
    
    vital_names = ['height', 'weight', 'bmi', 'respiratory rate', 'heart rate', 'oxygen saturation', 'temperature']
    recent_vitals = {vital_name: {'observation': None, 'warning_level': 'normal'} for vital_name in vital_names}
    
    recent_vitals = add_most_recent(recent_vitals, height_observation_model_list, 'height')
    recent_vitals = add_most_recent(recent_vitals, weight_observation_model_list, 'weight')
    recent_vitals = add_most_recent(recent_vitals, bmi_observation_model_list, 'bmi')
    recent_vitals = add_most_recent(recent_vitals, respiratory_rate_observation_model_list, 'respiratory rate')
    recent_vitals = add_most_recent(recent_vitals, heart_rate_observation_model_list, 'heart rate')
    recent_vitals = add_most_recent(recent_vitals, oxygen_saturation_observation_model_list, 'oxygen saturation')
    recent_vitals = add_most_recent(recent_vitals, temperature_observation_model_list, 'temperature')
    # Only include head circumference for children under 3 years
    if patient_model.birthDate is None or (date.today() - patient_model.birthDate).days < (365 * 3):
        recent_vitals['head'] = None
        recent_vitals = add_most_recent(recent_vitals, head_observation_model_list, 'head')
        
    # Define vital sign thresholds
    vital_thresholds = {
        'heart rate': {
            'danger_low': 50, 'warning_low': 60, 
            'warning_high': 100, 'danger_high': 120
        },
        'respiratory rate': {
            'danger_low': 8, 'warning_low': 12, 
            'warning_high': 20, 'danger_high': 25
        },
        'temperature': {  # Celsius
            'danger_low': 35.0, 'warning_low': 36.0, 
            'warning_high': 37.8, 'danger_high': 39.0
        },
        'oxygen saturation': {
            'danger_low': 90, 'warning_low': 95, 
            'warning_high': float('inf'), 'danger_high': float('inf')
        },
    }

    for vital_name, vital in recent_vitals.items():
        if vital is None:
            continue
        vital_model = vital['observation']
        if vital_model is None:
            continue
        warning_level = 'normal'
        if vital_name in vital_thresholds:
            value = vital_model.get_value_float()
            if value is not None:
                thresholds = vital_thresholds[vital_name]
                
                if value < thresholds['warning_low'] or value > thresholds['warning_high']:
                    warning_level = 'bg-warning text-dark'
                
                if value < thresholds['danger_low'] or value > thresholds['danger_high']:
                    warning_level = 'bg-danger text-dark'        
        recent_vitals[vital_name]['warning_level'] = warning_level
    

    #doing blood presure separately because it's not a single float
    most_recent_BP = None
    for obs in blood_pressure_observation_model_list:
        if most_recent_BP is None or obs.get_effective_datetime() > most_recent_BP.get_effective_datetime():
            most_recent_BP = obs

    blood_pressure_thresholds = {
        'systolic': {
        'danger_low': 80, 'warning_low': 90,
            'warning_high': 140, 'danger_high': 180
        },
        'diastolic': {
            'danger_low': 50, 'warning_low': 60,
            'warning_high': 90, 'danger_high': 120
        }
    }

    recent_blood_pressure = {'observation': most_recent_BP, 'warning_level': 'normal', 'formatted_bp': None}
    if most_recent_BP is not None:
        systolic = None
        diastolic = None
        unit = None
        for component in most_recent_BP.Observation_component.all():
            if component.code_cc.first() is not None:
                code = component.code_cc.first().code
                if code == '8480-6':  # Systolic
                    systolic = component.value_Quantity.value
                    unit = component.value_Quantity.unit
                elif code == '8462-4':  # Diastolic
                    diastolic = component.value_Quantity.value
        recent_blood_pressure['formatted_bp'] = f"{round(systolic)}/{round(diastolic)} {unit}"

        if systolic is not None and diastolic is not None:
            sys_thresholds = blood_pressure_thresholds['systolic']
            dia_thresholds = blood_pressure_thresholds['diastolic']
            
            if (systolic < sys_thresholds['warning_low'] or 
                systolic > sys_thresholds['warning_high'] or 
                diastolic < dia_thresholds['warning_low'] or 
                diastolic > dia_thresholds['warning_high']):
                recent_blood_pressure['warning_level'] = 'bg-warning text-dark'
            
            if (systolic < sys_thresholds['danger_low'] or 
                systolic > sys_thresholds['danger_high'] or 
                diastolic < dia_thresholds['danger_low'] or 
                diastolic > dia_thresholds['danger_high']):
                recent_blood_pressure['warning_level'] = 'bg-danger text-dark'
            
    return render(request, 'PatientOverview.html', {
        'patient': patient_model, 
        'patientAgeStr': patientAgeStr, 
        'related_fields': related_objects['related_fields'],
        'related_models': related_objects['related_models'],
        'recent_vitals': recent_vitals,
        'recent_blood_pressure': recent_blood_pressure,
        })

def add_most_recent(recent_vitals, observation_model_list, key):
    for obs in observation_model_list:
        #might not include head circumference if not baby
        if recent_vitals[key] is not None:
            #use most recent observation
            if recent_vitals[key]['observation'] is None or obs.get_effective_datetime() > recent_vitals[key]['observation'].get_effective_datetime():
                recent_vitals[key]['observation'] = obs
    return recent_vitals

def explorer_row(request, model_name, model_id):
    model_class = apps.get_app_config('potato').get_model(model_name)
    model = model_class.objects.get(id=model_id)
    related_objects = get_all_related_objects(model)
    return render(request, 'PatientOverview_explorerRow.html', {
        'related_fields': related_objects['related_fields'],
        'related_models': related_objects['related_models']
    })

def get_all_related_objects(obj):
    """Get all objects that have a relationship with the provided object."""
    related_fields = {}
    related_models = {}
    
    obj_model = obj.__class__    
    
    for field in obj_model._meta.fields:
        field_name = field.name
        field_value = getattr(obj, field_name)
        related_fields[field_name] = field_value
    
    for model in apps.get_app_config('potato').get_models():
        if model == obj_model:
            continue
        
        # Check for ForeignKey and ManyToManyField relationships
        for field in model._meta.get_fields():
            # Check if this field relates to our target model
            if isinstance(field, (models.ForeignKey, models.ManyToManyField)):
                if field.related_model == obj_model:
                    if hasattr(field, 'get_accessor_name'):
                        # For ManyToManyField
                        accessor_name = field.get_accessor_name()
                    else:
                        # For ForeignKey
                        accessor_name = field.remote_field.get_accessor_name()
                    
                    if hasattr(obj, accessor_name):
                        related_manager = getattr(obj, accessor_name)
                        related_objects = related_manager.all()
                        relatedModel_id_name_list = []
                        for related_object in related_objects:
                            relatedModel_id_name_list.append({'str' : str(related_object), 'id' : related_object.id, 'name' : related_object.__class__.__name__})
                        related_models[f"{model.__name__} (via {field.name})"] = relatedModel_id_name_list

    return {"related_fields": related_fields, "related_models": related_models}
