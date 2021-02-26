from django.urls import path
from .import views
from committeeChairs.urls import urlpatterns
urlpatterns = [ 
    path('', views.login, name='login'),
    # committees paths
    path('committee-home', views.home, name='committee-home'),
    path('committee-add-idea', views.addidea, name='committee-add-idea'),
    path('committee-show-idea', views.showidea, name='committee-show-idea'),
    path('committee-add-student-to-groups', views.Add_student_To_groups,name='committee-add-student-to-groups'),
    path('committee-add-doctor-to-groups', views.Add_doctor_To_groups,name='committee-add-doctor-to-groups'),
    # doctors paths
    # students paths
    ]
