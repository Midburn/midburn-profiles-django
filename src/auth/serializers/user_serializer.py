from django.contrib.auth import get_user_model
from rest_framework import serializers

from src.auth.auth_models.user import UserStatus
from src.fields.django_rest_enumfield import EnumField

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    status = EnumField(choices=UserStatus)

    class Meta:
        model = User
        fields = ('pk', 'email', 'first_name', 'last_name', 'city', 'country_code', 'address',
                  'primary_phone_number', 'status')

        read_only_fields = ('pk', 'email', 'status')
