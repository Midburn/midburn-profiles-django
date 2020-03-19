from rest_auth.serializers import PasswordResetSerializer
from allauth.account.forms import ResetPasswordForm


class PasswordSerializer(PasswordResetSerializer):

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    password_reset_form_class = ResetPasswordForm
