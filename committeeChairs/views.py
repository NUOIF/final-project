from django.shortcuts import render


# Create your views here.

def home(request):
        return render(request, 'pages_Committee/home.html')


def addidea(request):
        return render(request, 'pages_Committee/add_idea.html')



def show_idea(request):
        return render(request, 'pages_Committee/show_idea.html')


        
