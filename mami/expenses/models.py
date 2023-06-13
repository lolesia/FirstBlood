import uuid

from django.db import models


class Type(models.Model):
    type = models.CharField(max_length=255, verbose_name='Тип витрат')

    def __str__(self):
        return self.type


class Expenses(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.ForeignKey(Type, on_delete=models.PROTECT, verbose_name='Тип витрат')
    name = models.CharField(max_length=255, verbose_name='Назва придбаного товару')
    cost = models.IntegerField(verbose_name='Вартість')
    date = models.DateTimeField(auto_now=True)
    comment = models.CharField(max_length=255, blank=True, verbose_name='Коментар')

    def __str__(self):
        return self.type



