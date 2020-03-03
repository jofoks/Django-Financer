from django.db import models
from django.contrib.auth.models import User

class KeyWord(models.Model):
    name        = models.CharField(max_length=150) 

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'keywords'

    def __str__(self):
        return self.name

class Category(models.Model):
    name        = models.CharField(max_length=150)
    keywords    = models.ManyToManyField(KeyWord)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
