from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('user/', views.User, name='user-register'),
    path('post/', views.post, name='user-post'),
    path('login/', views.login, name='user-login'),
]