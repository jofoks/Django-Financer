from .models import Transaction
from django import forms
from django.template.loader import render_to_string
from django.shortcuts import render

def transaction_widget(request):
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

