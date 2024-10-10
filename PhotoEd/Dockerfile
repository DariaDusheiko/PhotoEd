# Используем Python 3 на базе Alpine
FROM python:3-alpine

# Устанавливаем рабочую директорию в /app/
WORKDIR /app/

# Копируем все файлы в рабочую директорию контейнера
COPY . /app

# Устанавливаем зависимости из requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт 8000
EXPOSE 8000

# Запуск приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
