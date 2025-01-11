from django.db import models


class Vacancy(models.Model):
    name = models.CharField(max_length=150)
    key_skills = models.TextField()
    salary_from = models.FloatField(null=True, blank=True)
    salary_to = models.FloatField(null=True, blank=True)
    salary_currency = models.CharField(max_length=5)
    area_name = models.CharField(max_length=50)
    published_at = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Vacancies'


class Salaries_for_years(models.Model):
    salary = models.FloatField()
    year = models.IntegerField()
    
    class Meta:
        verbose_name_plural = 'Salaries_for_years'
        db_table = 'Salaries_for_years'