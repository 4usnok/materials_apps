from django.core.serializers import serialize
from django.template.context_processors import request
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from course.models import Course
from users.models import Payments, User, Subscription
from users.serializers import PaymentsSerializers, UserSerializers, SubscriptionSerializers


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
        payments = serializer.save(user=self.request.user)
        payments.user = self.request.user
        payments.save()


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

class SubscriptionActivate(APIView):
    """Активация подписки"""

    permission_classes = [IsAuthenticated]

    def post(self, *args, **kwargs):
        user = self.request.user
        course_item = get_object_or_404(Course, pk=self.request.data.get('course_id'))

        subs_item = Subscription.objects.filter(user=user, course=course_item)

        if subs_item.exists():
            subs_item.delete()
            message = 'подписка удалена'
        else:
            Subscription.objects.create(user=user, course=course_item)
            message = 'подписка добавлена'
        return Response({"message": message})
