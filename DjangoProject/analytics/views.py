from django.shortcuts import render
from analytics.models import *

def Extra(request):
    data = Vacancy.objects.all()
    a = Vacancy.objects.filter(name = 'a')

    return render(request, 'shablon.html')

def Extra2(request):
    data = ['a', 'b', 'c']
    return render(request, 'index.html', {'cycle_name': data})
