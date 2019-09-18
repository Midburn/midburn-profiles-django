from django.db import models
import uuid


class BurnEvent(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    details = models.TextField()

