# Generated by Django 4.1 on 2022-08-17 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0014_alter_company_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='latitude',
            field=models.CharField(max_length=255),
        ),
        migrations.AddField(
            model_name='company',
            name='longitude',
            field=models.CharField(max_length=255),
        ),
    ]
