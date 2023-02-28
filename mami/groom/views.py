from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import *
import telebot
from django.core.exceptions import ValidationError


menu = [
    {'title': 'Головна сторінка', 'url_name': 'home'},
    {'title': "Прайс", 'url_name': 'cost'},
    {'title': 'Про нас', 'url_name': 'about'}

]
def home(request):
    return render(request, 'groom/base.html')
def apply(request):
    if request.method == 'POST':
        form = Apply(request.POST)
        if form.is_valid():
            form.save()
            send_telegram(form.cleaned_data)
            return redirect(reverse('thanks'))
    else:
        form = Apply()
    return render(request, 'groom/apply.html', {'form': form})

def send_telegram(data):
    client_name = data['client_name']
    city = data['city']
    breed = data['breed']
    phone_number = data['phone_number']

    message = f"Новая заявка: {client_name}, {city}, {breed}, {phone_number}"

    bot_token = "6160007408:AAHRFJQaKNsxD5l7Mdv1aHfjNDxZvvB3CG8"
    chat_id = "-941286352"
    bot = telebot.TeleBot(token=bot_token)
    bot.send_message(chat_id=chat_id, text=message)

def thanks(request):
    return render(request, 'groom/Thanks.html')