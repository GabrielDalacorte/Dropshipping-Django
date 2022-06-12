# Generated by Django 3.2.7 on 2022-06-12 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('parameter_id', models.IntegerField(primary_key=True, serialize=False)),
                ('departments', models.CharField(choices=[('Eletronicos', 'Eletronicos'), ('Acessorios', 'Acessorios')], max_length=100)),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
            },
        ),
    ]
