from django.contrib import admin
from .models import Portfolio


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['image', 'breed']
    list_display_links = ['image']


admin.site.register(Portfolio)


