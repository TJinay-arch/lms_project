from datetime import timedelta

from celery import shared_task
from django.contrib.auth import get_user_model
from django.utils.timezone import now

User = get_user_model()


@shared_task
def deactivate_inactive_users():
    month_ago = now() - timedelta(days=30)

    users = User.objects.filter(last_login__lt=month_ago, is_active=True)

    users.update(is_active=False)
