from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class doctors_db(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50,default=False)
    dob = models.DateField(auto_now=False,default=False)
    gender = models.CharField(max_length=12)
    age= models.IntegerField()
    qualifications = models.TextField(default=False)
    workexperience = models.TextField(default=False)
    speciality = models.ForeignKey('speciality_mod',on_delete=models.CASCADE)
    aadhar = models.BigIntegerField(unique=True)
    email = models.EmailField(unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{12}$', message="Phone number must be entered in the format: '+999999999'. upto 10 digits.")
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True) # Validators should be a list
    address = models.CharField(max_length=150)
    username = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=150)
    city = models.CharField(max_length=40,default=False)
    state = models.CharField(max_length=40,default=False)
    pin = models.CharField(max_length=6,default=False)
    registered_at = models.DateTimeField(auto_now=False)

class speciality_mod(models.Model):
    specialities = models.CharField(max_length=40)
    specialization = models.CharField(max_length=40)