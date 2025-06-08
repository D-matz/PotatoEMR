from django.http import HttpResponse
from django.core.management import call_command
from django.shortcuts import render
from potato.models import FHIR_GP_Binding

def empty_view(request):
    return HttpResponse("")

def save_codings_from_url(request):
    """
    View that takes a bindingURL parameter and runs the saveCodingsToDB command
    Usage: /save-codings/?bindingURL=https://hl7.org/fhir/valueset-condition-clinical.html
    """
    if request.method == 'GET':
        return render(request, 'save_codings_from_url.html')
    else:
        binding_url = request.POST.get('bindingURL')
    
        try:
            call_command('saveCodingsToDB', binding_url)
            num_codings = FHIR_GP_Binding.objects.get(binding_rule=binding_url).binding_codings.count()
            return render(request, 'save_codings_from_url.html', {'response': str(num_codings) + " codings for " + binding_url})
            
        except Exception as e:
            return render(request, 'save_codings_from_url.html', {'response': "Error: " +str(e)})

