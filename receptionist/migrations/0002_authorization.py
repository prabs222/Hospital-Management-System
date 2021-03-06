# Generated by Django 2.1.5 on 2022-05-30 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients_App', '0006_auto_20220529_0058'),
        ('doctors', '0001_initial'),
        ('receptionist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='authorization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dr_username', models.CharField(default=None, max_length=40, null=True)),
                ('pt_username', models.CharField(default=None, max_length=40, null=True)),
                ('r_username', models.CharField(default=None, max_length=40, null=True)),
                ('authorization_key', models.CharField(max_length=100)),
                ('authorized_at', models.DateTimeField(auto_now_add=True)),
                ('doctor', models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctors.doctors_db')),
                ('patient', models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patients_App.patients')),
                ('receptionist', models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='receptionist.Receptionist')),
            ],
        ),
    ]
