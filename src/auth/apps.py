from django.apps import AppConfig


class AuthConfig(AppConfig):
    name = 'src.auth'
    label = 'tech_auth'

    def ready(self):
        from .signals.password_reset_email_sender import reset_password_token_created
