from django.shortcuts import render


# Create your views here.

def home(request):
        return render(request, 'pages_Comm/home.html')


def addidea(request):
        return render(request, 'pages_Comm/add_idea.html')



def showidea(request):
        return render(request, 'pages_Comm/show_idea.html')


        