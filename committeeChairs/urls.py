from django.urls import path
from .import views

urlpatterns = [ 
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('add_idea.html', views.addidea, name='add_idea'),
    path('show_idea', views.showidea, name='show_idea'),
    ]
