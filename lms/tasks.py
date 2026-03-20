from celery import shared_task
from django.core.mail import send_mail

from .models import Subscription


@shared_task
def send_course_update_email(course_id):
    subscriptions = Subscription.objects.filter(course_id=course_id)

    emails = [sub.user.email for sub in subscriptions]

    if emails:
        send_mail(
            subject="Обновление курса",
            message="Курс был обновлен!",
            from_email="admin@test.com",
            recipient_list=emails,
        )
