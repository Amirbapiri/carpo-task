from django.db import models

from monitoring.organs.models import Organ


# Create your models here.
class Host(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    organ = models.ForeignKey(
        Organ,
        on_delete=models.CASCADE,
        related_name="hosts",
    )

    def __str__(self):
        return f"{self.name} -> {self.organ}"
