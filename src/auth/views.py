from django.contrib.auth import get_user_model
from rest_framework import viewsets

from src.auth.auth_models.blacklisted_user import BlacklistedUser
from src.auth.serializers.user_serializer import UserSerializer
from .serializers.blacklisted_user_serializer import BlacklistedUserSerializer

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class BlacklistedUsersViewSet(viewsets.ModelViewSet):
    queryset = BlacklistedUser.objects.all()
    serializer_class = BlacklistedUserSerializer