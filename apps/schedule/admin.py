from django.contrib import admin
from .models import TrainingSession, Record

@admin.register(TrainingSession)
class TrainingSessionAdmin(admin.ModelAdmin):
    list_display = ['title', 'trainer', 'start_time', 'end_time', 'capacity']
    list_filter = ['start_time', 'trainer']
    
@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ['client', 'exercise_name', 'result_value', 'session', 'created_at']
    list_filter = ['client', 'session']
