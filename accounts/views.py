from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import RegisterForm
from datetime import datetime as dt
from django.contrib.auth.decorators import login_required
from transaction.models import Transaction
from django.db.models import Sum

def suffix(d):
    return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')

def custom_strftime(format, t):
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def initial_view(request):
    return render(request, 'accounts/initial.html')

@login_required
def home_view(request):
    if request.user.is_authenticated:
        transaction_snippet = Transaction.objects.filter(owner=request.user)[:5]
        balance = Transaction.objects.filter(owner=request.user).aggregate(Sum('amount'))['amount__sum']
        if not balance:
            balance = 0.00
        context = {
            'user': request.user,
            'date' : custom_strftime('%B {S}', dt.now()),
            'trans_snippet' : transaction_snippet,
            'balance': "$%.2f" % round(balance, 2),
        }
        return render(request, 'home.html', context)
    return redirect('login')
