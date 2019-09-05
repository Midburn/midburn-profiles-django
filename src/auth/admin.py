from django.contrib import admin

# Register your models here.
from src.auth.auth_models import BurnerUser

admin.site.register(BurnerUser)