from django.contrib import admin

from .models import Sensor


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ("name", "temperature", "oxygen_level", "department")
    search_fields = ("name", "department__name")
    list_filter = ("department",)
