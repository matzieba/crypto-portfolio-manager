from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


STATUS_CHOICES = [("active", "active"), ("disabled", "disabled")]


class User(AbstractUser):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["email"]
    objects = UserManager()

    first_name = models.CharField(max_length=1024)
    last_name = models.CharField(max_length=1024)
    phone = models.CharField(max_length=1024, null=True, blank=True)
    email = models.EmailField(max_length=1024)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="active")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    groups = models.ManyToManyField("auth.Group", blank=True, related_name="crypto_api_user_groups")
    user_permissions = models.ManyToManyField("auth.Permission", blank=True, related_name="crypto_api_user_permissions")

    def __str__(self):
        return f"{self.first_name} {self.last_name or ''} - {self.id}"
