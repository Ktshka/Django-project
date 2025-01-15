from django.core.management import BaseCommand
import matplotlib.pyplot as plt
import numpy as np
from analytics.models import Vacancies_for_years
import pandas as pd


class Command(BaseCommand):
    def handle(self, *args, **options):
        data = Vacancies_for_years.objects.all().values('year', 'vacancies_amount')
        stats = self.get_vacancy_stats(data)
        labels = ['vacancy', 'Vacancies for year']

        fig, ax = plt.subplots()
        self.generate_vertical_graph(stats, ax, labels)

        fig.tight_layout()
        plt.savefig('vacancies_for_years.png')
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

    def get_vacancy_stats(self, data):
        df = pd.DataFrame(data)
        vacancy_for_year = df.set_index('year')['vacancies_amount'].to_dict()
        return vacancy_for_year
