from django.urls import path, include

from .apis import OrganAPI

urlpatterns = [
    path(
        "",
        OrganAPI.as_view(),
        name="list",
    ),
]
