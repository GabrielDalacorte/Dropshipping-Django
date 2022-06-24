# Generated by Django 3.2.7 on 2022-06-21 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0003_product_departament'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='max_price',
        ),
        migrations.AddField(
            model_name='product',
            name='min_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]