from django.db import models
from django.conf import settings
from subscriptions.models import SubscriptionType

class Order(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новий'),
        ('paid', 'Оплачено'),
        ('failed', 'Помилка'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    subscription_type = models.ForeignKey(SubscriptionType, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.status}"

class Transaction(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Очікує'),
        ('success', 'Успіх'),
        ('failed', 'Відхилено'),
    ]

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='transactions')
    transaction_id = models.CharField(max_length=100, unique=True, verbose_name="ID транзакції банку")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Trx {self.transaction_id} ({self.status})"
