from django.urls import path
from .views import LoginView, dashboard, register

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', register, name='register'),
    path('', dashboard, name='dashboard'),
]