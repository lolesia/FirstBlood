from django.contrib import admin
from .models import Reviews


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'score', 'date')
    list_display_links = ('user', 'text')


admin.site.register(Reviews, ReviewsAdmin)
