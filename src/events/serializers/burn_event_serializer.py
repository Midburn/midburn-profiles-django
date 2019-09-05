from rest_framework import serializers

from src.events.events_models.event import BurnEvent


class BurnEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BurnEvent
        fields = ('id', 'name', 'start_time', 'end_time')
