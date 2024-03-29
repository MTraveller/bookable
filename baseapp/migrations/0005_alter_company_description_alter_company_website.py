# Generated by Django 4.0.6 on 2022-07-25 18:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0004_category_company_in_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='website',
            field=models.CharField(max_length=255, validators=[django.core.validators.URLValidator()]),
        ),
    ]
