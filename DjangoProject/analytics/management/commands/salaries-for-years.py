from django.core.management.base import BaseCommand
from django.db.models import F, Avg
from django.db.models.functions import Substr, Round
from analytics.models import Vacancy, Currencies, Salaries_for_years

class Command(BaseCommand):
    help = 'Generate general statistics of vacancies'

    def handle(self, *args, **kwargs):
        Salaries_for_years.objects.all().delete()
        data = Vacancy.objects.all()
        bd = Currencies.objects.all()

        # Преобразуем bd в словарь для более удобного доступа
        currency_dict = {(item.date.strftime('%Y-%m-%d'), item.cur_code): item.currencies for item in bd}

        # Преобразуем зарплаты в рубли
        for item in data:
            if item.salary_currency and item.salary_currency != 'RUR':
                date = item.published_at.replace(day=1)
                exchange_rate = currency_dict.get((date.strftime('%Y-%m-%d'), item.salary_currency), 0)
                item.salary_from = float(item.salary_from or 0) * exchange_rate
                item.salary_to = float(item.salary_to or 0) * exchange_rate

        # Фильтруем вакансии, чтобы убрать те, у которых зарплата выше 10 миллионов рублей
        data = data.filter(salary_from__lte=10000000, salary_to__lte=10000000)

        # Рассчитываем среднее значение (salary_from + salary_to) / 2
        data = data.annotate(avg_salary=((F('salary_from') + F('salary_to')) / 2))

        data = (data.annotate(year=Substr('published_at', 1, 4))  # Аннотируем данные, извлекая год из даты публикации
                .values('year')  # Группируем данные по годам
                .annotate(avg_salary=Round(Avg('avg_salary'), 2)))  # Рассчитываем среднюю зарплату по годам и округляем до 2 знаков после запятой

        # Сохраняем новые данные в модель Salary_by_year
        for item in data:
            Salaries_for_years.objects.create(year=item['year'], salary=item['avg_salary'])