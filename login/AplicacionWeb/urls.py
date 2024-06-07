from django.contrib import admin
from django.urls import path, include
from .views import home
from login.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('login.urls')),  # Asegúrate de que hay una coma aquí
    path('', home, name='home')
]