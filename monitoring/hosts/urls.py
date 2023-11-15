from django.urls import path

from .apis import HostAPI

urlpatterns = [
    path("", HostAPI.as_view(), name="create"),
]
