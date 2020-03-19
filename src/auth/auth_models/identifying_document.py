import uuid
from django.db import models
from src.auth.auth_models import BurnerUser


class IdentifyingDocument(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(BurnerUser, null=False, related_name='identifying_documents', on_delete=models.CASCADE)
    identification_number = models.CharField(max_length=15, null=False, blank=False)
    identification_type = models.CharField(choices=(('tz', 'tz'), ('ps', 'ps'),), default='tz', max_length=2)
    passport_country = models.CharField(max_length=15, default='IL')

    class Meta:
        unique_together = ('identification_number', 'identification_type', 'passport_country')
