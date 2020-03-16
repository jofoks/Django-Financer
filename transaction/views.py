from .models import Transaction
from django import forms
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from .forms import TransactionForm
from datetime import datetime
from django.contrib.auth.decorators import login_required
from static.scripts.csv_interpreter import handle_file

def home_widget(request):
    total_count = Transaction.objects.filter(owner=request.user).count()
    if total_count > 5:
        show_count = 5
    else: show_count = total_count
    show_content = reversed( Transaction.objects.order_by('-id')[:show_count] )
    text = f'These are your last {show_count} transactions. And here will go some more information about some other crap'
    content = {
        'total_count'   : total_count,
        'show_count'    : show_count,
        'show_content'  : show_content,
        'text'          : text
    }
    return render(request, 'transaction/transaction_widget.html', content)

def edit_view(request):
    context = {
        'form': TransactionForm,
        'now' : datetime.now,
        'user' : request.user
    }
    return render(request, 'transaction/edit.html', context)

@login_required
def upload_view(request):
    if request.method == 'POST':
        if len(request.FILES) != 0:
            error = handle_file(user=request.user, csv=request.FILES['csv'])
            print(f'\n {error} \n')
            if error:
                return render(request, 'transaction/upload.html', {'error': error})
            return redirect('home')
        return render(request, 'transaction/upload.html', {'error': 'Please select a file'})
    return render(request, 'transaction/upload.html')

@login_required
def oversight_view(request):
    user_transactions = Transaction.objects.filter(owner=request.user)
    context = {
        'transactions' : user_transactions,
    }
    return render(request, 'transaction/oversight.html', context)
