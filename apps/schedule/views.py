from django.shortcuts import render
from .models import TrainingSession

def schedule_list(request):
    # Беремо всі тренування з бази
    sessions = TrainingSession.objects.all().order_by('start_time')
    return render(request, 'core/schedule.html', {'sessions': sessions})
