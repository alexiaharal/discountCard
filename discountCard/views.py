from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,redirect
from discountCard.forms import  UserForm,LoginForm
from discountCard.models import Card,Profile
from datetime import date
from django.template.context import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login as auth_login


def index(request):
    return render(request, 'discountCard/index.html')

def become_member(request):
    context = RequestContext(request)
    registered=False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid() :
            #Create user instance
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            #Create card instance
            renewal_period=1
            print(date)
            #r_date=date.replace(year = date.year + renewal_period)
            new_card = Card(date_joined= date.today(), renewal_date=date.today())
            new_card.save()

            #Create Profile instance
            profile = Profile(user=user,card_number=new_card,account_type='Client')
            profile.save()

            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request, 'discountCard/become_member.html', {
        'user_form': user_form,
        'registered': registered,
        'context': context
    })
def become_partner(request):
    context = RequestContext(request)
    registered=False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid() :
        #Create user instance
            user = user_form.save()
            user.set_password(user.password)
            user.save()

        #Create card instance
            renewal_period=1
            #r_date=date.replace(year = date.year + renewal_period)
            new_card = Card(date_joined= date.today(), renewal_date=date.today())
            new_card.save()

        #Create Profile instance
            profile = Profile(user=user,card_number=new_card,account_type='Partner')
            profile.save()

            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request,'discountCard/become_partner.html', {
        'user_form': user_form,
        'registered': registered,
        'context': context
    })

def partners(request):
    return render(request, 'discountCard/partners.html')


def faq(request):
    return render(request, 'discountCard/faq.html')

def login(request):
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        login_form=LoginForm(request.POST)
        if login_form.is_valid():
            username=login_form.cleaned_data['username']
            password=login_form.cleaned_data['password']

            # Use Django's machinery to attempt to see if the username/password
            # combination is valid - a User object is returned if it is.
            user = authenticate(username=username, password=password)

            # If we have a User object, the details are correct.
            # If None, no user with matching credentials was found.
            if user:
                # Is the account active? It could have been disabled.
                if user.is_active:
                    # If the account is valid and active, we can log the user in.
                    # send the user back to the homepage.
                    auth_login(request, user)
                    return redirect('index')
                else:
                    # An inactive account was used - no logging in!
                    return HttpResponse("Your account is disabled.")
            else:
                # Bad login details were provided. So we can't log the user in.
                print ("Invalid login details: {0}, {1}".format(username, password))
                return HttpResponse("Invalid login details supplied.")
        else:
            print(login_form.errors)


    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        login_form=LoginForm()
        return render(request, 'discountCard/login.html', {'login_form': login_form}, context)

@login_required
def logout(request):
    django_logout(request)
    return redirect('index')