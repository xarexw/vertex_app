from django.db import models
from django.conf import settings

class TrainingSession(models.Model):
    title = models.CharField(max_length=100, verbose_name="Назва тренування")
    trainer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, limit_choices_to={'is_manager': True})
    start_time = models.DateTimeField(verbose_name="Початок")
    end_time = models.DateTimeField(verbose_name="Кінець")
    capacity = models.PositiveIntegerField(default=20, verbose_name="Місць")

    def __str__(self):
        return f"{self.title} at {self.start_time}"
