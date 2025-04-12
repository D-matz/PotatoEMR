from django.contrib import admin

from .models_dir.FHIR_Resources.AllergyIntolerance import FHIR_AllergyIntolerance

class AllergyIntoleranceAdmin(admin.ModelAdmin):
    pass

admin.site.register(FHIR_AllergyIntolerance, AllergyIntoleranceAdmin)