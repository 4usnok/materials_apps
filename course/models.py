from django.db import models

class Course(models.Model):
    """ Модель "Курс" """
    title = models.CharField(max_length=50, blank=True, null=True, help_text='Напишите название курса')
    image = models.ImageField(max_length=50, blank=True, null=True, help_text='Загрузите картинку курса')
    description = models.TextField(max_length=100, blank=True, null=True, help_text='Заполните описание курса')

    class Meta:
        fields = '__all__'
        ordering = [
            'title',
            'image',
            'description',
        ]

        def __str__(self):
            return self.title
