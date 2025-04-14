from django.shortcuts import render, redirect

def lists(request):
    return render(request, "PatientLists.html")
