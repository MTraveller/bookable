# Generated by Django 4.0.6 on 2022-07-29 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0006_alter_company_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['company_name']},
        ),
        migrations.AlterField(
            model_name='category',
            name='company_in_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='baseapp.company'),
        ),
    ]
