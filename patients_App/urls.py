from django.urls import path

# from patients.models import bookappointments
from .views import BookAppointment, LogoutPatient, RegisterPatient,LoginPatient, Dashboard, addM_history,  previousAppointments, rejectedAppointments, rejectreason, showPendingAppointment_pt, showPtFixedAppointments, viewpendingappointments, viewptprescription
urlpatterns = [
    # path('', home_views , name='home'),
    # path('admin/', admin.site.urls),
    # path('about/', about , name='about'),
    path('register/', RegisterPatient),
    path('login/', LoginPatient),
    path('logout/', LogoutPatient),
    path('dashboard/', Dashboard),
    path('bookappointment/', BookAppointment),
    path('pt_pendingappointments/', showPendingAppointment_pt),
    path('ptfixedappointments/', showPtFixedAppointments),
    path('addmedicalhistory/', addM_history),
    path('ptpreviousappointments/', previousAppointments),
    path('viewptprescription/', viewptprescription), 
    path('ptrejectedappointments/', rejectedAppointments),
    path('rejectreason/', rejectreason),
    path('viewpendingappointments/', viewpendingappointments),


]   