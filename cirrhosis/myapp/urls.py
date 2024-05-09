
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.login, name='login'),
    path('home',views.home, name='home'),
    path('result/',views.result, name="result"),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    
    
]
