from django.contrib import admin
from .models import Services


class ServicesAdmin(admin.ModelAdmin):
    list_display = '__all__'
    list_display_links = ['service']


admin.site.register(Services)