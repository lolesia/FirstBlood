from django.shortcuts import render

menu = [
    ()
]
def home(request):
    return render(request, 'groom/base.html')