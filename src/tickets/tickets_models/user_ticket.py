from datetime import datetime
import uuid

from django.db import models

from src.auth.auth_models import BurnerUser
from src.tickets.tickets_models.ticket_type import TicketType


class UserTicket(models.Model):

    # For barcode all you need is to encode the UUID into a barcode
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(BurnerUser, null=False, related_name='tickets', on_delete=models.PROTECT)
    ticket_type = models.ForeignKey(TicketType, null=False, related_name='user_tickets', on_delete=models.PROTECT)
    purchase_time = models.DateTimeField(default=datetime.now)
    used = models.BooleanField(default=False)

    #If cancelled can change to False
    active = models.BooleanField(default=False)

