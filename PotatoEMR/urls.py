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
from potato.Modules.ModuleProblemList import ProblemList_view
from potato.Modules.ModuleImmunizations import Immunizations_view
from potato.Modules.ModuleGrowthChart import GrowthChart_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('empty', common_views.empty_view, name="empty"),
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

    path("patient/<int:patient_id>/encounter/<int:encounter_id>", AppointmentEncounter_view.overview, name="AppointmentEncounter_overview"),

    path("patient/<int:patient_id>/growth-chart", GrowthChart_view.GrowthChart_overview, name="GrowthChart_overview"),

    path("patient/<int:patient_id>/allergy-intolerance", AllergyIntoleranceBootstrap_view.allergy_intolerance_overview, name="AllergyIntoleranceBootstrap_overview"),
    path("patient/<int:patient_id>/allergy-intolerance-existing/<int:allergy_id>", AllergyIntoleranceBootstrap_view.allergy_intolerance_existing, name="AllergyIntoleranceBootstrap_existing"),
    path("patient/<int:patient_id>/allergy-intolerance-new", AllergyIntoleranceBootstrap_view.allergy_intolerance_new, name="AllergyIntoleranceBootstrap_new"),

    path("patient/<int:patient_id>/immunizations", Immunizations_view.immunization_overview, name="Immunizations_overview"),
    path("patient/<int:patient_id>/immunizations-existing/<int:immunization_id>", Immunizations_view.immunization_existing, name="Immunizations_existing"),
    path("patient/<int:patient_id>/immunizations-new", Immunizations_view.immunization_new, name="Immunizations_new"),

    path("patient/<int:patient_id>/problem-list", ProblemList_view.problem_list_overview, name="ProblemList_overview"),
    path("patient/<int:patient_id>/problem-list-existing/<int:condition_id>", ProblemList_view.problem_list_existing, name="ProblemList_existing"),
    path("patient/<int:patient_id>/problem-list-new", ProblemList_view.problem_list_new, name="ProblemList_new"),

]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)