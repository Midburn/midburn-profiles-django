from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer


class MidburnRegisterSerializer(RegisterSerializer):

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    address = serializers.CharField(max_length=15)
    birthday = serializers.DateField(format='%Y-%m-%d', input_formats=None)
    city = serializers.CharField(max_length=15, default='IL')
    country_code = serializers.CharField(max_length=15, default='IL')
    email = serializers.EmailField(max_length=40, min_length=None, allow_blank=False)
    identification_number = serializers.CharField(max_length=15)
    identification_type = serializers.ChoiceField(
        choices=(
            ('tz', 'tz'),
            ('ps', 'ps'),
        ),
        default='tz',
    )
    passport_country = serializers.CharField(max_length=15, default='IL')
    primary_phone_number = serializers.CharField(max_length=15, default='IL')

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['id'] = self.validated_data.get('id', '')
        data_dict['email'] = self.validated_data.get('email', '')
        data_dict['passport_country'] = self.validated_data.get('passport_country', '')
        data_dict['country_code'] = self.validated_data.get('country_code', '')
        data_dict['city'] = self.validated_data.get('city', '')
        data_dict['address'] = self.validated_data.get('address', '')
        data_dict['birthday'] = self.validated_data.get('birthday', '')
        data_dict['primary_phone_number'] = self.validated_data.get('primary_phone_number', '')
        data_dict['identification_number'] = self.validated_data.get('identification_number', '')
        data_dict['identification_type'] = self.validated_data.get('identification_type', '')
        return data_dict
