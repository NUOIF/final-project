from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    path('', views.login, name='login'),
    # committees paths
    path('loginCommittee', views.loginCommittee, name='loginCommittee'),
    path('committee_home', views.committee_home, name='committee_home'),
    path('committee_add_idea', views.committee_add_idea, name='committee_add_idea'),
    path('committee_show_idea', views.committee_show_idea, name='committee_show_idea'),
    path('committee_add_student_to_groups', views.committee_add_student_to_groups,name='committee_add_student_to_groups'),
    path('committee_add_doctor_to_groups', views.committee_add_doctor_to_groups,name='committee_add_doctor_to_groups'),
    path('Add_CRN', views.Add_CRN,name='Add_CRN'),
    path('show_evaluation', views.evaluation, name='show_evaluation'),
    # doctors paths
    path('loginDoctors', views.loginDoctors, name='loginDoctors'),
    path('doctors_home', views.doctors_home, name='doctors_home'),
    # students paths
    path('loginStudents', views.loginStudents, name='loginStudents'),
    path('studnet_home' ,views.students_home, name='students_home'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
