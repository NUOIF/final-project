import os
import re
from typing import ContextManager
from django.shortcuts import render 
from django.db.models import Q
from django.conf import settings
from django.templatetags.static import static
from .models import Evaluation, Projects, Students
from .forms import Add_Idea, CRN, ChoiceIdea, Doc, Stu, Distrbution  ,dont_have_groupeFORM ,UploadIdeaForm, Add_GRP, ChoiceIdea , Choose_group, InsertIdea, ChooseGroupDoctor, DoctorCreatingGroup, DoctorEvaluatingGroupForm
from django import forms
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
from .models import Doctors,CommitteesCharis,Students,Groups 
from django.shortcuts import redirect
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session
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
            request.session['name'] = request.POST.get('username')
            return render(request, 'pages_Committee/home.html')
        except CommitteesCharis.DoesNotExist as committeeNull:
            messages.error(request, message_error_sorry + request.POST.get('username') + message_error_reason)
    return render(request, "pages_login/loginCommittee.html")







def loginDoctors(request):
    if request.method=="POST":
        try:
            check_doctor = Doctors.objects.get(
                id_bu = request.POST.get('id'), 
                passwords = request.POST.get('password')
                )
            messages.success(request, message_welcome + request.POST.get('id'))
            ## get session of the doctor name
            doctorName = Doctors.objects.filter(id_bu = request.POST.get('id')).values('name_doctors')
            toStr = str(doctorName)
            format1 = re.findall('[a-zA-Z]+', toStr)
            request.session['name'] = format1[3]
            # end the session of the doctor name 
            # get doctor id in the system
            doctorIdSystem = Doctors.objects.filter(id_bu = request.POST.get('id')).values('id_doctors')
            tostring = str(doctorIdSystem)
            format1 = re.findall('[0-9]+', tostring)
            returnToIntId = int(format1[0])
            request.session['id'] = returnToIntId
            global doctorID
            def doctorID():
                return returnToIntId
            # end the doctor id in the system
            #get the doctor group id 
            doctorBU_ID = request.POST.get('id')
            doctorGroupID = Doctors.objects.filter(id_bu = doctorBU_ID).values('id_groups_fk')
            tostr = str(doctorGroupID)
            format1 = re.findall('[0-9]+', tostr)
            format2 = format1[0]
            format3 = int(format2)
            getDoctor = Doctors.objects.filter(id_groups_fk = format2)
            print(getDoctor)
            global hisGroupID
            def hisGroupID():
                return format3
            # end the doctor group id 
            # get the doctor bu id 
            request.session['idbu'] = doctorBU_ID
            global doctor_bu_id
            def doctor_bu_id():
                return doctorBU_ID
            # end the doctor bu id 
            return render(request, 'pages_Doctors/home.html')
        except Doctors.DoesNotExist as doctorNull:
            messages.error(request, message_error_sorry + request.POST.get('id') + message_error_reason)
    return render(request, "pages_login/loginDoctors.html")


#doctorName = request.POST.get('username')
#request.session['name'] = doctorName





def loginStudents(request):
    if request.method=="POST":
        try:
            check_student = Students.objects.get(
                bu_id = request.POST.get('bu_id'), 
                passwords = request.POST.get('password')
                )
            messages.success(request, message_welcome + request.POST.get('bu_id'))
            ## get session of the student name
            student_name = Students.objects.filter(bu_id = request.POST.get('bu_id')).values('name_Students')
            toStr = str(student_name)
            format1 = re.findall('[a-zA-Z]+', toStr)
            request.session['Name'] = format1
            print(format1[3])
            # end the session of the student name 
            # get student id in the system
            studentIdSystem = Students.objects.filter(bu_id = request.POST.get('bu_id')).values('id_students')
            tostring = str(studentIdSystem)
            format1 = re.findall('[0-9]+', tostring)
            returnToIntId = int(format1[0])
            request.session['id'] = returnToIntId
            print(returnToIntId)
            global studentID
            def studentID():
                return returnToIntId
            # end the student id in the system
            #get the student group id 
            studentBU_ID = request.POST.get('bu_id')
            studentGroupID = Students.objects.filter(bu_id = studentBU_ID).values('id_groups_fk')
            tostr = str(studentGroupID)
            format1 = re.findall('[0-9]+', tostr)
            format2 = format1[0]
            format3 = int(format2)
            get_student = Students.objects.filter(id_groups_fk = format3)
            print(get_student)
            global hisGroupID
            def hisGroupID():
                return get_student
            # end the doctor group id 
            # get the doctor bu id 
            request.session['idbu'] = studentBU_ID
            global student_bu_id
            def student_bu_id():
                return studentBU_ID
            # end the doctor bu id 
            request.session['name'] = request.POST.get('bu_id')
            return render(request, 'pages_Students/student_home.html')
        except Students.DoesNotExist as studentNull:
            messages.error(request, message_error_sorry + request.POST.get('bu_id') + message_error_reason)
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
        'evaluator' : Evaluation.objects.filter( Q(id_doctor_fk = None) | Q(id_doctor_fk2 = None) | Q(id_doctor_fk3 = None) ).exclude(id_groups_fk = None),
        'evaluators': Evaluation.objects.all()
        }
    return render(request, 'pages_Committee/distrbution_doctors_to_groups.html', distrbution_doctors)

redirect_distrbution_page = '/distrbution_doctors_to_groups'
path_distrbution_update = 'pages_Committee/distrbution_update.html'

def distrbution_update(request,id):
    evaluators = Evaluation.objects.get(id_evaluation = id)
    if request.method == "POST":
        evaluator_save = Distrbution(request.POST, instance = evaluators)
        if evaluator_save.is_valid():
            evaluator_save.save()
            return redirect(redirect_distrbution_page) 
    else:
        evaluator_save = Distrbution(instance = evaluators)

    context={
        'evaluator_from':evaluator_save,
    }
    return render(request, 'pages_Committee/distrbution_update.html', context)

# doctors views

def doctors_home(request):
    return render(request, 'pages_Doctors/home.html')


def doctor_show_idea(request):

    context = {
    
        'show':Groups.objects.all(),
        'projects':Projects.objects.all().exclude(id_groups_fk = None),
        'doctors':Doctors.objects.filter(id_bu = doctor_bu_id()),
        'doctorForm':ChooseGroupDoctor()
    }
    return render(request, 'pages_Doctors/doctor_show_idea.html', context)

def doctor_choose_idea(request,id):
    chooseID = Doctors.objects.get(id_doctors=id)
    if request.method =='POST':
        Choose_save = ChooseGroupDoctor(request.POST,instance=chooseID)
        if Choose_save.is_valid():
            Choose_save.save()
            return redirect('/doctor_show_idea')
    else:
        Choose_save = ChooseGroupDoctor(instance=chooseID)

    context={'from':Choose_save}
    return render(request, 'pages_Doctors/doctor_choose_idea.html', context)

def doctor_create_group(request):
    if request.method =='POST':
        global upload 
        upload = Groups.objects.create(name_groups = request.POST.get('create'))
        upload.save()
        return redirect('/doctor_message_creating_group')
    global groupsID
    def groupsID():
        return upload
        

    context = {
        'students':Students.objects.all(),
        'create': DoctorCreatingGroup(),
        'hi':Add_GRP(),
    }
    return render(request, 'pages_Doctors/doctor_create_group.html', context)

def doctor_message_creating_group(request):
    msg = {'msg':"Success You have been added group ID " + str(groupsID())}
    return render(request, 'pages_Doctors/doctor_message_creating_group.html', msg)

def doctor_creating_group(request, id):
    Group = Students.objects.get(id_students=id)
    if request.method =='POST':
        Choose_save = Add_GRP(request.POST,instance=Group)
        if Choose_save.is_valid():
            Choose_save.save()
            return redirect('/doctor_create_group')
    else:
        Choose_save = Add_GRP(instance=Group)
    context={
        'from':Choose_save
    }
    return render(request,'pages_Doctors/doctor_creating_group.html', context)


def doctor_show_my_group(request):
    student = Students.objects.all().filter(id_groups_fk = hisGroupID()).values('name_Students')
    for n in student:
        x = n
    tostr = str(student)
    format1 = re.findall('[a-zA-Z]+', tostr)
    context = {
        'groupid':Groups.objects.all().filter(id_groups = hisGroupID()),
        'hisStudents':Students.objects.all().filter(id_groups_fk = hisGroupID()),
        'mygroup':hisGroupID()
    }
    return render(request, 'pages_Doctors/doctor_show_my_group.html',context)

def doctor_evaluating_groups(request):

    context ={
        'evaluations': Evaluation.objects.filter(Q(id_doctor_fk = doctorID()) | Q(id_doctor_fk2 = doctorID() ) | Q(id_doctor_fk3 = doctorID())),
    }
    return render(request, 'pages_Doctors/doctor_evaluating_groups.html' ,context)


def doctor_upload_file(request,id):
    Eval = Evaluation.objects.get(id_evaluation=id)
    if request.method =='POST':
        Chose_save = DoctorEvaluatingGroupForm(request.POST,instance=Eval)
        if Chose_save.is_valid():
            Chose_save.save()
            return redirect('/doctor_evaluating_groups')
    else:
        Chose_save = DoctorEvaluatingGroupForm(instance=Eval)
    context={
        'from':Chose_save
    }
    return render(request,'pages_Doctors/doctor_upload_file.html', context)


def doctor_show_my_group_evaluation(request):
    context = {
        'doctor_evaluating':Evaluation.objects.filter(id_groups_fk = hisGroupID()),
    }
    return render(request, 'pages_Doctors/doctor_show_my_group_evaluation.html',context)

# students views

def student_home(request):
    return render(request, 'pages_Students/student_home.html')




def student_show_the_department_idea(request):
    if request.method =='POST':
        ge = ChoiceIdea(request.POST)
        if ge.is_valid():
            ge.save()
    context={
        'froms':ChoiceIdea(),
        'project':Projects.objects.all(),
        'choiceidea':Students.objects.all(),   
    }
    return render(request, 'pages_Students/student_show_the_department_idea.html',context)


def Chose_Enter(request,id):
    Group = Students.objects.get(id_students=id)
    if request.method =='POST':
        Chose_save = ChoiceIdea(request.POST,instance=Group)
        if Chose_save.is_valid():
            Chose_save.save()
            return redirect('/student_show_the_department_idea')
    else:
        Chose_save = ChoiceIdea(instance=Group)
    context={
        'from':Chose_save
    }
    return render(request,'pages_students/Chose_Enter.html', context)










def student_show_archived_idea(request):
    context = {
        'archiveed': Projects.objects.all(),
    }
    return render(request, 'pages_students/student_show_archived_idea.html' ,context)


     

def student_upload_project(request):
    if request.method =='POST':
        upload = UploadIdeaForm(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('student_show_archived_idea')

    context ={
        'Upload_form': UploadIdeaForm(),
    }
    return render(request, 'pages_students/student_upload_project.html' ,context)


def student_create_groups(request):
    if request.method =='POST':
        upload = InsertIdea(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('message_create_group')

    context ={
        'students': Students.objects.all(),
        'from': InsertIdea(),
        'projects': Projects.objects.all()
    }
    return render(request, 'pages_students/student_create_groups.html' ,context)

def choose_group(request,id):
    choose_group = Students.objects.get(id_students=id)
    if request.method =='POST':
        save_group = Choose_group(request.POST,instance=choose_group)
        if save_group.is_valid():
            save_group.save()
            return redirect('/student_create_groups')
    else:
        save_group = Choose_group(instance=choose_group)
    context={
        'from':save_group
    }
    return render(request,'pages_students/choose_group.html', context)

# def insert_idea(request):
#     if request.method =='POST':
#         upload = InsertIdea(request.POST, request.FILES)
#         if upload.is_valid():
#             upload.save()
#             return redirect('message_create_group')

#     context ={
#         'from': InsertIdea(),
#     }
#     return render(request,'pages_students/insert_idea.html', context)

def message_create_group(request):
    msg = {'msg':'You have been insert your idea'}
    return render(request, 'pages_students/message_create_group.html', msg)


def student_dont_groups(request):
    context ={
        'dont_have_groupe_form': dont_have_groupeFORM()
    }
    return render(request,'pages_students/create_update.html', context)






def student_dont_groups(request):
    context = {
        'grops': Students.objects.all(),
        'stdname': Session.objects.all()
    }
    return render(request, 'pages_students/student_dont_groups.html' ,context)






