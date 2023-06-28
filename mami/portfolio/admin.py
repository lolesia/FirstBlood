from django.contrib import admin
from .models import Portfolio
from django.utils.html import format_html


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('breed', 'image_preview', 'date')
    list_display_links = ('image_preview',)

    def image_preview(self, obj):
        return format_html('<img src="{}" width="324" height="432" />', obj.image.url)


admin.site.register(Portfolio, PortfolioAdmin)


