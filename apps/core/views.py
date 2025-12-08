from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from subscriptions.models import UserSubscription
from schedule.models import TrainingSession

@login_required
def dashboard(request):
    user = request.user
    today = timezone.now().date()
    
    context = {
        'user': user,
        # дефолт пусті значення
        'has_active_sub': False,
        'days_left': 0,
        'sub_end_date': None,
        'notifications': [],
        'trainer_sessions': [] # змінна для тренера
    }

    # ЛОГІКА ДЛЯ ТРЕНЕРА
    if user.is_staff:
        # тренування де є тренером
        upcoming_sessions = TrainingSession.objects.filter(
            trainer=user,
            start_time__date__gte=today
        ).order_by('start_time')[:5] # 5 найближчих
        
        context['trainer_sessions'] = upcoming_sessions

    # ЛОГІКА ДЛЯ КЛІЄНТА
    else:

        context['notifications'] = user.notifications.filter(is_read=False)[:3]
        active_sub = UserSubscription.objects.filter(
            user=user, 
            is_active=True, 
            end_date__gte=today
        ).first()

        if active_sub:
            context['has_active_sub'] = True
            context['sub_end_date'] = active_sub.end_date
            delta = active_sub.end_date - today
            context['days_left'] = max(0, delta.days)

    return render(request, 'core/dashboard.html', context)
