from django.contrib import admin
from .models import Services


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('service', 'breed', 'cost_kiev', 'cost_murgorod', 'service_time', 'content')
    list_display_links = ('service',)


admin.site.register(Services, ServicesAdmin)