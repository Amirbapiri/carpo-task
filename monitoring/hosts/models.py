from django.db import models
from django.contrib.auth import get_user_model

from monitoring.organs.models import Organ


User = get_user_model()

class Host(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    organ = models.ForeignKey(
        Organ,
        on_delete=models.CASCADE,
        related_name="hosts",
    )
    host_admin = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="hosts",
    )

    def __str__(self):
        return f"{self.name} -> {self.organ}"
