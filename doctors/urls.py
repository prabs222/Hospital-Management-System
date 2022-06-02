from django.urls import path
from .views import AddSpeciality, DoctorFix, DoctorReject, Dr_Dashboard, LoginDoctor, LogoutDoctor, RegisterDoctor, displayDoctors, displaySpecialities, displaySpecializations, getprescriptiondata, showDrFixAptData, showDrFixedAppointments, showDrFixedMedicalHistory, showDrPatients, showDrPendingAppointments, showDrPendingAppointments_name, showDrPtVisits, uploadprescription
urlpatterns = [
    # path('', home_views , name='home'),
    # path('admin/', admin.site.urls),
    # path('about/', about , name='about'),
    path('register/', RegisterDoctor),
    path('login/', LoginDoctor),
    path('logout/', LogoutDoctor),
    path('speciality/', AddSpeciality),
    path('displayspeciality/', displaySpecialities),
    path('displayspecializations/', displaySpecializations),
    path('dashboard/', Dr_Dashboard),
    path('displaydoctors/', displayDoctors),
    path('drpendingappointments/', showDrPendingAppointments_name),
    path('drappointmentdata/', showDrPendingAppointments),
    path('doctorfix/', DoctorFix),
    path('doctorreject/', DoctorReject),
    path('showdrfixappointments/', showDrFixedAppointments),
    path('drfixaptdata/', showDrFixAptData),
    path('drfixmedicalhistory/', showDrFixedMedicalHistory),
    path('uploadprescription/', uploadprescription),
    path('getprescriptiondata/', getprescriptiondata),
    path('showdrpatients/', showDrPatients),
    path('showdrptvisits/', showDrPtVisits),

]