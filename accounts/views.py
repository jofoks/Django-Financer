from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import os

def signup_view(request):
    form = UserCreationForm()
    context = {'form':form}
    return render(request, '../templates/accounts/signup.html', context)

def login_view(request):
    return render(request, 'accounts/login.html')

print(os.getcwd())