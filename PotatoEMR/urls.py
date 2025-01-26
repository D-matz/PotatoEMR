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

from potato.ModuleRegisterPatient import view_registerPatient
from potato.ModulePatientOverview import view_patientOverview
from potato.ModuleAddAllergy import view_allergyIntolerance

urlpatterns = [
    path('admin/', admin.site.urls),
    path("patient-registration", view_registerPatient.create_patient, name="register_patient"),
    path("patient/<int:id>/", view_patientOverview.patient_overview, name="patient_overview"),
    path("patient/<int:id>/allergy-intolerance", view_allergyIntolerance.allergy_intolerance, name="allergy_intolerance"),
    path("patient/allergy-intolerance-reactionDetail/<int:allergy_id>", view_allergyIntolerance.allergy_intolerance_reactionDetail, name="allergy_intolerance_reactionDetail"),
]
