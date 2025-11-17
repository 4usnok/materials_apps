from django.db import models

from config import settings


class Course(models.Model):
    """Модель "Курс" """

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True
    )
    title = models.CharField(
        max_length=50,
        help_text="Напишите название курса",
        verbose_name="Название",
    )
    image = models.ImageField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Загрузите картинку курса",
        verbose_name="Картинка",
    )
    description = models.TextField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Заполните описание курса",
        verbose_name="Описание",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = [
            "title",
            "image",
            "description",
        ]


class Lesson(models.Model):
    """Модель "Урок" """

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=50,
        help_text="Напишите название урока",
        verbose_name="Название",
    )
    description = models.TextField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Заполните описание урока",
        verbose_name="Описание",
    )
    image = models.ImageField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Загрузите картинку урока",
        verbose_name="Картинка",
    )
    url_on_video = models.URLField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Загрузите ссылку на видео урока",
        verbose_name="Ссылка на видео",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = [
            "title",
            "description",
            "image",
            "url_on_video",
        ]


class Subscription(models.Model):
    """Модель 'Подписка'"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Подписчик",
        help_text="Выберите подписчика",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Курс",
        help_text="Выберите курс",
    )

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
        ordering = ["user", "course"]
