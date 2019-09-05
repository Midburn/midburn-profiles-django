from rest_framework import viewsets
from src.events.events_models.event import BurnEvent
from src.events.serializers.burn_event_serializer import BurnEventSerializer


class EventsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = BurnEvent.objects.all()

    serializer_class = BurnEventSerializer