from django.conf.urls import url, include
from rest_framework import routers
from .views import TicketsTypeViewSet, UserTicketsViewSet

router = routers.DefaultRouter()
router.register(r'types', TicketsTypeViewSet)
router.register(r'user_tickets', UserTicketsViewSet)


tickets_url_patterns = [
    url(r'^tickets/', include(router.urls)),
]