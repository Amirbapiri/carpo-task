from django.contrib import admin
from .models import Organ


@admin.register(Organ)
class OrganAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "sys_admin")
    search_fields = ("name", "sys_admin__email")
    list_filter = ("sys_admin",)
