# Generated by Django 2.1.5 on 2022-05-28 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients_App', '0004_auto_20220528_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookappointments',
            name='dr_resp',
            field=models.BooleanField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='bookappointments',
            name='receptionist_resp',
            field=models.BooleanField(default=None, null=True),
        ),
    ]
