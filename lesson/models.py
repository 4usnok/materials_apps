from django.db import models

from course.models import Course


class Lesson(models.Model):
    """ Модель "Урок" """
    title = models.ForeignKey(Course, on_delete=models.CASCADE, help_text='Напишите название урока')
    description = models.TextField(max_length=100, blank=True, null=True, help_text='Заполните описание урока')
    image = models.ImageField(max_length=50, blank=True, null=True, help_text='Загрузите картинку урока')
    url_on_video = models.URLField(max_length=50, blank=True, null=True, help_text='Загрузите ссылку на видео урока')

    class Meta:
        ordering = [
            'title',
            'description',
            'image',
            'url_on_video',
        ]

        def __str__(self):
            return self.title
