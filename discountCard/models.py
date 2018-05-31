from django.db import models
from django.contrib.auth.models import User


class Card(models.Model):
    card_number = models.AutoField(primary_key=True)
    date_joined = models.DateField(null=False)
    renewal_date = models.DateField(null=False)

class Profile(models.Model):
    type_CHOICES = {
        ("Client","Client"),
        ("Partner", "Partner"),
    }
    id = models.AutoField(primary_key=True)
    user=models.OneToOneField(User, on_delete=models.PROTECT)
    account_type = models.CharField(choices = type_CHOICES,default = "Client", max_length=10)
    card_number = models.OneToOneField(Card, on_delete=models.CASCADE,)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.id
