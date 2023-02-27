from django.shortcuts import render
from .forms import *

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
    else:
        form = Apply()
    return render(request, 'groom/apply.html', {'form' : form})

def thanks(request):
    return render(request, 'groom/Thanks.html')