from django.core.management import BaseCommand
from analytics.models import Vacancies_for_years, Vacancy
from django.db.models import Count
from django.db.models.functions import Substr

class Command(BaseCommand):
    def handle(self, *args, **options):
        data = Vacancy.objects.filter(published_at__isnull=False)
        Vacancies_for_years.objects.all().delete()

        data = (data.annotate(year=Substr('published_at', 1, 4))  
                .values('year')
                .annotate(amount_of_vacancies=Count('published_at')))
                 

        for item in data:
            Vacancies_for_years.objects.create(vacancies_amount=item['amount_of_vacancies'], year=item['year'])
