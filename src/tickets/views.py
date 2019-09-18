from rest_framework import viewsets

from src.tickets.serializers.ticket_type_serializer import TicketTypeSerializer
from src.tickets.models import TicketType, UserTicket
from src.tickets.serializers.user_ticket_serializer import UserTicketSerializer


class TicketsTypeViewSet(viewsets.ModelViewSet):
    queryset = TicketType.objects.all()

    serializer_class = TicketTypeSerializer


class UserTicketsViewSet(viewsets.ModelViewSet):
    queryset = UserTicket.objects.all()

    serializer_class = UserTicketSerializer