from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    type_CHOICES = {
        ("Client","Client"),
        ("Partner", "Partner"),
    }
    city_CHOICES = {
        ("Limassol","Limassol"),
        ("Nicosia", "Nicosia"),
        ("Paphos", "Paphos"),
        ("Paralimni", "Paralimni"),
        ("Larnaka", "Larnaka"),
    }
    country_CHOICES = {
        ("Cyprus","Cyprus"),
        ("Greece", "Greece"),
    }
    id = models.AutoField(primary_key=True)
    user=models.OneToOneField(User, on_delete=models.PROTECT)
    account_type = models.CharField(choices = type_CHOICES,default = "Client", max_length=10)
    phone = models.CharField(max_length=12,default="")
    address = models.CharField(max_length = 40,default="")
    city = models.CharField(choices = city_CHOICES, max_length=20,default="")
    country = models.CharField(choices = country_CHOICES, max_length=10,default="")



    # Override the __unicode__() method to return out something meaningful!
    def __str__(self):
        return self.user.first_name



class Card(models.Model):
    type_CHOICES= {
        ("Synolic Personal","Synolic Personal"),
        ("Synolic Corporate", "Synolic Corporate"),
        ("Synolic Visitors", "Synolic Visitors"),
        ("Synolic Youth", "Synolic Youth"),

    }
    card_number = models.AutoField(primary_key=True)
    date_joined = models.DateField(null=False)
    renewal_date = models.DateField(null=False)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE,default="")
    card_type = models.CharField(choices = type_CHOICES,max_length=30,default="")
    expired = models.BooleanField(default=False)
    active = models.BooleanField(default = False)
    reminder_send = models.BooleanField(default = False)
    # Override the __unicode__() method to return out something meaningful!
    def __str__(self):
        return str(self.card_number)