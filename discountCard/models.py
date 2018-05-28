from __future__ import unicode_literals
from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
# Create your models here.

class Client(models.Model):
    card_number = models.AutoField(primary_key=True)
    date_joined = models.DateField(null=False)
    name=models.CharField(max_length=20)
    surname=models.CharField(max_length=25)
    email_address=models.EmailField()
    points=models.IntegerField(default=0)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return str(self.name)+ ' ' + str(self.surname) + '--'+ str(self.card_number)
