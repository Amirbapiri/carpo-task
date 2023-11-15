from django.urls import path

from .apis import SensorAPI

urlpatterns = [
    path("<int:department_id>/list", SensorAPI.as_view(), name="list"),
]
