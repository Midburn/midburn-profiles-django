from django.apps import AppConfig


class AuthConfig(AppConfig):
    name = 'src.auth'
    label = 'tech_auth'

    def ready(self):
        from .signals import email_confirmed, email_confirmation_sent, password_reset_token_created
