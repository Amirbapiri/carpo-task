from django.db import models

from monitoring.departments.models import Department


# Create your models here.
class Sensor(models.Model):
    name = models.CharField(max_length=255)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    oxygen_level = models.DecimalField(max_digits=5, decimal_places=2)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="sensors",
    )

    def __str__(self):
        return f"{self.name} ({self.department.name})"
