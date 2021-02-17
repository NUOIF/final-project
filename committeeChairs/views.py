from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

def index(request):
    mycontent = {'name':'hamad'}
    return render(request, 'committeeChairs/index.html',mycontent)

def style(request):
    return render(request, 'committeeChairs/style.css'),