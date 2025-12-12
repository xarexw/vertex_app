# 1. Беремо легкий офіційний образ Python
FROM python:3.12-slim

# 2. Вимикаємо кешування байт-коду (щоб не смітити .pyc файлами)
# і буферизацію виводу (щоб логи з'являлися миттєво)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Встановлюємо робочу папку всередині контейнера
WORKDIR /app

# 4. Спочатку копіюємо тільки файл вимог (для кешування Docker шарів)
COPY requirements.txt .

# 5. Встановлюємо залежності системи (для Postgres) і Python
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir -r requirements.txt

# 6. Копіюємо весь інший код проєкту
COPY . .

# 7. Відкриваємо порт
EXPOSE 8000

# 8. Команда запуску (для MVP запускаємо так, для Прода це міняють на Gunicorn)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]