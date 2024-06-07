from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def estadisticas(request):
    return render(request, 'estadisticas.html')


def app(request):
    return render(request, 'app.html')


def base(request):
    return render(request, 'base.html')


def user(request):
    return render(request, 'user.html')
