from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

from .views import UserViewSet
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatters = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='django_rest')),
    url(r'^auth/token/verify', verify_jwt_token),
    url(r'^auth/token', obtain_jwt_token),
]