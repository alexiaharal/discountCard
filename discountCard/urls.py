from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('become_member/', views.become_member, name = 'become_member'),
    path('become_partner/', views.become_partner, name = 'become_partner'),
    path('faq/', views.faq, name = 'faq'),
    path('login/',views.login, name = 'login'),
    path('logout/',views.logout, name = 'logout'),
    path('user_account/', views.user_account, name='user_account'),
    path('user_account/renew/', views.renew, name='renew'),
    path('choose_card/', views.choose_card, name='choose_card'),
    path('partners/', views.partners, name='partners'),
    path('register_card/', views.register_card, name='register_card'),






]