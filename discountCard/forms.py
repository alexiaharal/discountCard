
from django.db import models
from django.forms import ModelForm
from django import forms
from discountCard.models import  Profile
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, login, logout


class UserForm(forms.Form):

    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password',widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='Confirm Password',widget=forms.PasswordInput())
    firstname= forms.CharField(label='First Name')
    lastname = forms.CharField(label = 'Last Name')
    email = forms.CharField(label = 'Email Address')
    phone = forms.CharField(label='Phone Number')
    address = forms.CharField(label='Address')
    city = forms.CharField(label='City')
    country = forms.CharField(label='Country')

    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')

        # Check to see if any users already exist with this email as a username.
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            # Unable to find a user, this is fine
            return email

        # A user was found with this as a username, raise an error.
        raise forms.ValidationError('This email address is already in use.')

    def clean(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Passwords do not match"
            )

class CardForm(forms.Form):
    type_CHOICES= {
        ("Synolic Personal","Synolic Personal"),
        ("Synolic Corporate", "Synolic Corporate"),
        ("Synolic Visitors", "Synolic Visitors"),
        ("Synolic Youth", "Synolic Youth"),
    }
    period_CHOICES= {
        ("Three Months","Three Months"),
        ("Six Months","Six Months"),
        ("Nine Months","Nine Months"),
        ("Year", "Year"),
    }
    card_type = forms.ChoiceField(choices = type_CHOICES, label='Card Type')
    #card_period = forms.ChoiceField(choices = period_CHOICES, label = 'Card Issue Period')


class LoginForm(forms.Form):
    username= forms.CharField(label='Username', max_length=30)
    password = forms.CharField(label='Password',widget=forms.PasswordInput())


class RegisterCardForm(forms.Form):
    type_CHOICES= {
        ("Synolic Personal","Synolic Personal"),
        ("Synolic Corporate", "Synolic Corporate"),
        ("Synolic Visitors", "Synolic Visitors"),
        ("Synolic Youth", "Synolic Youth"),
    }
    number = forms.CharField(label='Card Number')
    card_type = forms.ChoiceField(choices = type_CHOICES, label='Card Type')
    #card_period = forms.ChoiceField(choices = period_CHOICES, label = 'Card Issue Period')

