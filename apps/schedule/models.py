from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

class TrainingSession(models.Model):
    title = models.CharField(max_length=100, verbose_name="Назва тренування")
    trainer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, limit_choices_to={'is_manager': True})
    start_time = models.DateTimeField(verbose_name="Початок")
    end_time = models.DateTimeField(verbose_name="Кінець")
    capacity = models.PositiveIntegerField(default=20, verbose_name="Місць")

    def __str__(self):
        return f"{self.title} at {self.start_time}"

class Record(models.Model):
    session = models.ForeignKey(TrainingSession, on_delete=models.CASCADE, related_name='records')
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='training_records')
    exercise_name = models.CharField(max_length=100, verbose_name="Вправа")
    rpe = models.IntegerField(verbose_name="RPE(Оцінка складності)", default=7, validators=[MinValueValidator(1), MaxValueValidator(10)], blank=True, null=True)
    result_value = models.CharField(max_length=100, verbose_name="Результат (кг/рази)")
    note = models.TextField(blank=True, verbose_name="Примітка тренера")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client.username} - {self.exercise_name}: {self.result_value}"

class Exercise(models.Model):

    title = models.CharField(max_length=200, unique=True, verbose_name="Назва вправи")
    description = models.TextField(blank=True, verbose_name="Опис / Техніка")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Вправа"
        verbose_name_plural = "Довідник вправ"
