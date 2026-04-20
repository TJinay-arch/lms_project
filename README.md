# 🚀 LMS Project (Django + Docker + Celery)

## 📦 Описание проекта

Проект представляет собой LMS-систему с поддержкой:

* Django + DRF
* PostgreSQL
* Redis
* Celery (асинхронные задачи)
* Celery Beat (периодические задачи)

---

## ⚙️ Требования

Перед запуском убедитесь, что установлен:

* Docker Desktop

---

## 📁 Настройка окружения

### 1. Клонировать репозиторий

```bash
git clone <repo_url>
cd lms_project
```

---

### 2. Создать файл `.env`

Создайте файл `.env` в корне проекта:

```env
DEBUG=True
SECRET_KEY=your_secret_key

DATABASE_NAME=lms_db
DATABASE_USER=postgres
DATABASE_PASSWORD=postgres
DATABASE_HOST=db
DATABASE_PORT=5432

REDIS_HOST=redis
REDIS_PORT=6379

STRIPE_SECRET_KEY=sk_test_...
STRIPE_PUBLIC_KEY=pk_test_...
```

---

## 🚀 Запуск проекта

```bash
docker compose up --build
```

После запуска будут подняты сервисы:

* backend (Django)
* PostgreSQL
* Redis
* Celery worker
* Celery Beat

---

## ✅ Проверка работоспособности

---

### 🔹 1. Django (backend)

Открыть в браузере:

```
http://localhost:8000
```

✔ Ожидаемый результат:

* API доступен
* или стандартная страница Django (404 / DRF)

---

### 🔹 2. PostgreSQL

Подключение к базе:

```bash
docker exec -it lms_db psql -U postgres
```

Проверка:

```sql
\l
```

✔ Ожидаемый результат:

* отображается список баз данных

---

### 🔹 3. Redis

Подключение:

```bash
docker exec -it lms_redis redis-cli
```

Проверка:

```bash
ping
```

✔ Ответ:

```
PONG
```

---

### 🔹 4. Celery Worker

Просмотр логов:

```bash
docker logs lms_celery
```

✔ Ожидаемый результат:

```
ready
```

---

### 🔹 5. Celery Beat

Просмотр логов:

```bash
docker logs lms_celery_beat
```

✔ Ожидаемый результат:

```
Scheduler: Sending due task
```

---

### 🔹 6. Проверка асинхронных задач

1. Выполните действие в API (например, обновление курса)
2. Проверьте логи Celery:

```bash
docker logs lms_celery
```

✔ Ожидаемый результат:

```
Task send_course_update_email received
```

---

## 🛠️ Полезные команды

Остановить контейнеры:

```bash
docker compose down
```

Пересобрать проект:

```bash
docker compose up --build
```

Посмотреть контейнеры:

```bash
docker ps
```

---

## ❗ Важно

* Не используйте `localhost` для подключения к БД и Redis внутри Docker
* Используйте:

  * `DATABASE_HOST=db`
  * `REDIS_HOST=redis`

---

## 📌 Примечание

Проект работает в тестовом режиме, включая интеграцию с Stripe (используются тестовые ключи).

## 🌐 Настройка сервера

1. Установлен Python, PostgreSQL, Redis
2. Настроен Gunicorn
3. Настроен Nginx
4. Настроен systemd для автозапуска
5. Открыты только порты 22, 80 и 443

- Используются SSH-ключи
- Парольный вход отключен
- Настроен UFW (firewall)

## CI/CD

- При push запускаются тесты
- При успешных тестах выполняется деплой
- Деплой происходит через Docker Compose

## Deploy

docker compose up -d --build
