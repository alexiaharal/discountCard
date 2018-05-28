from django.db import models

# Create your models here.

class Client(models.Model):
    card_number = models.AutoField(primary_key=True)
    date_joined = models.DateField(null=False)
    name=models.CharField(max_length=20)
    surname=models.CharField(max_length=25)
    email_address=models.EmailField()
    points=models.IntegerField(default=0)
