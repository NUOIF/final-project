from django.shortcuts import render
from django.contrib.auth import authenticate, login
# from committeeChairs.models import CommitteesCharis
# from students.models import Students
# from doctors.models import Doctors
from .models import Doctors,CommitteesCharis,Students

# Create your views here.

def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    committeeInfo = CommitteesCharis(name_committees_charis = username , passwords = password)
    committeeInfo.save()
    return render(request, 'login.html')


# from django.contrib.auth import authenticate
# user = authenticate(username='john', password='secret')
# if user is not None:
#     # A backend authenticated the credentials
# else:
#     # No backend authenticated the credentials

# from django.contrib.auth import authenticate, login

# def my_view(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         # Redirect to a success page.
#         ...
#     else:
#         # Return an 'invalid login' error message.
#         ...