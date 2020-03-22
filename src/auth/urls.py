from rest_framework import routers

from .views import BlacklistedUsersViewSet, IDViewSet

router = routers.DefaultRouter()
router.register(r'users/blacklisted', BlacklistedUsersViewSet)
router.register(r'users/id', IDViewSet)

users_api_router = router
