from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView as AuthLoginView
from django.contrib.auth.views import LogoutView as AuthLogoutView
from account.forms import RegisterForm
from django.contrib.auth import authenticate, login
# Create your views here.

class LoginView(AuthLoginView):
    template_name = 'account/login.html'

class LogoutView(AuthLogoutView):
    template_name = 'account/logout.html'

def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'account/register.html', context={'form': form})
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username, password)
            if user:
                login(request, user)
            return redirect('/')