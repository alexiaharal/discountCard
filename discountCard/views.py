from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
    return render(request, 'discountCard/index.html')

def become_member(request):
    return render(request,'discountCard/become_member.html')

def become_partner(request):
    return render(request,'discountCard/become_partner.html')