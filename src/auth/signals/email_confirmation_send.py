from allauth.account.signals import email_confirmed, email_confirmation_sent
from django.dispatch import receiver
from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

sg_client = SendGridAPIClient(settings.SENDGRID_API_KEY)


@receiver(email_confirmed)
def email_confirmed(request, email_address, **kwargs):
    sg_client.client.marketing.contacts.put(request_body={"contacts": [{
        'email': email_address.email,
        'user_id': str(email_address.user.pk)
    }]})


@receiver(email_confirmation_sent)
def email_confirmation_sent(request, confirmation, **kwargs):
    mail = Mail(
        from_email=settings.DEFAULT_FROM_EMAIL,
        to_emails=confirmation.email_address.email
    )

    mail.template_id = settings.SENDGRID_VERIFY_EMAIL
    mail.dynamic_template_data = {'key': confirmation.key}

    sg_client.send(mail)
