from django.urls import path

from .apis import DepartmentAPI

urlpatterns = [
    path("", DepartmentAPI.as_view(), name="create"),
]
