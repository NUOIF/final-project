import os
from django.shortcuts import render 
from django.db.models import Q
from django.conf import settings
from django.templatetags.static import static
from .models import Evaluation, Projects, Students
from .forms import Add_Idea, CRN, Doc, Stu, Distrbution
from django import forms
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
from .models import Doctors,CommitteesCharis,Students,Groups 
from django.shortcuts import redirect

# Login Pages


## messages for login page

message_welcome = 'Welcome Mr.'
message_error_sorry = "Sorry Mr."
message_error_reason = " the username or password are invalid - please try again"

def login(request):
    return render(request, "login.html")


def loginCommittee(request):
    if request.method=="POST":
        try:
            check_committee = CommitteesCharis.objects.get(
                name_committees_charis = request.POST.get('username'), 
                passwords = request.POST.get('password')
                )
            messages.success(request, message_welcome + request.POST.get('username'))
            return render(request, 'pages_Committee/home.html')
        except CommitteesCharis.DoesNotExist as committeeNull:
            messages.error(request, message_error_sorry + request.POST.get('username') + message_error_reason)
    return render(request, "pages_login/loginCommittee.html")


def loginDoctors(request):
    if request.method=="POST":
        try:
            check_doctor = Doctors.objects.get(
                name_doctors = request.POST.get('username'), 
                passwords = request.POST.get('password')
                )
            messages.success(request, message_welcome + request.POST.get('username'))
            return render(request, 'pages_Doctors/home.html')
        except Doctors.DoesNotExist as doctorNull:
            messages.error(request, message_error_sorry + request.POST.get('username') + message_error_reason)
    return render(request, "pages_login/loginDoctors.html")

def loginStudents(request):
    if request.method=="POST":
        try:
            check_student = Students.objects.get(
                name_Students = request.POST.get('username'), 
                passwords = request.POST.get('password')
                )
            messages.success(request, message_welcome + request.POST.get('username'))
            hisname = {'stdName':request.POST.get('username')}
            return render(request, 'pages_Students/home.html',hisname)
        except Students.DoesNotExist as studentNull:
            messages.error(request, message_error_sorry + request.POST.get('username') + message_error_reason)
    return render(request, "pages_login/loginStudents.html")


## committee chairs views

def committee_home(request):
    return render(request, 'pages_Committee/home.html')





def committee_add_idea(request):
    
    if request.method =='POST':
        Idea = Add_Idea(request.POST, request.FILES)
        if Idea.is_valid():
            Idea.save()
            return redirect('show_suggested_idea')

    context={
        'from':Add_Idea(),
        
    }
    return render(request, 'pages_Committee/add_idea.html',context)

def show_suggested_idea(request):
    
    context={
            'project':Projects.objects.all(),
            
    }
    return render(request, 'pages_Committee/show_suggested_idea.html',context)


def committee_show_idea(request):    
    return render(request, 'pages_Committee/show_idea.html')

def modifying_groups(request):
    if request.method =='POST':
        stu = Stu(request.POST)
        doc = Doc(request.POST)
        if stu.is_valid() and doc.is_valid():
            stu.save()
            doc.save()

    context = {
        'std_forms':Stu(),
        'student':Students.objects.all(),
        'group_forms':Doc(),
        'doctors':Doctors.objects.all(),
    }
    return render(request,'pages_Committee/modifying_groups.html', context)

def Student_update(request,id):
    id_Stu = Students.objects.get(id_students=id)
    if request.method =='POST':
        stu_save = Stu(request.POST,instance= id_Stu)
        if stu_save.is_valid():
            stu_save.save()
            return redirect('/modifying_groups')

    else:
        stu_save = Stu(instance=id_Stu)
        
    context={
        'std_forms':stu_save

    }
    return render(request,'pages_Committee/Student_update.html', context)

def Doctor_update(request,id):
    id_GRO = Doctors.objects.get(id_doctors=id)
    if request.method =='POST':
        do_save = Doc(request.POST,instance= id_GRO)
        if do_save.is_valid():
            do_save.save()
            return redirect('/modifying_groups')

    else:
        do_save = Doc(instance=id_GRO)
        
    context={
        'group_forms':do_save

    }
    return render(request,'pages_Committee/Doctor_update.html', context)


def Add_CRN(request):
    if request.method =='POST':
        cr = CRN(request.POST)
        if cr.is_valid():
            cr.save()

    context={
        'froms':CRN(),
        'groub':Groups.objects.all(),
    }
    return render(request, 'pages_Committee/Add_CRN.html',context)


#CRNهنا سويت فنكشن عشان اقدر اسوي تعديل ل 
def CRN_update(request,id):
    groub_id = Groups.objects.get(id_groups=id)
    if request.method =='POST':
        groub_save = CRN(request.POST,instance=groub_id)
        if groub_save.is_valid():
            groub_save.save()
            return redirect('/Add_CRN')

    else:
        groub_save = CRN(instance=groub_id)
        
    context={
        'form':groub_save

    }
    return render(request,'pages_Committee/CRN_update.html', context)


def show_evaluation(request):
    evaluate = {'evaluation' : Evaluation.objects.all()}
    return render(request, 'pages_Committee/show_evaluation.html', evaluate)

def distrbution_doctors_to_groups(request):
    distrbution_doctors = {
        'evaluation' : Evaluation.objects.exclude(id_doctor_fk = None),
        'evaluator' : Evaluation.objects.filter( Q(id_doctor_fk = None) | Q(id_doctor_fk2 = None) | Q(id_doctor_fk2 = None) ).exclude(id_groups_fk = None),
        }
    return render(request, 'pages_Committee/distrbution_doctors_to_groups.html', distrbution_doctors)

# def distrbution_update(request, id):
#     evaluator1 = Evaluation.objects.get(id_doctor_fk = id)
#     # evaluator2 = Evaluation.objects.get(id_doctor_fk2 = id)
#     # evaluator3 = Evaluation.objects.get(id_doctor_fk3 = id)
#     if request.method == "POST":
#         evaluator1_save = Distrbution(request.POST, instance = evaluator1)
#         # evaluator2_save = Distrbution(request.POST, instance = evaluator2)
#         # evaluator3_save = Distrbution(request.POST, instance = evaluator3)
#         if evaluator1_save.is_valid():
#             evaluator1_save.save()
#             # evaluator2_save.save()
#             # evaluator3_save.save()
#             redirect('/distrbution_doctors_to_groups')
#     else:
#         evaluator1_save = Distrbution(instance = evaluator1)
#         # evaluator2_save = Distrbution(instance = evaluator2)
#         # evaluator3_save = Distrbution(instance = evaluator3)
#     context={
#         'form':evaluator1_save

#     }
#     return render(request,'pages_Committee/distrbution_update.html', context)
# doctors views

def doctors_home(request):
    return render(request, 'pages_Doctors/home.html')

def doctor_show_idea(request):
    return render(request, 'pages_Doctors/doctor_show_idea.html')

def doctor_create_group(request):
    return render(request, 'pages_Doctors/doctor_create_group.html')

def doctor_modification_the_group(request):
    return render(request, 'pages_Doctors/doctor_modification_the_group.html')

def doctor_evaluating_groups(request):
    return render(request, 'pages_Doctors/doctor_evaluating_groups.html')

def doctor_show_my_group_evaluation(request):
    return render(request, 'pages_Doctors/doctor_show_my_group_evaluation.html')


# students views

def student_home(request):
    return render(request, 'pages_students/student_home.html')

def student_show_the_department_idea(request):
    return render(request, 'pages_students/student_show_the_department_idea.html')

def student_show_archived_idea(request):
    return render(request, 'pages_students/student_show_archived_idea.html')

def student_upload_project(request):
    return render(request, 'pages_students/student_upload_project.html')

def student_create_groups(request):
    return render(request, 'pages_students/student_create_groups.html')

def student_dont_groups(request):
    return render(request, 'pages_students/student_dont_groups.html')