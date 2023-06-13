from django.contrib import admin
from .models import Visits


class VisitsAdmin(admin.ModelAdmin):
    list_display = '__all__'
    list_display_links = ['user']


admin.site.register(Visits)

