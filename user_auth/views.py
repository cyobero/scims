from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

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
