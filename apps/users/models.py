from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # додаткові поля юзера
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="Телефон")
    is_manager = models.BooleanField(default=False, verbose_name="Це менеджер/тренер")

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"