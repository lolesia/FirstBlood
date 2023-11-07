from django.db import models
from pets.models import Breed
from profiles.models import Groomer


class Portfolio(models.Model):

    image = models.ImageField(upload_to='static/portfolio', default='')
    date = models.DateTimeField(auto_now_add=True)
    breed = models.ForeignKey(Breed, on_delete=models.PROTECT, related_name='portfolio')
    groomer = models.ForeignKey(Groomer, on_delete=models.CASCADE, related_name='portfolio')


