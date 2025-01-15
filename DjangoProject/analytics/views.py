from django.shortcuts import render
from analytics.models import *

def main(request):
    data = Vacancy.objects.all()
    a = Vacancy.objects.filter(name = 'a')

    return render(request, 'main.html')

def Extra2(request):
    data = ['a', 'b', 'c']
    return render(request, 'index.html', {'cycle_name': data})

def demand_full(request):
    salaries_for_years = Salaries_for_years.objects.all()
    vacancies_for_years = Vacancies_for_years.objects.all()

    return render(request, 'demand.html', 
    {'salaries_for_years' : salaries_for_years, 'vacancies_for_years' : vacancies_for_years})
