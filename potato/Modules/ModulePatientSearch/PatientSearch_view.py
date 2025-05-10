from django.shortcuts import render, redirect
from django.db import transaction
from .PatientSearch_form import PatientSearchForm
from potato.models import (
    FHIR_Patient,
    FHIR_Patient_name,
    FHIR_Patient_telecom
)
from django.db.models import Q

def search_patient(request):
    if request.method == 'GET':
        return render(request, 'PatientSearch.html', {'form': PatientSearchForm()})    
    elif request.method == 'POST':
        form = PatientSearchForm(request.POST)
        if not form.is_valid():
            return render(request, 'PatientSearch_errorPartial.html', {'form': form})
        else:
            have_data = False
            for field in form.cleaned_data:
                if field != 'fuzzy' and form.cleaned_data[field]:
                    have_data = True
                    break
            if not have_data:
                return render(request, 'PatientSearch_resultPartial.html', {'results': []})
            
            fuzzy = form.cleaned_data['fuzzy']
            name = form.cleaned_data['Name']
            email = form.cleaned_data['Email']
            phone = form.cleaned_data['Phone']
            
            query = Q()    
        
            if name: query |= Q(Patient_name__text__icontains=name) | Q(Patient_name__family__icontains=name)                
            if email: query |= Q(Patient_telecom__system='email', Patient_telecom__value__icontains=email)
            if phone: query |= Q(Patient_telecom__system='phone', Patient_telecom__value__icontains=phone)

            results = FHIR_Patient.objects.filter(query).distinct()

            fuzzy_results = []
            if fuzzy:
                existing_ids = set(results.values_list('id', flat=True))
                patient_list = FHIR_Patient.objects.all()
                for patient in patient_list:
                    if patient.id in existing_ids:
                        continue
                    should_add = False
                    
                    if name:
                        compare_names = FHIR_Patient_name.objects.filter(Patient=patient)
                        for compare_name in compare_names:
                            fuzzy_distance = fuzzy_match(name, compare_name.text)
                            if fuzzy_distance <= 0.5:
                                should_add = True
                                break
                    
                    if not should_add and email:
                        patient_telecoms = FHIR_Patient_telecom.objects.filter(Patient=patient)
                        compare_emails = patient_telecoms.filter(system='email')
                        for compare_email in compare_emails:
                            fuzzy_distance = fuzzy_match(email, compare_email.value)
                            if fuzzy_distance <= 0.5:
                                should_add = True
                                break
                    
                    if not should_add and phone:
                        patient_telecoms = FHIR_Patient_telecom.objects.filter(Patient=patient)
                        compare_phones = patient_telecoms.filter(system='phone')
                        for compare_phone in compare_phones:
                            fuzzy_distance = fuzzy_match(phone, compare_phone.value)
                            if fuzzy_distance <= 0.5:
                                should_add = True
                                break
                    
                    if should_add:
                        fuzzy_results.append(patient)
                
                if fuzzy_results:
                    fuzzy_ids = [patient.id for patient in fuzzy_results]
                    fuzzy_results = FHIR_Patient.objects.filter(id__in=fuzzy_ids)
            
            return render(request, 'PatientSearch_resultPartial.html', {'precise_and_fuzzy': [results, fuzzy_results]})
        

def fuzzy_match(str1, str2):
    if str1 == "" or str2 == "":
        return 1
    if str1 == str2:
        return 0
    #compare shorter string to each substring of longer string
    #return levenshtein distance of best match
    longer = str1
    shorter = str2
    if(len(str1) < len(str2)):
        longer = str2
        shorter = str1
    longer = longer.lower()
    shorter = shorter.lower()
    best_distance = len(longer)
    for i in range(len(longer) - len(shorter) + 1):
        substring = longer[i:i + len(shorter)]
        distance = levenshtein_distance(shorter, substring)
        distance = distance / len(shorter)
        #dividing all scores by matching string length to reward matching longer strings
        #can revist later 
        best_distance = min(best_distance, distance)
    return best_distance

def levenshtein_distance(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)
    matrix = [[0 for _ in range(len_str2 + 1)] for _ in range(len_str1 + 1)]
    for i in range(len_str1 + 1):
        matrix[i][0] = i
    for j in range(len_str2 + 1):
        matrix[0][j] = j
    for i in range(1, len_str1 + 1):
        for j in range(1, len_str2 + 1):
            cost = 0 if str1[i - 1] == str2[j - 1] else 1
            matrix[i][j] = min(
                matrix[i - 1][j] + 1,      # Deletion
                matrix[i][j - 1] + 1,      # Insertion
                matrix[i - 1][j - 1] + cost  # Substitution
            )
    return matrix[len_str1][len_str2]
