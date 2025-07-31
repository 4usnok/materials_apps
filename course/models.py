from django.db import models

class Course(models.Model):
    """ Модель "Курс" """
    title = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text='Напишите название курса',
        verbose_name='Название',
    )
    image = models.ImageField(
        max_length=50,
        blank=True,
        null=True,
        help_text='Загрузите картинку курса',
        verbose_name='Картинка',
    )
    description = models.TextField(
        max_length=100,
        blank=True,
        null=True,
        help_text='Заполните описание курса',
        verbose_name='Описание',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = [
            'title',
            'image',
            'description',
        ]
