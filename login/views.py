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
            return render(request, 'basic_committee.html')
        except CommitteesCharis.DoesNotExist as committeeNull:
            messages.success(request,"Username OR Password Invalid ..!")
    return render(request, "login.html")

## committee chairs views

def home(request):
        return render(request, 'pages_Committee/home.html')


def addidea(request):
        return render(request, 'pages_Committee/add_idea.html')



def showidea(request):
        return render(request, 'pages_Committee/show_idea.html')


def Add_student_To_groups(request):
        context = {
                'student':Students.objects.all(),
                'group':Groups.objects.all(),
                }
        return render(request, 'pages_Committee/Add_student_To_groups.html', context)


def Add_doctor_To_groups(request):
        return render(request, 'pages_Committee/Add_doctor_To_groups.html')
