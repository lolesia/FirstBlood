from django.db import models
import uuid
from users.models import User
from services.models import Services


class Visits(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='visits')
    service = models.ForeignKey(Services, on_delete=models.PROTECT, related_name='services')
    data = models.DateField()
    time = models.TimeField()
