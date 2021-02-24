from django.shortcuts import render
from django.contrib.auth import authenticate, login
# from committeeChairs.models import CommitteesCharis
# from students.models import Students
# from doctors.models import Doctors
from .models import Doctors,CommitteesCharis,Students

# Create your views here.

# def login(request):
#     con = mysql.connctor.connect(host="localhost",user="root",passwd="root",database="projectDB")
#     cursor = con.cursor()
#     con2 = mysql.connctor.connect(host="localhost",user="root",passwd="root",database="projectDB")
#     cursor2 = con2.cursor()
#     sqlcommand = "select name_committees_charis from committee_chairs"
#     sqlcommand = "select passwords from committee_chairs"
#     u = []
#     p = []
# def login(request):
#     username = request.POST.get('username')
#     password = request.POST.get('password')
#     committeeInfo = CommitteesCharis(name_committees_charis = username , passwords = password)
#     committeeInfo.save()
#     return render(request, 'login.html')