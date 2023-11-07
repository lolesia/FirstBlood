from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


class BaseProfile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    avatar = models.ImageField(upload_to="static/avatars", blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(auto_now_add=False, default=None, null=True, blank=True)

    class Meta:
        abstract = True

    @property
    def age(self):
        return (timezone.now() - self.date_of_birth).days // 365

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Owner(BaseProfile):

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='owner')


class Groomer(BaseProfile):

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='groomer')




