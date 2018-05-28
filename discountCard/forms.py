
from django.db import models
from django.forms import ModelForm
from django import forms
from discountCard.models import Client
from django.contrib.auth.models import User

# User Form
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

#Client Form

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['card_number','date_joined','name','surname','email_address']
    labels = {
        'card_number' : "Card Number",
        'date_joined' : "Date Joined",
        'name': "Name",
        'surname': "Surname",
        'email_address': "Email Address"
    }
