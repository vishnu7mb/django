from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name="home"),
    path('blackpink',views.bp,name="bp"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact")  
    
]
