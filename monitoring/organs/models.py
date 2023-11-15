from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# User with role of SYSADMIN can create instance of the following model


class Organ(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    sys_admin = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="organs",
    )

    def __str__(self):
        return self.name
