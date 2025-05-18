"Search for patient by name, phone number, etc" is used in a lot of places in an EMR
So this is the common search to power that
    -Form to take search params
    -Function to match patients
    -Results of matching patients

For example, common_base.html which has the top level nav bar on all pages
has a search patient dropdown with a simple patient search which uses this.

ModulePatientLists has an add patient button to add patient to a list,
which also uses this.

PatientSearch GET -> PatientSearch POST (with params) -> Result list -> choose patient action
choose patient action uses a template you pass through all of these
may also have result args you pass through all of these, eg list id from PatientLists to know which to add to

For example the top level search template is:
    {% extends 'Common_PatientSearch_resultPartial.html' %}
    {% block patient_link_attrs %}
        href="{% url 'PatientOverview' patient.id %}" 
        onclick="this.closest('.dropdown-menu').classList.remove('show')"
    {% endblock %}

And the patient list add patient template is:
    {% extends 'Common_PatientSearch_resultPartial.html' %}
    {% block patient_link_attrs %}
        href="{% url 'PatientOverview' patient.id %}" 
        onclick="this.closest('.dropdown-menu').classList.remove('show')"
    {% endblock %}

So from the point of view of the module doing the search, you hit one (1) url: SearchPatient
    path("search-patient/<str:result_template>/<str:result_args>", CommonPatientSearch_view.SearchPatient, name="SearchPatient"),

