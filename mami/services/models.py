from django.db import models
from profile.models import Breed


class Services(models.Model):
    service = models.CharField(max_length=50)
    breed = models.ForeignKey(Breed, on_delete=models.PROTECT, blank=True, verbose_name='Порода')
    cost_kiev = models.IntegerField(verbose_name='Вартість Київ')
    cost_murgorod = models.IntegerField(verbose_name='Вартість Миргород')
    service_time = models.CharField(max_length=255, verbose_name='Час виконання')
    content = models.TextField(max_length=255, blank=True, null=True, verbose_name='Опис')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ціни'
        verbose_name_plural = 'Ціна'

