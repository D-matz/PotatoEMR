from django.shortcuts import render, redirect
from django.db import transaction
from .form_registerPatient import RegisterPatientForm
from potato.models import (
    FHIR_Patient,
    FHIR_Patient_name,
    FHIR_Patient_address,
    FHIR_Patient_telecom,
    FHIR_GP_HumanName,
    FHIR_GP_ContactPoint,
    FHIR_GP_Address,
    FHIR_GP_HumanName_Given,
    FHIR_GP_HumanName_Prefix,
    FHIR_GP_HumanName_Suffix
)

def create_patient(request):
    if request.method == "GET":
        form = RegisterPatientForm()
        return render(request, 'form_registerPatient.html', {'form': form})
    elif request.method == "POST":
        form = RegisterPatientForm(request.POST)
        if not form.is_valid():
            print(form.errors)
            return render(request, 'form_registerPatient.html', {'form': form})
        else:
            try:
                with transaction.atomic():
                    form_data = form.cleaned_data
                    patient_model = FHIR_Patient.objects.create(
                        gender=form_data['gender'],
                        birthDate=form_data['birth_date'],
                    )

                    patient_name = FHIR_Patient_name.objects.create(
                        Patient=patient_model,
                        text=f"{form_data['prefix']} {form_data['given_name']} {form_data['family_name']} {form_data['suffix']}".strip(),
                        use=form_data.get('name_use', FHIR_GP_HumanName.NameUseChoices.OFFICIAL),
                        family=form_data['family_name'],
                    )
                    
                    if form_data.get('given_name'): FHIR_GP_HumanName_Given.objects.create(name_given=form_data['given_name'], human_name=patient_name)
                    if form_data.get('middle_name'): FHIR_GP_HumanName_Given.objects.create(name_given=form_data['middle_name'], human_name=patient_name)
                    if form_data.get('prefix'): FHIR_GP_HumanName_Prefix.objects.create(name_prefix=form_data['prefix'], human_name=patient_name)
                    if form_data.get('suffix'): FHIR_GP_HumanName_Suffix.objects.create(name_suffix=form_data['suffix'], human_name=patient_name)

                    fcity = form_data.get('city')
                    fstate = form_data.get('state')
                    fpostalCode = form_data.get('zip_code')
                    ftext = form_data.get('address') + ", " + fcity + ", " + fstate + ", " + fpostalCode
                    FHIR_Patient_address.objects.create(
                        Patient=patient_model,
                        use=form_data.get('address_use', FHIR_GP_Address.AddressUse.HOME),
                        type=form_data.get('address_type', FHIR_GP_Address.AddressType.POSTAL),
                        city=fcity,
                        state=fstate,
                        postalCode=fpostalCode,
                        text=ftext,
                        country=form_data.get('country', None),  # Add country if available
                    )

                    if form_data.get('phone_number'):
                        FHIR_Patient_telecom.objects.create(
                            Patient=patient_model,
                            system=FHIR_GP_ContactPoint.System.PHONE,
                            use=form_data.get('phone_use'),
                            value=form_data.get('phone_number')
                        )
                    if form_data.get('email_addr'):
                        FHIR_Patient_telecom.objects.create(
                            Patient=patient_model,
                            system=FHIR_GP_ContactPoint.System.EMAIL,
                            value=form_data.get('email_addr')
                        )

                    return redirect("PatientOverview", patient_id=patient_model.id)
            except Exception as e:
                print("error", e)
                form.add_error(None, str(e))  # Add the error to form.errors as a non-field error
                return render(request, 'form_registerPatient.html', {'form': form})



#if this was to be repeated you could put it in the RegisterPatientForm
#but it's probably only used in this one view/template
