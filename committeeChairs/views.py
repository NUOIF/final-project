from django.shortcuts import render
from .models import Students, Groups



# Create your views here.

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
