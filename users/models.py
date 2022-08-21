from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class ClubCard(models.Model):
    owner = models.OneToOneField(User, on_delete=models.PROTECT, verbose_name="Владелец")
    balance = models.PositiveIntegerField(default=0)
    discount_value = models.DecimalField(default=0, max_digits=3, decimal_places=0)

    def __str__(self):
        return self.owner
