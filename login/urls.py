from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [

    path('', views.login, name='login'),

    # committees paths

    path('loginCommittee',                   views.loginCommittee,                    name='loginCommittee'),
    path('committee_home',                   views.committee_home,                    name='committee_home'),
    path('committee_add_idea',               views.committee_add_idea,                name='committee_add_idea'),
    path('committee_show_idea',              views.committee_show_idea,               name='committee_show_idea'),
    path('show_suggested_idea',              views.show_suggested_idea,               name='show_suggested_idea'),
    path('modifying_groups',                 views.modifying_groups,                  name='modifying_groups'),
    path('show_evaluation',                  views.show_evaluation,                   name='committee_add_doctor_to_groups'),
    path('distrbution_doctors_to_groups',    views.distrbution_doctors_to_groups,     name='modifying_groups'),
    path('Add_CRN',                          views.Add_CRN,                           name='Add_CRN'),
    path('<int:id>/CRN_update/',             views.CRN_update,                        name='CRN_update'),#Url for page update
    path('<int:id>/Doctor_update/',          views.Doctor_update,                     name='Doctor_update'),
    path('<int:id>/Student_update',          views.Student_update,                    name='Student_update'),
    path('distrbution_update/<int:id>',      views.distrbution_update,                name='distrbution_update'),

    # doctors paths   

    path('loginDoctors',                     views.loginDoctors,                      name='loginDoctors'),
    path('doctors_home',                     views.doctors_home,                      name='doctors_home'),
    path('doctor_show_idea',                 views.doctor_show_idea,                  name='doctor_show_idea'),
    path('doctor_create_group',              views.doctor_create_group ,              name='doctor_create_group'),
    path('doctor_modification_the_group',    views.doctor_modification_the_group ,    name='doctor_modification_the_group'),
    path('doctor_evaluating_groups',         views.doctor_evaluating_groups ,         name='doctor_evaluating_groups'),
    path('doctor_show_my_group_evaluation',  views.doctor_show_my_group_evaluation ,  name='doctor_show_my_group_evaluation'),
    # students paths  

    path('loginStudents',                    views.loginStudents,                     name='loginStudents'),
    path('student_home' ,                    views.student_home,                      name='student_home'),
    path('student_show_the_department_idea', views.student_show_the_department_idea , name='student_show_the_department_idea'),
    path('student_show_archived_idea',       views.student_show_archived_idea ,       name='student_show_archived_idea'),
    path('student_upload_project',           views.student_upload_project ,           name='student_upload_project'),
    path('student_create_groups',            views.student_create_groups ,            name='student_create_groups'),
    path('student_dont_groups',              views.student_dont_groups ,              name='student_dont_groups'),
    path('Chose_Enter/<int:id>',             views.Chose_Enter,                       name='Chose_Enter'),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
