from django.core.management.base import BaseCommand
from potato.models import (
    FHIR_Patient,
    FHIR_Patient_name,
    FHIR_Patient_telecom,
    FHIR_Patient_address,
    FHIR_GP_Address,
    FHIR_Patient_photo,
    FHIR_Patient_contact,
    FHIR_GP_HumanName,
    FHIR_GP_HumanName_Prefix,
    FHIR_GP_HumanName_Given,
    FHIR_Practitioner, 
    FHIR_Practitioner_name,
)
import os
import datetime

patients = [
    {'name': 'Elijah Wood', 'gender': 'male', 'birthDate': '1981-09-28', 'photo': 'frodo.png', 'birthCity': 'Cedar Rapids', 'birthState': 'Iowa'},
    {'prefix': 'Sir', 'name': 'Ian McKellen', 'gender': 'male', 'birthDate': '1939-05-25', 'photo': 'gandalf.jpg', 'birthCity': 'Burnley', 'birthState': 'Lancashire'},
    {'prefix': 'Sir', 'name': 'Christopher Lee', 'gender': 'male', 'birthDate': '1922-05-27', 'photo': 'sauraman.jpg', 'birthCity': 'Belgravia', 'birthState': 'London'},
    {'name': 'Liv Tyler', 'gender': 'female', 'birthDate': '1977-07-01', 'photo': 'arwen.JPG', 'birthCity': 'New York City', 'birthState': 'New York'},
    {'name': 'Orlando Bloom', 'gender': 'male', 'birthDate': '1977-01-13', 'photo': 'legolas.png', 'birthCity': 'Canterbury', 'birthState': 'Kent'},
    {'name': 'Sean Astin', 'gender': 'male', 'birthDate': '1971-02-25', 'photo': 'sam.png', 'birthCity': 'Santa Monica', 'birthState': 'California'},
    {'name': 'Viggo Mortensen', 'gender': 'male', 'birthDate': '1958-10-20', 'photo': 'aragorn.jpg', 'birthCity': 'Watertown', 'birthState': 'New York'},
    {'name': 'John Rhys-Davies', 'gender': 'male', 'birthDate': '1944-03-06', 'photo': 'gimli.JPG', 'birthCity': 'Salisbury', 'birthState': 'Wiltshire'},
    {'name': 'Billy Boyd', 'gender': 'male', 'birthDate': '1968-11-20', 'photo': 'pippin.png', 'birthCity': 'Glasgow'},
    {'name': 'Dominic Monaghan', 'gender': 'male', 'birthDate': '1976-12-08', 'photo': 'merry.jpg', 'birthCity': 'West Berlin'},
    {'name': 'Sean Bean', 'gender': 'male', 'birthDate': '1959-04-17', 'photo': 'boromir.JPG', 'birthCity': 'Sheffield'},
    {'name': 'Andy Serkis', 'gender': 'male', 'birthDate': '1959-04-20', 'photo': 'gollum.jpg', 'birthCity': 'Ruislip Manor', 'birthState': 'Middlesex'},
    {'name': 'Miranda Otto', 'gender': 'female', 'birthDate': '1967-07-16', 'photo': 'eowyn.JPG', 'birthCity': 'Brisbane', 'birthState': 'Queensland'},
    {'name': 'John Noble', 'gender': 'male', 'birthDate': '1952-09-12', 'photo': 'denethor.JPG', 'birthCity': 'Port Pirie', 'birthState': 'South Australia'},
    {'prefix': 'Sir', 'name': 'Ian Holm', 'gender': 'male', 'birthDate': '1931-09-12', 'photo': 'bilbo.jpg', 'birthCity': 'Goodmayes', 'birthState': 'Essex'},
    {'name': 'Hugo Weaving', 'gender': 'male', 'birthDate': '1960-04-04', 'photo': 'elrond.JPG', 'birthCity': 'Ibadan'},
    {'name': 'Karl Urban', 'gender': 'male', 'birthDate': '1972-06-07', 'photo': 'eomer.png', 'birthCity': 'Wellington'},
    {'name': 'David Wenham', 'gender': 'male', 'birthDate': '1965-09-21', 'photo': 'faromir.JPG', 'birthCity': 'Marickville', 'birthState': 'New South Wales'},
    {'name': 'Cate Blanchett', 'gender': 'female', 'birthDate': '1969-05-14', 'photo': 'galadriel.png', 'birthCity': 'Melbourne', 'birthState': 'Victoria'},
    {'name': 'Brad Dourif', 'gender': 'male', 'birthDate': '1950-03-18', 'photo': 'grima.JPG', 'birthCity': 'Huntington', 'birthState': 'West Virginia'},
    {'name': 'Bernard Hill', 'gender': 'male', 'birthDate': '1944-12-17', 'photo': 'theoden.jpg', 'birthCity': 'Blackley', 'birthState': 'Manchester'},
    {'name': 'Howard Shore', 'gender': 'male', 'birthDate': '1946-01-13', 'photo': 'howardshore.jpg', 'birthCity': 'Toronto', 'birthState': 'Ontario'},
]

class Command(BaseCommand):
    def handle(self, *args, **options):

        luthien_practitioner = FHIR_Practitioner.objects.filter(Practitioner_name__text__contains='Lúthien Tinúviel').first()
        if not luthien_practitioner:
            luthien_practitioner, created = FHIR_Practitioner.objects.get_or_create(
                active=True,
                gender='female',
                birthDate=datetime.date.fromisoformat('1000-01-01')
            )        
            practitioner_name = FHIR_Practitioner_name.objects.create(
                Practitioner=luthien_practitioner,
                text='Lúthien Tinúviel',
                use=FHIR_GP_HumanName.NameUseChoices.OFFICIAL,
                family='Tinúviel'
            )
            

        #FHIR_Patient.objects.all().delete() #maybe add identifiers to add/delete with at some point

        # Path to mock pictures directory
        pictures_dir = os.path.join(os.path.dirname(__file__), 'mock_pictures')

        for patient_data in patients:
            patient_model = FHIR_Patient.objects.create(
                birthDate=datetime.date.fromisoformat(patient_data['birthDate']),
                gender=patient_data['gender']
            )

            patient_model.generalPractitioner_Practitioner.set([luthien_practitioner])

            name_model = FHIR_Patient_name.objects.create(
                Patient = patient_model,
                text = patient_data['name'],
                use = FHIR_GP_HumanName.NameUseChoices.OFFICIAL,
                family = patient_data['name'].split(' ')[-1],
            )

            given_names = patient_data['name'].split(' ')[:-1]
            for given_name in given_names:
                FHIR_GP_HumanName_Given.objects.create(
                    name_given = given_name,
                    human_name = name_model
                )

            if 'prefix' in patient_data:
                prefix_model = FHIR_GP_HumanName_Prefix.objects.create(
                    name_prefix = patient_data['prefix'],
                    human_name = name_model
                )

            nickname = patient_data['photo'].split('.')[0]
            if nickname == "howardshore":
                nickname = "Concerning Hobbits"
            nickname_model = FHIR_Patient_name.objects.create(
                text = nickname,
                Patient = patient_model,
                use = FHIR_GP_HumanName.NameUseChoices.NICKNAME
            )

            address_model = FHIR_Patient_address.objects.create(
                Patient=patient_model,
                use=FHIR_GP_Address.AddressUse.OLD,
                city=patient_data.get('birthCity', ''),
                state=patient_data.get('birthState', ''),
                text=f"{patient_data.get('birthCity', '')}, {patient_data.get('birthState', '')}".strip(', ')
            )

            # Handle photo attachment
            if 'photo' in patient_data:
                photo_filename = patient_data['photo']
                photo_path = os.path.join(pictures_dir, photo_filename)
                
                if os.path.exists(photo_path):
                    photo_attachment = FHIR_Patient_photo(
                        Patient=patient_model,
                        contentType='image/' + photo_filename.split('.')[-1],
                        title=photo_filename,
                        size=os.path.getsize(photo_path),
                        time_datetime=datetime.datetime.now().replace(tzinfo=datetime.timezone.utc)
                    )
                    
                    # Open the file and save it to the upload_to field
                    with open(photo_path, 'rb') as f:
                        photo_attachment.upload_to.save(photo_filename, f)                    
                else:
                    print(f"Photo file not found: {photo_path}")
