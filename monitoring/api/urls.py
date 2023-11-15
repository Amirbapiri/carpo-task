from django.urls import path, include

urlpatterns = [
    path("users/", include(("monitoring.users.urls", "users"))),
]
