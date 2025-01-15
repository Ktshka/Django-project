from django.shortcuts import render
from analytics.models import *

def main(request):
    data = Vacancy.objects.all()
    a = Vacancy.objects.filter(name = 'a')

    return render(request, 'main.html')

def demand_full(request):
    salaries_for_years = Salaries_for_years.objects.all()
    vacancies_for_years = Vacancies_for_years.objects.all()

    return render(request, 'demand.html', 
    {'salaries_for_years' : salaries_for_years, 'vacancies_for_years' : vacancies_for_years})

def geography_full(request):
    salaries_for_cities = Salaries_for_cities.objects.all()
    vacancies_for_cities = Vacancies_for_cities.objects.all()

    return render(request, 'geography.html', 
    {'salaries_for_cities' : salaries_for_cities, 'vacancies_for_cities' : vacancies_for_cities})

def skills_full(request):
    top_skills = Top_skills.objects.all()

    return render(request, 'skills.html', {'top_skills' : top_skills})

def statistics(request):
    salaries_for_years = Salaries_for_years.objects.all()
    vacancies_for_years = Vacancies_for_years.objects.all()
    salaries_for_cities = Salaries_for_cities.objects.all()
    vacancies_for_cities = Vacancies_for_cities.objects.all()
    top_skills = Top_skills.objects.all()

    return render(request, 'statistics.html', {'salaries_for_years' : salaries_for_years, 'vacancies_for_years' : vacancies_for_years, 'salaries_for_cities' : salaries_for_cities, 'vacancies_for_cities' : vacancies_for_cities, 'top_skills' : top_skills})