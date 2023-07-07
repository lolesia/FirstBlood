import uuid

from django.db import models
from profile.models import Breed


class Portfolio(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='static/portfolio', default='')
    date = models.DateTimeField(auto_now_add=True)
    breed = models.ForeignKey(Breed, on_delete=models.PROTECT, related_name='portfolio')


