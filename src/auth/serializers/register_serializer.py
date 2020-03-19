from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer


class MidburnRegisterSerializer(RegisterSerializer):

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['username'] = self.validated_data.get('email')
        return data_dict
