from django.shortcuts import render
from .models import *



# Create your views here.

def home(request):
        return render(request, 'pages_Comm/home.html')


def addidea(request):
        return render(request, 'pages_Comm/add_idea.html')



def showidea(request):
        return render(request, 'pages_Comm/show_idea.html')


def Add_student_To_groups(request):

        # context = {
         
        #  'stu':Students.objects.all(),

        # }

        return render(request, 'pages_Comm/Add_student_To_groups.html')


def Add_doctor_To_groups(request):
        return render(request, 'pages_Comm/Add_doctor_To_groups.html')