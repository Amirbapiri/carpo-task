from .models import SYSAdminUser, HostAdminUser


def register_sysadmin(email, password):
    return SYSAdminUser.objects.create_user(email=email, password=password)


def register_hostadmin(email, password):
    return HostAdminUser.objects.create_user(email=email, password=password)
