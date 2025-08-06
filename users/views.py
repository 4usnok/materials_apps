from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.filters import OrderingFilter

from users.models import Payments, User
from users.serializers import PaymentsSerializers, UserSerializers


class UserViewSet(viewsets.ModelViewSet):
    """ViewSet CRUD для модели 'User'"""

    queryset = User.objects.all()
    serializer_class = UserSerializers


class PaymentsListAPIView(generics.ListAPIView):
    """Фильтрация и сортировка платежей"""

    serializer_class = PaymentsSerializers
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ("paid_course", "paid_lesson", "payment_method")
    ordering_fields = ("date_of_payment",)


class PaymentsAPICreate(generics.CreateAPIView):
    """Создание платежа"""

    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializers


class PaymentsAPIUpdate(generics.UpdateAPIView):
    """Редактирование платежа"""

    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializers


class PaymentsDetailList(generics.RetrieveAPIView):
    """Просмотр отдельного платежа"""

    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializers


class PaymentsAPIDestroy(generics.DestroyAPIView):
    """Удаление платежа"""

    queryset = Payments.objects.all()
