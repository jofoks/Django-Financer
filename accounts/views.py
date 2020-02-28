from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'You did it {username}!')
    else:
        form =UserCreationForm()
    context = {'form':form}
    return render(request, 'accounts/register.html', context)

def login_view(request):
    if request.method =='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('admin')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})

print(os.getcwd())