from django.shortcuts import render
from django.urls import include, path

from . import views

urlpatterns = [
    path('register/', views.index, name='register'),
    path('', views.index, name='index'),
    path('sports/', views.sports, name='sports'),
    path('forms/<str:sport>', views.bookSlot, name='bookSlot')
]

