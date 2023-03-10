FROM python:3.11-alpine

WORKDIR /app

RUN apk update && \
    apk add build-base python3-dev libpq postgresql-dev

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

CMD ["gunicorn", "--reload", "--workers=2", "--worker-tmp-dir", "/dev/shm", "--bind=0.0.0.0:80", "--chdir", "/app/treasury", "tresury.wsgi"]
