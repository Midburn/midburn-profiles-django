from rest_framework import serializers

from src.tickets.tickets_models.ticket_type import TicketType


class TicketTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketType
        fields = ('id', 'name', 'event', 'price', 'currency', 'allocation', 'allocation_type')
