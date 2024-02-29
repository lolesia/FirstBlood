from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.exceptions import ValidationError
from django.db import models
import re
from typing import List


class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields) -> 'User':

        email = self.normalize_email(email)
        user = self.model(email=email,  **extra_fields)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email=email, password=password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=12, unique=True)
    first_name = None
    last_name = None
    username = None
    objects = UserAccountManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: List[str] = []

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


