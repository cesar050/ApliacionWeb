from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from .forms import LoginForm, RegisterForm
from django.contrib.auth.decorators import login_required

@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('user')  # Redirect to dashboard page
        else:
            return render(request, 'account/login.html', {'form': form})

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'account/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:login')  # Redirect to login page
        else:
            return render(request, 'account/register.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'user.html')



