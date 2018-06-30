from django.apps import AppConfig
from datetime import date
from django.core.mail import send_mail
from django.conf import settings



class DiscountcardConfig(AppConfig):
    name = 'discountCard'

    def ready(self):
        import discountCard.models

        #check any expired cards
        for card in discountCard.models.Card.objects.all():
            print('date today' + str(date.today()))
            print('renewal date' + str(card.renewal_date))
            if date.today()>card.renewal_date:
                    card.expired=True
                    card.save()
            #send email reminder if reminder was not already sent
            if card.expired==True and card.reminder_send==False :
                receiver_email = card.owner.user.email
                text = 'This is a reminder that your discount card has expired and can no longer be used. Please log in to your account to renew your card. Thank you!'
                send_mail(
                    'Contract Renewal Notification',
                    text,
                    settings.EMAIL_HOST_USER,
                    [receiver_email]
                )
                card.reminder_send=True
                card.save()
