from django.db import models
from django.core.validators import RegexValidator

from doctors.models import doctors_db
from patients_App.models import patients

# Create your models here.
class Receptionist(models.Model):
    name = models.CharField(max_length= 50)
    gender = models.CharField(max_length=14)
    age = models.SmallIntegerField()
    email = models.EmailField(unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{12}$', message="Phone number must be entered in the format: '+999999999'. upto 10 digits.")
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True) 
    username = models.CharField(max_length=24)
    password = models.CharField(max_length=180)

class authorization(models.Model):
    doctor = models.ForeignKey(doctors_db,on_delete=models.CASCADE,null=True,default=True)
    patient = models.ForeignKey(patients,on_delete=models.CASCADE,null=True,default=True)
    receptionist = models.ForeignKey(Receptionist,on_delete=models.CASCADE,null=True,default=True)
    dr_username = models.CharField(max_length=40,null=True,default=None)
    pt_username = models.CharField(max_length=40,null=True,default=None)
    r_username = models.CharField(max_length=40,null=True,default=None)
    authorization_key = models.CharField(max_length=100)
    authorized_at = models.DateTimeField(auto_now_add=True)