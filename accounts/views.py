from django.shortcuts import render

# from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreateForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required



def register_account(request):
    if request.method == 'GET':
        # return render(request, 'register.html', {'form': UserCreationForm})
        return render(request, 'register.html', {'form': UserCreateForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'],
                    password=request.POST['password1']
                )
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'register.html', {'form': UserCreateForm, 'error': 'User already exists'})
                # return render(request, 'register.html', {'form': UserCreationForm, 'error': 'User already exists'})

        else:
            return render(request, 'register.html', {'form': UserCreateForm, 'error': 'Passwords do not match'})
            # return render(request, 'register.html', {'form': UserCreationForm, 'error': 'Passwords do not match'})

@login_required
def logout_account(request):
    logout(request)
    return redirect('home')

def login_account(request):
    if request.method == 'GET':
        return render(request, 'login_account.html', {'form': AuthenticationForm})
    else:
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is None:
            return render(request, 'login_account.html', {'form': AuthenticationForm, 'error': 'Username and Password do not match'})
        else:
            login(request, user)
            return redirect('home')

