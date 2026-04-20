# LMS Project (Django + Docker + Celery + CI/CD)

---

## 🌐 Демо (развёрнутый сервер)

- http://81.26.179.6/
- http://81.26.179.6/api/
- http://81.26.179.6/admin/
- http://81.26.179.6/swagger/

---

## 📦 Описание проекта

LMS‑система, реализованная с использованием:

- Django + Django REST Framework;
- PostgreSQL;
- Redis;
- Celery (асинхронные задачи);
- Celery Beat (периодические задачи);
- Nginx (reverse proxy);
- Docker / Docker Compose;
- GitHub Actions (CI/CD).

---

## ⚙️ Требования

- Docker Desktop;
- Git;
- Python 3.13 (для локальной разработки).

---

## 🧪 Локальный запуск

### 1. Клонирование репозитория

```bash
git clone <repo_url>
cd lms_project

 Создание .env
Создать файл .env в корне проекта:

env
DEBUG=True
SECRET_KEY=your_secret_key

DATABASE_NAME=lms_db
DATABASE_USER=postgres
DATABASE_PASSWORD=postgres
DATABASE_HOST=db
DATABASE_PORT=5432

REDIS_HOST=redis
REDIS_PORT=6379
3. Запуск проекта
bash
docker compose up --build
4. Проверка локально
Django: ;

Admin: ;

Swagger: .

🐳 Архитектура Docker
Сервисы проекта:

web → Django + Gunicorn;

db → PostgreSQL;

redis → брокер сообщений;

celery → worker задач;

celery_beat → планировщик задач;

nginx → reverse proxy.

🌍 Продакшн (сервер)
📌 Адрес сервера

📌 Структура деплоя
При push в ветку feature/ci_cd:

Запуск CI (GitHub Actions).

Прогон тестов (pytest).

Проверка линтера (flake8).

Проверка Docker build.

Деплой на сервер через SSH.

Перезапуск контейнеров через Docker Compose.

⚙️ CI/CD (GitHub Actions)
Файл: .github/workflows/ci_cd.yml

Этапы pipeline:

Test stage:

PostgreSQL (service);

Redis (service);

migrations;

pytest.

Lint stage:

flake8 — проверка стиля кода.

Build stage:

сборка Docker‑образов.

Deploy stage:

SSH‑подключение к серверу;

git pull;

docker compose down;

docker compose up -d --build.

🔐 GitHub Secrets
Настроены в репозитории:

SERVER_HOST;

SERVER_USER;

SSH_KEY.

🖥 Настройка сервера
1. Установка Docker
bash
apt update
apt install docker.io docker-compose -y
2. Клонирование проекта
bash
git clone <repo_url>
cd lms_project
3. Запуск на сервере
bash
docker compose up -d --build
4. Открытые порты
22 (SSH);

80 (HTTP);

443 (HTTPS).

🚀 Ручной деплой
bash
docker compose down
docker compose up -d --build