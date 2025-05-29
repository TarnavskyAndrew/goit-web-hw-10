FROM python:3.13.2

# Робоча директорія
WORKDIR /app

# Копіюємо pyproject.toml і poetry.lock у контейнер
COPY pyproject.toml poetry.lock ./

# Встановлюємо залежності через poetry
RUN pip install --upgrade pip && pip install poetry && poetry config virtualenvs.create false && poetry install --no-root

#Копіюємо вихідний код у контейнер
COPY src/ ./src
ENV PYTHONPATH=/app/src

# Позначимо порт, де працює застосунок всередині контейнера
EXPOSE 5000

# Робоча директорія у коді
WORKDIR /app/src

# Запуск CLI помічника
ENTRYPOINT ["python", "bot_assistant/main.py"]

LABEL maintainer="Tarnavsky Andrew"
LABEL description="Docker image for CLI assistant bot"
LABEL version="1.0"