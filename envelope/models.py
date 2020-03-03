from django.db import models
from django.contrib.auth.models import User
author = models.ForeignKey(User, on_delete=models.CASCADE)

class fixedCharge(models.Model):
    name            = models.CharField(max_length=252, unique=True)
    description     = models.CharField(max_length=1024, blank=True)
    amount          = models.DecimalField(max_digits=99, decimal_places=2)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-amount']

class incomeFraction(models.Model):
    name            = models.CharField(max_length=252, unique=True)
    description     = models.CharField(max_length=1024, blank=True)
    amount          = models.DecimalField('Allocation (%)', max_digits=99, decimal_places=2)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-amount']
