from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Notification

@login_required
def notification_list(request):
    # всі повідомлення поточного юзера, спочатку нові
    notifications = Notification.objects.filter(recipient=request.user).order_by('-created_at')
    
    # gозначаємо як прочитані (проста логіка для MVP)
    # notifications.update(is_read=True)
    
    return render(request, 'notifications/list.html', {'notifications': notifications})
