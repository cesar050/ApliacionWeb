from django.urls import path
from .views import LoginView, dashboard

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('', dashboard, name='dashboard')
]