from django.core.management import BaseCommand
from analytics.models import Vacancies_for_cities, Vacancy
from django.db.models import F, Count
from django.db.models.functions import Round

class Command(BaseCommand):
    def handle(self, *args, **options):
        data = Vacancy.objects.filter(published_at__isnull=False)
        Vacancies_for_cities.objects.all().delete()

        total = data.count()

        data = data.annotate(area=F('area_name'))  
        data = data.values('area_name') 
        data = data.annotate(count_vacancies=Count('area_name'))  
        data = data.filter(count_vacancies__gt=total * 0.01)  
        data = data.annotate(share_of_vacancies=Round(Count('id') * 1.0 / total, 4))

        data = data.order_by('-count_vacancies')

        for item in data:
            Vacancies_for_cities.objects.create(share_of_vacancies = item['share_of_vacancies'], city=item['area_name'])