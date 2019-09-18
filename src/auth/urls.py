from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

from .views import UserViewSet, BlacklistedUsersViewSet
router = routers.DefaultRouter()
router.register(r'blacklisted', BlacklistedUsersViewSet)
router.register(r'', UserViewSet)

urlpatters = [
    url(r'^users/', include(router.urls)),
    url(r'^web-login/', include('rest_auth.urls')),
    url(r'^token/verify', verify_jwt_token),
    url(r'^token', obtain_jwt_token),
]