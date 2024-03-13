from django.db import models
from profiles.models import Groomer


class Type(models.Model):
    type = models.CharField(max_length=255, verbose_name='Тип витрат')

    def __str__(self):
        return self.type


class Expenses(models.Model):
    groomer = models.ForeignKey(Groomer, on_delete=models.SET_NULL, null=True, related_name='grooming_expenses')
    type = models.ForeignKey(Type, on_delete=models.PROTECT, related_name='expenses_type', verbose_name='Тип витрат')
    name = models.CharField(max_length=255, verbose_name='Назва придбаного товару')
    cost = models.IntegerField(verbose_name='Вартість')
    date = models.DateField()
    comment = models.CharField(max_length=255, blank=True, verbose_name='Коментар')

    def __str__(self):
        return self.type.type
