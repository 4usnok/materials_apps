from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from users.models import Payments, User, Product
from users.serializers import (
    PaymentsSerializers,
    UserSerializers,
    ProductSerializers,
    PriceSerializers,
    PaymentStatusSerializer,
)
from users.services import create_product, create_price, create_session_to_url


class UserViewSet(viewsets.ModelViewSet):
    """ViewSet CRUD для модели 'User'"""

    queryset = User.objects.all()
    serializer_class = UserSerializers


class UserCreateAPIView(CreateAPIView):
    """Регистрация пользователя"""

    queryset = User.objects.all()
    serializer_class = UserSerializers

    def perform_create(self, serializer):
        """Создание нового экземпляра модели "User" """
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class PaymentsListAPIView(generics.ListAPIView):
    """Фильтрация и сортировка платежей"""

    serializer_class = PaymentsSerializers
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ("paid_course", "paid_lesson", "payment_method")
    ordering_fields = ("date_of_payment",)
    permission_classes = [IsAuthenticated]


class PaymentsAPICreate(generics.CreateAPIView):
    """Создание платежа"""

    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializers
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Автоматическая подвязка поля пользователя к модели"""
        product = create_product("test_name", "test_info")  # вызов сервисной функции продукта
        price = create_price(product, 1555)  # вызов сервисной функции цены

        # Создаем сессию
        session_id, session_url = create_session_to_url(price)

        payment = serializer.save(
            user=self.request.user,
            stripe_product_id=product.id,  # ID продукта в Stripe
            stripe_price_id=price.id,  # ID цены в Stripe
            stripe_session_id=session_id,  # ID сессии
            payment_url=session_url  # URL для оплаты
        )


class PaymentsStatus(generics.RetrieveAPIView):
    """Просмотр статуса платежа"""

    queryset = Payments.objects.all()
    serializer_class = PaymentStatusSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Пользователь видит только свои платежи"""
        return Payments.objects.filter(user=self.request.user)


class PaymentsAPIUpdate(generics.UpdateAPIView):
    """Редактирование платежа"""

    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializers
    permission_classes = [IsAuthenticated]


class PaymentsDetailList(generics.RetrieveAPIView):
    """Просмотр отдельного платежа"""

    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializers
    permission_classes = [IsAuthenticated]


class PaymentsAPIDestroy(generics.DestroyAPIView):
    """Удаление платежа"""

    queryset = Payments.objects.all()
    permission_classes = [IsAuthenticated]


class ProductAPICreate(generics.CreateAPIView):
    """Создание продукта"""

    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializers

    def perform_create(self, serializer):
        product = serializer.save(user=self.request.user)
        product.save()


class PriceAPICreate(generics.CreateAPIView):
    """Создание цены"""

    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PriceSerializers

    def perform_create(self, serializer):
        price = serializer.save(user=self.request.user)
        price.save()
