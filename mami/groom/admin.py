from django.contrib import admin
from django.utils.html import format_html

from .models import *


class ClientAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'pet_name', 'breed', 'phone_number', 'photo', 'comments', 'status', 'data']
    list_display_links = ['client_name', 'phone_number']
    search_fields = ['data']
    list_filter = ['client_name', 'data', 'phone_number']


class BreedAdmin(admin.ModelAdmin):
    list_display = ['breed']
    list_display_links = ['breed']


class PriceAdmin(admin.ModelAdmin):
    list_display = ['breed', 'cost_kiev', 'cost_murgorod', 'time', 'content']
    list_display_links = ['breed']
    list_filter = ['cost_kiev', 'cost_murgorod']


class PortfolioAdmin(admin   .ModelAdmin):
    list_display = ['image_tag', 'breed']
    list_display_links = ['image_tag']

    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width: 100px; max-height: 100px;" />'.format(obj.image.url))


class ExpensesAdmin(admin.ModelAdmin):
    list_display = ['type', 'name', 'cost', 'data', 'comment', 'total_expenses']
    list_display_links = ['name', 'cost']
    list_filter = ['data']

    def total_expenses(self, obj):
        exp = Expenses.objects.all()
        total = 0
        for ex in exp:
            total += ex.cost
        return total



class TypeAdmin(admin.ModelAdmin):
    list_display = ['type']
    list_display_links = ['type']


admin.site.register(Client, ClientAdmin)
admin.site.register(Breed, BreedAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Expenses, ExpensesAdmin)
admin.site.register(Type, TypeAdmin)