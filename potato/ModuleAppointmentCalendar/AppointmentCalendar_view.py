from django.shortcuts import render, redirect
from datetime import date, datetime

def calendar(request):
    return render(request, "AppointmentCalendar_home.html", {'today': date.today()})

def calendar_partial(request):
    return render(request, "AppointmentCalendar_partial.html", {'today': date.today()})

def dateAppointmentList_partial(request):
    selected_datestr = request.GET.get('selected_date')
    if selected_datestr:
        date_obj = datetime.strptime(selected_datestr, '%Y-%m-%d').date()
    else:
        date_obj = date.today()
    return render(request, "AppointmentCalendar_DateAppointmentTable_partial.html", {'seeDate': date_obj})
