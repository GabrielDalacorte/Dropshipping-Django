# Generated by Django 3.2.7 on 2022-06-21 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('parameter_id', models.IntegerField(primary_key=True, serialize=False)),
                ('url', models.URLField(max_length=300)),
                ('price', models.FloatField()),
                ('name', models.CharField(max_length=150)),
                ('sales_number', models.IntegerField()),
                ('description', models.TextField(blank=True, max_length=400, null=True)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
