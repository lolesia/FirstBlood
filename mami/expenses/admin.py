from django.contrib import admin
from .models import *


class ExpensesAdmin(admin.ModelAdmin):
    list_display = '__all__'
    list_display_links = ['name']


class TypeAdmin(admin.ModelAdmin):
    list_display = '__all__'
    list_display_links = '__all__'


admin.site.register(Expenses)
admin.site.register(Type)
