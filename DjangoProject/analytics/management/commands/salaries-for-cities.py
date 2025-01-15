from django.core.management.base import BaseCommand
from django.db.models import F, Avg, Count
from django.db.models.functions import Round
from analytics.models import Vacancy, Currencies, Salaries_for_cities

class Command(BaseCommand):
    help = 'Generate general statistics of vacancies'

    def handle(self, *args, **kwargs):
        Salaries_for_cities.objects.all().delete()
        data = Vacancy.objects.all()
        bd = Currencies.objects.all()

        currency_dict = {(item.date.strftime('%Y-%m-%d'), item.cur_code): item.currencies for item in bd}

        for item in data:
            if item.salary_currency and item.salary_currency != 'RUR':
                date = item.published_at.replace(day=1)
                exchange_rate = currency_dict.get((date.strftime('%Y-%m-%d'), item.salary_currency), 0)
                item.salary_from = float(item.salary_from or 0) * exchange_rate
                item.salary_to = float(item.salary_to or 0) * exchange_rate

        data = data.filter(salary_from__lte=10000000, salary_to__lte=10000000)

        data = data.annotate(av_salary=((F('salary_from') + F('salary_to')) / 2))
        total = data.count()

        data = data.annotate(area=F('area_name'))  
        data = data.values('area_name')  
        data = data.annotate(count_vacancies=Count('area_name'))  
        data = data.filter(count_vacancies__gt=total * 0.01)  
        data = data.annotate(average_salary=Round(Avg('av_salary'), 2))

        for item in data:
            Salaries_for_cities.objects.create(city=item['area_name'], average_salary=item['average_salary'])