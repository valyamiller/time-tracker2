# Базовая инструкция
FROM python:3.12-slim

# Рабочая директория внутри контейнера
WORKDIR /app

# Копируем файл с зависимостями и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь остальной код
COPY . .

# Указываем порт
EXPOSE 5001

# КОМАНДА ЗАПУСКА (именно она нам и нужна)
CMD ["python", "app.py"]