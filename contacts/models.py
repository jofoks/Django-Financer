import os
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User


STATE_CHOICES = (
    ('AL', ('Alabama')),
    ('AZ', ('Arizona')),
    ('AR', ('Arkansas')),
    ('CA', ('California')),
    ('CO', ('Colorado')),
    ('CT', ('Connecticut')),
    ('DE', ('Delaware')),
    ('DC', ('District of Columbia')),
    ('FL', ('Florida')),
    ('GA', ('Georgia')),
    ('ID', ('Idaho')),
    ('IL', ('Illinois')),
    ('IN', ('Indiana')),
    ('IA', ('Iowa')),
    ('KS', ('Kansas')),
    ('KY', ('Kentucky')),
    ('LA', ('Louisiana')),
    ('ME', ('Maine')),
    ('MD', ('Maryland')),
    ('MA', ('Massachusetts')),
    ('MI', ('Michigan')),
    ('MN', ('Minnesota')),
    ('MS', ('Mississippi')),
    ('MO', ('Missouri')),
    ('MT', ('Montana')),
    ('NE', ('Nebraska')),
    ('NV', ('Nevada')),
    ('NH', ('New Hampshire')),
    ('NJ', ('New Jersey')),
    ('NM', ('New Mexico')),
    ('NY', ('New York')),
    ('NC', ('North Carolina')),
    ('ND', ('North Dakota')),
    ('OH', ('Ohio')),
    ('OK', ('Oklahoma')),
    ('OR', ('Oregon')),
    ('PA', ('Pennsylvania')),
    ('RI', ('Rhode Island')),
    ('SC', ('South Carolina')),
    ('SD', ('South Dakota')),
    ('TN', ('Tennessee')),
    ('TX', ('Texas')),
    ('UT', ('Utah')),
    ('VT', ('Vermont')),
    ('VA', ('Virginia')),
    ('WA', ('Washington')),
    ('WV', ('West Virginia')),
    ('WI', ('Wisconsin')),
    ('WY', ('Wyoming'))
)

class Contact(models.Model):
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    email           = models.EmailField(max_length=70, blank=True)
    limit           = models.Q(app_label = 'bankAccounts', model = 'nl_account') | models.Q(app_label = 'bankAccounts', model = 'us_account')
    content_type    = models.ForeignKey(ContentType,
                                    on_delete=models.CASCADE,
                                    blank=True,
                                    limit_choices_to= limit)
    object_id       = models.PositiveIntegerField(blank=True)
    account         = GenericForeignKey('content_type', 'object_id')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
