from django.shortcuts import render
from analytics.models import *

def main(request):
    data = Vacancy.objects.all()
    a = Vacancy.objects.filter(name = 'a')

    return render(request, 'main.html')

def Extra2(request):
    data = ['a', 'b', 'c']
    return render(request, 'index.html', {'cycle_name': data})
