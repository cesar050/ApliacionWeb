# Description: This file contains the URL patterns for the login app.
from django.urls import path, include
from .views import login

urlpatterns = [
    path('', login, name='login'),
]

