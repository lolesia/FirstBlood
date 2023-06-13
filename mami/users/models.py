import uuid

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.exceptions import ValidationError
from django.db import models
import re


class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, last_name, phone, password=None) -> 'User':

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, last_name=last_name, phone=phone)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, last_name, phone,  password=None):
        user = self.create_user(email, name, last_name, phone,  password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    CITY = [
        ('KIEV', 'Київ'),
        ('MYRGOROD', 'Миргород'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=12, unique=True)
    city = models.CharField(max_length=10, choices=CITY, verbose_name='Місто')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        pattern = r'^[\+]?3?[\s]?8?[\s]?\(?0\d{2}?\)?[\s]?\d{3}[\s|-]?\d{2}[\s|-]?\d{2}$'
        if not re.match(pattern, self.phone):
            raise ValidationError({'phone_number': 'Перевірте вірність номеру телефону'})
        else:
            super(User, self).save(*args, **kwargs)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'last_name', 'phone']