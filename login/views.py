from django.shortcuts import render, get_object_or_404
from django import forms
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
from .models import Doctors,CommitteesCharis,Students,Groups
# Create your views here.

def login(request):
    if request.method=="POST":
        try:
            committee = CommitteesCharis.objects.get(
                name_committees_charis = request.POST.get('username'), 
                passwords = request.POST.get('password')
                )
            print("Welcome committee = ", committee)
            request.session['username'] = committee.name_committees_charis
            messages.success(request, "Correct ..!")
            return render(request, 'basic_committee.html')
        except CommitteesCharis.DoesNotExist as committeeNull:
            messages.error(request,"Username OR Password Invalid ..!")
    return render(request, "login.html")

## committee chairs views

def committee_home(request):
    return render(request, 'pages_Committee/home.html')


def committee_add_idea(request):
    return render(request, 'pages_Committee/add_idea.html')



def committee_show_idea(request):
    return render(request, 'pages_Committee/show_idea.html')


def committee_add_student_to_groups(request):
    # studnetData = request.GET.get('stdselect')
    # groupData = request.GET.get('groupselect')
    # databoth = Students.objects.update(name_Students=studnetData)
    studnetField = Students.objects.filter(id_groups_fk=None)
    groupField = Groups.objects.exclude(id_groups=None)
    std  = Students.objects.filter(id_groups_fk=None)
    our_form = request.POST
    if request.method == 'POST':
        studentsID = request.POST.create('std')
        groupID = request.POST.create('group')
        data = Students,Groups(id_Students = studentsID, id_groups = groupID)
        data.save()
    #studnetField.save()
    context = {
            'student':std,
            'groups': groupField,
    }

    return render(request, 'pages_Committee/Add_student_To_groups.html', context)


# def committee_add_student_to_groups(request):
#     context = {
#             'student':Students.objects.all(),
#             }
    
#     if request.method=="POST":
#         studentsID = request.POST['students']
#         groupID = request.POST.['group']
#         data = Students(name_Students = studentsID, id_groups_fk = groupID)
#         data.save()
#     return render(request, 'pages_Committee/Add_student_To_groups.html', context)


def committee_add_doctor_to_groups(request):
    context = {
            'doctor':Doctors.objects.all(),
            }
    return render(request, 'pages_Committee/Add_doctor_To_groups.html', context)

def Add_CRN(request):
        context={
                'doctor':Doctors.objects.all(),
                'groub':Groups.objects.all(),

        }


        return render(request, 'pages_Committee/Add_CRN.html',context)












def evaluation(request):
        return render(request, 'pages_Committee/show_evaluation.html')
# doctors views

def doctors_home(request):
    return render(request, 'baisc_doctors.html')

# students views
