
from django.db import models
from django.forms import ModelForm
from django import forms
from discountCard.models import  Profile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
            model = User
            fields = ('username','first_name', 'last_name', 'email','password')

