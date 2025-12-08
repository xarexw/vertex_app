from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # додаткові поля юзера
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="Телефон")
    is_manager = models.BooleanField(default=False, verbose_name="Це менеджер/тренер")

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

class ClientStat(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='stats')
    weight = models.FloatField(verbose_name="Вага (кг)", default=0.0)
    height = models.FloatField(verbose_name="Зріст (см)", default=0.0)
    # можна додати об'єми, жир, тд
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Stat for {self.user.username}"