import uuid

from django.db import models

from src.auth.auth_models import BurnerUser


class BlacklistedUser(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(BurnerUser, null=False, related_name='blacklists', on_delete=models.CASCADE)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)

    details = models.TextField(null=False)


