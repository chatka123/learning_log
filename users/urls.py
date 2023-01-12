"""Defines circuit of URL for users"""
from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns=[
    # include URL login default
    path('', include('django.contrib.auth.urls')),
    # page of registration
    path('register/', views.register, name='register'),
]