from django.urls import path
from .views import home, about, estadisticas, app, base, user

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('estadisticas/', estadisticas, name='estadisticas'),
    path('app/', app, name='app'),
    path('base/', base, name='base'),
    path('user/', user, name='user'),
]
