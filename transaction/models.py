from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import migrations

class Transaction(models.Model):
    kind            = models.CharField(max_length=150)
    date            = models.DateField(default=timezone.now)
    amount          = models.DecimalField(max_digits=100, decimal_places=2)
    name            = models.CharField(max_length=150)
    description     = models.CharField(max_length=1000, blank=True)
    category        = models.CharField(max_length=150, blank=True)
    counterparty    = models.CharField(max_length=150, blank=True)
    account         = models.CharField(max_length=150, blank=True)
    owner           = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta: 
        ordering = ['-owner', '-date']

class CsvFile(models.Model):
    csv = models.FileField(upload_to='transaction/cache')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
