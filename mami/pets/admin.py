from django.contrib import admin
from django.utils.html import format_html

from .models import Breed, Pet


class BreedAdmin(admin.ModelAdmin):
    list_display = ('breed', )
    list_display_links = ('breed',)


class PetAdmin(admin.ModelAdmin):
    list_display = ('pet_name', 'breed', 'weight', 'owner_name', 'image_preview', 'description')
    list_display_links = ('pet_name', 'breed')

    def image_preview(self, obj):
        return format_html('<img src="{}" width="324" height="432" />', obj.photo.url)

    def owner_name(self, obj):
        return f"{obj.owner.user.first_name} {obj.owner.user.last_name}"

    owner_name.short_description = 'Owner Name'


admin.site.register(Breed, BreedAdmin)
admin.site.register(Pet, PetAdmin)
