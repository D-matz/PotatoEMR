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
from potato.ModuleRegisterPatient import view_registerPatient
from potato.ModulePatientOverview import view_patientOverview
from potato.ModuleAddAllergyBigForm import view_AllergyBig
from potato.ModuleAllergyIntolerance import view_allergyIntolerance

urlpatterns = [
    path('admin/', admin.site.urls),
    path('empty', common_views.empty_view, name="empty"),
    path("patient-registration", view_registerPatient.create_patient, name="register_patient"),
    path("patient/<int:id>/", view_patientOverview.patient_overview, name="patient_overview"),

    #allergy/intolerance, one big form
    path("patient/<int:id>/allergy-intolerance-bigForm", view_AllergyBig.allergy_intolerance_bigForm, name="allergy_intolerance_bigForm"),
    path("patient/allergy-intolerance-bigForm-reactionDetail/<int:allergy_id>", view_AllergyBig.allergy_intolerance_bigForm_reactionDetail, name="allergy_intolerance_bigForm_reactionDetail"),
 
    #allergy/intolerance
    path("patient/<int:id>/allergy-intolerance", view_allergyIntolerance.allergy_intolerance, name="allergy_intolerance"),
    path("patient/<int:allergy_id>/allergy-form-allergy-row", view_allergyIntolerance.allergy_form_allergy_row, name="allergy_form_allergy_row"),
    path("patient/<int:patient_id>/allergy-form-get-new", view_allergyIntolerance.allergy_form_get_new, name="allergy_form_get_new"),
    path("patient/<int:patient_id>/allergy-form-save-new", view_allergyIntolerance.allergy_form_save_new, name="allergy_form_save_new"),
    path("patient/<int:allergy_id>/allergy-form-get-existing", view_allergyIntolerance.allergy_form_get_existing, name="allergy_form_get_existing"),
    path("patient/<int:allergy_id>/allergy-form-save-existing", view_allergyIntolerance.allergy_form_save_existing, name="allergy_form_save_existing"),
]
