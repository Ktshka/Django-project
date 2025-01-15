from django.core.management import BaseCommand
import matplotlib.pyplot as plt
import numpy as np
from analytics.models import Vacancies_for_cities
import pandas as pd


class Command(BaseCommand):
    def handle(self, *args, **options):
        data = Vacancies_for_cities.objects.all().values('city', 'share_of_vacancies')
        stats = self.get_salary_stats(data)
        labels = ['city', 'Vacancy for city']

        fig, ax = plt.subplots()
        self.generate_vertical_graph(stats, ax, labels)

        fig.tight_layout()
        plt.savefig('vacancies_for_cities.png')
        plt.show()

    def generate_vertical_graph(self, stats, ax, labels):
        x = np.arange(len(stats))
        cities = list(stats.keys())
        values = list(stats.values())

        ax.bar(x, values, label=labels[0])
        ax.set_title(labels[1], fontsize=12)
        ax.set_xticks(x)
        ax.set_xticklabels(cities, fontsize=10, rotation=90)
        ax.tick_params(axis='y', labelsize=10)
        ax.legend(fontsize=10)
        ax.grid(axis='y')

    def get_salary_stats(self, data):
        df = pd.DataFrame(data)
        salary_for_city = df.set_index('city')['share_of_vacancies'].to_dict()
        return salary_for_city
