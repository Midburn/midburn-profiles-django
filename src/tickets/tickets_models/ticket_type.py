import uuid

from django.db import models

from src.events.events_models.event import BurnEvent


class TicketType(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()
    event = models.ForeignKey(BurnEvent, null=False, related_name='ticket_types', on_delete=models.CASCADE)
    price = models.IntegerField()
    currency = models.CharField(max_length=8, default='NIS')
    #How many tickets of this type exist
    allocation = models.IntegerField(null=False)
    allocation_type = models.TextField(null=True, default=None, blank=True)
    # should add limitations etc maybe type from an enum