from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = '__all__'
    list_display_links = ['email', 'first_name']


admin.site.register(User)
