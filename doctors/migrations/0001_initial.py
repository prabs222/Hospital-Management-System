# Generated by Django 2.1.5 on 2022-05-24 23:10

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='doctors_db',
            fields=[
                ('doctor_id', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(default=False, max_length=50)),
                ('dob', models.DateField(default=False)),
                ('gender', models.CharField(max_length=12)),
                ('age', models.IntegerField()),
                ('qualifications', models.TextField(default=False)),
                ('workexperience', models.TextField(default=False)),
                ('aadhar', models.BigIntegerField(unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. upto 10 digits.", regex='^\\+?1?\\d{12}$')])),
                ('address', models.CharField(max_length=150)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=150)),
                ('city', models.CharField(default=False, max_length=40)),
                ('state', models.CharField(default=False, max_length=40)),
                ('pin', models.CharField(default=False, max_length=6)),
                ('registered_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='speciality_mod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialities', models.CharField(max_length=40)),
                ('specialization', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='doctors_db',
            name='speciality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.speciality_mod'),
        ),
    ]
