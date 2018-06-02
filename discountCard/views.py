from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,redirect
from discountCard.forms import  UserForm
from discountCard.models import Card,Profile
from datetime import date
from django.template.context import RequestContext


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
