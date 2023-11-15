from .models import SYSAdminUser


def register_sysadmin(email, password):
    return SYSAdminUser.objects.create_user(email=email, password=password)
