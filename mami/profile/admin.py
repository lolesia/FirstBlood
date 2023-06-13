from django.contrib import admin
from .models import Breed, Pet


class BreedAdmin(admin.ModelAdmin):
    list_display = ['breed']
    list_display_links = ['breed']


class PetAdmin(admin.ModelAdmin):
    list_display = '__all__'
    list_display_links = ['user', 'pet_name', 'breed']


admin.site.register(Breed)
admin.site.register(Pet)
