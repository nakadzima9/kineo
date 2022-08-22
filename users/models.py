from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class ClubCard(models.Model):
    owner = models.OneToOneField(User, on_delete=models.PROTECT, verbose_name="Владелец")
    balance = models.PositiveIntegerField(default=0, verbose_name="Баланс")
    discount_value = models.DecimalField(default=0, max_digits=3, decimal_places=0, verbose_name="Скидка")

    def __str__(self):
        return self.owner

    class Meta:
        verbose_name = "Клубная карта"
        verbose_name_plural = "Клубные карты"


class Feedback(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name="Пользователь")
    description = models.TextField(max_length=1000, verbose_name="Описание")

    def __str__(self):
        return self.user

    class Meta:
        verbose_name_plural = "Обратная связь"
