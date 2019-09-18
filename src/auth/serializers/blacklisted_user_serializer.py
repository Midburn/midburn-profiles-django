from rest_framework import serializers

from src.auth.auth_models.blacklisted_user import BlacklistedUser


class BlacklistedUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BlacklistedUser
        fields = ('id', 'user_id', 'start_date', 'end_date', 'details')