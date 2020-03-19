from django.urls import path
from rest_auth.views import LoginView, LogoutView, UserDetailsView, PasswordChangeView

from .auth.urls import users_api_router
from rest_framework.documentation import include_docs_urls
from django.conf.urls import include, url
from django.contrib import admin

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenVerifyView,
)

rest_auth_url_patterns = [
    # URLs that do not require a session or valid token
    url(r'^login/$', LoginView.as_view(), name='rest_login'),
    # URLs that require a user to be logged in with a valid session / token.
    url(r'^logout/$', LogoutView.as_view(), name='rest_logout'),
    url(r'^user/$', UserDetailsView.as_view(), name='rest_user_details'),
    url(r'^password/change/$', PasswordChangeView.as_view(),
        name='rest_password_change'),
]


urlpatterns = [
    path('tech_admin/', admin.site.urls),
    url(r'^api/auth/', include(rest_auth_url_patterns)),
    url(r'^api/auth/registration/', include('rest_auth.registration.urls')),
    url(r'^api/auth/password/reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    url(r'^docs/', include_docs_urls(title='Midburn API', public=False)),
    url(r'^api/v1/', include(users_api_router.urls))
]
