from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('become_member/', views.become_member, name = 'become_member'),
    path('become_partner/', views.become_partner, name = 'become_partner'),
    path('partners/', views.become_partner, name = 'partners'),
    path('faq/', views.become_partner, name = 'faq')


]