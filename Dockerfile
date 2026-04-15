FROM python:3.12-slim

WORKDIR /app

# Создаем виртуальное окружение
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Обновляем pip и устанавливаем зависимости
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Копируем весь код
COPY . .

# Открываем порт
EXPOSE 8080

# Запускаем приложение
CMD ["python", "app.py"]