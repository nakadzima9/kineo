from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError("The username must be set!")
        if not email:
            raise ValueError("The email must be set!")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        if not password:
            raise ValueError("Password must be set!")
        user.save()
        return user

    def create_superuser(self, username, email, password, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")
        return self.create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class ClubCard(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, verbose_name="Владелец")
    balance = models.PositiveIntegerField(default=0, verbose_name="Баланс")
    discount_value = models.DecimalField(
        default=0, max_digits=3, decimal_places=0, verbose_name="Скидка"
    )

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = "Клубная карта"
        verbose_name_plural = "Клубные карты"


class Feedback(models.Model):
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    description = models.TextField(max_length=1000, verbose_name="Описание")

    def __str__(self):
        return self.user

    class Meta:
        verbose_name_plural = "Обратная связь"
