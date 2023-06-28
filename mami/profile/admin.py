from django.contrib import admin
from django.utils.html import format_html

from .models import Breed, Pet


class BreedAdmin(admin.ModelAdmin):
    list_display = ('breed', )
    list_display_links = ('breed',)


class PetAdmin(admin.ModelAdmin):
    list_display = ('user', 'pet_name', 'breed', 'weight', 'image_preview', 'description')
    list_display_links = ('user', 'pet_name', 'breed')

    def image_preview(self, obj):
        return format_html('<img src="{}" width="324" height="432" />', obj.photo.url)


admin.site.register(Breed, BreedAdmin)
admin.site.register(Pet, PetAdmin)
