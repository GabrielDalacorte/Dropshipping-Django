# Generated by Django 3.2.7 on 2022-06-21 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0004_auto_20220621_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
