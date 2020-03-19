from django.dispatch import receiver
from django.conf import settings
from django_rest_passwordreset.signals import reset_password_token_created
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

sg_client = SendGridAPIClient(settings.SENDGRID_API_KEY)


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    mail = Mail(
        from_email=settings.DEFAULT_FROM_EMAIL,
        to_emails=reset_password_token.user.email
    )

    mail.template_id = settings.SENDGRID_RESET_PASSWORD_TEMPLATE
    mail.dynamic_template_data = {'key': reset_password_token.key}

    try:
        sg_client.send(mail)
    except Exception as e:
        print(e.message)
