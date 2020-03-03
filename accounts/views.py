from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created, you can now log in!')
            return redirect('login')
    else:
        form =UserCreationForm()
    context = {'form':form}
    return render(request, 'accounts/register.html', context)

def home_view(request):
    if request.user.is_authenticated:
        context = {'user'}
        return render(request, 'home.html')
    return redirect('login')