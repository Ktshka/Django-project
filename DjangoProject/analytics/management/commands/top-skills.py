from django.core.management.base import BaseCommand
from analytics.models import Vacancy, Top_skills

class Command(BaseCommand):
    def handle(self, *args, **options):
        Top_skills.objects.all().delete()
        all_vacancies = Vacancy.objects.all()
        skills = {}

        overall_skills = {}

        for vacancy in all_vacancies:
            year = vacancy.published_at.year
            skills_string = vacancy.key_skills

            if isinstance(skills_string, str):
                skills_list = skills_string.replace('\n', ',').replace(';', ',').split(',')
                skills_list = [skill.strip() for skill in skills_list if skill.strip()]

                for skill in skills_list:
                    if year not in skills:
                        skills[year] = {}
                    if skill not in skills[year]:
                        skills[year][skill] = 0
                    skills[year][skill] += 1

                    if skill not in overall_skills:
                        overall_skills[skill] = 0
                    overall_skills[skill] += 1

        top_skills_sorted = {
            year: dict(sorted(skill_counts.items(), key=lambda item: item[1], reverse=True)[:20])
            for year, skill_counts in skills.items()
        }

        for year, skills in top_skills_sorted.items():
            Top_skills.objects.create(year=year, skills=skills)

    
