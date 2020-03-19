from allauth.account.models import EmailAddress
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from enum import Enum
import uuid


class UserStatus(Enum):
    PENDING = 'PENDING'
    MISSING_INFO = 'MISSING_INFO'
    VERIFIED = 'VERIFIED'


class BurnerUserManager(UserManager):
    def create_superuser(self, email, password, **extra_fields):
        print(email, password)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        user = self._create_user(email, email, password, **extra_fields)

        EmailAddress.objects.create(email=email, verified=True, primary=True, user_id=user.id)

        return user


class BurnerUser(AbstractUser):
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    address = models.TextField(null=True, default=None)
    birthday = models.DateField(null=True)
    city = models.TextField(null=True, default=None)
    country_code = models.CharField(max_length=15, default='IL')
    email = models.EmailField(_('email address'), unique=True, db_index=True, blank=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    primary_phone_number = PhoneNumberField(default=None, blank=True, null=True)

    objects = BurnerUserManager()

    def clean(self):
        self.username = self.email
        super().clean()

    def get_model_fields(self):
        return self._meta.fields

    def is_missing_info(self):
        from src.auth.auth_models.identifying_document import IdentifyingDocument
        
        return not IdentifyingDocument.objects.filter(user_id=self.pk).exists()

    @property
    def status(self):
        if EmailAddress.objects.filter(user_id=self.pk, verified=True).exists():
            return UserStatus.MISSING_INFO if self.is_missing_info() else UserStatus.VERIFIED

        return UserStatus.PENDING
