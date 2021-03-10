from django.urls import path
from .import views

urlpatterns = [
    path('', views.login, name='login'),
    # committees paths
    path('committee_home', views.committee_home, name='committee_home'),
    path('committee_add_idea', views.committee_add_idea, name='committee_add_idea'),
    path('committee_show_idea', views.committee_show_idea, name='committee_show_idea'),
    path('show_suggested_idea', views.show_suggested_idea, name='show_suggested_idea'),
    path('committee_add_student_to_groups', views.committee_add_student_to_groups,name='committee_add_student_to_groups'),
    path('committee_add_doctor_to_groups', views.committee_add_doctor_to_groups,name='committee_add_doctor_to_groups'),
    path('Add_CRN', views.Add_CRN,name='Add_CRN'),
    path('<int:id>',views.update,name='update'),#Url for page update
    # doctors paths
    path('doctors_home', views.doctors_home, name='doctors_home'),
    # students paths
    ]
