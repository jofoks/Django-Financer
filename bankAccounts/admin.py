from django.contrib import admin
from .models import US_Account, NL_Account

admin.site.register(US_Account)
admin.site.register(NL_Account)