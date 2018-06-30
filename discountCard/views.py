from django.http import HttpResponse, HttpResponseRedirect
from discountCard.forms import  *
from discountCard.models import Card,Profile
from datetime import date, timedelta
from django.template.context import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.contrib import messages


#Email code snippet
# text = 'This is a reminder that your ' + plans + ' contract, with contract number: ' + str(
#     contract.idcontract) + ' is expiring today! If you dont\' want it to be renewed please get in touch. Thank you, Leads Master'
# send_mail(
#     'Contract Renewal Notification',
#     text,
#     settings.EMAIL_HOST_USER,
#     [contract.client.email]
# )

def index(request):
    return render(request, 'discountCard/index.html')

def become_member(request):
    context = RequestContext(request)
    registered=False
    if request.user.is_authenticated:
        return redirect('choose_card')
    else:
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
                return render(request, 'discountCard/login.html',{'invalid':True,'login_form':login_form},context)

        else:
            print(login_form.errors)

    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        login_form=LoginForm()
        return render(request, 'discountCard/login.html', {'invalid':False,'login_form': login_form}, context)


@login_required
def logout(request):
    django_logout(request)
    return redirect('index')


def choose_card(request):
    context = RequestContext(request)

    if request.method == 'POST':
        card_form = CardForm(data=request.POST)
        if card_form.is_valid():
            current_profile = Profile.objects.get(user=request.user)

            # Card Instance variables
            card_type=card_form.cleaned_data['card_type']
            date_joined=date.today()
            expired = False
            reminder_send = False
            active = True
            if card_type=="Synolic Visitors":
                duration = 15 #days
            else:
                duration = 365 #days
            renewal_date = date_joined + timedelta(days = duration)
            owner = current_profile

            #Create card instance
            new_card = Card(date_joined= date_joined, renewal_date=renewal_date,owner=owner, card_type=card_type, expired=expired,reminder_send=reminder_send, active=active)
            #TODO: This should be done after payment process
            new_card.save()
            return redirect('user_account')
        else:
            print(card_form.errors)
    else:
        card_form=CardForm()
        return render(request, 'discountCard/choose_card.html', {'card_form':card_form}, context)

def register_card(request):
    wrong_card_type=False
    wrong_card_number=False
    if request.method == 'POST':
        register_form = RegisterCardForm(data=request.POST)
        if register_form.is_valid():
            cards=[]

            currentuser = request.user
            current_profile = Profile.objects.get(user=request.user)

            # Card Instance variables
            card_type=register_form.cleaned_data['card_type']
            card_num=register_form.cleaned_data['number']

            #check if card type chosen is same as card type purchased
            found=False
            for card in Card.objects.all():
                print(card.card_number)
                if str(card.card_number)==card_num:
                    if card.card_type==card_type:
                        card.owner= current_profile
                        card.date_joined=date.today()
                        card.expired = False
                        card.reminder_send = False
                        card.active = True
                        if card_type=="Synolic Visitors":
                            duration = 15 #days
                        else:
                            duration = 365 #days
                        card.renewal_date = card.date_joined + timedelta(days = duration)
                        card.save()
                    else:
                        wrong_card_type=True
                        return render(request, 'discountCard/register_card.html',{'register_form':register_form,'wrong_card_type':wrong_card_type,'wrong_card_number':wrong_card_number})
                else:
                    wrong_card_number=True
                    return render(request, 'discountCard/register_card.html',{'register_form':register_form,'wrong_card_type':wrong_card_type,'wrong_card_number':wrong_card_number})

                if found==True:
                            break
            return redirect('user_account')
        else:
            print(register_form.errors)
    else:
        register_form=RegisterCardForm()
        return render(request, 'discountCard/register_card.html',{'register_form':register_form,'wrong_card_type':wrong_card_type,'wrong_card_number':wrong_card_number})


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
                expired=card.expired
        return render(request, 'discountCard/user_account.html',{'user':currentuser,'hascard':hascard,'card':card, 'renewal_date':renewal_d, 'expired':expired},context)
    else:
        return redirect('login')

def renew(request):
    context = RequestContext(request)

    if request.user.is_authenticated:
        #TODO: Pay Here
        card = (Card.objects.get(owner=Profile.objects.get(user=request.user)))
        if card.card_type =="Synolic Visitors":
            card.renewal_date = date.today() + timedelta(days = 15)
        else:
            card.renewal_date = date.today() + timedelta(days = 365)
        card.expired=False
        card.reminder_send=False
        card.save()
        return redirect('user_account')
    else:
        return redirect('login')

def partners(request):
    context = RequestContext(request)
    current_partners=[]
    for partner in User.objects.filter(profile__account_type="Partner"):
        current_partners.append(partner)
    return render(request, 'discountCard/our_partners.html',{'context':context,'partners':current_partners})


def faq(request):
    return render(request, 'discountCard/faq.html')