from django.db import models
from contacts.models import Contact
from django.utils.timezone import now
from django.contrib.auth.models import User

class Debt(models.Model):
    name        = models.CharField(max_length=256)
    description = models.CharField(max_length=1024, blank=True)
    amount      = models.DecimalField(max_digits=64, decimal_places=2)
    creditor    = models.ForeignKey(Contact, on_delete=models.CASCADE)
    dueDate     = models.DateField('Due Date', blank=True)
    startDate   = models.DateField('Start Date', default=now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-amount']