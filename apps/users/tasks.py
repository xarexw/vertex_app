from celery import shared_task
from django.contrib.auth import get_user_model
from ..schedule.models import Record

User = get_user_model()

@shared_task
def recalculate_client_stats():
    # задача - перераховування статистики для всіх клієнтів
    # MVP - найважчий жим лежачи
    
    active_clients = User.objects.filter(is_staff=False)
    
    for client in active_clients:
        try:
            # знаходження рекордсменів по жиму (приклад складної логіки)
            best_bench_press = Record.objects.filter(
                client=client,
                exercise_name__icontains='жим'
            ).order_by('-result_value').first()
            
            if best_bench_press:
                # демонстрація, що задача виконується
                print(f"📊 {client.username} найкращий жим: {best_bench_press.result_value}")

        except Exception as e:
            print(f"Помилка перерахунку для {client.username}: {e}")
            continue
            
    return "Finished recalculating stats."