import uuid

from django.db import models
from users.models import User


class Breed(models.Model):

    breed = models.CharField(max_length=255, db_index=True, verbose_name='Порода')

    def __str__(self):
        return self.breed


class Pet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pet_users')
    pet_name = models.CharField(max_length=50, verbose_name="ім'я улюбленця")
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, related_name='breeds')
    weight = models.FloatField(verbose_name='вага')
    photo = models.ImageField(upload_to='static/pet_photo')
    description = models.CharField(max_length=255, verbose_name='особливості')

    def __str__(self):
        return self.pet_name


