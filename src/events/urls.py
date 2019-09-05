from django.conf.urls import url, include
from rest_framework import routers
from .views import EventsViewSet

router = routers.DefaultRouter()
router.register(r'events', EventsViewSet)

events_url_patterns = [
    url(r'^events/', include(router.urls)),
]