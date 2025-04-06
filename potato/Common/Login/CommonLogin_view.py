from django.shortcuts import render

def login_page(request):
    return render(request, 'CommonLogin_index.html')

