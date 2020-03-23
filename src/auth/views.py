from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions

from src.auth.auth_models.blacklisted_user import BlacklistedUser
from src.auth.serializers.user_serializer import UserSerializer
from .auth_models.identifying_document import IdentifyingDocument
from .serializers.blacklisted_user_serializer import BlacklistedUserSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers.identifying_document_serializer import IDSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class IsOwner(permissions.IsAuthenticated):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Instance must have an attribute named `owner`.
        return obj.user == request.user


class IDViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwner]
    http_method_names = ['get', 'post', 'head']
    queryset = IdentifyingDocument.objects.all()
    serializer_class = IDSerializer

    def get_queryset(self):
        return IdentifyingDocument.objects.filter(user=self.request.user)


class BlacklistedUsersViewSet(viewsets.ModelViewSet):
    queryset = BlacklistedUser.objects.all()
    serializer_class = BlacklistedUserSerializer


@api_view()
def null_view(request):
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view()
def complete_view(request):
    return Response("Email account is activated")
