"""PotatoEMR URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse

from potato.Common import common_views
from potato.Common.Login import CommonLogin_view
from potato.Common.PatientSearch import CommonPatientSearch_view
from potato.Modules.ModuleHomePage import CommonHomePage_view
from potato.Modules.ModuleRegisterPatient import view_registerPatient
from potato.Modules.ModulePatientOverview import view_patientOverview
from potato.Modules.ModuleAllergyIntoleranceBootstrap import AllergyIntoleranceBootstrap_view
from potato.Modules.ModuleAppointmentCalendar import AppointmentCalendar_view
from potato.Modules.ModulePatientLists import PatientLists_view
from potato.Modules.ModuleAppointmentEncounter import AppointmentEncounter_view
from potato.Modules.ModuleEncounters import Encounters_view
from potato.Modules.ModuleProblemList import ProblemList_view
from potato.Modules.ModuleImmunizations import Immunizations_view
from potato.Modules.ModuleGrowthChart import GrowthChart_view
from potato.Modules.ModuleOrders import Orders_view
from potato.Modules.ModuleMedications import Medications_view
from potato.Modules.ModuleLabResults import LabResults_view
from potato.Modules.ModuleNotes import Notes_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('empty', common_views.empty_view, name="empty"),
    path('save-codings/', common_views.save_codings_from_url, name="save_codings_from_url"),
    path('', CommonHomePage_view.home_page, name="CommonHomePage_index"),
    path("login", CommonLogin_view.CustomLoginView.as_view(), name="CommonLogin_loginIndex"),
    path("login/", CommonLogin_view.CustomLoginView.as_view(), name="CommonLogin_loginIndex"),
    path("login_partial", CommonLogin_view.CustomLoginViewPartial.as_view(), name="CommonLogin_loginPartial"),
    path("signup", CommonLogin_view.CustomSignupView.as_view(), name="CommonSignup_signupIndex"),
    path("signup/", CommonLogin_view.CustomSignupView.as_view(), name="CommonSignup_signupIndex"),
    path("signup_partial", CommonLogin_view.CustomSignupViewPartial.as_view(), name="CommonSignup_signupPartial"),
    path('logout', CommonLogin_view.logout_view, name="CommonLogout_index"),
    path('logout/', CommonLogin_view.logout_view, name="CommonLogout_index"),
    path('accounts/', include('allauth.urls')),

    path('calendar', AppointmentCalendar_view.calendar_whole, name="home_calendar"),
    path('calendar-partial', AppointmentCalendar_view.calendar_partial, name="home_calendar_partial"),
    path('calendar-appt-peek/<int:appt_id>', AppointmentCalendar_view.calendar_peek, name="home_calendar_peek"),

    path("register-patient", view_registerPatient.create_patient, name="RegisterPatient"),
    path("search-patient/<str:result_template>/<str:result_args>", CommonPatientSearch_view.SearchPatient, name="SearchPatient"),

    path("patient/<int:patient_id>/", view_patientOverview.patient_overview, name="PatientOverview"),
    path("explorer/<str:model_name>/<int:model_id>", view_patientOverview.explorer_row, name="PatientOverview_explorer"),

    path("patient-lists", PatientLists_view.lists, name="home_patient_lists"),
    path("patient-lists/<int:list_id>", PatientLists_view.get_patient_list, name="PatientLists_get"),
    path("patient-lists/create", PatientLists_view.create_patient_list, name="PatientLists_create"),
    path("patient-lists/edit-title/<int:list_id>", PatientLists_view.edit_title, name="PatientLists_editTitle"),
    path("patient-lists/saved-title/<int:list_id>", PatientLists_view.saved_title, name="PatientLists_savedTitle"),
    path("patient-lists/delete/<int:list_id>", PatientLists_view.delete_list, name="PatientLists_delete"),
    path("patient-lists/searchModal/<int:list_id>", PatientLists_view.searchModal, name="PatientLists_searchModal"),
    path("patient-lists/remove-patient/<int:list_id>/<int:patient_id>", PatientLists_view.remove_patient, name="PatientLists_removePatient"),
    path("patient-lists/add-patient/<int:list_id>/<int:patient_id>", PatientLists_view.add_patient, name="PatientLists_addPatient"),

    path("patient/<int:patient_id>/appointment-encounter/<int:encounter_id>", AppointmentEncounter_view.overview, name="AppointmentEncounter_overview"),

    path("patient/<int:patient_id>/encounters", Encounters_view.encounters_table, name="Encounters_table"),
    path("patient/<int:patient_id>/encounters/new", Encounters_view.encounters_new, name="Encounters_new"),
    path("patient/<int:patient_id>/encounters/<int:encounter_id>/edit", Encounters_view.encounters_existing_edit, name="Encounters_edit"),
    path("patient/<int:patient_id>/encounters/<int:encounter_id>/cancel", Encounters_view.encounters_existing_cancel, name="Encounters_cancel"),

    path("patient/<int:patient_id>/growth-chart", GrowthChart_view.GrowthChart_overview, name="GrowthChart_overview"),

    path("patient/<int:patient_id>/orders", Orders_view.orders_table, name="Orders_table"),
    path("patient/<int:patient_id>/medication-request/new", Orders_view.medicationRequest_new, name="Orders_medicationRequest_new"),
    path("patient/<int:patient_id>/medication-request/<int:med_request_id>/edit", Orders_view.medicationRequest_existing_edit, name="Orders_medicationRequest_existing_edit"),
    path("patient/<int:patient_id>/medication-request/<int:med_request_id>/cancel", Orders_view.medicationRequest_existing_cancel, name="Orders_medicationRequest_existing_cancel"),

    path("patient/<int:patient_id>/lab-results", LabResults_view.labResults_table, name="LabResults_table"),
    path("patient/<int:patient_id>/lab-results/new", LabResults_view.labResults_new, name="LabResults_new"),
    path("patient/<int:patient_id>/lab-results/<int:diagnosticReport_id>/edit", LabResults_view.labResults_existing_edit, name="LabResults_existing_edit"),
    path("patient/<int:patient_id>/lab-results/<int:diagnosticReport_id>/cancel", LabResults_view.labResults_existing_cancel, name="LabResults_existing_cancel"),

    path("patient/<int:patient_id>/medication", Medications_view.medication_table, name="Medication_table"),
    path("patient/<int:patient_id>/medication/dispense", Medications_view.medication_dispense_table, name="Medication_dispense_table"),
    path("patient/<int:patient_id>/medication/dispense/new", Medications_view.medicationDispense_new, name="Medication_dispense_new"),
    path("patient/<int:patient_id>/medication/dispense/<int:med_dispense_id>/edit", Medications_view.medicationDispense_existing_edit, name="Medication_dispense_edit"),
    path("patient/<int:patient_id>/medication/dispense/<int:med_dispense_id>/cancel", Medications_view.medicationDispense_existing_cancel, name="Medication_dispense_cancel"),
    path("patient/<int:patient_id>/medication/administration", Medications_view.medication_administration_table, name="Medication_administration_table"),
    path("patient/<int:patient_id>/medication/administration/new", Medications_view.medicationAdministration_new, name="Medication_administration_new"),
    path("patient/<int:patient_id>/medication/administration/<int:med_admin_id>/edit", Medications_view.medicationAdministration_existing_edit, name="Medication_administration_edit"),
    path("patient/<int:patient_id>/medication/administration/<int:med_admin_id>/cancel", Medications_view.medicationAdministration_existing_cancel, name="Medication_administration_cancel"),
    

    path("patient/<int:patient_id>/allergy-intolerance", AllergyIntoleranceBootstrap_view.allergy_intolerance_overview, name="AllergyIntoleranceBootstrap_overview"),
    path("patient/<int:patient_id>/allergy-intolerance-existing/<int:allergy_id>", AllergyIntoleranceBootstrap_view.allergy_intolerance_existing, name="AllergyIntoleranceBootstrap_existing"),
    path("patient/<int:patient_id>/allergy-intolerance-new", AllergyIntoleranceBootstrap_view.allergy_intolerance_new, name="AllergyIntoleranceBootstrap_new"),

    path("patient/<int:patient_id>/immunizations", Immunizations_view.immunization_overview, name="Immunizations_overview"),
    path("patient/<int:patient_id>/immunizations-existing/<int:immunization_id>", Immunizations_view.immunization_existing, name="Immunizations_existing"),
    path("patient/<int:patient_id>/immunizations-new", Immunizations_view.immunization_new, name="Immunizations_new"),

    path("patient/<int:patient_id>/problem-list", ProblemList_view.problem_list_overview, name="ProblemList_overview"),
    path("patient/<int:patient_id>/problem-list-existing/<int:condition_id>", ProblemList_view.problem_list_existing, name="ProblemList_existing"),
    path("patient/<int:patient_id>/problem-list-new", ProblemList_view.problem_list_new, name="ProblemList_new"),

    path("patient/<int:patient_id>/notes", Notes_view.notes_table, name="Notes_table"),
    path("patient/<int:patient_id>/notes/new", Notes_view.notes_new, name="Notes_new"),
    path("patient/<int:patient_id>/notes/<int:note_id>/edit", Notes_view.notes_existing_edit, name="Notes_edit"),
    path("patient/<int:patient_id>/notes/<int:note_id>/cancel", Notes_view.notes_existing_cancel, name="Notes_cancel"),

]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)