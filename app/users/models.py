from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    birth_date = models.DateField("Дата рождения", blank=True, null=True)

    REQUIRED_FIELDS = ["first_name", "last_name"]

    class Meta:
        ordering = ("-id",)
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
