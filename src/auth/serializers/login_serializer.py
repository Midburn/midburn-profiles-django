from rest_framework import serializers
from rest_auth.serializers import LoginSerializer


class MidburnLoginSerializer(LoginSerializer):

    username = None

    email = serializers.EmailField(required=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
