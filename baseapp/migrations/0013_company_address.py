# Generated by Django 4.1 on 2022-08-16 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0012_company_previous_brand_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='address',
            field=models.CharField(max_length=255),
            preserve_default=False,
        ),
    ]