from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .forms import UserCreationForm

# Create your views here.


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'invalid username or password')
            form = AuthenticationForm(request.POST)
            return render(request, 'user_auth/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'user_auth/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return render(request, 'user_auth/logout.html')


def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password1)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'user_auth/signup.html', {'form': form})
