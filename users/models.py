from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    Group,
    Permission,
    PermissionsMixin,
)
from django.db import models
from django.utils import timezone

# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, ID, password=None, **extra_fields):
        if not ID:
            raise ValueError("The ID must be set")
        user = self.model(ID=ID, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, ID, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(ID, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    ID = models.CharField(unique=True, max_length=150)
    nickname = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    rank = models.CharField(max_length=50, null=True, blank=True)
    rating = models.FloatField(default=0)

    objects = CustomUserManager()

    USERNAME_FIELD = "ID"
    REQUIRED_FIELDS = ["nickname"]

    groups = models.ManyToManyField(Group, related_name="custom_users")
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_users",
        blank=True,
    )

    def __str__(self):
        return self.ID
