from django.db import models

class User(models.Model):
    """ Модель "Пользователь" """
    phone = models.CharField(max_length=10, blank=True, null=True, help_text='Напишите номер телефона')
    city = models.CharField(max_length=50, blank=True, null=True, help_text='Напишите название города')
    avatar = models.ImageField(max_length=50, blank=True, null=True, help_text='Загрузите аватарку пользователя')

    class Meta:
        fields = '__all__'
        ordering = [
            'phone',
            'city',
            'avatar',
        ]

        def __str__(self):
            return self.phone
