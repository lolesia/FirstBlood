from django.db import models
from profiles.models import Owner


class Breed(models.Model):

    breed = models.CharField(max_length=255, db_index=True, verbose_name='Порода')

    def __str__(self):
        return self.breed


class Pet(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='pets_owner')
    pet_name = models.CharField(max_length=50, verbose_name="ім'я улюбленця")
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, related_name='breeds')
    weight = models.FloatField(verbose_name='вага')
    photo = models.ImageField(upload_to='static/pet_photo')
    description = models.CharField(max_length=255, verbose_name='особливості')

    def __str__(self):
        return self.pet_name

