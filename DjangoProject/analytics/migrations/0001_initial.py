# Generated by Django 5.1.4 on 2025-01-09 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Salaries_for_years',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.FloatField()),
                ('year', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Salaries_for_years',
                'db_table': 'Salaries_for_years',
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('key_skills', models.TextField()),
                ('salary_from', models.FloatField(blank=True, null=True)),
                ('salary_to', models.FloatField(blank=True, null=True)),
                ('salary_currency', models.CharField(max_length=5)),
                ('area_name', models.CharField(max_length=50)),
                ('published_at', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'Vacancies',
            },
        ),
    ]
