from django.urls import path

from .apis import SysAdminRegistrationAPI


urlpatterns = [
    path(
        "sysadmin/register/",
        SysAdminRegistrationAPI.as_view(),
        name="sysadmin_register",
    ),
]
