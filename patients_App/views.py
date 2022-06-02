from django.http import JsonResponse
import string
import secrets

from doctors.models import doctors_db, speciality_mod
from receptionist.models import Receptionist, authorization
from .models import  medicalhistory, patients ,bookappointments
from django.contrib.auth.hashers import make_password, check_password
import json,re
from time import tzname
from pytz import timezone
import datetime

def RegisterPatient(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        Name = body["name"]
        Gender = body["gender"]
        Dob = body["dob"]
        Age = body["age"]
        Occupation = body["occupation"]
        User_name=body["username"]
        Address = body["address"]
        Email_Id=body["email"]
        Pass_word=body["pass"]
        C_Password = body["cpass"]
        Aadhar = body["aadhar"]
        Phone = body["phone_number"]
        City = body["city"]
        State = body["state"]
        Pin = body["pin"]
        emailformat = "^[a-zA-Z0-9\-\_\.]+@[a-zA-Z0-9]{2,}\.[a-zA-Z0-9]{2,}$"
        Aadharformat = "^[0-9]{12,12}$"
        Phoneformat = "^[0-9]{10,10}$"
        if (not Name):
            res = {
            'success': False,
            'message': 'Name is required'
             }
            return JsonResponse(res, status = 200)
        elif (not Gender):
            res = {
            'success': False,
            'message': 'Gender is required'
             }
            return JsonResponse(res, status = 200)
        elif (not Age):
            res = {
            'success': False,
            'message': 'Age is required'
             }
            return JsonResponse(res, status = 200)
        elif (not Occupation):
            res = {
            'success': False,
            'message': 'Occupation is required'
             }
            return JsonResponse(res, status = 200)
        elif (not Dob):
            res = {
            'success': False,
            'message': 'DOB is required'
             }
            return JsonResponse(res, status = 200)
        elif (not Aadhar):
            res = {
            'success': False,
            'message': 'Aadhar is required'
             }
            return JsonResponse(res, status = 200)
        elif (not Address):
            res = {
            'success': False,
            'message': 'Address is required'
             }
            return JsonResponse(res, status = 200)
        elif (not Phone):
            res = {
            'success': False,
            'message': 'Phone Number is required'
             }
            return JsonResponse(res, status = 200)
        elif (not Email_Id):
            res = {
            'success': False,
            'message': 'Emailid is required'
             }
            return JsonResponse(res, status = 200)
        elif (not User_name):
            res = {
            'success': False,
            'message': 'Username is required'
             }
            return JsonResponse(res, status = 200)
        elif (not Pass_word):
            res = {
            'success': False,
            'message': 'Password is required'
             }
            return JsonResponse(res, status = 200)
        elif (not C_Password):
            res = {
            'success': False,
            'message': 'Confirm Password is required'
             }
            return JsonResponse(res, status = 200)
        elif (len(Pass_word)<6):
            res = {
            'success': False,
            'message': 'Password cannot be less then 6 characters'
             }
            return JsonResponse(res, status = 200)
        elif (len(Pass_word) >16):
            res = {
            'success': False,
            'message': 'Password cannot be more than 16 characters'
             }
            return JsonResponse(res, status = 200)
        elif (patients.objects.filter(username = User_name)):
            res = {
            'success': False,
            'message': 'Username Already Exists'
             }
            return JsonResponse(res, status = 200)
        emailvalidator = re.search(emailformat, Email_Id)
        if(not emailvalidator):
                res = {
                    
                'success': False,
                'message': 'Email Format Doesnot Match'
                }           
    
                return JsonResponse(res)
        Aadharvalidator = re.search(Aadharformat, str(Aadhar))
        if(not Aadharvalidator):
                res = {
                    
                'success': False,
                'message': 'Aadhar Format Doesnot Match'
                }           
    
                return JsonResponse(res)
        Phonevalidator = re.search(Phoneformat, str(Phone))
        if(not Phonevalidator):
                res = {
                    
                'success': False,
                'message': 'Phone Munber Format Doesnot Match'
                }           
    
                return JsonResponse(res)
        tday = datetime.datetime.today()
        date = tday.day
        month = tday.month
        year = tday.year
        hour = tday.hour
        min = tday.minute
        sec = tday.second
        currdate = datetime.datetime(year,month,date,hour,min,sec)
        if Pass_word == C_Password:
            hashPass = make_password(Pass_word)
            newUser = patients(name=Name,gender=Gender,age=Age, occupation=Occupation,address= Address, aadhar=Aadhar,phone_number = Phone,dob=Dob, email=Email_Id, city = City, state = State , pin = Pin, username=User_name,password=hashPass,registered_at = currdate)
            newUser.save()
        else:
            res = {
            'success': False,
            'message': 'OOPS!! Password mismatch'
              }
            return JsonResponse(res)
        res = {
            'success': True,
            'message': 'User Successfully Registered'
        }
    else:
        res = {
            'success': False,
            'message': 'Invalid method of requesting'
        }
    return JsonResponse(res)
    
def LoginPatient(request):
    if(request.method == 'POST'):
            body = json.loads(request.body)
            usernamelog = body["username"]
            Passlog = body["pass"]
            tday = datetime.datetime.today()
            if (patients.objects.filter(username = usernamelog).exists()):
                users = patients.objects.filter(username = usernamelog)[0]
                currpass = users.password
                flag = check_password( Passlog , currpass ) 
                if flag:
                    alphabet = string.ascii_letters + string.digits
                    secret_key = ''.join(secrets.choice(alphabet) for i in range(16))
                    auth_obj = authorization(patient = users , pt_username = usernamelog , authorization_key = secret_key , doctor = None , receptionist = None)
                    auth_obj.save()
                    res = {
                    'success': True,
                    'message': 'Login Successfully',
                    'user': usernamelog,
                    'authorization_key' : secret_key
                    }          
                    return JsonResponse(res, status = 200)
                else:
                    res = {
                    'success': False,
                    'message': 'Wrong credentials'
                    }
                    return JsonResponse(res, status = 200)
            else:
                res = {
                'success': False,
                'message': 'Username does not exist'
                }       
                return JsonResponse(res)

def LogoutPatient(request):
    if request.method == 'POST':
        body = json.loads(request.body)     
        auth_key = body['auth_key']               
        auth_obj = authorization.objects.get(authorization_key = auth_key)
        auth_obj.delete()
        res = {      
        'message'    : "Secret key has been deleted!"
        }
        return JsonResponse(res,status=200,safe=False) 

def Dashboard(request):
    if(request.method == 'POST'):
        body = json.loads(request.body)
        patientlog = body["username"]
        auth_key = body["auth_key"]
        if(authorization.objects.filter(authorization_key = auth_key,pt_username = patientlog).exists()):
            patient = patients.objects.filter(username = patientlog)[0]
            # patient = patients.objects.get(request.username)
            pName = patient.name
            pGender = patient.gender
            pAge = patient.age
            pDob = patient.dob
            pEmail = patient.email
            pPhone = patient.phone_number
            res = {
            'success': True,
            'Name': pName,
            'Age': pAge,
            'Gender': pGender,
            'Dob': pDob,
            'Email': pEmail,
            'Phone': pPhone
            }     
            return JsonResponse(res,status = 200)
        else:
            res= {
            'success': False,
            'message': 'Login First!!',
            'status': 401
            }
            return JsonResponse(res)


def BookAppointment(request):
    if(request.method == 'POST'):
        body = json.loads(request.body)
        patientlog = body["username"]
        Symptoms = body["symptoms"]
        Specialist_app = body["specialist"]
        Doctor_app = body["doctor_app"]
        Date_app = body["date_app"]
        Time_app = body["time_app"]
        auth_key = body["auth_key"]
        if(authorization.objects.filter(authorization_key = auth_key,pt_username = patientlog).exists()):

            if (not Symptoms):
                res = {
                'success': False,
                'message': 'Symptoms is required'
                 }
                return JsonResponse(res)
            elif (not Specialist_app):
                res = {
                'success': False,
                'message': 'Specialist is required'
                 }
                return JsonResponse(res)
            elif (not Doctor_app):
                res = {
                'success': False,
                'message': 'Doctor is required'
                 }
                return JsonResponse(res)
            elif (not Date_app):
                res = {
                'success': False,
                'message': 'Date of appointment is required'
                 }
                return JsonResponse(res)
            elif (not Time_app):
                res = {
                'success': False,
                'message': 'Time of appointment is required'
                 }
                return JsonResponse(res)
            Speciality_save = speciality_mod.objects.get(id = Specialist_app)
            Doctor_save = doctors_db.objects.get(doctor_id = Doctor_app)
            Patient_save = patients.objects.get(username = patientlog)

            newAppointment = bookappointments(symptoms = Symptoms,time_app = Time_app, doctors_app=Doctor_save,specialist = Speciality_save , username = patientlog,
            patient = Patient_save ,date_app = Date_app , reject_reason = None)#is_pending=True,has_paid=False
            newAppointment.save()
            print(newAppointment)
            res = {
            'success': True,
            'message': 'Appointment is sent form approval!!'
            }     
            return JsonResponse(res, status = 200)
        else:
            res= {
            'success': False,
            'message': 'Login First!!',
            'status': 401
            }
        return JsonResponse(res)

def showPendingAppointment_pt(request):
    if(request.method == 'POST'):
        body = json.loads(request.body)
        patientlog = body["username"]
        auth_key = body["auth_key"]
        if(authorization.objects.filter(authorization_key = auth_key,pt_username = patientlog).exists()):
            p_appointment = list(bookappointments.objects.filter(is_pending = True,username=patientlog).values())
            return JsonResponse(p_appointment, status = 200, safe=False)
        else:
            res= {
            'success': False,
            'message': 'Login First!!',
            'status': 401
            }
            return JsonResponse(res)


def showPtFixedAppointments(request):
    if(request.method == 'POST'):
        body = json.loads(request.body)
        patientlog = body["username"]
        auth_key = body["auth_key"]
        if(authorization.objects.filter(authorization_key = auth_key,pt_username = patientlog).exists()):
            print(request.body)
            # doctor_id = body["doctorid"]
            # dr_obj = doctors_db.objects.get(doctor_id = p)
            pt_appointments = list(bookappointments.objects.filter(is_pending = False, receptionist_resp = True , username = patientlog, tests_pr = None).values('id','username','doctors_app_id','date_app','time_app','tests_pr'))
            for i in range(len(pt_appointments)):
                Patient_save = patients.objects.get(username = pt_appointments[i]['username'])
                apt_date = pt_appointments[i]['date_app'].strftime("%d-%m-%Y")
                pt_appointments[i]["ptname"] = Patient_save.name
                pt_appointments[i]["apt_date"] = apt_date
                dr_obj = doctors_db.objects.get(doctor_id = pt_appointments[i]['doctors_app_id'])
                pt_appointments[i]["drname"] = dr_obj.fname + " " +dr_obj.lname
            return JsonResponse(pt_appointments, status = 200, safe=False)
        else:
            res= {
            'success': False,
            'message': 'Login First!!',
            'status': 401
            }
            return JsonResponse(res)    

def addM_history(request):
    if(request.method == 'POST'):
        body = json.loads(request.body)
        patientlog = body["username"]
        auth_key = body["auth_key"]
        Height = body["height"]
        Weight = body["weight"]
        Drug_all = body["drug_all"]
        Illness = body["illness"]
        Operations = body["operations"]
        Medications = body["medications"]
        Habits = body["habits"]
        Extra_info = body["extra_info"]
        auth_key = body["auth_key"]
        if(authorization.objects.filter(authorization_key = auth_key,pt_username = patientlog).exists()):
            if (not Height):
                res = {
                'success': False,
                'message': 'Symptoms is required'
                 }
                return JsonResponse(res, status = 204)
            elif (not Weight):
                res = {
                'success': False,
                'message': 'Specialist is required'
                 }
                return JsonResponse(res, status = 204)
            elif (not Drug_all):
                res = {
                'success': False,
                'message': 'Doctor is required'
                 }
                return JsonResponse(res, status = 204)
            elif (not Illness):
                res = {
                'success': False,
                'message': 'Date of appointment is required'
                 }
                return JsonResponse(res, status = 204)
            elif (not Operations):
                res = {
                'success': False,
                'message': 'Time of appointment is required'
                 }
                return JsonResponse(res, status = 204)
            elif (not Medications):
                res = {
                'success': False,
                'message': 'Doctor is required'
                 }
                return JsonResponse(res, status = 204)
            elif (not Habits):
                res = {
                'success': False,
                'message': 'Date of appointment is required'
                 }
                return JsonResponse(res, status = 204)
            elif (not Extra_info):
                res = {
                'success': False,
                'message': 'Time of appointment is required'
                 }
                return JsonResponse(res, status = 204)
            Patient_save = patients.objects.get(username = patientlog)
            print(Patient_save)
            addMH = medicalhistory(patient = Patient_save , height = Height , weight = Weight , drug_allergies = Drug_all , illnesses = Illness , operations = Operations , medications_history = Medications, habits = Habits , extrainfo = Extra_info)#is_pending=True,has_paid=False
            addMH.save()
            res = {
            'success': True,
            'message': 'Medical history successfully saved!!'
            }     
            return JsonResponse(res, status = 200)
        else:
            res= {
            'success': False,
            'message': 'Login First!!',
            'status': 401
            }
            return JsonResponse(res)


def previousAppointments(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        patientlog = body["username"]
        auth_key = body["auth_key"]
        if(authorization.objects.filter(authorization_key = auth_key,pt_username = patientlog).exists()):
            print(request.body)
            pt_appointments = list(bookappointments.objects.filter(is_pending = False , username = patientlog , presciption_uploaded = True).values('id','username','doctors_app_id','date_app','time_app','tests_pr','receptionist_resp','dr_resp','reject_reason','presciption_uploaded'))
            for i in range(len(pt_appointments)):
                        Patient_save = patients.objects.get(username = pt_appointments[i]['username'])
                        apt_date = pt_appointments[i]['date_app'].strftime("%d-%m-%Y")
                        pt_appointments[i]["ptname"] = Patient_save.name
                        pt_appointments[i]["status"] = "Visited"

                        pt_appointments[i]["apt_date"] = apt_date
                        dr_obj = doctors_db.objects.get(doctor_id = pt_appointments[i]['doctors_app_id'])
                        pt_appointments[i]["drname"] = "Dr. " + dr_obj.fname + " " +dr_obj.lname
            return JsonResponse(pt_appointments, status = 200, safe=False)
        else:
            res= {
            'success': False,
            'message': 'Login First!!',
            'status': 401
            }
            return JsonResponse(res)

def rejectedAppointments(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        patientlog = body["username"]
        auth_key = body["auth_key"]
        if(authorization.objects.filter(authorization_key = auth_key,pt_username = patientlog).exists()):
            print(request.body)
            pt_appointments = list(bookappointments.objects.filter(is_pending = False , username = patientlog , dr_resp = False).values('id','username','doctors_app_id','date_app','time_app','tests_pr','receptionist_resp','dr_resp','reject_reason','presciption_uploaded') | bookappointments.objects.filter(is_pending = False , username = patientlog , receptionist_resp = False).values('id','username','doctors_app_id','date_app','time_app','tests_pr','receptionist_resp','dr_resp','reject_reason','presciption_uploaded'))
            for i in range(len(pt_appointments)):
                        Patient_save = patients.objects.get(username = pt_appointments[i]['username'])
                        apt_date = pt_appointments[i]['date_app'].strftime("%d-%m-%Y")
                        pt_appointments[i]["ptname"] = Patient_save.name
                        pt_appointments[i]["apt_date"] = apt_date
                        pt_appointments[i]["status"] = "Rejected"

                        dr_obj = doctors_db.objects.get(doctor_id = pt_appointments[i]['doctors_app_id'])
                        pt_appointments[i]["drname"] = "Dr. " + dr_obj.fname + " " +dr_obj.lname
            return JsonResponse(pt_appointments, status = 200, safe=False)
        else:
            res= {
            'success': False,
            'message': 'Login First!!',
            'status': 401
            }
            return JsonResponse(res)

def rejectreason(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        patientlog = body["username"]
        index = body["id"]
        auth_key = body["auth_key"]
        if(authorization.objects.filter(authorization_key = auth_key,pt_username = patientlog).exists()):
            print(request.body)
            pt_appointments = list(bookappointments.objects.filter(is_pending = False , username = patientlog , dr_resp = False).values('id','username','doctors_app_id','date_app','time_app','tests_pr','receptionist_resp','dr_resp','reject_reason','presciption_uploaded') | bookappointments.objects.filter(is_pending = False , username = patientlog , receptionist_resp = False).values('id','username','doctors_app_id','date_app','time_app','tests_pr','receptionist_resp','dr_resp','reject_reason','presciption_uploaded'))
            reason = pt_appointments[index]["reject_reason"]
            res = {
                'idr': index,
                'reason': reason
            }
            return JsonResponse(res, status = 200, safe=False)
        else:
            res= {
            'success': False,
            'message': 'Login First!!',
            'status': 401
            }
            return JsonResponse(res)

def viewptprescription(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        patientlog = body["username"]
        index = body["id"]
        auth_key = body["auth_key"]
        if(authorization.objects.filter(authorization_key = auth_key,pt_username = patientlog).exists()):
            print(request.body)
            pt_appointments = list(bookappointments.objects.filter(is_pending = False , username = patientlog , presciption_uploaded = True).values('id','username','doctors_app_id','date_app','time_app','tests_pr', 'medications_pr','receptionist_resp','dr_resp','reject_reason','presciption_uploaded'))
            Patient_save = patients.objects.get(username = pt_appointments[index]['username'])
            apt_date = pt_appointments[index]['date_app'].strftime("%d-%m-%Y")
            pt_appointments[index]["ptname"] = Patient_save.name
            pt_appointments[index]["ptage"] = Patient_save.age
            pt_appointments[index]["ptdob"] = Patient_save.dob.strftime("%d-%m-%Y")
            pt_appointments[index]["ptgender"] = Patient_save.gender
            pt_appointments[index]["ptphone"] = Patient_save.phone_number
            pt_appointments[index]["apt_date"] = apt_date
            dr_obj = doctors_db.objects.get(doctor_id = pt_appointments[index]['doctors_app_id'])
            pt_appointments[index]["drname"] = "Dr. " + dr_obj.fname + " " +dr_obj.lname
            pt_appointments[index]
            return JsonResponse(pt_appointments[index], status = 200, safe=False)
        else:
            res= {
            'success': False,
            'message': 'Login First!!',
            'status': 401
            }
            return JsonResponse(res)

def viewpendingappointments(request):
    if request.method  == 'POST':
        body = json.loads(request.body)
        patientlog = body["username"]
        auth_key = body["auth_key"]
        if(authorization.objects.filter(authorization_key = auth_key,pt_username = patientlog).exists()):
            pt_appointments = list(bookappointments.objects.filter(is_pending = True , username = patientlog ).values('id','username','doctors_app_id','date_app','time_app','tests_pr', 'medications_pr','receptionist_resp','dr_resp','reject_reason','presciption_uploaded'))
            for i in range(len(pt_appointments)):
                        Patient_save = patients.objects.get(username = pt_appointments[i]['username'])
                        apt_date = pt_appointments[i]['date_app'].strftime("%d-%m-%Y")
                        pt_appointments[i]["ptname"] = Patient_save.name
                        pt_appointments[i]["apt_date"] = apt_date
                        pt_appointments[i]["status"] = "Rejected"
                        dr_obj = doctors_db.objects.get(doctor_id = pt_appointments[i]['doctors_app_id'])
                        pt_appointments[i]["drname"] = "Dr. " + dr_obj.fname + " " +dr_obj.lname

            return JsonResponse(pt_appointments, status = 200 ,safe=False)
        else:
            res= {
            'success': False,
            'message': 'Login First!!',
            'status': 401
            }
            return JsonResponse(res)

