from django import forms
from django.contrib.auth.models import User
from django.utils import timezone
from category.models import Category, CATEGORY_CHOICES

TRANSACTION_TYPES =(
    ('1','Incasso'),
    ('2','Batch payment'),
    ('3','Batch payment'),
    ('4','Branch withdrawal'),
    ('5','Cash machine'),
    ('6','Deposit'),
    ('7','Online Banking'),
    ('8','Payment terminal'),
    ('9','SEPA direct debit'),
    ('10','Sundries'),
    ('11','Transfer'),
)

class TransactionForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        self.owner = user
        super(CsvFileForm, self).__init__(*args, **kwargs)

    classification  = forms.ChoiceField(label='classification*', choices=TRANSACTION_TYPES)
    amount          = forms.DecimalField(label='amount*', max_digits=100, decimal_places=2)
    date            = forms.DateField(label='date*', initial=timezone.now)
    name            = forms.CharField(label='name*', max_length=150)
    description     = forms.CharField(label='description', max_length=1000)
    counterparty    = forms.CharField(label='counterparty', max_length=150)
    account         = forms.CharField(label='account', max_length=150)
    category        = forms.ChoiceField(label='category', choices=CATEGORY_CHOICES)
