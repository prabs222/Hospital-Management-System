from django.db import models
from django.core.validators import RegexValidator
from pytz import timezone
# from doctors import doctors_db

from doctors.models import doctors_db, speciality_mod
# Create your models here.
class patients(models.Model):
    # patient_id = models.AutoField(primary_key=True,default=True)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=12)
    age= models.IntegerField()
    dob = models.DateField(auto_now=False,default=False)
    email = models.EmailField(unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{12}$', message="Phone number must be entered in the format: '+999999999'. upto 10 digits.")
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True) # Validators should be a list
    aadhar = models.CharField(max_length=16, unique=True)
    username = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=150)
    occupation = models.CharField(max_length=40)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=20)
    pin = models.CharField(max_length=10)
    registered_at = models.DateTimeField( auto_now=False)
    

# class medical_history(models.Model):
    # patientId=models.PositiveIntegerField(null=True)
    # doctorId=models.PositiveIntegerField(null=True)s
    # patientName=models.CharField(max_length=40,null=True)
    # doctorName=models.CharField(max_length=40,null=True)
    # appointmentDate=models.DateField(auto_now=True)
    # description=models.TextField(max_length=500)
    # status=models.BooleanField(default=False)

class bookappointments(models.Model):
    patient = models.ForeignKey('patients',on_delete=models.CASCADE, default=None)
    username = models.CharField(max_length=40)
    symptoms = models.TextField()
    specialist = models.ForeignKey('doctors.speciality_mod',on_delete=models.CASCADE)
    doctors_app = models.ForeignKey('doctors.doctors_db',on_delete=models.CASCADE)
    date_app = models.DateField(auto_now=False,default=False)
    time_app = models.CharField(max_length=40)
    is_pending = models.BooleanField(default=True)
    receptionist_resp = models.BooleanField(null=True, default=None)
    dr_resp = models.BooleanField(null = True , default=None)
    reject_reason = models.TextField(null = True, default=None)
    has_paid = models.BooleanField(default=False)
    medications_pr = models.CharField(max_length=1000,null=True,blank=True,default=None)
    tests_pr = models.CharField(max_length=300,null=True,blank=True,default=None)
    presciption_uploaded = models.BooleanField(default=False)

class medicalhistory(models.Model):
    patient = models.ForeignKey('patients',on_delete=models.CASCADE)
    height = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    drug_allergies = models.TextField()
    illnesses = models.TextField()
    operations = models.TextField()
    medications_history = models.TextField()
    habits = models.TextField()
    extrainfo = models.TextField()

# class prescription(models.Model):
#     medications_pr = models.CharField(max_length=1000)
#     tests_pr = models.CharField(max_length=300)
#     appointment = models.ForeignKey(bookappointments,on_delete=models.CASCADE)
#     aptdate = models.DateField(auto_now=False)