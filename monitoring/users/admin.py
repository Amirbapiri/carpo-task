from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import BaseUser, SYSAdminUser, HostAdminUser, OtherUser


class BaseUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_active", "is_admin", "role")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_active",
                    "is_admin",
                    "role",
                ),
            },
        ),
    )
    list_display = ("email", "is_active", "is_admin", "role")
    list_filter = ("is_active", "is_admin", "role")
    search_fields = ("email",)
    ordering = ("email",)


class SYSAdminUserAdmin(UserAdmin):
    list_display = ("email", "is_active")
    list_filter = ("is_active",)
    search_fields = ("email",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_active", "role")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "is_active", "role"),
            },
        ),
    )
    ordering = ("email",)


class HostAdminUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_admin', 'role')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_admin', 'role'),
        }),
    )
    list_display = ('email', 'is_active', 'is_admin', 'role')
    list_filter = ('is_active', 'is_admin', 'role')
    search_fields = ('email',)
    ordering = ('email',)


class OtherUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_admin', 'role')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_admin', 'role'),
        }),
    )
    list_display = ('email', 'is_active', 'is_admin', 'role')
    list_filter = ('is_active', 'is_admin', 'role')
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(BaseUser, BaseUserAdmin)
admin.site.register(SYSAdminUser, SYSAdminUserAdmin)
admin.site.register(HostAdminUser, HostAdminUserAdmin)
admin.site.register(OtherUser, OtherUserAdmin)
