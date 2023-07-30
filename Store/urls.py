from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('<int:id>', views.index, name="Home2"),
    path('product/<str:slug>', views.product, name="Product"),
    path('checkout/', views.checkout, name="Checkout"),
    path('search/', views.search, name="Search"),
    
   
]
