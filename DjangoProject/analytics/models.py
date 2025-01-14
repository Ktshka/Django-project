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
        db_table = 'Vacancies'


class Salaries_for_years(models.Model):
    salary = models.FloatField()
    year = models.IntegerField()
    
    class Meta:
        verbose_name_plural = 'Salaries_for_years'
        db_table = 'Salaries_for_years'


class Vacancies_for_years(models.Model):
    vacancies_amount = models.IntegerField()
    year = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Vacancies_for_years'
        db_table = 'Vacancies_for_years'


class Salaries_for_cities(models.Model):
    average_salary = models.FloatField()
    city = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = 'Salaries_for_cities'
        db_table = 'Salaries_for_cities'


class Vacancies_for_cities(models.Model):
    share_of_vacancies = models.FloatField()
    city = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = 'Vacancies_for_cities'
        db_table = 'Vacancies_for_cities'


class Top_skills(models.Model):
    skills = models.JSONField()
    year = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Top_skills'
        db_table = 'Top_skills'


class Currencies(models.Model):
    date = models.DateField()
    cur_code = models.CharField(max_length = 5)
    currencies = models.FloatField()

    class Meta:
        verbose_name_plural = 'Currencies'
        db_table = 'Currencies'
        unique_together = ('cur_code', 'date')