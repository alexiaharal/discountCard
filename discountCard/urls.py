from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('become_member/', views.become_member, name = 'become_member'),
    path('become_partner/', views.become_partner, name = 'become_partner'),
    path('partners/', views.partners, name = 'partners'),
    path('faq/', views.faq, name = 'faq'),
    path('login/',views.login, name = 'login'),
    path('logout/',views.logout, name = 'logout'),
    path('user_account/', views.user_account, name='user_account'),
    path('user_account/renew/', views.renew, name='renew'),
    path('payment_process/', views.payment, name='payment')




]