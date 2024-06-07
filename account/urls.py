from django.urls import path
from .views import LoginView, dashboard, RegisterView

app_name = 'account'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    #path('agregar_brazo/', agregar_brazo, name='agregar_brazo'),
    path('', dashboard, name='dashboard')
]