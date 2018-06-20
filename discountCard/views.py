from django.http import HttpResponse
from discountCard.forms import  UserForm,LoginForm,CardForm
from discountCard.models import Card,Profile
from datetime import date
from django.template.context import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.contrib import messages

def index(request):
    return render(request, 'discountCard/index.html')

def become_member(request):
    context = RequestContext(request)
    registered=False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid() :
            #Store fields into variables
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']
            confirm_password = user_form.cleaned_data['confirm_password']
            firstname= user_form.cleaned_data['firstname']
            lastname = user_form.cleaned_data['lastname']
            email = user_form.cleaned_data['email']
            phone = user_form.cleaned_data['phone']
            address = user_form.cleaned_data['address']
            city = user_form.cleaned_data['city']
            country = user_form.cleaned_data['country']
           # card_type = user_form.cleaned_data['card_type']

            #Create user instance

            user = User(username=username, password=password, first_name=firstname, last_name=lastname, email=email)
            #user.set_password(user.password)
            user.save()

            #Create Profile instance
            profile = Profile(user=user,account_type='Client',phone= phone, address=address,city=city,country=country)
            profile.save()

            # #Create card instance
            # renewal_period=1
            # #r_date=date.replace(year = date.year + renewal_period)
            # new_card = Card(date_joined= date.today(), renewal_date=date.today(),owner=profile,card_type=card_type)
            # new_card.save()

            registered = True
            auth_login(request, user)
            return redirect('choose_card')
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
            #Store fields into variables
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']
            confirm_password = user_form.cleaned_data['confirm_password']
            firstname= user_form.cleaned_data['firstname']
            lastname = user_form.cleaned_data['lastname']
            email = user_form.cleaned_data['email']
            phone = user_form.cleaned_data['phone']
            address = user_form.cleaned_data['address']
            city = user_form.cleaned_data['city']
            country = user_form.cleaned_data['country']
            #card_type = user_form.cleaned_data['card_type']

            #Create user instance

            user = User(username=username, password=password, first_name=firstname, last_name=lastname, email=email)
            #user.set_password(user.password)
            user.save()

            #Create Profile instance
            profile = Profile(user=user,account_type='Partner',phone= phone, address=address,city=city,country=country)
            profile.save()



            registered = True
            return redirect('choose_card')
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request, 'discountCard/become_member.html', {
        'user_form': user_form,
        'registered': registered,
        'context': context
    })


def partners(request):
    context = RequestContext(request)
    current_partners=[]
    for partner in User.objects.filter(profile__account_type="Partner"):
        current_partners.append(partner)
    return render(request, 'discountCard/our_partners.html',{'context':context,'partners':current_partners})


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

def choose_card(request):
    context = RequestContext(request)

    if request.method == 'POST':
        card_form = CardForm(data=request.POST)
        if card_form.is_valid():
            card_type=card_form.cleaned_data['card_type']
            card_period=card_form.cleaned_data['card_period']
            current_profile = Profile.objects.get(user=request.user)

            #Create card instance
            renewal_period=1
            #r_date=date.today.replace(year = date.today.year + renewal_period)
            new_card = Card(date_joined= date.today(), renewal_date=date.today(),owner=current_profile, card_type=card_type)
            new_card.save()
            return redirect('user_account')
        else:
            print(card_form.errors)
    else:
        card_form=CardForm()
        return render(request, 'discountCard/choose_card.html', {'card_form':card_form}, context)

def register_card(request):
    user = request.user
    return render(request, 'discountCard/register_card.html',{'user':user})


@login_required
def logout(request):
    django_logout(request)
    return redirect('index')

def user_account(request):
    context = RequestContext(request)

    if request.user.is_authenticated:
        hascard=False
        expired=False
        currentuser=request.user
        renewal_d=date.today
        card=""
        for card in Card.objects.all():
            if card.owner==currentuser.profile:
                card = (Card.objects.get(owner=Profile.objects.get(user=request.user)))
                renewal_d=(Card.objects.get(owner=Profile.objects.get(user=request.user))).renewal_date
                hascard=True
                if renewal_d<date.today():
                    expired=-True
        return render(request, 'discountCard/user_account.html',{'user':currentuser,'hascard':hascard,'card':card,'expired':expired, 'renewal_date':renewal_d},context)
    else:
        return redirect('login')

def renew(request):
    context = RequestContext(request)

    if request.user.is_authenticated:
        currentuser=request.user
        renewal_d=currentuser.profile.card_number.renewal_date
        expired=False
        if renewal_d<date.today():
            expired=-True
        return render(request, 'discountCard/renew.html',{'expired':expired},context)
    else:
        return redirect('login')