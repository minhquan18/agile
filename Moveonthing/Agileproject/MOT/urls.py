from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Agile, name= 'Agile'),
    path('forgot',views.Forgot, name='Forgot'),
]
