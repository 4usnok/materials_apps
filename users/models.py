from django.contrib.auth.models import AbstractUser
from django.db import models

from config import settings
from course.models import Course, Lesson


class User(AbstractUser):
    """Модель "Пользователь" """

    email = models.EmailField(unique=True, verbose_name="email-почта")
    phone = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        help_text="Напишите номер телефона",
        verbose_name="Номер телефона",
    )
    city = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Напишите название города",
        verbose_name="Город",
    )
    avatar = models.ImageField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Загрузите аватарку пользователя",
        verbose_name="Аватарка",
    )

    USERNAME_FIELD = (
        "email"  # email поле для логина - проверка при входе будет по полю email
    )
    REQUIRED_FIELDS = [
        "username",
    ]  # дополнительное поле при создании суперпользователя

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = [
            "city",
            "phone",
            "avatar",
        ]


class Payments(models.Model):
    """Модель 'Платежи'"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        help_text="Выберите пользователя",
        verbose_name="Пользователь",
    )
    date_of_payment = models.DateField(
        help_text="Введите дату платежа",
        verbose_name="Дата оплаты",
    )
    paid_course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Выберите название курса",
        verbose_name="Оплаченный курс",
    )
    paid_lesson = models.ForeignKey(
        Lesson,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Выберите название урока",
        verbose_name="Оплаченный урок",
    )
    payment_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Укажите сумму в формате 100.00",
        verbose_name="Сумма оплаты",
    )

    class PaymentMethod(models.TextChoices):
        CASH = (
            "cash",
            "Наличные",
        )
        TRANSFER = "transfer", "Перевод на счет"

    payment_method = models.CharField(
        max_length=20,
        choices=PaymentMethod.choices,  # Подключаем варианты
        verbose_name="Способ оплаты",
        help_text="Выберите способ оплаты",
    )

    def __str__(self):
        return self.payment_method

    class Meta:
        verbose_name = "Платёж"
        verbose_name_plural = "Платежи"
        ordering = [
            "-date_of_payment",
            "user",
        ]  # Сортировка по убыванию сначала по дате, потом по пользователю

class Product(models.Model):
    """Модель `Продукт`"""

    name = models.CharField(
        max_length=20,
        verbose_name="Название продукта",
        help_text="Напишите название продукта"
    )
    description = models.TextField(
        max_length=400,
        blank=True,
        null=True,
        verbose_name="Описание",
        help_text="Заполните описание продукта"
    )
    link = models.URLField(
        max_length=400,
        blank=True,
        null=True,
        verbose_name="Ссылка на оплату",
        help_text="Укажите ссылку на оплату"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = [
            "name",
            "description",
            "link",
        ]

class Price(models.Model):
    """Модель `Цена`"""

    product = models.ForeignKey(
        Product,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="Продукт",
        help_text="Выберите продукт"
    )
    currency = models.CharField(
        max_length=3,
        blank=True,
        null=True,
        verbose_name="Валюта",
        help_text="Напишите валюту"
    )
    unit_amount = models.DecimalField(
        max_digits=19,
        decimal_places=4,
        verbose_name ="Цена продукта",
        help_text="Укажите цену продукта",
    )

    def __str__(self):
        return self.product

    class Meta:
        verbose_name = "Цена"
        verbose_name_plural = "Цены"
        ordering = [
            "unit_amount",
            "product",
            "currency",
        ]
