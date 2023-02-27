from django import forms
from .models import *


class Apply(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['client_name', 'city', 'pet_name', 'breed', 'phone_number', 'comments']



