from django.contrib import admin

from .models import Host


@admin.register(Host)
class HostAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "organ")
    search_fields = ("name", "organ__name")
    list_filter = ("organ",)
