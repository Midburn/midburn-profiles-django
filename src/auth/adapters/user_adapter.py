from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):

    def send_mail(self, template_prefix, email, context):
        a = 5
        print(template_prefix, email)

    def send_confirmation_mail(self, request, email_confirmation, signup):
        a = 5
        print(email_confirmation.key)
