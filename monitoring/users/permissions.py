from rest_framework import permissions

from .models import BaseUser


class IsSYSAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == BaseUser.UserRoles.SYSADMIN
