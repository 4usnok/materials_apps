from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """ Модель "Пользователь" """
    email = models.EmailField(
        unique=True,
        verbose_name='email почта'
    )
    phone = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        help_text='Напишите номер телефона',
        verbose_name='Номер телефона',
    )
    city = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text='Напишите название города',
        verbose_name='Город'
    )
    avatar = models.ImageField(
        max_length=50,
        blank=True,
        null=True,
        help_text='Загрузите аватарку пользователя',
        verbose_name='Аватарка',
    )

    USERNAME_FIELD = 'email'  # email поле для логина - проверка при входе будет по этому полю
    REQUIRED_FIELDS = ['username', ]  # дополнительное поле при создании суперпользователя

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = [
            'phone',
            'city',
            'avatar',
        ]

