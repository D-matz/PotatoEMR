from django.shortcuts import render
from .form_registerPatient import RegisterPatientForm
from ..models import FHIR_Patient
from ..FHIR_DataTypes.FHIR_generalpurpose import *

def create_patient(request):
    if request.method == "POST":
        form = RegisterPatientForm(request.POST)
        if form.is_valid():
            try:
                save_patient(form.cleaned_data)
                print("success")
                return render(request, 'form_registerPatient.html', {'form': RegisterPatientForm(), 'success': True})
            except Exception as e:
                print("error", e)
                return render(request, 'form_registerPatient.html', {'form': form, 'error': str(e)})
    else:
        form = RegisterPatientForm()
        return render(request, 'form_registerPatient.html', {'form': form})


#if this was to be repeated you could put it in the RegisterPatientForm
#but it's probably only used in this one view/template
def save_patient(clean_patient_data):
    print(clean_patient_data)
    patient = FHIR_Patient()
    patient.gender=clean_patient_data['gender']
    birth_date_model = FHIR_primitive_DateField()
    birth_date_model.date = clean_patient_data['birth_date']
    birth_date_model.precision = FHIR_primitive_DateField.Precision.DAY
    birth_date_model.save()
    patient.birth_date = birth_date_model

    human_name_model = FHIR_GP_HumanName.objects.create(
        use=clean_patient_data['name_use'],
        family=clean_patient_data['family_name'],
        text=f"{clean_patient_data.get('prefix', '')} {clean_patient_data['family_name']} {clean_patient_data.get('suffix', '')}".strip()
    )
    for name in (clean_patient_data['given_name']).split(','):
        FHIR_GP_HumanName_Given.objects.create(value=name.strip(), human_name=human_name_model)
    if clean_patient_data.get('prefix'):
        FHIR_GP_HumanName_Prefix.objects.create(value=clean_patient_data['prefix'], human_name=human_name_model)
    if clean_patient_data.get('suffix'):
        FHIR_GP_HumanName_Suffix.objects.create(value=clean_patient_data['suffix'], human_name=human_name_model)
    patient.name = human_name_model
    patient.save()

    address = FHIR_GP_Address(
        use=cleaned_patient_data.get("address_use"),
        text=cleaned_patient_data.get("address"),
        city=cleaned_patient_data.get("city"),
        state=cleaned_patient_data.get("state"),
        postalCode=cleaned_patient_data.get("zip_code"),
    )
    
