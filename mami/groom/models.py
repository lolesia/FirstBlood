from django.core.exceptions import ValidationError
from django.db import models
import re


class Client(models.Model):

    STATUS_CHOICES = [
        ('WAITING', 'Очікує'),
        ('ACCEPTED', 'Прийнято'),
        ('PROCESSING', 'В обробці'),
        ('DECLINED', 'Відхилено'),
    ]

    CITY = [
        ('KIEV', 'Київ'),
        ('MYRGOROD', 'Миргород'),
    ]
    client_name = models.CharField(max_length=255, verbose_name="Ім'я")
    city = models.CharField(max_length=10, choices=CITY, verbose_name='Місто')
    pet_name = models.CharField(max_length=255, verbose_name='Кличка тварини')
    breed = models.ForeignKey('Breed', on_delete=models.PROTECT, verbose_name='Порода')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефону')
    photo = models.FileField(upload_to='static/groom', verbose_name='Фото')
    comments = models.TextField(max_length=255, blank=True, null=True, verbose_name='Коментар')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='WAITING', verbose_name='Статус заявки')
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client_name

    def num(self):
        if not re.Match('/^[\+]?3?[\s]?8?[\s]?\(?0\d{2}?\)?[\s]?\d{3}[\s|-]?\d{2}[\s|-]?\d{2}$/', self.phone_number):
            raise ValidationError({'phone_number': 'Перевірте вірність номеру телефону'})

    class Meta:
        verbose_name = 'Заявки'
        verbose_name_plural = 'Заявка'
        ordering = ['data']


class Breed(models.Model):
    breed = models.CharField(max_length=255, db_index=True, verbose_name='Порода')

    def __str__(self):
        return self.breed

    class Meta:
        verbose_name = 'Породи'
        verbose_name_plural = 'Порода'


class Price(models.Model):
    service = models.CharField(max_length=255, verbose_name='Послуга')
    cost = models.IntegerField(verbose_name='Вартість')
    time = models.CharField(max_length=255, verbose_name='Час виконання')
    content = models.TextField(max_length=255, blank=True, null=True, verbose_name='Опис')

    def __str__(self):
        return self.service

    class Meta:
        verbose_name = 'Ціни'
        verbose_name_plural = 'Ціна'


class Portfolio(models.Model):
    photo = models.FileField(upload_to='static/portfolio')
    data = models.DateTimeField(auto_now_add=True)
    breed = models.ForeignKey('Breed', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Портфоліо'
        verbose_name_plural = 'Портфоліо'


class Expenses(models.Model):
    type = models.ForeignKey('Type', on_delete=models.PROTECT, verbose_name='Тип витрат')
    name = models.CharField(max_length=255, verbose_name='Назва придбаного товару')
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Вартість')
    data = models.DateTimeField(auto_now=True)
    comment = models.CharField(max_length=255, verbose_name='Коментар')

    class Meta:
        verbose_name = 'Витрати'
        verbose_name_plural = 'Витрати'

    def total_expenses(self):
        exp = Expenses.objects.all()
        total = 0
        for ex in exp:
            total += ex.cost
        return total








class Type(models.Model):
    type = models.CharField(max_length=255, verbose_name='Тип витрат')

    class Meta:
        verbose_name = 'Тип витрат'
        verbose_name_plural = 'Типи витрат'

    def __str__(self):
        return self.type




