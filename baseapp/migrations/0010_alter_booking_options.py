# Generated by Django 4.1 on 2022-08-11 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0009_alter_company_spots'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['-placed_at'],},
        ),
    ]
