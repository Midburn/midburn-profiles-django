from rest_framework import serializers

from src.tickets.tickets_models.user_ticket import UserTicket


class UserTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTicket
        fields = ('id', 'user_id', 'ticket_type_id', 'purchase_time', 'used', 'active')
