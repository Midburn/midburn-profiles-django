from django.contrib.auth import get_user_model
from rest_framework import serializers

from src.auth.auth_models.user import UserStatus
from src.auth.serializers.identifying_document_serializer import IDSerializer
from src.fields.django_rest_enumfield import EnumField

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    status = EnumField(choices=UserStatus)
    ids = IDSerializer(many=False, read_only=True)

    class Meta:
        model = User
        fields = ('pk', 'email', 'first_name', 'last_name', 'city', 'country_code', 'address',
                  'primary_phone_number', 'status', 'ids')

        read_only_fields = ('pk', 'email', 'status', 'ids')
