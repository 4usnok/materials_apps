from django.utils import timezone

from celery import shared_task

from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

from users.models import User


@shared_task
def send_info_about_update_course(email):
    send_mail("Обновление курса", "Курс обновился", EMAIL_HOST_USER, [email])


@shared_task
def check_login_user():
    one_month_ago = timezone.now() - timezone.timedelta(
        days=30
    )  # отматываем на 30 дней назад

    # забираем необходимые объекты из модели
    user_get = User.objects.filter(last_login__lt=one_month_ago, is_active=True)

    for user in user_get:
        user.is_active = False  # меняем статус на неактивный
        user.save()  # сохраняем изменение в базу
