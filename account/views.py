from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from .forms import LoginForm, UserRegistrationForm
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
            return redirect('dashboard')  # Redirect to dashboard page
        else:
            return render(request, 'account/login.html', {'form': form})


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirecciona al usuario a la página de inicio de sesión
    else:
        form = UserRegistrationForm()
    return render(request, 'account/register.html', {'form': form})
