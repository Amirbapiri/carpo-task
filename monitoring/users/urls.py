from django.urls import path

from .apis import SysAdminRegistrationAPI, HostAdminRegistrationAPI


urlpatterns = [
    path(
        "sysadmin/register/",
        SysAdminRegistrationAPI.as_view(),
        name="sysadmin_register",
    ),
    path(
        "hostadmin/register/",
        HostAdminRegistrationAPI.as_view(),
        name="hostadmin_register",
    ),
]
