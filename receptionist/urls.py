from django.urls import path
from .views import LoginReceptionist, LogoutReceptionist, R_Dashboard, ReceptionistForward, ReceptionistReject, showAllAppointments, showAllDoctors_name, showAllPatients_name, showDoctorsData, showPatientData, showPendingAppointments, showPendingAppointments_name, showPtMedicalHistory, showRPendingMedicalHistory
urlpatterns = [
    # path('', home_views , name='home'),
    # path('admin/', admin.site.urls),
    # path('about/', about , name='about'),
    path('login/', LoginReceptionist),
    path('logout/', LogoutReceptionist),
    path('dashboard/', R_Dashboard),
    path('showpendingappointments/', showPendingAppointments),
    path('showptpendingmedicaldata/', showRPendingMedicalHistory),

    path('showallappointments/', showAllAppointments),
    path('showpendingappointments_name/', showPendingAppointments_name),
    path('showalldoctors_name/', showAllDoctors_name),
    path('showdoctordata/', showDoctorsData),
    path('showallpatients_name/', showAllPatients_name),
    path('showpatientdata/', showPatientData),
    path('receptionistforward/', ReceptionistForward),
    path('receptionistreject/', ReceptionistReject),

    path('showptmedicaldata/', showPtMedicalHistory),
    # path('dashboard/', Dashboard),
    # path('/login', Login),
]