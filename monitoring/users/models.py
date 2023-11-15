from enum import IntEnum, Enum

from django.db import models
from django.db.models.query import QuerySet
from monitoring.common.models import BaseModel

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager as BUM
from django.contrib.auth.models import PermissionsMixin


class BaseUserManager(BUM):
    def create_user(self, email, is_active=True, is_admin=False, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email.lower()),
            is_active=is_active,
            is_admin=is_admin,
        )

        if password is not None:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.full_clean()
        user.save(using=self._db)

        return user

    def create_sys_user(self, email, password=None):
        return self.create_user(
            email=email,
            password=password,
        )

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email=email,
            is_active=True,
            is_admin=True,
            password=password,
        )

        user.is_superuser = True
        user.save(using=self._db)

        return user

    def is_system_user(self, user):
        return user.role == BaseUser.UserRoles.SYSADMIN

    def is_host_user(self, user):
        return user.role == BaseUser.UserRoles.HOSTADMIN


class BaseUser(BaseModel, AbstractBaseUser, PermissionsMixin):
    class UserRoles(models.TextChoices):
        SYSADMIN = "SYSADMIN"
        HOSTADMIN = "HOSTADMIN"
        OTHER = "OTHER"

    base_role = UserRoles.OTHER

    email = models.EmailField(
        verbose_name="email address",
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    role = models.CharField(
        max_length=10,
        choices=UserRoles.choices,
        default=base_role,
    )

    objects = BaseUserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email

    def is_staff(self):
        return self.is_admin

    def save(self, *args, **kwargs):
        if not self.id:
            self.role = self.base_role
        return super().save(*args, **kwargs)


class SYSAdminUserManager(BUM):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(role=BaseUser.UserRoles.SYSADMIN)

    def create_user(self, email, is_active=True, is_admin=False, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email.lower()),
            is_active=is_active,
            is_admin=is_admin,
        )

        if password is not None:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.full_clean()
        user.save(using=self._db)

        return user


class SYSAdminUser(BaseUser):
    base_role = BaseUser.UserRoles.SYSADMIN
    objects = SYSAdminUserManager()

    class Meta:
        proxy = True
        verbose_name = "System Admin User"
        verbose_name_plural = "System Admin User"


class HostAdminUserManager(BUM):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(role=BaseUser.UserRoles.HOSTADMIN)

    def create_user(self, email, is_active=True, is_admin=False, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email.lower()),
            is_active=is_active,
            is_admin=is_admin,
        )

        if password is not None:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.full_clean()
        user.save(using=self._db)

        return user


class HostAdminUser(BaseUser):
    base_role = BaseUser.UserRoles.HOSTADMIN
    objects = HostAdminUserManager()

    class Meta:
        proxy = True


class OtherUserManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(role=BaseUser.UserRoles.OTHER)


class OtherUser(BaseUser):
    base_role = BaseUser.UserRoles.OTHER
    objects = OtherUserManager()

    class Meta:
        proxy = True
