from django.urls import path, include

urlpatterns = [
    path("auth/", include(("monitoring.authentication.urls", "authentication"))),
    path("users/", include(("monitoring.users.urls", "users"))),
    path("organs/", include(("monitoring.organs.urls", "organs"))),
    path("hosts/", include(("monitoring.hosts.urls", "hosts"))),
    path("departments/", include(("monitoring.departments.urls", "departments"))),
    path("sensors/", include(("monitoring.sensors.urls", "sensors"))),
]
