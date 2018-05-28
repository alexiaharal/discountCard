from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from discountCard.forms import ClientForm, UserForm

def index(request):
    return render(request, 'discountCard/index.html')

def become_member(request):

    registered = False

    if request.method == 'POST':
        client_form =  ClientForm(data=request.POST)

        #if form is valid ...
        if client_form.is_valid():
            client = client_form.save()
            registered = True
        else:
            print(client_form.errors)
    else:
        client_form = ClientForm()
    return render(request,'discountCard/become_member.html',{'client_form':client_form,'registered':registered})

def become_partner(request):
    return render(request,'discountCard/become_partner.html')