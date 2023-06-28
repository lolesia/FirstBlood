from django.contrib import admin
from .models import *


class ExpensesAdmin(admin.ModelAdmin):
    list_display = ('type', 'name', 'cost', 'date', 'comment')
    list_display_links = ('name',)


class TypeAdmin(admin.ModelAdmin):
    list_display = ('type',)
    list_display_links = ('type',)


admin.site.register(Expenses, ExpensesAdmin)
admin.site.register(Type, TypeAdmin)
