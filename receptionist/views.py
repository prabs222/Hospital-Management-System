from django.http import JsonResponse
from doctors.models import doctors_db, speciality_mod
from patients_App.models import bookappointments, medicalhistory, patients
from .models import Receptionist, authorization
from django.contrib.auth.hashers import make_password, check_password
import json
import string
import secrets

def RegisterReceptionist(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        Name = body["name"]
        Gender = body["gender"]
        Age = body["age"]
        Phone = body["phone_number"]
        Email_Id=body["email"]
        User_name=body["username"]
        Pass_word=body["pass"]
        C_Password = body["cpass"]
        
        if Pass_word == C_Password:
            miserr = False
            hashPass = make_password(Pass_word)
            newUser = Receptionist(name=Name, age=Age, phone_number = Phone, email=Email_Id,username=User_name,password=hashPass ,gender= Gender )
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

def LoginReceptionist(request):
    if(request.method == 'POST'):
            body = json.loads(request.body)
            usernamelog = body["username"]
            Passlog = body["pass"]            
            if (Receptionist.objects.filter(username = usernamelog).exists()):
                users = Receptionist.objects.filter(username = usernamelog)[0]
                currpass = users.password
                flag = check_password( Passlog , currpass ) 
                if flag:
                    alphabet = string.ascii_letters + string.digits
                    secret_key = ''.join(secrets.choice(alphabet) for i in range(16))
                    
                    auth_obj = authorization(receptionist = users , r_username = usernamelog , authorization_key = secret_key , patient = None , doctor = None)
                    auth_obj.save()
                    res = {
                    'success': True,
                    'message': 'Login Successfully',
                    'user': usernamelog,
                    'authorization_key' : secret_key

                    }           
        
                    return JsonResponse(res,status = 200)
                else:
                    res = {
                    'success': False,
                    'message': 'Invalid Credentials'
                    }           
        
                    return JsonResponse(res)
            else:
                res = {
                'success': False,
                'message': 'Username does not exists'
                }           
    
                return JsonResponse(res)

def LogoutReceptionist(request):
    if request.method == 'POST':
        body = json.loads(request.body)     
        auth_key = body['auth_key']               
        auth_obj = authorization.objects.get(authorization_key = auth_key)
        auth_obj.delete()
        res = {      
        'message'    : "Secret key has been deleted!"
        }
        return JsonResponse(res,status=200,safe=False) 

def R_Dashboard(request):
    if(request.method == 'POST'):
        body = json.loads(request.body)
        recp_log = body["username"]
        auth_key = body["auth_key"]
        if(authorization.objects.filter(authorization_key = auth_key,r_username = recp_log).exists()):
            r_obj = Receptionist.objects.filter(username = recp_log)[0]
            # patient = patients.objects.get(request.username)
            dfName =   r_obj.name
            dGender = r_obj.gender
            dAge =    r_obj.age
            dEmail =  r_obj.email
            # dSpeciality = r_obj.speciality_id
            res = {
            'success': True,
            'Name': dfName ,
            'Age': dAge,
            'Gender': dGender,
            'Email': dEmail            }     
            return JsonResponse(res,status = 200)
        else:
            res= {
                'success': False,
                'message': 'Login First!!',
                'status': 401
            }
            return JsonResponse(res)

def showPendingAppointments(request):
    if(request.method == 'POST'):
        body = json.loads(request.body)
        index = body["id"]
        recp_log = body["username"]
        auth_key = body["auth_key"]
        if(authorization.objects.filter(authorization_key = auth_key,r_username = recp_log).exists()):
            appointment = list(bookappointments.objects.filter(is_pending = True , receptionist_resp = None).values())
            print(appointment[index]['username'])
            Speciality_save = speciality_mod.objects.get(id = appointment[index]['specialist_id'])
            Doctor_save = doctors_db.objects.get(doctor_id = appointment[index]['doctors_app_id'])
            Patient_save = patients.objects.get(username = appointment[index]['username'])
            name = Patient_save.name        
            age = Patient_save.age
            gender = Patient_save.gender
            email = Patient_save.email
            mobile = Patient_save.phone_number
            specialist_name = Speciality_save.specialization
            dr_name = "Dr. " + Doctor_save.fname + " " + Doctor_save.lname
            appointment[index]["ptname"] = name
            appointment[index]["ptage"]= age
            appointment[index]["ptemail"] = email
            appointment[index]["ptmobile"] = mobile
            appointment[index]["ptgender"] = gender
            appointment[index]["specialist"] = specialist_name
            appointment[index]["dr_name"] = dr_name
            return JsonResponse(appointment[index],status = 200, safe=False)
        else:
            res= {
                'success': False,
                'message': 'Login First!!',
                'status': 401
            }
            return JsonResponse(res)


def showRPendingMedicalHistory(request):
    if(request.method == 'POST'):
        body = json.loads(request.body)
        index = body["id"]
        recp_log = body["username"]
        auth_key = body["auth_key"]
        if(authorization.objects.filter(authorization_key = auth_key,r_username = recp_log).exists()):

            print(request.body)
            print(index)
            appointment = list(bookappointments.objects.filter(is_pending = True , receptionist_resp = None).values('id','specialist_id','username','doctors_app_id'))
            print(appointment[index]['username'])
            Speciality_save = speciality_mod.objects.get(id = appointment[index]['specialist_id'])
            Doctor_save = doctors_db.objects.get(doctor_id = appointment[index]['doctors_app_id'])
            Patient_save = patients.objects.get(username = appointment[index]['username'])
            medical_history = medicalhistory.objects.get(patient_id = Patient_save.id)
            name = Patient_save.name        
            age = Patient_save.age
            gender = Patient_save.gender
            email = Patient_save.email
            mobile = Patient_save.phone_number
            specialist_name = Speciality_save.specialization
            dr_name = "Dr. " + Doctor_save.fname + " " + Doctor_save.lname
            appointment[index]["ptname"] = name
            appointment[index]["ptage"]= age
            appointment[index]["ptdob"] = Patient_save.dob
            appointment[index]["ptgender"] = gender
            appointment[index]["height"] = medical_history.height
            appointment[index]["weight"]= medical_history.weight
            appointment[index]["drug_all"] = medical_history.drug_allergies
            appointment[index]["illness"] = medical_history.illnesses
            appointment[index]["operations"] = medical_history.operations
            appointment[index]["medications"] = medical_history.medications_history
            appointment[index]["habits"] = medical_history.habits
            appointment[index]["extrainfo"] = medical_history.extrainfo
            return JsonResponse(appointment[index],status = 200, safe=False)
        else:
            res= {
                'success': False,
                'message': 'Login First!!',
                'status': 401
            }
            return JsonResponse(res)

def showPendingAppointments_name(request):
    if(request.method == 'GET'):
        appointments = list(bookappointments.objects.filter(is_pending = True, receptionist_resp = None).values('id','username'))
        for i in range(len(appointments)):
                Patient_save = patients.objects.get(username = appointments[i]['username'])
                name = Patient_save.name
                appointments[i]["ptname"] = name
        return JsonResponse(appointments, status = 200,safe=False)
        

def showDoctorsData(request):
    if(request.method == 'POST'):
        body = json.loads(request.body)
        index = body["id"]
        recp_log = body["username"]
        auth_key = body["auth_key"]
        if(authorization.objects.filter(authorization_key = auth_key,r_username = recp_log).exists()):
            drprofile = list(doctors_db.objects.all().values('fname','lname','dob','username','gender','email','phone_number','speciality_id','address','city','state','pin','qualifications','workexperience'))
            Speciality_save = speciality_mod.objects.get(id = drprofile[index]['speciality_id'])
            specialist_name = Speciality_save.specialization
            drprofile[index]["specialist"] = specialist_name
            return JsonResponse(drprofile[index],status = 200, safe=False)
        else:
            res= {
                'success': False,
                'message': 'Login First!!',
                'status': 401
            }
            return JsonResponse(res)



def showAllAppointments(request):
    if(request.method == 'GET'):
        p_appointment = list(bookappointments.objects.filter(is_pending = True).values())
        return JsonResponse(p_appointment, status = 200,safe=False)

def showAllDoctors_name(request):
    if(request.method == 'GET'):
        doctors = list(doctors_db.objects.all().values('doctor_id','fname','lname')) 
        return JsonResponse(doctors, status = 200,safe=False)

def showAllPatients_name(request):
    if(request.method == 'GET'):
        patients_obj = list(patients.objects.all().values('id','name')) 
        return JsonResponse(patients_obj,status = 200, safe=False)

def showPatientData(request):
    if(request.method == 'POST'):
        body = json.loads(request.body)
        index = body["id"]
        recp_log = body["username"]
        auth_key = body["auth_key"]
        if(authorization.objects.filter(authorization_key = auth_key,r_username = recp_log).exists()):
            ptprofile = list(patients.objects.all().values('name','dob','username','gender','email','phone_number','address','city','state','pin','occupation'))
            return JsonResponse(ptprofile[index],status = 200, safe=False)
        else:
            res= {
                'success': False,
                'message': 'Login First!!',
                'status': 401
            }
            return JsonResponse(res)

def showPtMedicalHistory(request):
    if(request.method == 'POST'):
        body = json.loads(request.body)
        index = body["id"]
        auth_key = body["auth_key"]
        recp_log = body["username"]
        if(authorization.objects.filter(authorization_key = auth_key,r_username = recp_log).exists()):
            ptMedicalHistory = list(medicalhistory.objects.all().values())
            return JsonResponse(ptMedicalHistory[index],status = 200, safe=False)
        else:
            res= {
                'success': False,
                'message': 'Login First!!',
                'status': 401
            }
            return JsonResponse(res)

def ReceptionistForward(request):
    if(request.method == 'POST'):
        body = json.loads(request.body)
        index = body["id"]
        aptid = body["aptid"]
        recp_log = body["username"]
        auth_key = body["auth_key"]
        if(authorization.objects.filter(authorization_key = auth_key,r_username = recp_log).exists()):
            appointment = list(bookappointments.objects.filter(is_pending = True , receptionist_resp = None).values('id','username','doctors_app_id'))
            Doctor_save = doctors_db.objects.get(doctor_id = appointment[index]['doctors_app_id'])
            dr_name  = "Request forwarded to Dr. " + Doctor_save.fname + " " + Doctor_save.lname + " successfully!!"
            appointment[index]["dr_name"] = dr_name
            frwdResp = bookappointments.objects.get(id = aptid)
            frwdResp.receptionist_resp = True
            frwdResp.save()
            return JsonResponse(appointment[index],status = 200, safe=False)
        else:
            res= {
                'success': False,
                'message': 'Login First!!',
                'status': 401
            }
            return JsonResponse(res)


def ReceptionistReject(request):
    if(request.method == 'POST'):
        body = json.loads(request.body)
        index = body["id"]
        aptid = body["aptid"]
        reason = body["reason"]
        auth_key = body["auth_key"]
        recp_log = body["username"]
        if(authorization.objects.filter(authorization_key = auth_key,r_username = recp_log).exists()):

            appointment = list(bookappointments.objects.filter(is_pending = True).values('id','username','symptoms','doctors_app_id'))
            print(appointment[index]['username'])
            Doctor_save = doctors_db.objects.get(doctor_id = appointment[index]['doctors_app_id'])
            Patients_obj = patients.objects.get(username = appointment[index]['username'])
            message = "Request has been rejected and " + Patients_obj.name + " has been notified about it!!"
            appointment[index]["message"] = message
            frwdResp = bookappointments.objects.get(id = aptid)
            frwdResp.receptionist_resp = False
            frwdResp.reject_reason = reason 
            frwdResp.is_pending = False
            frwdResp.save()
            return JsonResponse(appointment[index],status = 200, safe=False)
        else:
            res= {
                'success': False,
                'message': 'Login First!!',
                'status': 401
            }
            return JsonResponse(res)