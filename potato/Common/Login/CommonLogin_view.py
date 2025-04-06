from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.urls import reverse
from django.contrib.auth.decorators import login_not_required

@login_not_required
def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.POST.get('next', '')
                if next_url:
                    return redirect(next_url)
                return redirect(reverse('CommonHomePage_index'))
    else:
        form = AuthenticationForm()
    
    return render(request, 'CommonLogin_index.html', {
        'form': form,
        'next': request.GET.get('next', '')
    })

