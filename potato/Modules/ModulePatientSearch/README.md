Because patient search is common functionality the search logic is all in
PotatoEMR\potato\Common\PatientSearch

For example this module does the top navbar search to find a patient,
but patient lists has its own search to add a patient to a list

The common search takes care of everything except what you do when you finally find the patient,
which in this case is just go to their patient overview page,
so this module only needs a template saying close the dropdown and go to the page:

{% extends 'Common_PatientSearch_resultPartial.html' %}

{% block patient_link_attrs %}
    href="{% url 'PatientOverview' patient.id %}" 
    onclick="this.closest('.dropdown-menu').classList.remove('show')"
{% endblock %}

and in the common base nav
      <a href="{% url 'SearchPatient' result_template='PatientSearch_result.html' result_args='none' %}"
passing in that result template, and no args needed