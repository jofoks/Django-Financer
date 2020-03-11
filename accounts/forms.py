from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.models import User


class SignInFrom(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class':'validate','placeholder': 'username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'password'}))

class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=TextInput(attrs={'class':'validate','placeholder': 'username'}))
    password1 = forms.CharField(widget=PasswordInput(attrs={'placeholder':'password'}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'placeholder':'repeat password'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')