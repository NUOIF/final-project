from django.shortcuts import render
from django.contrib import messages
from .models import Doctors,CommitteesCharis,Students,Groups
# Create your views here.

def login(request):
    if request.method=="POST":
        try:
            committee = CommitteesCharis.objects.get(id_committees_charis = request.POST['username'], passwords = request.POST['password'])
            print("Welcome committee = ", committee)
            request.session['username'] = committee.id_committees_charis
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
    context = {
            'student':Students.objects.all(),
            'group':Groups.objects.all(),
            }
    return render(request, 'pages_Committee/Add_student_To_groups.html', context)


def committee_add_doctor_to_groups(request):
    return render(request, 'pages_Committee/Add_doctor_To_groups.html')











def evaluation(request):
        return render(request, 'pages_Comm/show_evaluation.html')
# doctors views

def doctors_home(request):
    return render(request, 'baisc_doctors.html')

# students views
