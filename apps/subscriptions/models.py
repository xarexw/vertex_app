from django.db import models
from django.conf import settings # посилання CustomUser

class SubscriptionType(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва (напр. Місячний)")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    duration_days = models.PositiveIntegerField(verbose_name="Тривалість (днів)")
    description = models.TextField(blank=True, verbose_name="Опис")

    def __str__(self):
        return f"{self.name} - {self.price} грн"

class UserSubscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='subscriptions')
    subscription_type = models.ForeignKey(SubscriptionType, on_delete=models.PROTECT)
    start_date = models.DateField(auto_now_add=True, verbose_name="Дата початку")
    end_date = models.DateField(verbose_name="Дата закінчення")
    is_active = models.BooleanField(default=True, verbose_name="Активна")

    def __str__(self):
        return f"{self.user.username} - {self.subscription_type.name}"