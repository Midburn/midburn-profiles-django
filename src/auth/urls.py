from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

from allauth.account.views import ConfirmEmailView
from src.auth.views import null_view, complete_view

from .views import UserViewSet, BlacklistedUsersViewSet

router = routers.DefaultRouter()
router.register(r'blacklisted', BlacklistedUsersViewSet)
router.register(r'', UserViewSet)

urlpatters = [
    url(r'^users/', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^token/verify', verify_jwt_token),
    url(r'^token', obtain_jwt_token),
    # Override urls
    url(r'^registration/account-email-verification-sent/', null_view, name='account_email_verification_sent'),
    url(r'^registration/account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(), name='account_confirm_email'),
    url(r'^registration/complete/$', complete_view, name='account_confirm_complete'),
    url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', null_view, name='password_reset_confirm'),
]