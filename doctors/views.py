from django.http import JsonResponse
import string
import secrets
from patients_App.models import bookappointments, medicalhistory, patients
from receptionist.models import authorization
from .models import doctors_db, speciality_mod
from django.contrib.auth.hashers import make_password, check_password
import json,re
import datetime
import datetime
def RegisterDoctor(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        F_Name = body["fname"]
        L_Name = body["lname"]
        Gender = body["gender"]
        Age = body["age"]
        Address = body["address"]
        Aadhar = body["aadhar"]
        Phone = body["phone_number"]
        Email_Id=body["email"]
        User_name=body["username"]
        Pass_word=body["pass"]
        C_Password = body["cpass"]
        Qualifications = body["qualifications"]
        Work_exp = body["workexperience"]
        Speciality = body["speciality"]
        City = body["city"]
        State = body["state"]
        Pin = body["pin"]
        Dob = body["dob"]
        emailformat = "^[a-zA-Z0-9\-\_\.]+@[a-zA-Z0-9]{2,}\.[a-zA-Z0-9]{2,}$"
        Aadharformat = "^[0-9]{12,12}$"
        # speci
        Phoneformat = "^[0-9]{10,10}$"
        if (not F_Name):
            res = {
            'success': False,
            'message': 'Name is required'
             }
            return JsonResponse(res,status = 204)
        elif (not Gender):
            res = {
            'success': False,
            'message': 'Gender is required'
             }
            return JsonResponse(res,status = 204)
        elif (not Age):
            res = {
            'success': False,
            'message': 'Age is required'
             }
            return JsonResponse(res,status = 204)
        elif (not Work_exp):
            res = {
            'success': False,
            'message': 'Work Experience is required'
             }
            return JsonResponse(res,status = 204)
        elif (not State):
            res = {
            'success': False,
            'message': 'State is required'
             }
            return JsonResponse(res,status = 204)
        elif (not City):
            res = {
            'success': False,
            'message': 'City is required'
             }
            return JsonResponse(res,status = 204)
        elif (not Pin):
            res = {
            'success': False,
            'message': 'Pin is required'
             }
            return JsonResponse(res,status = 204)
        elif (not Speciality):
            res = {
            'success': False,
            'message': 'Speciality is required'
             }
            return JsonResponse(res,status = 204)
        elif (not L_Name):
            res = {
            'success': False,
            'message': 'Last Name is required'
             }
            return JsonResponse(res,status = 204)
        elif (not Qualifications):
            res = {
            'success': False,
            'message': 'Occupation is required'
             }
            return JsonResponse(res,status = 204)
        elif (not Aadhar):
            res = {
            'success': False,
            'message': 'Aadhar is required'
             }
            return JsonResponse(res,status = 204)
        elif (not Address):
            res = {
            'success': False,
            'message': 'Address is required'
             }
            return JsonResponse(res,status = 204)
        elif (not Phone):
            res = {
            'success': False,
            'message': 'Phone Number is required'
             }
            return JsonResponse(res,status = 204)
        elif (not Email_Id):
            res = {
            'success': False,
            'message': 'Emailid is required'
             }
            return JsonResponse(res,status = 204)
        elif (not User_name):
            res = {
            'success': False,
            'message': 'Username is required'
             }
            return JsonResponse(res,status = 204)
        elif (not Pass_word):
            res = {
            'success': False,
            'message': 'Password is required'
             }
            return JsonResponse(res,status = 204)
        elif (not C_Password):
            res = {
            'success': False,
            'message': 'Confirm Password is required'
             }
            return JsonResponse(res,status = 204)
        elif (not Dob):
            res = {
            'success': False,
            'message': 'DOB is required'
             }
            return JsonResponse(res,status = 204)
        # elif (Pass_word)
        elif (len(Pass_word)<6):
            res = {
            'success': False,
            'message': 'Password cannot be less then 6 characters'
             }
            return JsonResponse(res,status = 204)
        elif (len(Pass_word) >16):
            res = {
            'success': False,
            'message': 'Password cannot be more than 16 characters'
             }
            return JsonResponse(res,status = 204)
        elif (doctors_db.objects.filter(username = User_name)):
            res = {
            'success': False,
            'message': 'Username Already Exists'
             }
            return JsonResponse(res,status = 204)
        emailvalidator = re.search(emailformat, Email_Id)
        if(not emailvalidator):
                res = {
                    
                'success': False,
                'message': 'Email format does not match.'
                }           
    
                return JsonResponse(res,status = 204)
        Aadharvalidator = re.search(Aadharformat, str(Aadhar))
        if(not Aadharvalidator):
                res = {
                    
                'success': False,
                'message': 'Aadhar format does not match.'
                }           
    
                return JsonResponse(res,status = 204)
        Phonevalidator = re.search(Phoneformat, str(Phone))
        if(not Phonevalidator):
                res = {
                    
                'success': False,
                'message': 'Phone number format does not match.'
                }           
    
                return JsonResponse(res)
    
        tday = datetime.datetime.today()
        print("----------------------")
        print(tday)
        date = tday.day
        month = tday.month
        year = tday.year
        hour = tday.hour
        min = tday.minute
        sec = tday.second
        currdate = datetime.datetime(year,month,date,hour,min,sec)
        Speciality_save = speciality_mod.objects.get(id = Speciality)
        print(Speciality_save)
        if Pass_word == C_Password:
            hashPass = make_password(Pass_word)
            newUser = doctors_db(fname=F_Name,lname = L_Name, age=Age,  aadhar=Aadhar,phone_number = Phone, email=Email_Id,username=User_name,password=hashPass, qualifications = Qualifications, workexperience = Work_exp , city = City, state = State , pin = Pin , address = Address, gender= Gender , speciality = Speciality_save , dob =Dob, registered_at=currdate)
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
def LoginDoctor(request):
    if(request.method == 'POST'):
            body = json.loads(request.body)
            usernamelog = body["username"]
            Passlog = body["pass"]
            tday = datetime.datetime.today()
            if (doctors_db.objects.filter(username = usernamelog).exists()):
                users = doctors_db.objects.filter(username = usernamelog)[0]
                currpass = users.password
                flag = check_password( Passlog , currpass ) 
                if flag:
                    alphabet = string.ascii_letters + string.digits
                    secret_key = ''.join(secrets.choice(alphabet) for i in range(16))
                    auth_obj = authorization(doctor = users , dr_username = usernamelog , authorization_key = secret_key , patient = None , receptionist = None)
                    auth_obj.save()
                    res = {
                    'success': True,
                    'message': 'Login Successfully',
                    'user': usernamelog,
                    'authorization_key' : secret_key
                    }           
        
                    return JsonResponse(res)
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

def AddSpeciality(request):
    if(request.method == 'POST'):
            body = json.loads(request.body)
            Speciality = body["speciality"]
            Specialization = body["specialization"]
            if (speciality_mod.objects.filter(specialities  = Speciality,specialization = Specialization)):
                res = {
                'success': False,
                'message': 'Username Already Exists'
                }
                return JsonResponse(res)
            newSpeciality = speciality_mod(specialities=Speciality,specialization = Specialization)
            newSpeciality.save()
            res = {
            'success': True,
            'message': 'Added new speciality'
            }           
        
            return JsonResponse(res)
    
def displaySpecialities(request):
    if(request.method == 'GET'):
        specialists = list(speciality_mod.objects.values())  # wrap in list(), because QuerySet is not JSON serializable
        return JsonResponse(specialists, safe=False) 

def displaySpecializations(request):
    if(request.method == 'GET'):
        specializations = list(speciality_mod.objects.values())  # wrap in list(), because QuerySet is not JSON serializable
        return JsonResponse(specializations, safe=False) 

def displayDoctors(request):
    if(request.method == 'POST'):
        body = json.loads(request.body)
        Speciality = body["id"]
        patientlog = body["username"]
        auth_key = body["auth_key"]
        if(authorization.objects.filter(authorization_key = auth_key,dr_username = patientlog).exists()):
            Speciality_save = speciality_mod.objects.get(id = Speciality)
            doctors_av = list(doctors_db.objects.filter(speciality_id = Speciality).values('doctor_id','fname','lname')) 
            return JsonResponse(doctors_av, safe=False) 
        else:
            res= {
                'success': False,
                'message': 'Login First!!',
                'status': 401
            }
            return JsonResponse(res)        


def Dr_Dashboard(request):
    if(request.method == 'POST'):
        body = json.loads(request.body)
        doctorlog = body["username"]
        auth_key = body["auth_key"]
        if(authorization.objects.filter(authorization_key = auth_key,dr_username = doctorlog).exists()):
            doctor = doctors_db.objects.filter(username = doctorlog)[0]
            speciality_obj = speciality_mod.objects.get(id = doctor.speciality_id)
            dfName =   doctor.fname
            dlName = doctor.lname
            dGender = doctor.gender
            dAge =    doctor.age
            dDob =    doctor.dob
            dEmail =  doctor.email
            dSpeciality = speciality_obj.specialization
            res = {
            'Name': dfName + " " + dlName,
            'Age': dAge,
            'Gender': dGender,
            'Dob': dDob,
            'Email': dEmail,
            'Speciality': dSpeciality
            }     
            return JsonResponse(res)
        else:
            res= {
                'success': False,
                'message': 'Login First!!',
                'status': 401
            }
            return JsonResponse(res)


def showDrPendingAppointments_name(request):
    if(request.method == 'POST'):
        body = json.loads(request.body)
        doctorlog = body["username"]
        auth_key = body["auth_key"]
        if(authorization.objects.filter(authorization_key = auth_key,dr_username = doctorlog).exists()):
            dr_obj = doctors_db.objects.get(username = doctorlog)
            dr_appointments = list(bookappointments.objects.filter(is_pending = True, receptionist_resp = True , doctors_app_id = dr_obj.doctor_id).values('id','username'))
            for i in range(len(dr_appointments)):
                Patient_save = patients.objects.get(username = dr_appointments[i]['username'])
                name = Patient_save.name
                dr_appointments[i]["ptname"] = name
            return JsonResponse(dr_appointments, safe=False)
        else:
            res= {
                'success': False,
                'message': 'Login First!!',
                'status': 401
            }
            return JsonResponse(res)


def showDrPendingAppointments(request):
    if(request.method == 'POST'):
        body = json.loads(request.body)
        index = body["id"]
        doctorlog = body["username"]
        auth_key = body["auth_key"]
        if(authorization.objects.filter(authorization_key = auth_key,dr_username = doctorlog).exists()):
            dr_obj = doctors_db.objects.get(username = doctorlog)
            dr_appointments = list(bookappointments.objects.filter(is_pending = True, receptionist_resp = True , doctors_app_id = dr_obj.doctor_id).values())
            Doctor_save = doctors_db.objects.get(doctor_id = dr_appointments[index]['doctors_app_id'])
            Patient_save = patients.objects.get(username = dr_appointments[index]['username'])
            name = Patient_save.name        
            age = Patient_save.age
            gender = Patient_save.gender
            email = Patient_save.email
            mobile = Patient_save.phone_number
            dr_name = "Dr. " + Doctor_save.fname + " " + Doctor_save.lname
            dr_appointments[index]["ptname"] = name
            dr_appointments[index]["ptage"]= age
            dr_appointments[index]["ptemail"] = email
            dr_appointments[index]["ptmobile"] = mobile
            dr_appointments[index]["ptgender"] = gender
            dr_appointments[index]["dr_name"] = dr_name
            return JsonResponse(dr_appointments[index], safe=False)
        else:
            res= {
                'success': False,
                'message': 'Login First!!',
                'status': 401
            }
            return JsonResponse(res)

def LogoutDoctor(request):
    if request.method == 'POST':
        body = json.loads(request.body)     
        auth_key = body['auth_key']               
        auth_obj = authorization.objects.get(authorization_key = auth_key)
        auth_obj.delete()
        res = {      
        'message'    : "Secret key has been deleted!"
        }
        return JsonResponse(res,status=200,safe=False) 

def DoctorFix(request):
    if(request.method == 'POST'):
        body = json.loads(request.body)
        index = body["id"]
        aptid = body["aptid"]
        doctorlog = body["username"]
        auth_key = body["auth_key"]
        if(authorization.objects.filter(authorization_key = auth_key,dr_username = doctorlog).exists()):
            dr_obj = doctors_db.objects.get(username = doctorlog)
            dr_appointments = list(bookappointments.objects.filter(is_pending = True, receptionist_resp = True , doctors_app_id = dr_obj.doctor_id).values())
            Doctor_save = doctors_db.objects.get(doctor_id = dr_appointments[index]['doctors_app_id'])
            message  = "Appointment approved!!"
            dr_appointments[index]["message"] = message
            frwdResp = bookappointments.objects.get(id = aptid)
            frwdResp.dr_resp = True
            frwdResp.is_pending = False
            frwdResp.save()
            return JsonResponse(dr_appointments[index], safe=False)
        else:
            res= {
                'success': False,
                'message': 'Login First!!',
                'status': 401
            }
            return JsonResponse(res)


def DoctorReject(request):
    if(request.method == 'POST'):
        body = json.loads(request.body)
        index = body["id"]
        aptid = body["aptid"]
        doctorlog = body["username"]
        reason = body["reason"]
        auth_key = body["auth_key"]
        if(authorization.objects.filter(authorization_key = auth_key,dr_username = doctorlog).exists()):
            dr_obj = doctors_db.objects.get(username = doctorlog)
            dr_appointments = list(bookappointments.objects.filter(is_pending = True, receptionist_resp = True , doctors_app_id = dr_obj.doctor_id).values())
            Doctor_save = doctors_db.objects.get(doctor_id = dr_appointments[index]['doctors_app_id'])
            print(dr_appointments[index]['username'])
            patient_obj = patients.objects.get(username = dr_appointments[index]['username'])
            message  = "Appointment approved!!"
            dr_appointments[index]["message"] = message
            message = "Request has been rejected and " + patient_obj.name + " has been notified about it!!"
            dr_appointments[index]["message"] = message
            RejResp = bookappointments.objects.get(id = aptid)
            RejResp.dr_resp = False
            RejResp.reject_reason = reason 
            RejResp.is_pending = False
            RejResp.save()
            return JsonResponse(dr_appointments[index], safe=False)
        else:
            res= {
                'success': False,
                'message': 'Login First!!',
                'status': 401
            }
            return JsonResponse(res)

def showDrFixedAppointments(request):
    if(request.method == 'POST'):
        body = json.loads(request.body)
        doctorlog = body["username"]
        auth_key = body["auth_key"]
        if(authorization.objects.filter(authorization_key = auth_key,dr_username = doctorlog).exists()):
            dr_obj = doctors_db.objects.get(username = doctorlog)
            dr_appointments = list(bookappointments.objects.filter(is_pending = False, dr_resp = True , doctors_app_id = dr_obj.doctor_id , presciption_uploaded = False).values('id','username','date_app','time_app', 'presciption_uploaded'))
            for i in range(len(dr_appointments)):
                apt_date = dr_appointments[i]['date_app'].strftime("%d-%m-%Y")
                dr_appointments[i]["apt_date"] = apt_date

                Patient_save = patients.objects.get(username = dr_appointments[i]['username'])
                name = Patient_save.name
                dr_appointments[i]["ptname"] = name
            return JsonResponse(dr_appointments, safe=False)
        else:
            res= {
                'success': False,
                'message': 'Login First!!',
                'status': 401
            }
            return JsonResponse(res)

def showDrFixAptData(request):
    if(request.method == 'POST'):
        body = json.loads(request.body)
        index = body["id"]
        doctorlog = body["username"]
        auth_key = body["auth_key"]
        if(authorization.objects.filter(authorization_key = auth_key,dr_username = doctorlog).exists()):
            dr_obj = doctors_db.objects.get(username = doctorlog)
            dr_appointments = list(bookappointments.objects.filter(is_pending = False, dr_resp = True ,  doctors_app_id = dr_obj.doctor_id , presciption_uploaded = False).values())
            Doctor_save = doctors_db.objects.get(doctor_id = dr_appointments[index]['doctors_app_id'])
            Patient_save = patients.objects.get(username = dr_appointments[index]['username'])
            name = Patient_save.name        
            age = Patient_save.age
            gender = Patient_save.gender
            email = Patient_save.email
            mobile = Patient_save.phone_number
            dr_name = "Dr. " + Doctor_save.fname + " " + Doctor_save.lname
            dr_appointments[index]["ptname"] = name
            dr_appointments[index]["ptage"]= age
            dr_appointments[index]["ptemail"] = email
            dr_appointments[index]["ptmobile"] = mobile
            dr_appointments[index]["ptgender"] = gender
            dr_appointments[index]["dr_name"] = dr_name
            return JsonResponse(dr_appointments[index], safe=False)
        else:
            res= {
                'success': False,
                'message': 'Login First!!',
                'status': 401
            }
            return JsonResponse(res)


def showDrFixedMedicalHistory(request):
    if(request.method == 'POST'):
        body = json.loads(request.body)
        # Name = body["name"]
        # body = json.loads(request.body)
        doctorlog = body["username"]
        index = body["id"]
        auth_key = body["auth_key"]
        if(authorization.objects.filter(authorization_key = auth_key,dr_username = doctorlog).exists()):
            dr_obj = doctors_db.objects.get(username = doctorlog)
            dr_appointments = list(bookappointments.objects.filter(is_pending = False, dr_resp = True ,  doctors_app_id = dr_obj.doctor_id , presciption_uploaded = False).values())
            Speciality_save = speciality_mod.objects.get(id = dr_appointments[index]['specialist_id'])
            Doctor_save = doctors_db.objects.get(doctor_id = dr_appointments[index]['doctors_app_id'])
            Patient_save = patients.objects.get(username = dr_appointments[index]['username'])
            medical_history = medicalhistory.objects.get(patient_id = Patient_save.id)
            name = Patient_save.name        
            age = Patient_save.age
            gender = Patient_save.gender
            email = Patient_save.email
            mobile = Patient_save.phone_number
            specialist_name = Speciality_save.specialization
            dr_name = "Dr. " + Doctor_save.fname + " " + Doctor_save.lname
            dr_appointments[index]["ptname"] = name
            dr_appointments[index]["ptage"]= age
            dr_appointments[index]["ptdob"] = Patient_save.dob
            dr_appointments[index]["ptgender"] = gender
            dr_appointments[index]["height"] = medical_history.height
            dr_appointments[index]["weight"]= medical_history.weight
            dr_appointments[index]["drug_all"] = medical_history.drug_allergies
            dr_appointments[index]["illness"] = medical_history.illnesses
            dr_appointments[index]["operations"] = medical_history.operations
            dr_appointments[index]["medications"] = medical_history.medications_history
            dr_appointments[index]["habits"] = medical_history.habits
            dr_appointments[index]["extrainfo"] = medical_history.extrainfo
            return JsonResponse(dr_appointments[index], safe=False)
        else:
            res= {
                'success': False,
                'message': 'Login First!!',
                'status': 401
            }
            return JsonResponse(res)

def getprescriptiondata(request):
    if(request.method == 'POST'):
        body = json.loads(request.body)
        doctorlog = body["username"]
        index = body["id"]
        auth_key = body["auth_key"]
        if(authorization.objects.filter(authorization_key = auth_key,dr_username = doctorlog).exists()):
            dr_obj = doctors_db.objects.get(username = doctorlog)
            dr_appointments = list(bookappointments.objects.filter(is_pending = False, dr_resp = True ,  doctors_app_id = dr_obj.doctor_id , presciption_uploaded = False).values('id','username','patient_id','time_app','date_app'))
            Patient_save = patients.objects.get(username = dr_appointments[index]['username'])
            name = Patient_save.name        
            age = Patient_save.age
            gender = Patient_save.gender
            phone = Patient_save.phone_number
            apt_date = dr_appointments[index]['date_app'].strftime("%d-%m-%Y")
            pt_dob = Patient_save.dob.strftime("%d-%m-%Y")
            dr_appointments[index]["apt_date"] = apt_date
            dr_appointments[index]["ptname"] = name
            dr_appointments[index]["ptphone"]= phone
            dr_appointments[index]["ptdob"] = pt_dob
            dr_appointments[index]["ptage"] = age
            return JsonResponse(dr_appointments[index],status = 200, safe=False)
        else:
            res= {
                'success': False,
                'message': 'Login First!!',
                'status': 401
            }
            return JsonResponse(res)





def uploadprescription(request):
    if(request.method == 'POST'):
        body = json.loads(request.body)
        doctorlog = body["username"]
        medications_pr = body["medications"]
        tests_pr = body["tests"]
        index = body["id"]
        auth_key = body["auth_key"]
        if(authorization.objects.filter(authorization_key = auth_key,dr_username = doctorlog).exists()):
            dr_obj = doctors_db.objects.get(username = doctorlog)
            dr_appointments = list(bookappointments.objects.filter(is_pending = False, dr_resp = True ,  doctors_app_id = dr_obj.doctor_id , presciption_uploaded = False).values())
            aptid = dr_appointments[index]["id"]
            newprescription = bookappointments.objects.get(id = aptid)
            newprescription.medications_pr = medications_pr
            newprescription.tests_pr = tests_pr
            newprescription.presciption_uploaded = True
            newprescription.save()
            res = {
                "success": "True",
                "message": "Successfully uploaded prescription!!"
            }
            return JsonResponse(res, status = 200,safe=False)
        else:
            res= {
                'success': False,
                'message': 'Login First!!',
                'status': 401
            }
            return JsonResponse(res)


def showDrPatients(request):
    if (request.method == 'POST'):
        body = json.loads(request.body)
        doctorlog = body["username"]
        auth_key = body["auth_key"]
        if(authorization.objects.filter(authorization_key = auth_key,dr_username = doctorlog).exists()):
            dr_obj = doctors_db.objects.get(username = doctorlog)
            pt_list = list(bookappointments.objects.filter(doctors_app_id = dr_obj.doctor_id , presciption_uploaded = True).values('id','date_app','time_app','patient_id','username'))
            for i in range(len(pt_list)):
                apt_date = pt_list[i]['date_app'].strftime("%d-%m-%Y")
                pt_list[i]["apt_date"] = apt_date

                Patient_save = patients.objects.get(username = pt_list[i]['username'])
                name = Patient_save.name
                pt_list[i]["ptname"] = name
            return JsonResponse(pt_list,status = 200, safe=False)
        else:
            res= {
                'success': False,
                'message': 'Login First!!',
                'status': 401
            }
            return JsonResponse(res)

def showDrPtProfile(request):
    if (request.method == 'POST'):
        body = json.loads(request.body)
        doctorlog = body["username"]
        auth_key = body["auth_key"]
        if(authorization.objects.filter(authorization_key = auth_key,dr_username = doctorlog).exists()):

            dr_obj = doctors_db.objects.get(username = doctorlog)
            pt_list = list(bookappointments.objects.filter(doctors_app_id = dr_obj.doctor_id , presciption_uploaded = True).values('id','date_app','time_app','patient_id','username'))
            for i in range(len(pt_list)):
                apt_date = pt_list[i]['date_app'].strftime("%d-%m-%Y")
                pt_list[i]["apt_date"] = apt_date

                Patient_save = patients.objects.get(username = pt_list[i]['username'])
                name = Patient_save.name
                pt_list[i]["ptname"] = name
            return JsonResponse(pt_list, safe=False)
        else:
            res= {
                'success': False,
                'message': 'Login First!!',
                'status': 401
            }
            return JsonResponse(res)


def showDrPtVisits(request):
    if (request.method == 'POST'):
        body = json.loads(request.body)
        doctorlog = body["username"]
        index = body["id"]
        auth_key = body["auth_key"]
        if(authorization.objects.filter(authorization_key = auth_key,dr_username = doctorlog).exists()):
            dr_obj = doctors_db.objects.get(username = doctorlog)
            pt_list = list(bookappointments.objects.filter(doctors_app_id = dr_obj.doctor_id , presciption_uploaded = True).values('id','date_app','time_app','patient_id','username'))
            pt_obj = patients.objects.get(id = pt_list[index]['patient_id'])
            pt_visit_list = list(bookappointments.objects.filter(doctors_app_id = dr_obj.doctor_id, presciption_uploaded = True ,  patient_id = pt_obj.id).values('id','date_app','time_app','username'))
            for i in range(len(pt_visit_list)):
                apt_date = pt_visit_list[i]['date_app'].strftime("%d-%m-%Y")
                pt_visit_list[i]["apt_date"] = apt_date

                Patient_save = patients.objects.get(username = pt_visit_list[i]['username'])
                name = Patient_save.name
                pt_visit_list[i]["ptname"] = name
            return JsonResponse(pt_visit_list, safe=False)
        else:
            res= {
                'success': False,
                'message': 'Login First!!',
                'status': 401
            }
            return JsonResponse(res)
