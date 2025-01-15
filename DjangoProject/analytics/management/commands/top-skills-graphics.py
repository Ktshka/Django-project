from django.core.management.base import BaseCommand
import matplotlib.pyplot as plt
import numpy as np
from analytics.models import Top_skills

class Command(BaseCommand):
    def handle(self, *args, **options):
        top_skills = Top_skills.objects.all()
        unique_years = top_skills.values_list('year', flat=True).distinct()

        for year in unique_years:
            data = {}
            skills_frequency = top_skills.filter(year=year).values_list('skills', flat=True)

            if skills_frequency.exists():
                top_skills_dict = skills_frequency.first()
                for skill, frequency in top_skills_dict.items():
                    data[skill] = frequency

                title = f'Частотность популярных навыков в {year} году' if year != 0 else 'Частотность популярных навыков за всё время'
                labels = ['Частота навыка', title]

                fig, ax = plt.subplots(figsize=(10, 6))
                self.generate_vertical_graph(data, ax, labels)

                fig.tight_layout()
                plt.savefig('top_skills_{year}.png')
                plt.close(fig)

    def generate_vertical_graph(self, data, ax, labels):
        x = np.arange(len(data))
        skills = list(data.keys())
        values = list(data.values())

        ax.bar(x, values, label=labels[0])
        ax.set_title(labels[1], fontsize=16)
        ax.set_xticks(x)
        ax.set_xticklabels(skills, fontsize=8, rotation=70, ha='right')
        ax.tick_params(axis='y', labelsize=10)
        ax.legend(fontsize=10)
        ax.grid(axis='y')
