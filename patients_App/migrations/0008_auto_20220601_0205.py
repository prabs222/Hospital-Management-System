# Generated by Django 2.1.5 on 2022-06-01 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients_App', '0007_medicalhistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookappointments',
            name='medications_pr',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='bookappointments',
            name='tests_pr',
            field=models.CharField(blank=True, default=None, max_length=300, null=True),
        ),
    ]