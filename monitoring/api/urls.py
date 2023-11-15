from django.urls import path, include

urlpatterns = [
    path("auth/", include(("monitoring.authentication.urls", "authentication"))),
    path("users/", include(("monitoring.users.urls", "users"))),
    path("organs/", include(("monitoring.organs.urls", "organs"))),
    path("hosts/", include(("monitoring.hosts.urls", "hosts"))),
]
