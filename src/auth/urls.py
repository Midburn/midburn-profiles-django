from rest_framework import routers

from .views import BlacklistedUsersViewSet

router = routers.DefaultRouter()
router.register(r'users/blacklisted', BlacklistedUsersViewSet)

users_api_router = router
