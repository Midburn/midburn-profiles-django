from django.contrib import admin

# Register your models here.
from src.events.events_models.event import BurnEvent

admin.site.register(BurnEvent)
