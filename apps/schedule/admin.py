from django.contrib import admin
from .models import TrainingSession

@admin.register(TrainingSession)
class TrainingSessionAdmin(admin.ModelAdmin):
    list_display = ['title', 'trainer', 'start_time', 'end_time', 'capacity']
    list_filter = ['start_time', 'trainer']
