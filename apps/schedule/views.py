from django.shortcuts import render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import get_user_model
from .models import TrainingSession, Record

User = get_user_model()

def schedule_list(request):
    # всі тренування з бази
    sessions = TrainingSession.objects.all().order_by('start_time')
    return render(request, 'core/schedule.html', {'sessions': sessions})

@staff_member_required
def session_manage(request, session_id):
    session = get_object_or_404(TrainingSession, id=session_id)
    # список клієнтів (не персонал), щоб вибрати зі списку
    clients = User.objects.filter(is_staff=False)
    # історія записів цієї сесії
    records = session.records.all().order_by('-created_at')
    
    return render(request, 'core/manage.html', {
        'session': session,
        'clients': clients,
        'records': records
    })

# метод додавання (HTMX)
@staff_member_required
def add_record(request, session_id):
    if request.method == "POST":
        session = get_object_or_404(TrainingSession, id=session_id)
        
        # отримання даних з форми
        client_id = request.POST.get('client_id')
        exercise = request.POST.get('exercise')
        rpe = request.POST.get('rpe')
        result = request.POST.get('result')
        
        client = get_object_or_404(User, id=client_id)
        
        # збереження
        Record.objects.create(
            session=session,
            client=client,
            exercise_name=exercise,
            rpe=rpe if rpe else None,
            result_value=result
        )
        
        # повернення оновлеого шматочку таблиці
        records = session.records.all().order_by('-created_at')
        return render(request, 'core/partials/records_table.html', {'records': records})

@staff_member_required
def session_summary(request, session_id):
    session = get_object_or_404(TrainingSession, id=session_id)
    
    # отримання всі записи, згруповані по клієнтах
    records = session.records.all().select_related('client').order_by('client__username', 'created_at')
    
    return render(request, 'core/summary.html', {
        'session': session,
        'records': records
    })