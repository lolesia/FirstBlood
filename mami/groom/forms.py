from django import forms
from .models import *


class Apply(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['client_name', 'city', 'pet_name', 'breed', 'phone_number', 'comments']

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        pattern = r'^[\+]?3?[\s]?8?[\s]?\(?0\d{2}?\)?[\s]?\d{3}[\s|-]?\d{2}[\s|-]?\d{2}$'
        if not re.match(pattern, phone_number):
            raise ValidationError('Перевірте вірність номеру телефону')

        return phone_number




