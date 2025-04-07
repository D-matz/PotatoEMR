from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_not_required
from allauth.account.views import LoginView, SignupView

@login_not_required
def logout_view(request):
    logout(request)
    return redirect('CommonLogin_loginIndex')

@login_not_required
class CustomLoginView(LoginView):
    template_name = "CommonLogin_loginIndex.html"

@login_not_required
class CustomLoginViewPartial(LoginView):
    template_name = "CommonLogin_loginPartial.html"

@login_not_required
class CustomSignupView(SignupView):
    template_name = "CommonLogin_signupIndex.html"

@login_not_required
class CustomSignupViewPartial(SignupView):
    template_name = "CommonLogin_signupPartial.html"
