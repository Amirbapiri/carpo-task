from django.db import models

from monitoring.hosts.models import Host


class Department(models.Model):
    name = models.CharField(max_length=120)
    host = models.ForeignKey(
        Host,
        on_delete=models.CASCADE,
        related_name="departments",
    )

    def __str__(self):
        return self.name
