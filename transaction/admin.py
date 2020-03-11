from django.contrib import admin

from .models import Transaction, CsvFile

admin.site.register(Transaction)
admin.site.register(CsvFile)
# Register your models here.
