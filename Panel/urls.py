from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('form/<str:slug>', views.form, name='form'),
    path('alter/<str:slug>', views.alter),
    path('delete/<str:slug>', views.delete)
    
]