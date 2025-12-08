from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from subscriptions.models import UserSubscription

@login_required
def dashboard(request):
    user = request.user
    context = {
        'user': user,
        'has_active_sub': False,
        'days_left': 0,
        'sub_end_date': None,
        'notifications': user.notifications.filter(is_read=False)[:3] # Останні 3 непрочитані
    }

    # Шукаємо активну підписку
    active_sub = UserSubscription.objects.filter(
        user=user, 
        is_active=True, 
        end_date__gte=timezone.now().date()
    ).first()

    if active_sub:
        context['has_active_sub'] = True
        context['sub_end_date'] = active_sub.end_date
        # Рахуємо дні до кінця
        delta = active_sub.end_date - timezone.now().date()
        context['days_left'] = max(0, delta.days)

    return render(request, 'core/dashboard.html', context)
