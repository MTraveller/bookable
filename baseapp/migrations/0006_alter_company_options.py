# Generated by Django 4.0.6 on 2022-07-26 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0005_alter_company_description_alter_company_website'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['company_name'],},
        ),
    ]
