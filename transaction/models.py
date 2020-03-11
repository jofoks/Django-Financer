from django.db import models
from django.contrib.auth.models import User

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

class Transaction(models.Model):
    _type           = models.CharField(max_length=150, choices=TRANSACTION_TYPES)
    amount          = models.DecimalField(max_digits=100, decimal_places=2)
    date            = models.DateField()
    name            = models.CharField(max_length=150)
    description     = models.CharField(max_length=1000, blank=True)
    category        = models.CharField(max_length=150, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta: 
        ordering = ['-date']

class CsvFile(models.Model):
    csv = models.FileField(upload_to='transaction/cache')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

