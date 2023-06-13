from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from users.models import User
import uuid


class Reviews(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET('Анонім'), blank=True)
    text = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True)
    score = models.IntegerField(default=5, validators=[MinValueValidator(0), MaxValueValidator(5)], help_text='оберіть оцінку якості обслуговування')

