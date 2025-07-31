from django.db import models

class User(models.Model):
    """ Модель "Пользователь" """
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

