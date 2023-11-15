from rest_framework.permissions import BasePermission

from monitoring.users.models import BaseUser


class IsSysAdmin(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.role == BaseUser.UserRoles.SYSADMIN


class IsHostAdmin(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.role == BaseUser.UserRoles.HOSTADMIN
