from django.db import models
from address.models import Country, Address
from django.contrib.auth.models import User

ACCOUNTTYPE_CHOICES = (
    ('checkings', 'Checkings'),
    ('savings', 'Savings'),
)

class US_Account(models.Model):
    address         = models.ForeignKey(Address, on_delete=models.CASCADE)
    routingNumber   = models.IntegerField('Routing Number')
    accountNumber   = models.IntegerField('Account Number', unique=True)
    accountType     = models.CharField('Account Type', max_length=50, choices=ACCOUNTTYPE_CHOICES)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'US Bank Account'

    def __str__(self):
        return str(self.routingNumber)

class NL_Account(models.Model):
    name = models.CharField(max_length=200, unique=True)
    AccountNumber = models.CharField('Account Number', max_length=34, unique=True) #18
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'NL Bank Account'

    def __str__(self):
        return self.name