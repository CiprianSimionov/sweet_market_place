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
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # save user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                # if login fails
                return render(request, 'account/register.html', {'form': form, 'error': 'Login failed.'})
    else:
        form = RegisterForm()  #creates new empty forms instance

    return render(request, 'account/register.html', {'form': form})