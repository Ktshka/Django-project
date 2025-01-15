from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Vacancy)
admin.site.register(Salaries_for_years)
admin.site.register(Vacancies_for_years)
admin.site.register(Salaries_for_cities)
admin.site.register(Vacancies_for_cities)
admin.site.register(Top_skills)
admin.site.register(Currencies)