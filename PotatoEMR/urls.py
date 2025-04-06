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

from potato.Common import common_views
from potato.Common.HomePage import CommonHomePage_view
from potato.Common.Login import CommonLogin_view
from potato.ModuleRegisterPatient import view_registerPatient
from potato.ModulePatientOverview import view_patientOverview
# from potato.ModuleAddAllergyBigForm import view_AllergyBig
# from potato.ModuleAllergyIntoleranceTest import view_allergyIntoleranceTest
from potato.ModuleAllergyIntoleranceBootstrap import AllergyIntoleranceBootstrap_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('empty', common_views.empty_view, name="empty"),
    path('', CommonHomePage_view.home_page, name="CommonHomePage_index"),
    path('login', CommonLogin_view.login_page, name="CommonLogin_index"),
    path('login/', CommonLogin_view.login_page, name="CommonLogin_index"),

    path("patient-registration", view_registerPatient.create_patient, name="register_patient"),
    path("patient/<int:id>/", view_patientOverview.patient_overview, name="patient_overview"),

    # #allergy/intolerance, one big form
    # path("patient/<int:id>/allergy-intolerance-bigForm", view_AllergyBig.allergy_intolerance_bigForm, name="allergy_intolerance_bigForm"),
    # path("patient/allergy-intolerance-bigForm-reactionDetail/<int:allergy_id>", view_AllergyBig.allergy_intolerance_bigForm_reactionDetail, name="allergy_intolerance_bigForm_reactionDetail"),
 
    # #allergy/intolerance test
    # path("patient/<int:id>/test-allergy-intolerance", view_allergyIntoleranceTest.allergy_intolerance, name="allergy_intolerance"),
    # path("patient/<int:allergy_id>/test-allergy-form-allergy-row", view_allergyIntoleranceTest.allergy_form_allergy_row, name="allergy_form_allergy_row"),
    # path("patient/<int:patient_id>/test-allergy-form-get-new", view_allergyIntoleranceTest.allergy_form_get_new, name="allergy_form_get_new"),
    # path("patient/<int:patient_id>/test-allergy-form-save-new", view_allergyIntoleranceTest.allergy_form_save_new, name="allergy_form_save_new"),
    # path("patient/<int:allergy_id>/test-allergy-form-get-existing", view_allergyIntoleranceTest.allergy_form_get_existing, name="allergy_form_get_existing"),
    # path("patient/<int:allergy_id>/test-allergy-form-save-existing", view_allergyIntoleranceTest.allergy_form_save_existing, name="allergy_form_save_existing"),

    #allergy/intolerance bootstrap
    path("patient/<int:patient_id>/allergy-intolerance", AllergyIntoleranceBootstrap_view.allergy_intolerance_overview, name="AllergyIntoleranceBootstrap_overview"),
    path("patient/<int:patient_id>/allergy-intolerance-table", AllergyIntoleranceBootstrap_view.allergy_intolerance_table, name="AllergyIntoleranceBootstrap_table"),
    path("patient/<int:patient_id>/allergy-intolerance-existing/<int:allergy_id>", AllergyIntoleranceBootstrap_view.allergy_intolerance_existing, name="AllergyIntoleranceBootstrap_existing"),
    path("patient/<int:patient_id>/allergy-intolerance-new", AllergyIntoleranceBootstrap_view.allergy_intolerance_new, name="AllergyIntoleranceBootstrap_new"),
]
