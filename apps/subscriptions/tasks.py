from celery import shared_task
from django.utils import timezone
from .models import UserSubscription

@shared_task
def check_expired_subs():
    #задача: раз на добу перевіряє та деактивує прострочені підписки.

    today = timezone.now().date()
    
    # всі активні підписки, термін дії яких минув
    expired_subs = UserSubscription.objects.filter(
        is_active=True,
        end_date__lt=today # дата закінчення менше сьогодні
    )
    
    count = expired_subs.update(is_active=False)
    
    print(f"✅ Celery: Деактивовано {count} прострочених підписок.")
    return f"Finished deactivating {count} subscriptions."