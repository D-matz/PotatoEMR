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
    FHIR_GP_Address
)

def create_patient(request):
    if request.method == "POST":
        form = RegisterPatientForm(request.POST)
        if not form.is_valid():
            return render(request, 'form_registerPatient.html', {'form': form, 'error': "invalid form"})
        else:
            try:
                with transaction.atomic():
                    form_data = form.cleaned_data
                    patient_model = FHIR_Patient.objects.create(
                        gender=form_data['gender'],
                        birthDate_date=form_data['birth_date'],
                    )

                    patient_name = FHIR_Patient_name.objects.create(
                        patient=patient_model,
                        text=f"{form_data['prefix']} {form_data['given_name']} {form_data['family_name']} {form_data['suffix']}".strip(),
                        use=form_data.get('name_use', FHIR_GP_HumanName.NameUseChoices.OFFICIAL),
                    )
                    #todo create given, prefix, suffix, maybe use modelform instead

                    fcity = form_data.get('city')
                    fstate = form_data.get('state')
                    fpostalCode = form_data.get('zip_code')
                    ftext = form_data.get('address') + ", " + fcity + ", " + fstate + ", " + fpostalCode
                    patient_address = FHIR_Patient_address.objects.create(
                        patient=patient_model,
                        use=form_data.get('address_use', FHIR_GP_Address.AddressUse.HOME),
                        type=form_data.get('address_type', FHIR_GP_Address.AddressType.POSTAL),
                        city=fcity,
                        state=fstate,
                        postalCode=fpostalCode,
                        text=ftext,
                        country=form_data.get('country', None),  # Add country if available
                    )

                    if form_data.get('phone_number'):
                        patient_telecom_phone = FHIR_Patient_telecom.objects.create(
                            patient=patient_model,
                            system=FHIR_GP_ContactPoint.System.PHONE,
                            use=form_data.get('phone_use'),
                            value=form_data.get('phone_number')
                        )
                    if form_data.get('email_addr'):
                        patient_telecom_email = FHIR_Patient_telecom.objects.create(
                            patient=patient_model,
                            system=FHIR_GP_ContactPoint.System.EMAIL,
                            value=form_data.get('email_addr')
                        )

                    return redirect("patient_overview", id=patient_model.id)
            except Exception as e:
                print("error", e)
                return render(request, 'form_registerPatient.html', {'form': form, 'error': str(e)})
    else:
        form = RegisterPatientForm()
        return render(request, 'form_registerPatient.html', {'form': form})


#if this was to be repeated you could put it in the RegisterPatientForm
#but it's probably only used in this one view/template
