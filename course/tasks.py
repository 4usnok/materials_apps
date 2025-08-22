from celery import shared_task
from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

@shared_task
def send_info_about_update_course(email):
    send_mail('Обновление курса', 'Курс обновился', EMAIL_HOST_USER, [email])
